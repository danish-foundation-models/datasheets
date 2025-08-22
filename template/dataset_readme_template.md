---
license: other
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- da
- en
- se
- nb
- nn
multilinguality:
- multilingual
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

# DFM Data: A Composite Dataset for Danish LLMs.

This page provides a detailed description of the composite dataset used to train large language models developed by Danish Foundation Models. The dataset is curated to offer a diverse and comprehensive corpus across multiple domains, including legal, financial, and literary texts, with the primary intention of developing language models for Danish.

## Dataset Description

### Summary

The DFM Data is a collection of datasets used for [Danish Foundation Models](https://www.foundationmodels.dk). This repository ensure documentation to data along with FAIR data practices.

### Curation Rationale

These datasets were collected and curated with the intention of developing language models for Danish.

### Data Collection and Processing
The dataset was constructed by collecting and integrating text from a wide variety of public and partner-provided sources. The raw data was subjected to a standardized cleaning pipeline, which included steps such as deduplication, filtering of low-quality content to prepare it for large-scale language model training.


### Dataset Statistics

<!-- START-DESC-STATS -->
- **Number of samples**: 16.23M
- **Number of tokens (Llama 3)**: 10.58B
- **Average document length in tokens (min, max)**: 651.9848074000665 (2, 13.35M)
<!-- END-DESC-STATS -->

The following plot pr. dataset histograms displaying document lengths.


<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dataset_size_plot.svg" width="800" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->

### Languages
This dataset includes the following languages:

- Danish
- English
- Swedish
- Norwegian Bokmål
- Norwegian Nynorsk

Below is a visualisation of the main languages in each of the datasets.

<p align="center">
<img src="./images/language_distribution.svg" width="1000" style="margin-right: 10px;" />
</p>



### Domains

This dataset consist of data from various domains (e.g., legal, books, social media). The following table and figure give an overview of the relative distributions of these domains.

<div style="display: flex; gap: 20px; align-items: flex-start;">

<div style="flex: 1;">


<!-- START-DOMAIN TABLE -->

<!-- END-DOMAIN TABLE -->

</div>

<div style="flex: 1;">

<p align="center">
<img src="./images/domain_distribution.png" width="400" style="margin-right: 10px;" />
</p>

</div>

</div>


### Licensing

The following gives an overview of the licensing in the DFMv1. To get the exact license of the individual datasets check out the individual datasets by clicking the links in the table.
These license is applied to the constituent data, i.e., the text. The collection of datasets (metadata, quality control, etc.) is licensed under [CC-0](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en).

<!-- START-LICENSE TABLE -->

<!-- END-LICENSE TABLE -->



## Additional Information

### Citation Information

If you use a model trained on this dataset, please cite the associated DFM project or research paper when it becomes available. A BibTeX entry will be provided here upon the official release of a corresponding paper.

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
    <img src="_static/icon.png" width="30" style="margin-right: 10px;" />
  </a>
  A&nbsp;<a href=https://www.foundationmodels.dk>Danish Foundation Models</a>&nbsp;dataset
</h3>
