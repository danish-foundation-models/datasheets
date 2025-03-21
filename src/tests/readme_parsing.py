from pathlib import Path
from typing import Any

import yaml


def read_frontmatter_and_body(file_path: Path) -> tuple[dict[str, Any], str]:
    with file_path.open("r") as f:
        content = f.read()
    if content.startswith("---"):
        end_idx = content.find("---", 3)
        if end_idx != -1:
            frontmatter = content[3:end_idx].strip()
            return yaml.safe_load(frontmatter), content[end_idx:]
    raise ValueError(f"No frontmatter found in file: {file_path}")


def get_tag_idx(readme: str, tag: str) -> tuple[int, int]:
    tag_start = f"<!-- START-{tag} -->"
    tag_end = f"<!-- END-{tag} -->"
    start_idx = readme.find(tag_start)
    end_idx = readme.find(tag_end)
    if end_idx != -1 and start_idx != -1 and start_idx < end_idx:
        return start_idx, end_idx
    raise ValueError(f"tag ({tag}) not found in readme")


def get_tag_content(readme: str, tag: str) -> str:
    s, e = get_tag_idx(readme, tag=tag)
    tag_start = f"<!-- START-{tag} -->"
    return readme[s + len(tag_start) : e].strip()


def replace_tag(markdown: str | Path, package: str, tag: str) -> str:
    if isinstance(markdown, Path):
        with markdown.open("r") as f:
            md = f.read()
        new_markdown = replace_tag(md, package=package, tag=tag)
        with markdown.open("w") as f:
            f.write(new_markdown)
        return new_markdown

    tag_start = f"<!-- START-{tag} -->"
    tag_end = f"<!-- END-{tag} -->"

    if markdown.count(tag_start) != 1 or markdown.count(tag_end) != 1:
        raise ValueError(
            f"The markers ({tag_start} ... {tag_end}) does not appear in the markdown. Markers should appear exactly once in the markdown."
        )

    start_md, _, remainder = markdown.partition(tag_start)
    _, _, end_md = remainder.partition(tag_end)

    return f"{start_md}{tag_start}\n{package.strip()}\n{tag_end}{end_md}"
