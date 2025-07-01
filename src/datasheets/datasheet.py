import logging
from enum import Enum
from pathlib import Path
from textwrap import dedent
from typing import Any, Self, cast

import yaml
from datasets import Dataset, load_dataset
from pydantic import BaseModel, field_validator

from datasheets.descriptive_stats import DescriptiveStatsOverview
from datasheets.plots import create_descriptive_statistics_plots
from datasheets.typings import (
    DOMAIN_TYPE,
    LANG_TYPE,
    LICENSE,
    LICENSE_NAMES_MAPPING,
    LANGUAGES,
    LANGUAGE_NAMES_MAPPING,
)

logger = logging.getLogger(__name__)


LICENSE_HEADER = "## License Information"


class DEFAULT_SECTION_TAGS(Enum):
    desc_stats = "DESC-STATS"
    dataset_plots = "DATASET PLOTS"
    short_description = "SHORT DESCRIPTION"


DATASET_PLOTS_template = """
<p align="center">
<img src="./images/dist_document_length.png" width="600" style="margin-right: 10px;" />
</p>
"""


def human_readable_large_int(value: int) -> str:
    thresholds = [
        (1_000_000_000, "B"),
        (1_000_000, "M"),
        (1_000, "K"),
    ]
    for threshold, label in thresholds:
        if value > threshold:
            return f"{value / threshold:.2f}{label}"

    return str(value)


