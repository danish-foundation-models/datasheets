from pathlib import Path
from typing import Any, Literal

import pytest
from pydantic import BaseModel

from .conftest import DATASET_NAMES
from .readme_parsing import get_tag_idx, read_frontmatter_and_body


def ensure_tuple(created: str | tuple) -> tuple:
    if isinstance(created, str):
        return tuple(created.split(", "))
    return created


def validate_sample_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    if "source-pretty" not in metadata:
        raise ValueError("'source-pretty' should be in metadata dict.")
    return metadata


class FrontmatterSchema(BaseModel):
    pretty_name: str
    language: list[Literal["da", "en"]]
    license: Literal["cc0-1.0", "other", "cc-by-sa-4.0"]


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_dataset_readme(repo_path: Path, dataset_name: str):
    """tests that the dataset frontmatter and markdown follows the correct format."""

    readme = repo_path / "data" / dataset_name / f"{dataset_name}.md"

    frontmatter, body = read_frontmatter_and_body(readme)
    frontmatter_validated = FrontmatterSchema(**frontmatter)

    # ensure tags:
    tags = ["SHORT DESCRIPTION"]
    for tag in tags:
        get_tag_idx(body, tag)

    h2_headings = {line for line in body.splitlines() if line.startswith("## ")}

    if (
        frontmatter_validated.license == "other"
    ):  # ensure description of underspecified licenses
        assert "## Usage restrictions" in h2_headings

    # required headings
    req_h2_headings = ["## Dataset Description", "## Additional Information"]
    for req_h2 in req_h2_headings:
        assert req_h2 in h2_headings
    pass


@pytest.mark.parametrize("dataset_name", DATASET_NAMES)
def test_dataset_folder_structure(repo_path: Path, dataset_name: str):
    """tests that the dataset folder structure is as follows.

    dataset_name
    |- dataset_name.md
    """
    path = repo_path / "data" / dataset_name

    assert (path / f"{path.name}.md").exists()
