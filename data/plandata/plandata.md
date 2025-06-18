---
pretty_name: Plan- og Landdistriktsstyrelsen - Plandata.dk
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
- Legal
---

# Dataset Card for Plan- og Landdistriktsstyrelsen - Plandata.dk

<!-- START-SHORT DESCRIPTION -->
A comprehensive dataset consisting of municipal planning documents from across Denmark, including local development plans, municipal plans, planning strategies, and related document types.
<!-- END-SHORT DESCRIPTION -->

This dataset contains approximately 114,000 documents related to physical and strategic planning in Danish municipalities. The documents include local development plans (lokalplaner), municipal master plans (kommuneplaner), municipal planning strategies (kommuneplanstrategier), and other related planning documents that define the framework for land use, urban development, infrastructure, nature conservation, business, and residential areas.

The documents are authored and adopted by municipal authorities and often carry legal weight, making them relevant in legal, administrative, and urban planning contexts.




## Dataset Description

<!-- START-DESC-STATS -->
- **Language**: dan, dansk, Danish
- **Domains**: Legal
- **Number of samples**: 114.28K
- **Number of tokens (Llama 3)**: 1.84B
- **Average document length (characters)**: 57558.79
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

The data have been pulled from [https://kort.plandata.dk](https://kort.plandata.dk/searchlist/#/). 

Each document have been extracted from different file types (docx, pdf, etc.) but primarily PDF.

For text extraction of PDF we have used the [marker](https://github.com/datalab-to/marker) tool. 


### Dataset Statistics

<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dist_document_length.png" width="600" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->


# Additional Information

## License Information
The license for this is a written agreement with "Plan- og Landdistriktsstyrelsen" that we can use the data for training.

> Plan- og Landdistriktsstyrelsen driver Plandata.dk mens det er kommunerne som planlægningsmyndighed, der udarbejder planerne.
>
> Planerne er offentligt tilgængelige, så dem henter I bare.

### Citation Information

No citation available.
