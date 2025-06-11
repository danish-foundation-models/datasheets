---
license: other
configs:
- config_name: default
- config_name: dsk-dkmedier
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
pretty_name: DFM Datasheets
language_bcp47:
- da
- da-bornholm
- da-synnejyl
---

# DFM Datasheets

This repository contains the datasheets for DFM. This repostory documents.

<!-- START README TABLE -->
|             |                                                                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Version** | 0.0.3 ([Changelog](/CHANGELOG.md)) |
| **License** | Non publicly available                                                                                                                   |
| **Models**  | Currently not model is publicly available that is trained on the data                                                                    |
| **Contact** | If you have question about this project please create an issue [here](https://github.com/danish-foundation-models/dfm-datasheets/issues) |
<!-- END README TABLE -->

## Table of Contents
- [DFM Datasheets](#dfm-datasheets)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Summary](#summary)
    - [Curation Rationale](#curation-rationale)
    - [Dataset Overview](#dataset-overview)
  - [Additional Information](#additional-information)
    - [Citation Information](#citation-information)
    - [Disclaimer](#disclaimer)
    - [Notice and take down policy](#notice-and-take-down-policy)

## Dataset Description

### Summary

The DFM Datasheets is a collection of datasheets for datasets used for [Danish Foundation Models](https://www.foundationmodels.dk). This repository ensure documentation to data along with FAIR data practices.

### Curation Rationale

These datasets were collected and curated with the intention of developing language models for Danish.


### Dataset Overview

We generally split the dataset into two categories: Public release sources and research sources. 

**Public Release sources**: These sources include datasets that either public released under permissible licenses or where explicit permission have been given by the data owner to train and release models based on the data. The primary source for the non-public training data is [DSK](https://alexandra.dk/dsk/).


| Source            | Description                                                                                 | N. Tokens | License                            | Version                                                                                                     |
| :---------------- | :------------------------------------------------------------------------------------------ | :-------- | :--------------------------------- | :--------------------------------- |
| [Common Corpus]   | Common Corpus is a large multilingual collection of open and permissible licensed text data | 1,998B    | Various open licenses (see source) | [1.0.0](https://huggingface.co/datasets/PleIAs/common_corpus/tree/4fa82b3b7f2aed19b5b2bf7750015a9c46c1f13d) |
| [Danish Dynaword] | Danish Dynaword, is the large openly licensed collection of Danish text data                | 4.26B     | Various open licenses (see source) | 1.1.0                                                                                                       |
| DK Medier | DK Medier, is a set of ~100K news articles written and published in the period 2000-2024                | 65.44M    | DSK-1 | 1.0.0                                                                                                       |

[Danish Dynaword]: https://huggingface.co/datasets/danish-foundation-models/danish-dynaword
[Common Corpus]: https://huggingface.co/datasets/PleIAs/common_corpus

**Research sources**: 

Below follows a brief overview of the sources in the corpus along with their individual license.

| Source               | Description                                                               | N. Tokens | License          |
| :------------------- | :------------------------------------------------------------------------ | :-------- | :--------------- |
| [AI4WELFARE KB Data] | The Danish Web Archive (Netarkivet) collected by The Royal Danish Library | 1,200B    | For internal use |

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
