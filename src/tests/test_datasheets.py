import pytest

from dynaword.datasheet import DEFAULT_SECTION_TAGS, DataSheet
from dynaword.paths import repo_path

from .conftest import DATASET_NAMES


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_datasheet_load(dataset_name: str):
    """tests that the dataset frontmatter and markdown follows the correct format."""

    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"
    ds_sheet = DataSheet.load_from_path(  # noqa: F841
        readme
    )  # will fail if format is not correct


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_datasheet_content_tags(dataset_name: str):
    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"
    ds_sheet = DataSheet.load_from_path(readme)

    # ensure tags:
    tags = [v.value for v in DEFAULT_SECTION_TAGS]
    for tag in tags:
        ds_sheet.get_tag_idx(tag)


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_datasheet_license_info(dataset_name: str):
    """Ensure that license information is present is license is other"""
    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"
    ds_sheet = DataSheet.load_from_path(readme)

    if ds_sheet.license == "other":  # ensure description of underspecified licenses
        assert ds_sheet.license_information.strip()
        assert ds_sheet.license_name


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_datasheet_required_headings(dataset_name: str):
    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"
    ds_sheet = DataSheet.load_from_path(readme)

    req_h2_headings = ["## Dataset Description", "## Additional Information"]
    for req_h2 in req_h2_headings:
        assert ds_sheet.get_section_by_header(req_h2)


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_domains_in_frontmatter(dataset_name: str):
    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"
    ds_sheet = DataSheet.load_from_path(readme)

    assert ds_sheet.domains, "domains annotations are missing"
