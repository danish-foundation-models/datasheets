from pathlib import Path
from typing import Any

import pytest
import yaml

from tests.readme_parsing import read_frontmatter_and_body

root_path = Path(__file__).parent.parent.parent

main_readme = root_path / "README.md"

frontmatter, _ = read_frontmatter_and_body(main_readme)
DATASET_NAMES = [
    cfg["config_name"]
    for cfg in frontmatter["configs"]
    if cfg["config_name"] != "default"
]


@pytest.fixture()
def repo_path() -> Path:
    return root_path


def readme_yaml_header(repo_path: Path) -> dict[str, Any]:
    readme_path = repo_path / "README.md"

    with readme_path.open("r") as f:
        readme = f.read()

    frontmatter = readme.split("---")[1]
    return yaml.safe_load(frontmatter)
