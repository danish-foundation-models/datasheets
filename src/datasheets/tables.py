from pathlib import Path
from typing import Literal

import pandas as pd

from datasheets.datasheet import DataSheet, convert_to_human_readable
from datasheets.paths import repo_path

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
        "Sources": [],
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
        table["Sources"] += [f"[{dataset_path.name}]"]
        table["License"] += [f"[{sheet.license_name}]"]
        table["Domain"] += [main_domain]
        table["Description"] += [sheet.short_description]
        table["N. Tokens"] += [desc_stats.number_of_tokens]

    df = pd.DataFrame.from_dict(table)
    df = df.sort_values("N. Tokens", ascending=False)

    if add_total_row:
        total_row = {
            "Source": "**Total**",
            "Sources": "**Total**",
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
        # replace Source with Sources
        df["Source"] = df["Sources"]
        df = df.drop(columns=["Sources"])
    else:
        # remove Sources
        df = df.drop(columns=["Sources"])

    if add_readable_tokens:
        df["N. Tokens"] = df["N. Tokens"].apply(convert_to_human_readable)

    return df


def _get_normalized_license(ds: DataSheet) -> str:
    non_standard_license_names = {
        "Apache 2.0": "Other (Attribution required)",
        "NLOD 2.0": "Other (Attribution required)",
        "DanNet 1.0": "Other (Attribution required)",
        "Gutenberg": "Other (Attribution required)",
        "Danish Copyright Law": "Other (No attribution required)",
    }
    if (
        ds.license_name not in non_standard_license_names
        and ds.license_name is not None
    ):
        return ds.license_name
    if ds.license_name is None:
        raise ValueError(
            f"Datasheet {ds.pretty_name} has no license name specified in the frontmatter."
        )
    return non_standard_license_names[ds.license_name]


def _get_feature_by_string(
    datasheet: DataSheet, feature_name: Literal["Domain", "Language", "License"]
) -> str:
    """Get a specific feature from the frontmatter."""

    match feature_name:
        case "Domain":
            return datasheet.domains[0] if datasheet.domains else "N/A"
        case "Language":
            return ", ".join(datasheet.language)
        case "License":
            return _get_normalized_license(datasheet)
        case _:
            raise ValueError(f"Unknown feature: {feature_name}")


def create_grouped_table(
    group: Literal["Domain", "Language", "License"] = "Domain",
    repo_path: Path = repo_path,
    add_readable_tokens: bool = True,
    add_total_row: bool = True,
) -> pd.DataFrame:
    table = {
        "Sources": [],
        group: [],
        "N. Tokens": [],
    }

    for dataset in _datasets:
        dataset_path = repo_path / "data" / dataset
        readme_path = dataset_path / f"{dataset_path.name}.md"

        sheet = DataSheet.load_from_path(readme_path)
        desc_stats = sheet.get_descritive_stats()
        feature = _get_feature_by_string(sheet, group)

        table["Sources"] += [f"[{dataset_path.name}]"]
        table[group] += [feature]
        table["N. Tokens"] += [desc_stats.number_of_tokens]

    if add_total_row:
        table["Sources"] += [""]
        table[group] += ["**Total**"]
        table["N. Tokens"] += [sum(table["N. Tokens"])]

    df = pd.DataFrame.from_dict(table)

    df = df.groupby(group).agg({"Sources": lambda x: ", ".join(x), "N. Tokens": "sum"})

    df = df.sort_values("N. Tokens", ascending=False)

    df.index.name = group
    df = df.reset_index()

    # Trick the Total row to be at the bottom.
    new_index = list(df.index.drop(0)) + [0]
    df = df.reindex(new_index)

    if add_readable_tokens:
        df["N. Tokens"] = df["N. Tokens"].apply(convert_to_human_readable)

    return df


def create_grouped_table_str(
    repo_path: Path = repo_path,
    group: Literal["Domain", "Language", "License"] = "Domain",
) -> str:
    table = create_grouped_table(group=group, repo_path=repo_path)
    readme_references = create_dataset_readme_references()
    package = f"{table.to_markdown(index=False, maxcolwidths=[None, None, None])}\n\n{readme_references}\n\n"
    return package


def create_overview_table_str(repo_path: Path = repo_path) -> str:
    main_table = create_overview_table(repo_path)
    readme_references = create_dataset_readme_references()
    license_references = create_license_references()
    package = f"{main_table.to_markdown(index=False)}\n\n{readme_references}\n\n{license_references}\n\n"
    return package
