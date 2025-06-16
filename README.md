---
license: other
configs:
- config_name: default
- config_name: dagw-adl
- config_name: dagw-botxt
- config_name: dagw-dannet
- config_name: dagw-depbank
- config_name: dagw-ep
- config_name: dagw-ft
- config_name: dagw-gutenberg
- config_name: dagw-hest
- config_name: dagw-jvj
- config_name: dagw-naat
- config_name: dagw-relig
- config_name: dagw-retsinformationdk
- config_name: dagw-retspraksis
- config_name: dagw-skat
- config_name: dagw-spont
- config_name: dagw-synne
- config_name: dagw-tv2r
- config_name: dagw-wiki
- config_name: dagw-wikibooks
- config_name: dagw-wikisource
- config_name: dsk-alexandra
- config_name: dsk-atp
- config_name: dsk-cbrain
- config_name: dsk-danskerhverv
- config_name: dsk-dkmedier
- config_name: dsk-hofor
- config_name: dsk-ida
- config_name: dsk-odense
- config_name: dsk-plesner
- config_name: dsk-salling
- config_name: dsk-vejle
- config_name: dsk-vitec
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
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Version** | 0.0.7 ([Changelog](/CHANGELOG.md)) |
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

<!-- START-DESC-STATS -->
- **Language**: dan, dansk, Danish
- **Number of samples**: 630.94K
- **Number of tokens (Llama 3)**: 1.65B
- **Average document length (characters)**: 7791.64
<!-- END-DESC-STATS -->

### Summary

