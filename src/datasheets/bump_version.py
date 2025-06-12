from pathlib import Path

import tomlkit
from packaging.version import Version

from datasheets.paths import pyproject_path, readme_path


def get_version(pyproject_path: Path = pyproject_path) -> str:
    with pyproject_path.open("r") as f:
        data = tomlkit.load(f)
        return data["project"]["version"]  # type: ignore


def update_pyproject_version(version: str, pyproject_path: Path) -> None:
    with pyproject_path.open("r") as f:
        data = tomlkit.load(f)
        data["project"]["version"] = version  # type: ignore

    with pyproject_path.open("w") as f:
        tomlkit.dump(data, f)


def update_readme(version: str, readme_path: Path) -> None:
    """Find version in README table and update it."""
    start = "<!-- START README TABLE -->"
    end = "<!-- END README TABLE -->"

    with readme_path.open("r") as f:
        lines = f.readlines()

    in_table = False
    for i, line in enumerate(lines):
        if start in line:
            in_table = True
        if in_table:
            if "**Version**" in line:
                lines[i] = f"| **Version** | {version} ([Changelog](/CHANGELOG.md)) |\n"
                break
        if end in line:
            raise ValueError("**Version** not found in README table.")

    with readme_path.open("w") as f:
        f.writelines(lines)


def main(pyproject_path: Path, readme_path: Path) -> None:
    version = get_version(pyproject_path)
    version = Version(version)
    version = Version(f"{version.major}.{version.minor}.{version.micro + 1}")
    update_pyproject_version(str(version), pyproject_path)
    update_readme(str(version), readme_path)


if __name__ == "__main__":
    main(pyproject_path, readme_path)
