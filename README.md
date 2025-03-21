---
license: other
configs:
- config_name: default
  data_files:
  - split: train
    path: 'data/*/*.parquet'
- config_name: ai4welfare-kb-data
  data_files:
  - split: train
    path: data/ai4welfare-kb-data/*.parquet
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- da
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: Danish Dynaword
language_bcp47:
- da
- da-bornholm
- da-synnejyl
---

<!-- 
readme structure is inspired by:
https://github.com/huggingface/datasets/blob/main/templates/README_guide.md 
-->


# 🧨 DFM Datasheets


<!-- START README TABLE -->
|              |                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Version**  | 0.0.1                                                                                                                                    |
| **Language** | dan, dansk, Danish                                                                                                                       |
| **License**  | Non publicly available                                                                                                                   |
| **Models**   | Currently not model is publicly available that is trained on the data                                                                    |
| **Contact**  | If you have question about this project please create an issue [here](https://github.com/danish-foundation-models/dfm-datasheets/issues) |
<!-- END README TABLE -->

## Table of Contents
- [🧨 DFM Datasheets](#-dfm-datasheets)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Summary](#summary)
    - [Languages:](#languages)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Annotations](#annotations)
    - [Source Data](#source-data)
  - [Additional Information](#additional-information)
    - [Citation Information](#citation-information)
    - [Disclaimer](#disclaimer)
    - [Notice and take down policy](#notice-and-take-down-policy)

## Dataset Description

<!-- START-DESC-STATS -->
- **Language**: dan, dansk, Danish
- **Number of samples**: 588.92K
- **Number of tokens (Llama 3)**: 1.85B
- **Average document length (characters)**: 9245.09
<!-- END-DESC-STATS -->


### Summary

The DFM Datasheets is a collection of datasheets for the subsection of data used for [Danish Foundation Models](https://www.foundationmodels.dk) that can't be shared publicly under open-licenses. This repository ensure documentation to data along with FAIR
data practices.


### Languages:
This dataset includes the following languages:

- dan-Latn
- dan-Latn-bornholm
- dan-Latn-synnejyl

Language is denoted using [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag), using the langauge code ISO 639-3 and the script code ISO 15924. The last element denote the region variant.


## Dataset Creation

### Curation Rationale

These datasets were collected and curated with the intention of developing language models for Danish.

### Annotations

This data generally contains no annotation besides the metadata attached to each sample such as what domain it belongs to. 

### Source Data

Below follows a brief overview of the sources in the corpus along with their individual license.

| Source               | Description                                                               | N. Tokens | License |
| :------------------- | :------------------------------------------------------------------------ | :-------- | :------ |
| [AI4WELFARE KB Data] | The Danish Web Archive (Netarkivet) collected by The Royal Danish Library |
| 1,200B               | For internal use                                                          |

[AI4WELFARE KB Data]: data/ai4welfare-kb-data/ai4welfare-kb-data.md


## Additional Information

### Citation Information

Currently no citation information is provided.

###  Disclaimer
We do not own any of the text from which the data has been extracted.
If you believe that we are not allowed to train on any of the datasets noted please do [contact us](https://github.com/danish-foundation-models/dfm-datasheets/issues).

### Notice and take down policy
Notice: Should you consider that our data contains material that is owned by you and should therefore not be included in the training of LLMs here, please:

- Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
- Clearly identify the copyrighted work claimed to be infringed.
- Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

You can contact us by making an [issue](https://github.com/danish-foundation-models/dfm-datasheets/issues).

Take down: We will comply to legitimate requests by removing the affected sources from the next release of the corpus.

---

<h3 style="display: flex; align-items: center;">
  <a href="https://www.foundationmodels.dk">
    <img src="./docs/icon.png" width="30" style="margin-right: 10px;" />
  </a>
  A&nbsp;<a href=https://www.foundationmodels.dk>Danish Foundation Models</a>&nbsp;dataset
</h3>