The DFM Datasheets is a collection of datasheets for datasets used for [Danish Foundation Models](https://www.foundationmodels.dk). This repository ensure documentation to data along with FAIR data practices.

### Curation Rationale

These datasets were collected and curated with the intention of developing language models for Danish.


### Dataset Overview

We generally split the dataset into two categories: Public release sources and research sources. 

<!-- START-MAIN TABLE -->
| Source                   | Description                                                                                                                                                                                             | Domain       | N. Tokens   | License                |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:------------|:-----------------------|
| [dagw-retsinformationdk] | [retsinformation.dk](https://www.retsinformation.dk) (legal-information.dk) the official legal information system of Denmark                                                                            | Legal        | 516.47M     | [Danish Copyright Law] |
| [dagw-hest]              | Samples from the Danish debate forum www.heste-nettet.dk                                                                                                                                                | Social Media | 389.31M     | [CC-0]                 |
| [dagw-skat]              | Skat is the Danish tax authority. This dataset contains content from its website skat.dk                                                                                                                | Legal        | 122.11M     | [CC-0]                 |
| [dagw-wiki]              | The Danish subsection of [wikipedia](https://en.wikipedia.org/wiki/Main_Page)                                                                                                                           | Encyclopedic | 121.74M     | [CC-0]                 |
| [dagw-ft]                | Records from all meetings of The Danish parliament (Folketinget) in the parliament hall                                                                                                                 | Conversation | 114.09M     | [CC-0]                 |
| [dagw-ep]                | The Danish subsection of [Europarl](https://aclanthology.org/2005.mtsummit-papers.11/)                                                                                                                  | Conversation | 100.88M     | [CC-0]                 |
| [dsk-dkmedier]           | A collection of ~100K news articles from [DK Medier](https://dkmedier.dk), written in the period 2000-2024                                                                                              | News         | 65.44M      | [DSK-1]                |
| [dagw-adl]               | Danish literature from 1700-2023 from the [Archive for Danish Literature](https://tekster.kb.dk/text?editorial=no&f%5Bsubcollection_ssi%5D%5B%5D=adl&match=one&search_field=Alt) (ADL)                  | Books        | 58.49M      | [CC-0]                 |
| [dagw-retspraksis]       | Case law or judical practice in Denmark derived from [Retspraksis](https://da.wikipedia.org/wiki/Retspraksis)                                                                                           | Legal        | 57.08M      | [CC-0]                 |
| [dsk-vejle]              | A collection of crawled webpages that is managed by Vejle Kommune. Contains various information, covering everything from tourists to garbage collection to historical knowledge of the area            | Web          | 33.52M      | [DSK-1]                |
| [dagw-tv2r]              | Contemporary Danish newswire articles published between 2010 and 2019                                                                                                                                   | News         | 21.62M      | [CC-BY-SA 4.0]         |
| [dsk-salling]            | A collection of crawled webpages that is managed by Salling Group. The dataset consists mainly of product pages from online stores such as bilka.dk, br.dk and such. The data consists of ~24K webpages | Web          | 10.75M      | [DSK-1]                |
| [dagw-gutenberg]         | The Danish subsection from Project [Gutenberg](https://www.gutenberg.org)                                                                                                                               | Books        | 6.76M       | [Gutenberg]            |
| [dagw-wikibooks]         | The Danish Subsection of [Wikibooks](https://www.wikibooks.org)                                                                                                                                         | Books        | 6.24M       | [CC-0]                 |
| [dsk-atp]                | A collection of crawled webpages that is managed by ATP                                                                                                                                                 | Web          | 6.10M       | [DSK-1]                |
| [dagw-wikisource]        | The Danish subsection of [Wikisource](https://en.wikisource.org/wiki/Main_Page)                                                                                                                         | Encyclopedic | 5.34M       | [CC-0]                 |
| [dsk-cbrain]             | A collection of Marketing material, product guides, and datasheets produced by cBrain for their products                                                                                                | Other        | 4.19M       | [DSK-1]                |
| [dagw-jvj]               | The works of the Danish author and poet, [Johannes V. Jensen](https://da.wikipedia.org/wiki/Johannes_V._Jensen)                                                                                         | Books        | 3.55M       | [CC-BY-SA 4.0]         |
| [dagw-spont]             | Conversational samples collected as a part of research projects at Aarhus University                                                                                                                    | Conversation | 1.56M       | [CC-0]                 |
| [dagw-dannet]            | [DanNet](https://cst.ku.dk/projekter/dannet) is a Danish WordNet                                                                                                                                        | Other        | 1.47M       | [DanNet 1.0]           |
| [dagw-relig]             | Danish religious text from the 1700-2022                                                                                                                                                                | Books        | 1.24M       | [CC-0]                 |
| [dsk-odense]             | A set of newsletters stories, covering events in Odense Municipality. Have been published on their website                                                                                              | News         | 1.19M       | [DSK-1]                |
| [dsk-danskerhverv]       | A set of newsletters written by Dansk Erhverv, primarily focusing on financials and companies world wide                                                                                                | News         | 1.12M       | [DSK-1]                |
| [dsk-plesner]            | A combination of crawled webpages from Plesners own website, and a series of internal documents outlining procedures                                                                                    | Other        | 970.32K     | [DSK-1]                |
| [dagw-botxt]             | The Bornholmsk Ordbog Dictionary Project                                                                                                                                                                | Dialect      | 847.87K     | [CC-0]                 |
| [dsk-alexandra]          | A collection of crawled webpages that is managed by Alexandra Institutet                                                                                                                                | Web          | 602.39K     | [DSK-1]                |
| [dsk-vitec]              | A collection of documents covering product descriptions, to newsletters, to internal documentation                                                                                                      | Other        | 540.80K     | [DSK-1]                |
| [dsk-ida]                | A collection of newsletters, articles and other texts produced by IDA                                                                                                                                   | News         | 438.44K     | [DSK-1]                |
| [dagw-naat]              | Danish speeches from 1930-2022                                                                                                                                                                          | Conversation | 286.55K     | [CC-0]                 |
| [dagw-depbank]           | The Danish subsection of the [Universal Dependencies Treebank](https://github.com/UniversalDependencies/UD_Danish-DDT)                                                                                  | Other        | 184.92K     | [CC-BY-SA 4.0]         |
| [dsk-hofor]              | A collection of articles, guides and newsletters written by HOFOR for their customers                                                                                                                   | Other        | 143.49K     | [DSK-1]                |
| [dagw-synne]             | Dataset collected from [synnejysk forening's website](https://www.synnejysk.dk), covering the Danish dialect sønderjysk                                                                                 | Other        | 52.33K      | [CC-0]                 |
| **Total**                |                                                                                                                                                                                                         |              | 1.65B       |                        |

[dagw-adl]: data/dagw-adl/dagw-adl.md
[dagw-botxt]: data/dagw-botxt/dagw-botxt.md
[dagw-dannet]: data/dagw-dannet/dagw-dannet.md
[dagw-depbank]: data/dagw-depbank/dagw-depbank.md
[dagw-ep]: data/dagw-ep/dagw-ep.md
[dagw-ft]: data/dagw-ft/dagw-ft.md
[dagw-gutenberg]: data/dagw-gutenberg/dagw-gutenberg.md
[dagw-hest]: data/dagw-hest/dagw-hest.md
[dagw-jvj]: data/dagw-jvj/dagw-jvj.md
[dagw-naat]: data/dagw-naat/dagw-naat.md
[dagw-relig]: data/dagw-relig/dagw-relig.md
[dagw-retsinformationdk]: data/dagw-retsinformationdk/dagw-retsinformationdk.md
[dagw-retspraksis]: data/dagw-retspraksis/dagw-retspraksis.md
[dagw-skat]: data/dagw-skat/dagw-skat.md
[dagw-spont]: data/dagw-spont/dagw-spont.md
[dagw-synne]: data/dagw-synne/dagw-synne.md
[dagw-tv2r]: data/dagw-tv2r/dagw-tv2r.md
[dagw-wiki]: data/dagw-wiki/dagw-wiki.md
[dagw-wikibooks]: data/dagw-wikibooks/dagw-wikibooks.md
[dagw-wikisource]: data/dagw-wikisource/dagw-wikisource.md
[dsk-alexandra]: data/dsk-alexandra/dsk-alexandra.md
[dsk-atp]: data/dsk-atp/dsk-atp.md
[dsk-cbrain]: data/dsk-cbrain/dsk-cbrain.md
[dsk-danskerhverv]: data/dsk-danskerhverv/dsk-danskerhverv.md
[dsk-dkmedier]: data/dsk-dkmedier/dsk-dkmedier.md
[dsk-hofor]: data/dsk-hofor/dsk-hofor.md
[dsk-ida]: data/dsk-ida/dsk-ida.md
[dsk-odense]: data/dsk-odense/dsk-odense.md
[dsk-plesner]: data/dsk-plesner/dsk-plesner.md
[dsk-salling]: data/dsk-salling/dsk-salling.md
[dsk-vejle]: data/dsk-vejle/dsk-vejle.md
[dsk-vitec]: data/dsk-vitec/dsk-vitec.md


[CC-0]: https://creativecommons.org/publicdomain/zero/1.0/legalcode.en
[CC-BY-SA 4.0]: https://creativecommons.org/licenses/by-sa/4.0/deed.en
[Apache 2.0]: https://www.apache.org/licenses/LICENSE-2.0
[DanNet 1.0]: ./data/dagw-dannet/dagw-dannet.md#license-information
[Gutenberg]: ./data/dagw-gutenberg/dagw-gutenberg.md#license-information
[Danish Copyright Law]: ./data/dagw-retsinformationdk/dagw-retsinformationdk.md#license-information
[DSK-1]: ./data/dsk-alexandra/dsk-alexandra.md#license-information
[DSK-1]: ./data/dsk-atp/dsk-atp.md#license-information
[DSK-1]: ./data/dsk-cbrain/dsk-cbrain.md#license-information
[DSK-1]: ./data/dsk-danskerhverv/dsk-danskerhverv.md#license-information
[DSK-1]: ./data/dsk-dkmedier/dsk-dkmedier.md#license-information
[DSK-1]: ./data/dsk-hofor/dsk-hofor.md#license-information
[DSK-1]: ./data/dsk-ida/dsk-ida.md#license-information
[DSK-1]: ./data/dsk-odense/dsk-odense.md#license-information
[DSK-1]: ./data/dsk-plesner/dsk-plesner.md#license-information
[DSK-1]: ./data/dsk-salling/dsk-salling.md#license-information
[DSK-1]: ./data/dsk-vejle/dsk-vejle.md#license-information
[DSK-1]: ./data/dsk-vitec/dsk-vitec.md#license-information
<!-- END-MAIN TABLE -->

<!-- **Public Release sources**: These sources include datasets that either public released under permissible licenses or where explicit permission have been given by the data owner to train and release models based on the data. The primary source for the non-public training data is [DSK](https://alexandra.dk/dsk/).


| Source            | Description                                                                                                                                                                                              | N. Tokens | License                            | Version                                                                                                     |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------------------|:------------------------------------------------------------------------------------------------------------|
| [Common Corpus]   | Common Corpus is a large multilingual collection of open and permissible licensed text data                                                                                                              | 1,998B    | Various open licenses (see source) | [1.0.0](https://huggingface.co/datasets/PleIAs/common_corpus/tree/4fa82b3b7f2aed19b5b2bf7750015a9c46c1f13d) |
| [Danish Dynaword] | Danish Dynaword, is the large openly licensed collection of Danish text data                                                                                                                             | 4.26B     | Various open licenses (see source) | 1.1.0                                                                                                       |
| DK Medier         | A collection of ~100K news articles from [DK Medier](https://dkmedier.dk), written in the period 2000-2024.                                                                                              | 65.44M    | DSK-1                              | 1.0.0                                                                                                       |
| Vejle Kommune     | A collection of crawled webpages that is managed by Vejle Kommune. Contains various information, covering everything from tourists to garbage collection to historical knowledge of the area.            | 33.52M    | DSK-1                              | 1.0.0                                                                                                       |
| Salling Group     | A collection of crawled webpages that is managed by Salling Group. The dataset consists mainly of product pages from online stores such as bilka.dk, br.dk and such. The data consists of ~24K webpages. | 10.75M    | DSK-1                              | 1.0.0                                                                                                       |

[Danish Dynaword]: https://huggingface.co/datasets/danish-foundation-models/danish-dynaword
[Common Corpus]: https://huggingface.co/datasets/PleIAs/common_corpus

**Research sources**: 

Below follows a brief overview of the sources in the corpus along with their individual license.

| Source               | Description                                                               | N. Tokens | License          |
|:---------------------|:--------------------------------------------------------------------------|:----------|:-----------------|
| [AI4WELFARE KB Data] | The Danish Web Archive (Netarkivet) collected by The Royal Danish Library | 1,200B    | For internal use |

[AI4WELFARE KB Data]: data/ai4welfare-kb-data/ai4welfare-kb-data.md --> 


### Dataset Statistics
The following plot show the domains distribution of the datasets:

<p align="center">
<img src="./images/domain_distribution.png" width="400" style="margin-right: 10px;" />
</p>



<details>
<summary>Per dataset histograms</summary>
<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dist_document_length.png" width="600" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->
</details>


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
