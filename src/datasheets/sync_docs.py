import logging
import re
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import markdown
import yaml

from datasheets.datasheet import DataSheet
from datasheets.descriptive_stats import DescriptiveStatsOverview
from datasheets.paths import repo_path
from datasheets.tables import create_grouped_table_str

download_path = repo_path.parent / "tmp"
logger = logging.getLogger(__name__)

def run_cmd(cmd, cwd=None):
    subprocess.run(cmd, check=True, cwd=cwd)

def download_repo(
    download_path: Path = download_path,
    repo_url: str = "https://github.com/danish-foundation-models/site",
) -> Path:
    """
    Downloads the repository from the given URL to the specified path
    and ensures it is on the main branch before creating a new branch.
    """
    logger.info(f"Downloading repository to {download_path}")
    download_path.mkdir(parents=True, exist_ok=True)
    site_path = download_path / repo_url.split("/")[-1]

    if site_path.exists():
        logger.info("Found dfm site locally. Ensuring main branch and pulling latest changes...")
        run_cmd(["git", "checkout", "main"], cwd=site_path)
        run_cmd(["git", "pull"], cwd=site_path)
    else:
        logger.info("Cloning site repository...")
        run_cmd(["git", "clone", repo_url], cwd=download_path)

    # Create new branch for updates
    new_branch = f"data-update-{datetime.now().strftime('%Y-%m-%d')}"
    logger.info(f"Creating and switching to branch: {new_branch}")
    run_cmd(["git", "checkout", "-B", new_branch], cwd=site_path)

    return site_path

def copy_data_files(src_base: Path, dest_base: Path):
    """
    Copies all markdown files from data/*/*.md and images from data/*/images/* into docs/data/.
    """
    dest_data_path = dest_base / "docs" / "data"
    dest_data_path.mkdir(parents=True, exist_ok=True)

    skip_folders = ["ai4welfare-kb-data"]

    for md_file in src_base.glob("data/*/*.md"):
        if md_file.parent.name in skip_folders:
            continue  # skip this folder

        rel_path = md_file.relative_to(src_base / "data")
        dest_file_path = dest_data_path / rel_path
        dest_file_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, dest_file_path)
        logger.info(f"Copied {md_file} -> {dest_file_path}")

    for img_file in src_base.glob("data/*/images/*"):
        if img_file.parents[1].name in skip_folders:  # one level above 'images'
            continue  # skip this folder
        rel_path = img_file.relative_to(src_base / "data")
        dest_file_path = dest_data_path / rel_path
        dest_file_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(img_file, dest_file_path)
        logger.info(f"Copied {img_file} -> {dest_file_path}")

def copy_images(src_base: Path, dest_base: Path):
    """
    Copies all images from data/*/images/* into docs/data/images/.
    """
    dest_images_path = dest_base / "docs" / "images"
    dest_images_path.mkdir(parents=True, exist_ok=True)

    for img_file in src_base.glob("images/*"):
        rel_path = img_file.relative_to(src_base / "images")
        dest_file_path = dest_images_path / rel_path
        dest_file_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(img_file, dest_file_path)
        logger.info(f"Copied {img_file} -> {dest_file_path}")


def get_pretty_name(datasheet: Path) -> str:
    sheet = DataSheet.load_from_path(datasheet)
    return sheet.pretty_name



def update_mkdocs(site_path: Path):
    """
    Updates mkdocs.yml nav to include dfm_data.md under DFM-Data
    and all other datasheet markdown files under Datasheets.
    """
    mkdocs_file = site_path / "mkdocs.yml"
    with open(mkdocs_file, "r") as f:
        mkdocs_text = f.read()
    
    # Rebuild Datasheets list
    datasheets_dir = site_path / "docs" / "data"
    datasheet_entries = []
    for md_file in sorted(datasheets_dir.glob("*/*.md")):
        name = get_pretty_name(md_file)
        rel_path = md_file.relative_to(site_path / "docs").as_posix()
        datasheet_entries.append((name, rel_path))
    
    datasheet_nav = "\n".join([f"        - {name}: {path}" for name, path in datasheet_entries])

    # Regex to match the datasets block inside nav
    pattern = re.compile(
        r"( {2}- Datasheets:\n)(?: {8}- .*?\n)*",  # Match existing datasets section
        re.MULTILINE
    )

    replacement = r"\1" + datasheet_nav + "\n"

    new_text, count = pattern.subn(replacement, mkdocs_text)

    if count == 0:
        raise ValueError("Could not find 'Datasets:' section in mkdocs.yml")

    mkdocs_file.write_text(new_text, encoding="utf-8")
    print(f"Updated {mkdocs_file} with {len(datasheet_entries)} dataset links.")


def generate_html_table(md_table: str) -> str:
    """
    Converts a markdown table to HTML.
    """
    html_table = markdown.markdown(md_table, extensions=['tables'])
    html_table = f'<div class="md-typeset__scrollwrap"><div class="md-typeset__table">{html_table}</div></div>'
    html_table = re.sub(r'(?<=\b)\.md\b', '.html', html_table)
    return html_table

def main():
    site_path = download_repo()
    
    # Copy all data markdowns and images
    copy_data_files(repo_path, site_path)
    copy_images(repo_path, site_path)

    # Build "main" readme for data
    template_path = repo_path / "template"
    markdown_path = template_path / "dataset_readme_template.md"
    desc_paths = (repo_path / "data").glob("**/*descriptive_stats.json")
    _desc_stats = [DescriptiveStatsOverview.from_disk(p) for p in desc_paths]
    desc_stats = sum(_desc_stats[1:], start=_desc_stats[0])
    sheet = DataSheet.load_from_path(markdown_path)
    sheet.body = sheet.add_descriptive_stats(descriptive_stats=desc_stats)

    logger.info("Creating domain table")
    domain_table = create_grouped_table_str(group="Domain")
    sheet.body = sheet.replace_tag(package=generate_html_table(domain_table), tag="DOMAIN TABLE")

    logger.info("Creating license table")
    license_table = create_grouped_table_str(group="License")
    sheet.body = sheet.replace_tag(package=generate_html_table(license_table), tag="LICENSE TABLE")

    sheet.write_to_path(readme_path=site_path / "docs" / "dfm_data.md")

    # Update mkdocs.yml navigation
    update_mkdocs(site_path)

if __name__ == "__main__":
    log_path = repo_path / "docs_sync.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path),
        ],
    )
    main()
