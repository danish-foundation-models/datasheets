from pathlib import Path

import pandas as pd

from dynaword.datasheet import DataSheet, human_readable_large_int
from dynaword.paths import repo_path

main_sheet = DataSheet.load_from_path(repo_path / "README.md")
_datasets = [
    cfg["config_name"]  # type: ignore
    for cfg in main_sheet.frontmatter["configs"]  # type: ignore
    if cfg["config_name"] != "default"  # type: ignore
]

DEFAULT_LICENSE_REFERENCES = """[CC-0]: https://creativecommons.org/publicdomain/zero/1.0/legalcode.en
[CC-BY-SA 4.0]: https://creativecommons.org/licenses/by-sa/4.0/deed.en
[Apache 2.0]: https://www.apache.org/licenses/LICENSE-2.0
"""


def create_license_references() -> str:
    license_references = DEFAULT_LICENSE_REFERENCES
    for dataset in _datasets:
        dataset_path = repo_path / "data" / dataset
        readme_path = dataset_path / f"{dataset_path.name}.md"

        sheet = DataSheet.load_from_path(readme_path)

        if sheet.license == "other":
            license_name = sheet.frontmatter["license_name"]
            license_references += f"[{license_name}]: ./data/{dataset_path.name}/{dataset_path.name}.md#license-information\n"

    return license_references


def create_dataset_readme_references():
    readme_references = ""

    for dataset in _datasets:
        dataset_path = repo_path / "data" / dataset

        readme_references += (
            f"[{dataset_path.name}]: data/{dataset_path.name}/{dataset_path.name}.md\n"
        )
    return readme_references


def create_overview_table(
    repo_path: Path = repo_path,
    add_readable_tokens: bool = True,
    add_total_row: bool = True,
    add_readme_references: bool = True,
) -> pd.DataFrame:
    table = {
        "Source": [],
        "Source with link": [],
        "Description": [],
        "Domain": [],
        "N. Tokens": [],
        "License": [],
    }

    for dataset in _datasets:
        dataset_path = repo_path / "data" / dataset
        readme_path = dataset_path / f"{dataset_path.name}.md"

        sheet = DataSheet.load_from_path(readme_path)
        desc_stats = sheet.get_descritive_stats()
        main_domain = sheet.domains[0] if sheet.domains else ""

        table["Source"] += [f"{dataset_path.name}"]
        table["Source with link"] += [f"[{dataset_path.name}]"]
        table["License"] += [f"[{sheet.license_name}]"]
        table["Domain"] += [main_domain]
        table["Description"] += [sheet.short_description]
        table["N. Tokens"] += [desc_stats.number_of_tokens]

    df = pd.DataFrame.from_dict(table)
    df = df.sort_values("N. Tokens", ascending=False)

    if add_total_row:
        total_row = {
            "Source": "**Total**",
            "Source with link": "**Total**",
            "Domain": "",
            "License": "",
            "Description": "",
            "N. Tokens": sum(table["N. Tokens"]),
        }
        df = pd.concat(
            [
                df,
                pd.DataFrame([total_row]),
            ],
            ignore_index=True,
        )
    if add_readme_references:
        # replace Source with Source with link
        df["Source"] = df["Source with link"]
        df = df.drop(columns=["Source with link"])
    else:
        # remove Source with link
        df = df.drop(columns=["Source with link"])

    if add_readable_tokens:
        df["N. Tokens"] = df["N. Tokens"].apply(human_readable_large_int)

    return df


def create_overview_table_str(repo_path: Path = repo_path) -> str:
    main_table = create_overview_table(repo_path)
    readme_references = create_dataset_readme_references()
    license_references = create_license_references()
    package = f"{main_table.to_markdown(index=False)}\n\n{readme_references}\n\n{license_references}\n\n"
    return package