class DataSheet(BaseModel):
    pretty_name: str
    license: LICENSE
    license_name: str | None
    language: list[LANG_TYPE]  # type: ignore
    domains: (
        list[DOMAIN_TYPE] | None  # type: ignore
    )  # None for main readme # TODO: make literal
    path: Path
    frontmatter: dict[str, Any]
    body: str

    # check that licence name is compatible with license
    @field_validator("license_name")  # type: ignore
    def check_license_name(cls, v: str | None, values: dict[str, Any]) -> str | None:
        if v is not None and v in LICENSE_NAMES_MAPPING:
            if values["license"] != LICENSE_NAMES_MAPPING[v]:
                raise ValueError(
                    f"License name '{v}' does not match license '{values['license']}'"
                )
        return v

    @property
    def short_description(self) -> str:
        short_description = self.get_tag_content(DEFAULT_SECTION_TAGS.short_description)
        if short_description.endswith("."):
            short_description = short_description[:-1]
        return short_description

    @property
    def license_information(self) -> str:
        return self.get_section_by_header(LICENSE_HEADER)

    @property
    def frontmatter_as_str(self) -> str:
        return yaml.dump(self.frontmatter, indent=2, sort_keys=False)

    def to_str(self) -> str:
        return f"---\n{self.frontmatter_as_str.strip()}\n---\n\n{self.body.strip()}\n"

    def get_dataset(self, **kwargs) -> Dataset:
        ds_path = self.path.parent
        ds = load_dataset(ds_path.as_posix(), split="train", **kwargs)
        ds = cast(Dataset, ds)
        return ds

    def get_descritive_stats(self) -> DescriptiveStatsOverview:
        path = self.path.parent / "descriptive_stats.json"
        return DescriptiveStatsOverview.from_disk(path)

    def get_section_indices_by_header(self, header: str) -> tuple[int, int]:
        level = header.split(" ")[0].count("#")

        next_is_end_section = False
        end_header = None
        for _header in self.get_headers(levels=list(range(1, level + 1))):
            if header.strip() == _header.strip():
                next_is_end_section = True
                continue

            if next_is_end_section:
                end_header = _header
                break

        if next_is_end_section is None:
            raise ValueError(f"The header '{header}' is not found in the text.")

        start_idx = self.body.find(header)
        if end_header:
            end_idx = self.body[start_idx:].find(end_header) + start_idx
        else:
            end_idx = len(self.body)

        return start_idx, end_idx

    def get_section_by_header(self, header: str) -> str:
        s, e = self.get_section_indices_by_header(header)
        return self.body[s:e]

    def get_headers(self, levels: list[int] = [1, 2, 3, 4]) -> list[str]:
        def __contains_level(text: str) -> bool:
            if text.startswith("#"):
                for level in levels:
                    if text.startswith("#" * level):
                        return True
            return False

        return [line for line in self.body.splitlines() if __contains_level(line)]

    def get_tag_idx(self, tag: str | DEFAULT_SECTION_TAGS) -> tuple[int, int]:
        if isinstance(tag, Enum):
            tag = tag.value
        tag_start = f"<!-- START-{tag} -->"
        tag_end = f"<!-- END-{tag} -->"
        start_idx = self.body.find(tag_start)
        end_idx = self.body.find(tag_end)
        if end_idx != -1 and start_idx != -1 and start_idx < end_idx:
            return start_idx, end_idx
        raise ValueError(f"tag ({tag}) not found in readme")

    def get_tag_content(self, tag: str | DEFAULT_SECTION_TAGS) -> str:
        if isinstance(tag, Enum):
            tag = tag.value
        s, e = self.get_tag_idx(tag=tag)
        tag_start = f"<!-- START-{tag} -->"
        return self.body[s + len(tag_start) : e].strip()

    def add_descriptive_stats(
        self, descriptive_stats: DescriptiveStatsOverview | None = None
    ) -> str:
        if descriptive_stats is None:
            d_stats = DescriptiveStatsOverview.from_dataset(self.get_dataset())
        else:
            d_stats = descriptive_stats

        if any(lang not in LANGUAGES for lang in self.language):
            raise NotImplementedError(  # raise NotImplementedError(
                f"This script only handles the language codes {', '.join(LANGUAGES)}"
            )
        languages = ", ".join([LANGUAGE_NAMES_MAPPING[lang] for lang in self.language])

        package = dedent(f"""
        - **Language**: {languages}\n""")

        if self.domains:
            domains = ", ".join(self.domains)
            package += f"- **Domains**: {domains}\n"

        package += (
            dedent(f"""
        - **Number of samples**: {human_readable_large_int(d_stats.number_of_samples)}
        - **Number of tokens (Llama 3)**: {human_readable_large_int(d_stats.number_of_tokens)}
        - **Average document length (characters)**: {d_stats.average_document_length:.2f}
        """).strip()
            + "\n"
        )

        return self.replace_tag(
            package=package,
            tag=DEFAULT_SECTION_TAGS.desc_stats,
        )

    def add_dataset_plots(self, dataset: Dataset, create_plot: bool = True) -> str:
        if create_plot:
            create_descriptive_statistics_plots(
                dataset=dataset, save_dir=self.path.parent
            )
        return self.replace_tag(
            package=DATASET_PLOTS_template, tag=DEFAULT_SECTION_TAGS.dataset_plots
        )

    def replace_tag(self, package: str, tag: str | DEFAULT_SECTION_TAGS) -> str:
        """Add replace a tag in the datasheet body.

        Args:
            package: What you want to replace it with
            tag: What tag you want to replace

        Returns:
            The entire body text
        """
        if isinstance(tag, Enum):
            tag = tag.value
        tag_start = f"<!-- START-{tag} -->"
        tag_end = f"<!-- END-{tag} -->"

        if self.body.count(tag_start) != 1 or self.body.count(tag_end) != 1:
            raise ValueError(
                f"The markers ({tag_start} ... {tag_end}) does not appear in the markdown. Markers should appear exactly once in the markdown."
            )

        start_md, _, remainder = self.body.partition(tag_start)
        _, _, end_md = remainder.partition(tag_end)

        return f"{start_md}{tag_start}\n{package.strip()}\n{tag_end}{end_md}"

    @staticmethod
    def get_frontmatter_and_body(file_path: Path) -> tuple[dict[str, Any], str]:
        with file_path.open("r") as f:
            content = f.read()
        if content.startswith("---"):
            end_idx = content.find("---", 3)
            start_idx_body = end_idx + 3
            if end_idx != -1:
                frontmatter = content[3:end_idx].strip()
                return yaml.safe_load(frontmatter), content[start_idx_body:]
        raise ValueError(f"No frontmatter found in file: {file_path}")

    @classmethod
    def load_from_path(cls, readme_path: Path) -> Self:
        frontmatter, body = cls.get_frontmatter_and_body(readme_path)
        return cls(
            frontmatter=frontmatter,
            body=body,
            license=frontmatter["license"],
            language=frontmatter["language"],
            pretty_name=frontmatter["pretty_name"],
            domains=frontmatter["domains"] if "domains" in frontmatter else None,
            license_name=frontmatter["license_name"]
            if "license_name" in frontmatter
            else None,
            path=readme_path,
        )

    def write_to_path(self, readme_path: Path | None = None) -> None:
        if readme_path is None:
            readme_path = self.path
        with readme_path.open("w") as f:
            f.write(self.to_str())


if __name__ == "__main__":
    from datasheets.paths import repo_path

    sheet = DataSheet.load_from_path(repo_path / "data" / "dannet" / "dannet.md")
    ds = sheet.get_dataset()

    sheet.body = sheet.add_descriptive_stats(descriptive_stats=None)
    sheet.write_to_path()
