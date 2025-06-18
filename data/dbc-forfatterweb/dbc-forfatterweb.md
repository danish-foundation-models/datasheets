---
pretty_name: DBC D1G1TAL - Forfatterweb
language:
- da
license: other
license_name: Written agreement (public models, private data)
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Books
- Encyclopedic
---


# Dataset Card for DBC D1G1TAL - Forfatterweb

<!-- START-SHORT DESCRIPTION -->
dbc-forfatterweb consists of more than 1 thousand articles created by DBC D1G1TAL (former Dansk Bibliotekscenter).
<!-- END-SHORT DESCRIPTION -->

All articles are written in Danish language. Instances that comprise this dataset represent articles on Danish writers. 
The dataset includes articles created between 1991 and 2024.




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
Danish Foundation Models have a written agreement with DBC D1G1TAL regarding the use of the data for training and releasing models. 
Data will only be available at the entity during the project. Requests regarding access to the dataset should be directed to the data owner DBC D1G1TAL.

### Citation Information

No citation at the moment.