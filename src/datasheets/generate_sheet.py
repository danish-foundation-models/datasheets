import questionary
import yaml
from pathlib import Path

from datasheets.datasheet import DataSheet
from datasheets.paths import repo_path

# --- Configuration ---

# Pre-defined choices for prompts
LANGUAGES_CHOICES = ["en", "da", "se", "no"]
DOMAINS_CHOICES = [
    "Books",
    "Conversation",
    "Dialect",
    "Encyclopedic",
    "Legal",
    "News",
    "Other",
    "Readaloud",
    "Social Media",
    "Speeches",
    "Spoken",
    "Subtitles",
    "Web",
]
LICENSE_ID_CHOICES = ["cc0-1.0", "cc-by-sa-4.0", "apache-2.0", "other"]
LICENSE_NAMES_MAPPING = {
    "cc0-1.0": "CC-0",
    "cc-by-sa-4.0": "CC-BY-SA 4.0",
    "apache-2.0": "Apache 2.0",
}

TEMPLATE_PATH = Path("template/template.md")
OUTPUT_DIR = Path("data")

# --- Helper Functions ---


def get_user_input():
    """Gathers all necessary information from the user via interactive prompts."""
    print("--- 🚀 Let's create a new Dataset Card! ---\n")

    data = {}

    # --- Basic Information ---
    data["pretty_name"] = questionary.text(
        "What is the pretty name of the dataset?",
        validate=lambda text: True if len(text) > 0 else "Please enter a name.",
    ).ask()

    data["dataset_id"] = questionary.text(
        "What is the ID of the dataset?",
        validate=lambda text: True if len(text) > 0 else "Please enter an ID.",
    ).ask()

    # --- Languages ---
    selected_langs = questionary.checkbox(
        "Select the languages (press space to select):",
        choices=LANGUAGES_CHOICES + ["Other..."],
    ).ask()

    if "Other..." in selected_langs:
        selected_langs.remove("Other...")
        other_langs_str = questionary.text(
            "Please enter other languages (comma-separated):"
        ).ask()
        other_langs = [lang.strip() for lang in other_langs_str.split(",")]
        selected_langs.extend(other_langs)
    data["languages"] = selected_langs

    # --- Domains ---
    data["domains"] = questionary.checkbox(
        "Select the domains:", choices=DOMAINS_CHOICES
    ).ask()

    # --- License ---
    data["license_id"] = questionary.select(
        "Select the license ID:", choices=LICENSE_ID_CHOICES
    ).ask()

    if data["license_id"] == "other":
        data["license_name"] = questionary.text(
            "Please specify the license name:"
        ).ask()
    else:
        data["license_name"] = LICENSE_NAMES_MAPPING.get(data["license_id"], "Unknown")
        print(f"✅ Automatically set License Name to: {data['license_name']}")

    # --- Descriptions ---
    print(
        "\n(You can use multiple lines for the next fields. Press ESC then Enter to finish.)"
    )
    data["short_description"] = questionary.text(
        "Enter the short description (for the top of the card):", multiline=True
    ).ask()
    data["long_description"] = questionary.text(
        "Enter the long description (main body):", multiline=True
    ).ask()
    data["license_information"] = questionary.text(
        "Enter the full license information:", multiline=True
    ).ask()
    data["citation_information"] = questionary.text(
        "Enter the citation information:", multiline=True
    ).ask()

    # --- Optional Contribution ---
    if questionary.confirm("Add a contribution notice from a company?").ask():
        company_name = questionary.text("What is the company's name?").ask()
        data["contribution_line"] = (
            f"This data has been contributed by [{company_name}] through the [Dansk Sprogmodel Konsortium](https://alexandra.dk/dsk)."
        )
    else:
        data["contribution_line"] = ""

    return data


def create_card_content(template_content, data):
    """Fills the template with user-provided data."""

    # --- 1. Fill YAML Front Matter ---
    # Split the template into YAML front matter and markdown body
    parts = template_content.split("---", 2)
    front_matter_str = parts[1]
    markdown_body = parts[2]

    # Load, update, and dump YAML to preserve structure and formatting
    front_matter = yaml.safe_load(front_matter_str)
    front_matter["pretty_name"] = data["pretty_name"]
    front_matter["language"] = data["languages"]
    front_matter["license"] = data["license_id"]
    front_matter["license_name"] = data["license_name"]
    front_matter["domains"] = data["domains"]

    # The 'sort_keys=False' is important to keep the original order
    updated_front_matter_str = yaml.dump(front_matter, sort_keys=False)

    # --- 2. Fill Markdown Body ---
    # Simple replacements
    body_content = markdown_body.replace("PRETTY_NAME", data["pretty_name"])
    body_content = body_content.replace(
        "LICENSE_INFORMATION", data["license_information"]
    )
    body_content = body_content.replace(
        "CITATION_INFORMATION", data["citation_information"]
    )

    # Block replacements using regex for safety
    body_content = body_content.replace("SHORT_DESCRIPTION", data["short_description"])
    body_content = body_content.replace("LONG_DESCRIPTION", data["long_description"])

    # Replace contribution placeholder
    body_content = body_content.replace(
        "<!-- CONTRIBUTION-PLACEHOLDER -->", data["contribution_line"]
    )

    return f"---\n{updated_front_matter_str}---\n{body_content}"


def add_dataset_to_readme(dataset_id: str):
    # Update main readme
    main_sheet = DataSheet.load_from_path(repo_path / "README.md")
    _datasets = [
        cfg["config_name"]  # type: ignore
        for cfg in main_sheet.frontmatter["configs"]  # type: ignore
        if cfg["config_name"] != "default"  # type: ignore
    ]

    if dataset_id not in _datasets:
        main_sheet.frontmatter["configs"].append({"config_name": dataset_id})
        main_sheet.write_to_path(repo_path / "README.md")


def main():
    """Main function to run the script."""
    if not TEMPLATE_PATH.exists():
        print(f"❌ Error: Template file not found at '{TEMPLATE_PATH}'")
        return

    try:
        user_data = get_user_input()
    except (KeyboardInterrupt, TypeError):  # Catch Ctrl+C and empty prompts
        print("\n👋 Canceled. No file was created.")
        return

    # Generate content
    template_str = TEMPLATE_PATH.read_text(encoding="utf-8")
    final_content = create_card_content(template_str, user_data)

    # Create output directory if it doesn't exist
    (OUTPUT_DIR / user_data["dataset_id"]).mkdir(exist_ok=True)

    # Create a filename-safe version of the pretty name
    # safe_filename = user_data['pretty_name'].lower().replace(" ", "-").replace("_", "-")
    output_path = OUTPUT_DIR / user_data["dataset_id"] / f"{user_data['dataset_id']}.md"

    # Write the file
    output_path.write_text(final_content, encoding="utf-8")

    add_dataset_to_readme(user_data["dataset_id"])

    print(f"\n✅ Successfully created dataset card at: {output_path}")


if __name__ == "__main__":
    main()
