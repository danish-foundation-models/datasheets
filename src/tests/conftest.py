from pathlib import Path

from datasheets.datasheet import DataSheet

root_path = Path(__file__).parent.parent.parent
main_readme = root_path / "README.md"

main_sheet = DataSheet.load_from_path(main_readme)

DATASET_NAMES = [
    cfg["config_name"]
    for cfg in main_sheet.frontmatter["configs"]
    if cfg["config_name"] != "default"
]
