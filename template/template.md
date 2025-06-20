---
pretty_name: PRETTY_NAME
language:
- LANGUAGES
license: LICENCE_ID
license_name: LICENSE_NAME
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- DOMAINS
---

# Dataset Card for PRETTY_NAME

<!-- START-SHORT DESCRIPTION -->
SHORT_DESCRIPTION
<!-- END-SHORT DESCRIPTION -->

LONG_DESCRIPTION

<!-- CONTRIBUTION-PLACEHOLDER -->


## Dataset Description

<!-- START-DESC-STATS -->
- **Language**: dan, dansk, Danish
- **Domains**: News
- **Number of samples**: 105.11K
- **Number of tokens (Llama 3)**: 65.44M
- **Average document length (characters)**: 1866.20
<!-- END-DESC-STATS -->


## Dataset Structure
An entry in the dataset consists of the following fields:

- `id` (`str`): An unique identifier for each document.
- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document (see [Source Data](#source-data)).
- `added` (`str`): An date for when the document was added to this collection.
- `created` (`str`): An date range for when the document was originally created.
- `token_count` (`int`): The number of tokens in the sample computed using the Llama 8B tokenizer


### Additional Processing


### Dataset Statistics

<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dist_document_length.png" width="600" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->


# Additional Information

## License Information
LICENSE_INFORMATION

### Citation Information

CITATION_INFORMATION