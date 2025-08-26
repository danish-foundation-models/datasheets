---
license: other
configs:
- config_name: adl
  set: dfm
- config_name: botxt
  set: dfm
- config_name: dannet
  set: dfm
- config_name: depbank
  set: dfm
- config_name: ep
  set: dfm
- config_name: ft
  set: dfm
- config_name: gutenberg
  set: dfm
- config_name: hest
  set: dfm
- config_name: jvj
  set: dfm
- config_name: naat
  set: dfm
- config_name: relig
  set: dfm
- config_name: retsinformationdk
  set: dfm
- config_name: retspraksis
  set: dfm
- config_name: skat
  set: dfm
- config_name: spont
  set: dfm
- config_name: synne
  set: dfm
- config_name: tv2r
  set: dfm
- config_name: wiki
  set: dfm
- config_name: wikibooks
  set: dfm
- config_name: wikisource
  set: dfm
- config_name: dsk-alexandra
  set: dfm
- config_name: dsk-atp
  set: dfm
- config_name: dsk-cbrain
  set: dfm
- config_name: dsk-danskerhverv
  set: dfm
- config_name: dsk-dkmedier
  set: dfm
- config_name: dsk-hofor
  set: dfm
- config_name: dsk-ida
  set: dfm
- config_name: dsk-odense
  set: dfm
- config_name: dsk-plesner
  set: dfm
- config_name: dsk-salling
  set: dfm
- config_name: dsk-vejle
  set: dfm
- config_name: dsk-vitec
  set: dfm
- config_name: plandata
  set: dfm
- config_name: ai-aktindsigt
  set: dfm
- config_name: danske-taler
  set: dfm
- config_name: fm-udgivelser
  set: dfm
- config_name: eur-lex-sum-da
  set: dfm
- config_name: memo
  set: dfm
- config_name: miljoeportalen
  set: dfm
- config_name: nordjyllandnews
  set: dfm
- config_name: nota
  set: dfm
- config_name: opensubtitles
  set: dfm
- config_name: cellar
  set: dfm
- config_name: ncc_books
  set: dfm
- config_name: ncc_maalfrid
  set: dfm
- config_name: ncc_newspaper
  set: dfm
- config_name: ncc_parliament
  set: dfm
- config_name: dbc-abstracts
  set: dfm
- config_name: dbc-faktalink
  set: dfm
- config_name: dbc-forfatterweb
  set: dfm
- config_name: dbc-reviews
  set: dfm
- config_name: danish-pd
  set: dfm
- config_name: cvr-reports
  set: dfm
- config_name: health_hovedstaden
  set: dfm
- config_name: grundtvig
  set: dfm
- config_name: domsdatabasen
  set: dfm
- config_name: enevaeldens_nyheder
  set: dfm
- config_name: arxiv_abstracts_filtered
  set: common-pile
- config_name: arxiv_papers_filtered
  set: common-pile
- config_name: biodiversity_heritage_library_filtered
  set: common-pile
- config_name: caselaw_access_project_filtered
  set: common-pile
- config_name: cccc_filtered
  set: common-pile
- config_name: data_provenance_initiative_filtered
  set: common-pile
- config_name: doab_filtered
  set: common-pile
- config_name: github_archive_filtered
  set: common-pile
- config_name: library_of_congress_filtered
  set: common-pile
- config_name: libretexts_filtered
  set: common-pile
- config_name: news_filtered
  set: common-pile
- config_name: oercommons_filtered
  set: common-pile
- config_name: peS2o_filtered
  set: common-pile
- config_name: pre_1929_books_filtered
  set: common-pile
- config_name: pressbooks_filtered
  set: common-pile
- config_name: project_gutenberg_filtered
  set: common-pile
- config_name: public_domain_review_filtered
  set: common-pile
- config_name: pubmed_filtered
  set: common-pile
- config_name: python_enhancement_proposals_filtered
  set: common-pile
- config_name: regulations_filtered
  set: common-pile
- config_name: stackexchange_filtered
  set: common-pile
- config_name: stackv2_edu_filtered
  set: common-pile
- config_name: ubuntu_irc_filtered
  set: common-pile
- config_name: uk_hansard_filtered
  set: common-pile
- config_name: usgpo_filtered
  set: common-pile
- config_name: uspto_filtered
  set: common-pile
- config_name: wikimedia_filtered
  set: common-pile
- config_name: wikiteam_filtered
  set: common-pile
- config_name: youtube_filtered
  set: common-pile
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
---

# DFM Datasheets

This repository contains the datasheets for DFM. This repostory documents.

<!-- START README TABLE -->
|             |                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Version** | 1.0.1 ([Changelog](/CHANGELOG.md)) |
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
    - [Languages](#languages)
    - [Domains](#domains)
    - [Licensing](#licensing)
    - [Dataset Statistics](#dataset-statistics)
  - [Additional Information](#additional-information)
    - [Citation Information](#citation-information)
    - [Disclaimer](#disclaimer)
    - [Notice and take down policy](#notice-and-take-down-policy)

## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 230.07M
- **Number of tokens (Llama 3)**: 430.24B
- **Average document length in tokens (min, max)**: 1.87K (1, 51.77M)
<!-- END-DESC-STATS -->

### Summary

The DFM Datasheets is a collection of datasheets for datasets used for [Danish Foundation Models](https://www.foundationmodels.dk). This repository ensure documentation to data along with FAIR data practices.

### Curation Rationale

These datasets were collected and curated with the intention of developing language models for Danish.

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

This dynaword consist of data from various domains (e.g., legal, books, social media). The following table and figure give an overview of the relative distributions of these domains. To see a full overview of the source check out the [source data section](#source-data)

<div style="display: flex; gap: 20px; align-items: flex-start;">

<div style="flex: 1;">


<!-- START-DOMAIN TABLE -->
| Domain       | Sources                                                                                                                                                                                                                                                                                                                                                 | N. Tokens   |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| Legal        | [retsinformationdk], [retspraksis], [skat], [fm-udgivelser], [eur-lex-sum-da], [miljoeportalen], [cellar], [domsdatabasen], [caselaw_access_project_filtered], [uspto_filtered]                                                                                                                                                                         | 162.19B     |
| Other        | [dannet], [depbank], [synne], [dsk-cbrain], [dsk-hofor], [dsk-plesner], [dsk-vitec], [ncc_parliament], [data_provenance_initiative_filtered], [public_domain_review_filtered], [stackv2_edu_filtered]                                                                                                                                                   | 63.56B      |
| Scientific   | [arxiv_abstracts_filtered], [arxiv_papers_filtered], [peS2o_filtered]                                                                                                                                                                                                                                                                                   | 46.15B      |
| Books        | [adl], [gutenberg], [jvj], [relig], [wikibooks], [memo], [ncc_books], [dbc-abstracts], [dbc-reviews], [danish-pd], [grundtvig], [biodiversity_heritage_library_filtered], [doab_filtered], [library_of_congress_filtered], [libretexts_filtered], [oercommons_filtered], [pre_1929_books_filtered], [pressbooks_filtered], [project_gutenberg_filtered] | 37.19B      |
| Medical      | [health_hovedstaden], [pubmed_filtered]                                                                                                                                                                                                                                                                                                                 | 35.35B      |
| Conversation | [ep], [ft], [naat], [spont], [danske-taler], [opensubtitles], [github_archive_filtered], [stackexchange_filtered], [ubuntu_irc_filtered]                                                                                                                                                                                                                | 34.30B      |
| Encyclopedic | [wiki], [wikisource], [dbc-faktalink], [dbc-forfatterweb], [wikimedia_filtered], [wikiteam_filtered]                                                                                                                                                                                                                                                    | 17.21B      |
| Web          | [dsk-alexandra], [dsk-atp], [dsk-salling], [dsk-vejle], [ai-aktindsigt], [ncc_maalfrid], [cccc_filtered]                                                                                                                                                                                                                                                | 14.20B      |
| Governmental | [plandata], [regulations_filtered], [uk_hansard_filtered], [usgpo_filtered]                                                                                                                                                                                                                                                                             | 12.10B      |
| Speeches     | [youtube_filtered]                                                                                                                                                                                                                                                                                                                                      | 4.07B       |
| Financial    | [cvr-reports]                                                                                                                                                                                                                                                                                                                                           | 2.32B       |
| News         | [tv2r], [dsk-danskerhverv], [dsk-dkmedier], [dsk-ida], [dsk-odense], [nordjyllandnews], [ncc_newspaper], [enevaeldens_nyheder], [news_filtered]                                                                                                                                                                                                         | 1.22B       |
| Social Media | [hest]                                                                                                                                                                                                                                                                                                                                                  | 389.32M     |
| Readaloud    | [nota]                                                                                                                                                                                                                                                                                                                                                  | 7.30M       |
| Technical    | [python_enhancement_proposals_filtered]                                                                                                                                                                                                                                                                                                                 | 2.54M       |
| Dialect      | [botxt]                                                                                                                                                                                                                                                                                                                                                 | 847.97K     |
| **Total**    |                                                                                                                                                                                                                                                                                                                                                         | 430.24B     |

[adl]: data/adl/adl.md
[botxt]: data/botxt/botxt.md
[dannet]: data/dannet/dannet.md
[depbank]: data/depbank/depbank.md
[ep]: data/ep/ep.md
[ft]: data/ft/ft.md
[gutenberg]: data/gutenberg/gutenberg.md
[hest]: data/hest/hest.md
[jvj]: data/jvj/jvj.md
[naat]: data/naat/naat.md
[relig]: data/relig/relig.md
[retsinformationdk]: data/retsinformationdk/retsinformationdk.md
[retspraksis]: data/retspraksis/retspraksis.md
[skat]: data/skat/skat.md
[spont]: data/spont/spont.md
[synne]: data/synne/synne.md
[tv2r]: data/tv2r/tv2r.md
[wiki]: data/wiki/wiki.md
[wikibooks]: data/wikibooks/wikibooks.md
[wikisource]: data/wikisource/wikisource.md
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
[plandata]: data/plandata/plandata.md
[ai-aktindsigt]: data/ai-aktindsigt/ai-aktindsigt.md
[danske-taler]: data/danske-taler/danske-taler.md
[fm-udgivelser]: data/fm-udgivelser/fm-udgivelser.md
[eur-lex-sum-da]: data/eur-lex-sum-da/eur-lex-sum-da.md
[memo]: data/memo/memo.md
[miljoeportalen]: data/miljoeportalen/miljoeportalen.md
[nordjyllandnews]: data/nordjyllandnews/nordjyllandnews.md
[nota]: data/nota/nota.md
[opensubtitles]: data/opensubtitles/opensubtitles.md
[cellar]: data/cellar/cellar.md
[ncc_books]: data/ncc_books/ncc_books.md
[ncc_maalfrid]: data/ncc_maalfrid/ncc_maalfrid.md
[ncc_newspaper]: data/ncc_newspaper/ncc_newspaper.md
[ncc_parliament]: data/ncc_parliament/ncc_parliament.md
[dbc-abstracts]: data/dbc-abstracts/dbc-abstracts.md
[dbc-faktalink]: data/dbc-faktalink/dbc-faktalink.md
[dbc-forfatterweb]: data/dbc-forfatterweb/dbc-forfatterweb.md
[dbc-reviews]: data/dbc-reviews/dbc-reviews.md
[danish-pd]: data/danish-pd/danish-pd.md
[cvr-reports]: data/cvr-reports/cvr-reports.md
[health_hovedstaden]: data/health_hovedstaden/health_hovedstaden.md
[grundtvig]: data/grundtvig/grundtvig.md
[domsdatabasen]: data/domsdatabasen/domsdatabasen.md
[enevaeldens_nyheder]: data/enevaeldens_nyheder/enevaeldens_nyheder.md
[arxiv_abstracts_filtered]: data/arxiv_abstracts_filtered/arxiv_abstracts_filtered.md
[arxiv_papers_filtered]: data/arxiv_papers_filtered/arxiv_papers_filtered.md
[biodiversity_heritage_library_filtered]: data/biodiversity_heritage_library_filtered/biodiversity_heritage_library_filtered.md
[caselaw_access_project_filtered]: data/caselaw_access_project_filtered/caselaw_access_project_filtered.md
[cccc_filtered]: data/cccc_filtered/cccc_filtered.md
[data_provenance_initiative_filtered]: data/data_provenance_initiative_filtered/data_provenance_initiative_filtered.md
[doab_filtered]: data/doab_filtered/doab_filtered.md
[github_archive_filtered]: data/github_archive_filtered/github_archive_filtered.md
[library_of_congress_filtered]: data/library_of_congress_filtered/library_of_congress_filtered.md
[libretexts_filtered]: data/libretexts_filtered/libretexts_filtered.md
[news_filtered]: data/news_filtered/news_filtered.md
[oercommons_filtered]: data/oercommons_filtered/oercommons_filtered.md
[peS2o_filtered]: data/peS2o_filtered/peS2o_filtered.md
[pre_1929_books_filtered]: data/pre_1929_books_filtered/pre_1929_books_filtered.md
[pressbooks_filtered]: data/pressbooks_filtered/pressbooks_filtered.md
[project_gutenberg_filtered]: data/project_gutenberg_filtered/project_gutenberg_filtered.md
[public_domain_review_filtered]: data/public_domain_review_filtered/public_domain_review_filtered.md
[pubmed_filtered]: data/pubmed_filtered/pubmed_filtered.md
[python_enhancement_proposals_filtered]: data/python_enhancement_proposals_filtered/python_enhancement_proposals_filtered.md
[regulations_filtered]: data/regulations_filtered/regulations_filtered.md
[stackexchange_filtered]: data/stackexchange_filtered/stackexchange_filtered.md
[stackv2_edu_filtered]: data/stackv2_edu_filtered/stackv2_edu_filtered.md
[ubuntu_irc_filtered]: data/ubuntu_irc_filtered/ubuntu_irc_filtered.md
[uk_hansard_filtered]: data/uk_hansard_filtered/uk_hansard_filtered.md
[usgpo_filtered]: data/usgpo_filtered/usgpo_filtered.md
[uspto_filtered]: data/uspto_filtered/uspto_filtered.md
[wikimedia_filtered]: data/wikimedia_filtered/wikimedia_filtered.md
[wikiteam_filtered]: data/wikiteam_filtered/wikiteam_filtered.md
[youtube_filtered]: data/youtube_filtered/youtube_filtered.md
<!-- END-DOMAIN TABLE -->

</div>

<div style="flex: 1;">

<p align="center">
<img src="./images/domain_distribution.png" width="400" style="margin-right: 10px;" />
</p>

</div>

</div>


### Licensing

The following gives an overview of the licensing in the Dynaword. To get the exact license of the individual datasets check out the [overview table](#source-data).
These license is applied to the constituent data, i.e., the text. The collection of datasets (metadata, quality control, etc.) is licensed under [CC-0](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en).

<!-- START-LICENSE TABLE -->
| License                                         | Sources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | N. Tokens   |
|:------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| Public Domain                                   | [danish-pd], [python_enhancement_proposals_filtered], [regulations_filtered], [ubuntu_irc_filtered], [usgpo_filtered], [uspto_filtered]                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 153.74B     |
| CC-BY-SA 4.0                                    | [depbank], [jvj], [tv2r], [fm-udgivelser], [eur-lex-sum-da], [memo], [cellar], [doab_filtered], [libretexts_filtered], [news_filtered], [oercommons_filtered], [peS2o_filtered], [pressbooks_filtered], [public_domain_review_filtered], [pubmed_filtered], [stackexchange_filtered], [wikimedia_filtered], [wikiteam_filtered], [youtube_filtered]                                                                                                                                                                                                                                      | 122.21B     |
| CC-0                                            | [adl], [botxt], [ep], [ft], [hest], [naat], [relig], [retspraksis], [skat], [spont], [synne], [wiki], [wikibooks], [wikisource], [danske-taler], [miljoeportalen], [nordjyllandnews], [nota], [opensubtitles], [ncc_books], [ncc_newspaper], [health_hovedstaden], [grundtvig], [enevaeldens_nyheder], [arxiv_abstracts_filtered], [arxiv_papers_filtered], [biodiversity_heritage_library_filtered], [caselaw_access_project_filtered], [cccc_filtered], [data_provenance_initiative_filtered], [library_of_congress_filtered], [pre_1929_books_filtered], [project_gutenberg_filtered] | 74.04B      |
| Various - MIT, BSD-3-Clause, Apache-2.0, etc.   | [github_archive_filtered], [stackv2_edu_filtered]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 72.60B      |
| Verbal agreement                                | [cvr-reports]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2.32B       |
| Open Parliament License                         | [uk_hansard_filtered]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 2.01B       |
| Written agreement (public models, private data) | [plandata], [dbc-abstracts], [dbc-faktalink], [dbc-forfatterweb], [dbc-reviews]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.78B       |
| Other (No attribution required)                 | [retsinformationdk], [domsdatabasen]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 904.61M     |
| Other (Attribution required)                    | [dannet], [gutenberg], [ai-aktindsigt], [ncc_maalfrid], [ncc_parliament]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 515.61M     |
| DSK-1                                           | [dsk-alexandra], [dsk-atp], [dsk-cbrain], [dsk-danskerhverv], [dsk-dkmedier], [dsk-hofor], [dsk-ida], [dsk-odense], [dsk-plesner], [dsk-salling], [dsk-vejle], [dsk-vitec]                                                                                                                                                                                                                                                                                                                                                                                                               | 113.35M     |
| **Total**                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 430.24B     |

[adl]: data/adl/adl.md
[botxt]: data/botxt/botxt.md
[dannet]: data/dannet/dannet.md
[depbank]: data/depbank/depbank.md
[ep]: data/ep/ep.md
[ft]: data/ft/ft.md
[gutenberg]: data/gutenberg/gutenberg.md
[hest]: data/hest/hest.md
[jvj]: data/jvj/jvj.md
[naat]: data/naat/naat.md
[relig]: data/relig/relig.md
[retsinformationdk]: data/retsinformationdk/retsinformationdk.md
[retspraksis]: data/retspraksis/retspraksis.md
[skat]: data/skat/skat.md
[spont]: data/spont/spont.md
[synne]: data/synne/synne.md
[tv2r]: data/tv2r/tv2r.md
[wiki]: data/wiki/wiki.md
[wikibooks]: data/wikibooks/wikibooks.md
[wikisource]: data/wikisource/wikisource.md
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
[plandata]: data/plandata/plandata.md
[ai-aktindsigt]: data/ai-aktindsigt/ai-aktindsigt.md
[danske-taler]: data/danske-taler/danske-taler.md
[fm-udgivelser]: data/fm-udgivelser/fm-udgivelser.md
[eur-lex-sum-da]: data/eur-lex-sum-da/eur-lex-sum-da.md
[memo]: data/memo/memo.md
[miljoeportalen]: data/miljoeportalen/miljoeportalen.md
[nordjyllandnews]: data/nordjyllandnews/nordjyllandnews.md
[nota]: data/nota/nota.md
[opensubtitles]: data/opensubtitles/opensubtitles.md
[cellar]: data/cellar/cellar.md
[ncc_books]: data/ncc_books/ncc_books.md
[ncc_maalfrid]: data/ncc_maalfrid/ncc_maalfrid.md
[ncc_newspaper]: data/ncc_newspaper/ncc_newspaper.md
[ncc_parliament]: data/ncc_parliament/ncc_parliament.md
[dbc-abstracts]: data/dbc-abstracts/dbc-abstracts.md
[dbc-faktalink]: data/dbc-faktalink/dbc-faktalink.md
[dbc-forfatterweb]: data/dbc-forfatterweb/dbc-forfatterweb.md
[dbc-reviews]: data/dbc-reviews/dbc-reviews.md
[danish-pd]: data/danish-pd/danish-pd.md
[cvr-reports]: data/cvr-reports/cvr-reports.md
[health_hovedstaden]: data/health_hovedstaden/health_hovedstaden.md
[grundtvig]: data/grundtvig/grundtvig.md
[domsdatabasen]: data/domsdatabasen/domsdatabasen.md
[enevaeldens_nyheder]: data/enevaeldens_nyheder/enevaeldens_nyheder.md
[arxiv_abstracts_filtered]: data/arxiv_abstracts_filtered/arxiv_abstracts_filtered.md
[arxiv_papers_filtered]: data/arxiv_papers_filtered/arxiv_papers_filtered.md
[biodiversity_heritage_library_filtered]: data/biodiversity_heritage_library_filtered/biodiversity_heritage_library_filtered.md
[caselaw_access_project_filtered]: data/caselaw_access_project_filtered/caselaw_access_project_filtered.md
[cccc_filtered]: data/cccc_filtered/cccc_filtered.md
[data_provenance_initiative_filtered]: data/data_provenance_initiative_filtered/data_provenance_initiative_filtered.md
[doab_filtered]: data/doab_filtered/doab_filtered.md
[github_archive_filtered]: data/github_archive_filtered/github_archive_filtered.md
[library_of_congress_filtered]: data/library_of_congress_filtered/library_of_congress_filtered.md
[libretexts_filtered]: data/libretexts_filtered/libretexts_filtered.md
[news_filtered]: data/news_filtered/news_filtered.md
[oercommons_filtered]: data/oercommons_filtered/oercommons_filtered.md
[peS2o_filtered]: data/peS2o_filtered/peS2o_filtered.md
[pre_1929_books_filtered]: data/pre_1929_books_filtered/pre_1929_books_filtered.md
[pressbooks_filtered]: data/pressbooks_filtered/pressbooks_filtered.md
[project_gutenberg_filtered]: data/project_gutenberg_filtered/project_gutenberg_filtered.md
[public_domain_review_filtered]: data/public_domain_review_filtered/public_domain_review_filtered.md
[pubmed_filtered]: data/pubmed_filtered/pubmed_filtered.md
[python_enhancement_proposals_filtered]: data/python_enhancement_proposals_filtered/python_enhancement_proposals_filtered.md
[regulations_filtered]: data/regulations_filtered/regulations_filtered.md
[stackexchange_filtered]: data/stackexchange_filtered/stackexchange_filtered.md
[stackv2_edu_filtered]: data/stackv2_edu_filtered/stackv2_edu_filtered.md
[ubuntu_irc_filtered]: data/ubuntu_irc_filtered/ubuntu_irc_filtered.md
[uk_hansard_filtered]: data/uk_hansard_filtered/uk_hansard_filtered.md
[usgpo_filtered]: data/usgpo_filtered/usgpo_filtered.md
[uspto_filtered]: data/uspto_filtered/uspto_filtered.md
[wikimedia_filtered]: data/wikimedia_filtered/wikimedia_filtered.md
[wikiteam_filtered]: data/wikiteam_filtered/wikiteam_filtered.md
[youtube_filtered]: data/youtube_filtered/youtube_filtered.md
<!-- END-LICENSE TABLE -->

### Source Data

Below follows a brief overview of the sources in the corpus along with their individual license. To get more information about the individual dataset click the hyperlink in the table.

<details>
<summary><b>Overview Table (click to unfold)</b></summary>

You can learn more about each dataset by pressing the link in the first column.

<!-- START-MAIN TABLE -->
| Source                                   | Description                                                                                                                                                                                                                        | Domain       | Language   | N. Tokens   | License                                           |
|:-----------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|:-----------|:------------|:--------------------------------------------------|
| [uspto_filtered]                         | In the United States, patent documents are released into the public domain as government works                                                                                                                                     | Legal        | English    | 142.39B     | [Public Domain]                                   |
| [stackv2_edu_filtered]                   | Stack V2 Edu is a dataset containing files in various programming and markup languages from openly licensed projects                                                                                                               | Other        | English    | 62.39B      | [Various - MIT, BSD-3-Clause, Apache-2.0, etc.]   |
| [peS2o_filtered]                         | A set of openly licensed scientific articles                                                                                                                                                                                       | Scientific   | English    | 39.51B      | [CC-BY-SA 4.0]                                    |
| [pubmed_filtered]                        | A set of permissively licensed papers collected from tthe PubMed Central                                                                                                                                                           | Medical      | English    | 35.32B      | [CC-BY-SA 4.0]                                    |
| [stackexchange_filtered]                 | StackExchange is a collection of Q&A communities spanning a wide variety of topics                                                                                                                                                 | Conversation | English    | 21.83B      | [CC-BY-SA 4.0]                                    |
| [caselaw_access_project_filtered]        | The Caselaw Access Project consists of nearly 40 million pages of U.S. federal and state court decisions and judges’ opinions from the last 365 years                                                                              | Legal        | English    | 17.36B      | [CC-0]                                            |
| [wikimedia_filtered]                     | Official Wikimedia wikis are released under a CC BY-SA license                                                                                                                                                                     | Encyclopedic | English    | 14.08B      | [CC-BY-SA 4.0]                                    |
| [cccc_filtered]                          | A dataset consisting of permissively licensed web pages processed from common crawl                                                                                                                                                | Web          | English    | 13.99B      | [CC-0]                                            |
| [pre_1929_books_filtered]                | A set of books published in the US pre-1929                                                                                                                                                                                        | Books        | English    | 10.56B      | [CC-0]                                            |
| [github_archive_filtered]                | A large set of issues and pull request descriptions along with their comments                                                                                                                                                      | Conversation | English    | 10.21B      | [Various - MIT, BSD-3-Clause, Apache-2.0, etc.]   |
| [biodiversity_heritage_library_filtered] | A set of ~15 million public domain books and documents from the BHL collection                                                                                                                                                     | Books        | English    | 8.62B       | [CC-0]                                            |
| [library_of_congress_filtered]           | A large set of public domain books from the "Selected Digitized Books" collection                                                                                                                                                  | Books        | English    | 8.06B       | [CC-0]                                            |
| [usgpo_filtered]                         | The United States Government Publishing Office (USGPO) is a federal agency responsible for disseminating official documents authored by the U.S. government                                                                        | Governmental | English    | 7.78B       | [Public Domain]                                   |
| [arxiv_papers_filtered]                  | Set of public domain papers, published on ArXiv                                                                                                                                                                                    | Scientific   | English    | 6.11B       | [CC-0]                                            |
| [project_gutenberg_filtered]             | All books from project gutenberg marked as english and public domain                                                                                                                                                               | Books        | English    | 4.91B       | [CC-0]                                            |
| [youtube_filtered]                       | YouTube is a large-scale video-sharing platform where users have the option of uploading content under a CC BY license                                                                                                             | Speeches     | English    | 4.07B       | [CC-BY-SA 4.0]                                    |
| [wikiteam_filtered]                      | There are many wikis on the internet that are not managed by the Wikimedia Foundation, but do use their MediaWiki software to power their wiki                                                                                     | Encyclopedic | English    | 2.94B       | [CC-BY-SA 4.0]                                    |
| [doab_filtered]                          | The Directory of Open Access Books (DOAB) is an online index of over 94,000 peer-reviewed books curated from trusted open-access publishers                                                                                        | Books        | English    | 2.80B       | [CC-BY-SA 4.0]                                    |
| [cvr-reports]                            | Annual reports from danish companies in the period 2010-2025                                                                                                                                                                       | Financial    | Danish     | 2.32B       | [Verbal agreement]                                |
| [uk_hansard_filtered]                    | Hansard represents the official record of parliamentary proceedings across the United Kingdom’s legislative bodies                                                                                                                 | Governmental | English    | 2.01B       | [Open Parliament License]                         |
| [ubuntu_irc_filtered]                    | Ubuntu-hosted Internet Relay Chat (IRC) is an online chat service                                                                                                                                                                  | Conversation | English    | 1.76B       | [Public Domain]                                   |
| [regulations_filtered]                   | This dataset includes all plain-text regulatory documents published by a variety of U.S. federal agencies on Regulations.Gov                                                                                                       | Governmental | English    | 1.28B       | [Public Domain]                                   |
| [cellar]                                 | The official digital repository for European Union legal documents and open data                                                                                                                                                   | Legal        | Danish     | 1.15B       | [CC-BY-SA 4.0]                                    |
| [enevaeldens_nyheder]                    | High quality OCR'd texts from Danish and Norwegian newspapers during the period of constitutional absolutism in Denmark (1660–1849)                                                                                                | News         | Danish     | 1.03B       | [CC-0]                                            |
| [plandata]                               | A comprehensive dataset consisting of municipal planning documents from across Denmark, including local development plans, municipal plans, planning strategies, and related document types                                        | Governmental | Danish     | 1.03B       | [Written agreement (public models, private data)] |
| [retsinformationdk]                      | [retsinformation.dk](https://www.retsinformation.dk) (legal-information.dk) the official legal information system of Denmark                                                                                                       | Legal        | Danish     | 818.25M     | [Danish Copyright Law]                            |
| [data_provenance_initiative_filtered]    | The Data Provenance Initiative is a digital library of supervised datasets that have been manually annotated with their source and license information                                                                             | Other        | English    | 817.36M     | [CC-0]                                            |
| [dbc-abstracts]                          | dbc-abstracts consists of more than 11.6 million abstracts of books and other materials collected and created by [DBC D1G1TAL](https://dbcdigital.dk/) (former Dansk Bibliotekscenter)                                             | Books        | Danish     | 694.42M     | [Written agreement (public models, private data)] |
| [danish-pd]                              | **PleIAs - Danish Public Domain** is a large collection aiming to aggregate all Danish monographies and periodicals in the public domain                                                                                           | Books        | Danish     | 532.43M     | [Public Domain]                                   |
| [ncc_books]                              | Danish books extracted from the [Norwegian Colossal Corpus](https://huggingface.co/datasets/NbAiLab/NCC) derived from OCR                                                                                                          | Books        | Danish     | 531.97M     | [CC-0]                                            |
| [arxiv_abstracts_filtered]               | A set of public domain arxiv paper abstracts                                                                                                                                                                                       | Scientific   | English    | 524.45M     | [CC-0]                                            |
| [hest]                                   | Samples from the Danish debate forum www.heste-nettet.dk                                                                                                                                                                           | Social Media | Danish     | 389.32M     | [CC-0]                                            |
| [ncc_parliament]                         | Collections from the Norwegian parliament in Danish. Extracted from the [Norwegian Colossal Corpus](https://huggingface.co/datasets/NbAiLab/NCC) derived from ocr                                                                  | Other        | Danish     | 338.87M     | [NLOD 2.0]                                        |
| [opensubtitles]                          | Danish subsection of [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles)                                                                                                                              | Conversation | Danish     | 271.60M     | [CC-0]                                            |
| [wiki]                                   | The Danish subsection of [wikipedia](https://en.wikipedia.org/wiki/Main_Page)                                                                                                                                                      | Encyclopedic | Danish     | 172.43M     | [CC-0]                                            |
| [ai-aktindsigt]                          | Multiple web scrapes from municipality websites collected as a part of the [AI-aktindsigt](https://ai-aktindsigt.dk) project                                                                                                       | Web          | Danish     | 139.23M     | [Apache 2.0]                                      |
| [miljoeportalen]                         | Data from [Danmarks Miljøportalen](https://www.miljoeportal.dk/om-danmarks-miljoeportal/) (Denmark's Environment Portal)                                                                                                           | Legal        | Danish     | 127.38M     | [CC-0]                                            |
| [pressbooks_filtered]                    | A set of openly licensed books                                                                                                                                                                                                     | Books        | English    | 125.65M     | [CC-BY-SA 4.0]                                    |
| [skat]                                   | Skat is the Danish tax authority. This dataset contains content from its website skat.dk                                                                                                                                           | Legal        | Danish     | 122.11M     | [CC-0]                                            |
| [ft]                                     | Records from all meetings of The Danish parliament (Folketinget) in the parliament hall                                                                                                                                            | Conversation | Danish     | 114.09M     | [CC-0]                                            |
| [memo]                                   | The MeMo corpus comprising almost all Danish novels from the period 1870-1899, known as the Modern Breakthrough                                                                                                                    | Books        | Danish     | 113.74M     | [CC-BY-SA 4.0]                                    |
| [ep]                                     | The Danish subsection of [Europarl](https://aclanthology.org/2005.mtsummit-papers.11/)                                                                                                                                             | Conversation | Danish     | 100.84M     | [CC-0]                                            |
| [domsdatabasen]                          | [Domsdatabasen.dk](https://domsdatabasen.dk/) is a public database containing selected judgments from the Danish courts                                                                                                            | Legal        | Danish     | 86.35M      | [Danish Copyright Law]                            |
| [libretexts_filtered]                    | A catalog of open-access text books                                                                                                                                                                                                | Books        | English    | 84.19M      | [CC-BY-SA 4.0]                                    |
| [dsk-dkmedier]                           | A collection of ~100K news articles from [DK Medier](https://dkmedier.dk), written in the period 2000-2024                                                                                                                         | News         | Danish     | 63.64M      | [DSK-1]                                           |
| [adl]                                    | Danish literature from 1700-2023 from the [Archive for Danish Literature](https://tekster.kb.dk/text?editorial=no&f%5Bsubcollection_ssi%5D%5B%5D=adl&match=one&search_field=Alt) (ADL)                                             | Books        | Danish     | 58.49M      | [CC-0]                                            |
| [retspraksis]                            | Case law or judical practice in Denmark derived from [Retspraksis](https://da.wikipedia.org/wiki/Retspraksis)                                                                                                                      | Legal        | Danish     | 56.26M      | [CC-0]                                            |
| [dbc-reviews]                            | dbc-reviews consists of more than 214 thousand reviews of books and other materials collected and created by DBC D1G1TAL (former Dansk Bibliotekscenter)                                                                           | Books        | Danish     | 53.96M      | [Written agreement (public models, private data)] |
| [news_filtered]                          | A set of news stories, scraped from opennewswire                                                                                                                                                                                   | News         | English    | 53.77M      | [CC-BY-SA 4.0]                                    |
| [fm-udgivelser]                          | The official publication series of the Danish Ministry of Finance containing economic analyses, budget proposals, and fiscal policy documents                                                                                      | Legal        | Danish     | 50.34M      | [CC-BY-SA 4.0]                                    |
| [nordjyllandnews]                        | Articles from the Danish Newspaper [TV2 Nord](https://www.tv2nord.dk)                                                                                                                                                              | News         | Danish     | 37.90M      | [CC-0]                                            |
| [eur-lex-sum-da]                         | The Danish subsection of EUR-lex SUM consisting of EU legislation paired with professionally written summaries                                                                                                                     | Legal        | Danish     | 31.37M      | [CC-BY-SA 4.0]                                    |
| [ncc_maalfrid]                           | Danish content from Norwegian institutions websites                                                                                                                                                                                | Web          | Danish     | 29.26M      | [NLOD 2.0]                                        |
| [dsk-vejle]                              | A collection of crawled webpages that is managed by Vejle Kommune. Contains various information, covering everything from tourists to garbage collection to historical knowledge of the area                                       | Web          | Danish     | 27.99M      | [DSK-1]                                           |
| [health_hovedstaden]                     | Guidelines and informational documents for healthcare professionals from the Capital Region                                                                                                                                        | Medical      | Danish     | 27.07M      | [CC-0]                                            |
| [tv2r]                                   | Contemporary Danish newswire articles published between 2010 and 2019                                                                                                                                                              | News         | Danish     | 21.67M      | [CC-BY-SA 4.0]                                    |
| [oercommons_filtered]                    | OERCommons is an online platform where educators share open-access instructional materials—such as textbooks, lesson plans, problem sets, course syllabi, and worksheets—with the goal of expanding access to affordable education | Books        | English    | 10.82M      | [CC-BY-SA 4.0]                                    |
| [grundtvig]                              | The complete collection of [Grundtvig](https://en.wikipedia.org/wiki/N._F._S._Grundtvig) (1783-1872) one of Denmark’s most influential figures                                                                                     | Books        | Danish     | 10.53M      | [CC-0]                                            |
| [dsk-salling]                            | A collection of crawled webpages that is managed by Salling Group. The dataset consists mainly of product pages from online stores such as bilka.dk, br.dk and such. The data consists of ~24K webpages                            | Web          | Danish     | 9.79M       | [DSK-1]                                           |
| [danske-taler]                           | Danish Speeches from [dansketaler.dk](https://www.dansketaler.dk)                                                                                                                                                                  | Conversation | Danish     | 8.72M       | [CC-0]                                            |
| [wikibooks]                              | The Danish Subsection of [Wikibooks](https://www.wikibooks.org)                                                                                                                                                                    | Books        | Danish     | 7.63M       | [CC-0]                                            |
| [nota]                                   | The text only part of the [Nota lyd- og tekstdata](https://sprogteknologi.dk/dataset/nota-lyd-og-tekstdata) dataset                                                                                                                | Readaloud    | Danish     | 7.30M       | [CC-0]                                            |
| [gutenberg]                              | The Danish subsection from Project [Gutenberg](https://www.gutenberg.org)                                                                                                                                                          | Books        | Danish     | 6.76M       | [Gutenberg]                                       |
| [wikisource]                             | The Danish subsection of [Wikisource](https://en.wikisource.org/wiki/Main_Page)                                                                                                                                                    | Encyclopedic | Danish     | 6.28M       | [CC-0]                                            |
| [dsk-cbrain]                             | A collection of Marketing material, product guides, and datasheets produced by cBrain for their products                                                                                                                           | Other        | Danish     | 4.19M       | [DSK-1]                                           |
| [jvj]                                    | The works of the Danish author and poet, [Johannes V. Jensen](https://da.wikipedia.org/wiki/Johannes_V._Jensen)                                                                                                                    | Books        | Danish     | 3.55M       | [CC-BY-SA 4.0]                                    |
| [dsk-atp]                                | A collection of crawled webpages that is managed by ATP                                                                                                                                                                            | Web          | Danish     | 2.86M       | [DSK-1]                                           |
| [python_enhancement_proposals_filtered]  | This set consists of almost all PEPs created                                                                                                                                                                                       | Technical    | English    | 2.54M       | [Public Domain]                                   |
| [dbc-faktalink]                          | dbc-faktalink consists of more than 5 hundred articles created by [DBC D1G1TAL](https://dbcdigital.dk/) (former Dansk Bibliotekscenter)                                                                                            | Encyclopedic | Danish     | 1.99M       | [Written agreement (public models, private data)] |
| [spont]                                  | Conversational samples collected as a part of research projects at Aarhus University                                                                                                                                               | Conversation | Danish     | 1.56M       | [CC-0]                                            |
| [public_domain_review_filtered]          | A set of articles describing works of art that is part of public domain                                                                                                                                                            | Other        | English    | 1.51M       | [CC-BY-SA 4.0]                                    |
| [dannet]                                 | [DanNet](https://cst.ku.dk/projekter/dannet) is a Danish WordNet                                                                                                                                                                   | Other        | Danish     | 1.48M       | [DanNet 1.0]                                      |
| [dbc-forfatterweb]                       | dbc-forfatterweb consists of more than 1 thousand articles created by DBC D1G1TAL (former Dansk Bibliotekscenter)                                                                                                                  | Encyclopedic | Danish     | 1.42M       | [Written agreement (public models, private data)] |
| [relig]                                  | Danish religious text from the 1700-2022                                                                                                                                                                                           | Books        | Danish     | 1.24M       | [CC-0]                                            |
| [dsk-odense]                             | A set of newsletters stories, covering events in Odense Municipality. Have been published on their website                                                                                                                         | News         | Danish     | 1.18M       | [DSK-1]                                           |
| [dsk-danskerhverv]                       | A set of newsletters written by Dansk Erhverv, primarily focusing on financials and companies world wide                                                                                                                           | News         | Danish     | 1.12M       | [DSK-1]                                           |
| [ncc_newspaper]                          | OCR'd Newspapers derived from [NCC](https://huggingface.co/datasets/NbAiLab/NCC)                                                                                                                                                   | News         | Danish     | 1.05M       | [CC-0]                                            |
| [dsk-plesner]                            | A combination of crawled webpages from Plesners own website, and a series of internal documents outlining procedures                                                                                                               | Other        | Danish     | 896.33K     | [DSK-1]                                           |
| [botxt]                                  | The Bornholmsk Ordbog Dictionary Project                                                                                                                                                                                           | Dialect      | Danish     | 847.97K     | [CC-0]                                            |
| [dsk-alexandra]                          | A collection of crawled webpages that is managed by Alexandra Institutet                                                                                                                                                           | Web          | Danish     | 584.35K     | [DSK-1]                                           |
| [dsk-vitec]                              | A collection of documents covering product descriptions, to newsletters, to internal documentation                                                                                                                                 | Other        | Danish     | 537.07K     | [DSK-1]                                           |
| [dsk-ida]                                | A collection of newsletters, articles and other texts produced by IDA                                                                                                                                                              | News         | Danish     | 417.32K     | [DSK-1]                                           |
| [naat]                                   | Danish speeches from 1930-2022                                                                                                                                                                                                     | Conversation | Danish     | 286.68K     | [CC-0]                                            |
| [depbank]                                | The Danish subsection of the [Universal Dependencies Treebank](https://github.com/UniversalDependencies/UD_Danish-DDT)                                                                                                             | Other        | Danish     | 185.45K     | [CC-BY-SA 4.0]                                    |
| [dsk-hofor]                              | A collection of articles, guides and newsletters written by HOFOR for their customers                                                                                                                                              | Other        | Danish     | 143.49K     | [DSK-1]                                           |
| [synne]                                  | Dataset collected from [synnejysk forening's website](https://www.synnejysk.dk), covering the Danish dialect sønderjysk                                                                                                            | Other        | Danish     | 52.02K      | [CC-0]                                            |
| **Total**                                |                                                                                                                                                                                                                                    |              |            | 430.24B     |                                                   |

[adl]: data/adl/adl.md
[botxt]: data/botxt/botxt.md
[dannet]: data/dannet/dannet.md
[depbank]: data/depbank/depbank.md
[ep]: data/ep/ep.md
[ft]: data/ft/ft.md
[gutenberg]: data/gutenberg/gutenberg.md
[hest]: data/hest/hest.md
[jvj]: data/jvj/jvj.md
[naat]: data/naat/naat.md
[relig]: data/relig/relig.md
[retsinformationdk]: data/retsinformationdk/retsinformationdk.md
[retspraksis]: data/retspraksis/retspraksis.md
[skat]: data/skat/skat.md
[spont]: data/spont/spont.md
[synne]: data/synne/synne.md
[tv2r]: data/tv2r/tv2r.md
[wiki]: data/wiki/wiki.md
[wikibooks]: data/wikibooks/wikibooks.md
[wikisource]: data/wikisource/wikisource.md
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
[plandata]: data/plandata/plandata.md
[ai-aktindsigt]: data/ai-aktindsigt/ai-aktindsigt.md
[danske-taler]: data/danske-taler/danske-taler.md
[fm-udgivelser]: data/fm-udgivelser/fm-udgivelser.md
[eur-lex-sum-da]: data/eur-lex-sum-da/eur-lex-sum-da.md
[memo]: data/memo/memo.md
[miljoeportalen]: data/miljoeportalen/miljoeportalen.md
[nordjyllandnews]: data/nordjyllandnews/nordjyllandnews.md
[nota]: data/nota/nota.md
[opensubtitles]: data/opensubtitles/opensubtitles.md
[cellar]: data/cellar/cellar.md
[ncc_books]: data/ncc_books/ncc_books.md
[ncc_maalfrid]: data/ncc_maalfrid/ncc_maalfrid.md
[ncc_newspaper]: data/ncc_newspaper/ncc_newspaper.md
[ncc_parliament]: data/ncc_parliament/ncc_parliament.md
[dbc-abstracts]: data/dbc-abstracts/dbc-abstracts.md
[dbc-faktalink]: data/dbc-faktalink/dbc-faktalink.md
[dbc-forfatterweb]: data/dbc-forfatterweb/dbc-forfatterweb.md
[dbc-reviews]: data/dbc-reviews/dbc-reviews.md
[danish-pd]: data/danish-pd/danish-pd.md
[cvr-reports]: data/cvr-reports/cvr-reports.md
[health_hovedstaden]: data/health_hovedstaden/health_hovedstaden.md
[grundtvig]: data/grundtvig/grundtvig.md
[domsdatabasen]: data/domsdatabasen/domsdatabasen.md
[enevaeldens_nyheder]: data/enevaeldens_nyheder/enevaeldens_nyheder.md
[arxiv_abstracts_filtered]: data/arxiv_abstracts_filtered/arxiv_abstracts_filtered.md
[arxiv_papers_filtered]: data/arxiv_papers_filtered/arxiv_papers_filtered.md
[biodiversity_heritage_library_filtered]: data/biodiversity_heritage_library_filtered/biodiversity_heritage_library_filtered.md
[caselaw_access_project_filtered]: data/caselaw_access_project_filtered/caselaw_access_project_filtered.md
[cccc_filtered]: data/cccc_filtered/cccc_filtered.md
[data_provenance_initiative_filtered]: data/data_provenance_initiative_filtered/data_provenance_initiative_filtered.md
[doab_filtered]: data/doab_filtered/doab_filtered.md
[github_archive_filtered]: data/github_archive_filtered/github_archive_filtered.md
[library_of_congress_filtered]: data/library_of_congress_filtered/library_of_congress_filtered.md
[libretexts_filtered]: data/libretexts_filtered/libretexts_filtered.md
[news_filtered]: data/news_filtered/news_filtered.md
[oercommons_filtered]: data/oercommons_filtered/oercommons_filtered.md
[peS2o_filtered]: data/peS2o_filtered/peS2o_filtered.md
[pre_1929_books_filtered]: data/pre_1929_books_filtered/pre_1929_books_filtered.md
[pressbooks_filtered]: data/pressbooks_filtered/pressbooks_filtered.md
[project_gutenberg_filtered]: data/project_gutenberg_filtered/project_gutenberg_filtered.md
[public_domain_review_filtered]: data/public_domain_review_filtered/public_domain_review_filtered.md
[pubmed_filtered]: data/pubmed_filtered/pubmed_filtered.md
[python_enhancement_proposals_filtered]: data/python_enhancement_proposals_filtered/python_enhancement_proposals_filtered.md
[regulations_filtered]: data/regulations_filtered/regulations_filtered.md
[stackexchange_filtered]: data/stackexchange_filtered/stackexchange_filtered.md
[stackv2_edu_filtered]: data/stackv2_edu_filtered/stackv2_edu_filtered.md
[ubuntu_irc_filtered]: data/ubuntu_irc_filtered/ubuntu_irc_filtered.md
[uk_hansard_filtered]: data/uk_hansard_filtered/uk_hansard_filtered.md
[usgpo_filtered]: data/usgpo_filtered/usgpo_filtered.md
[uspto_filtered]: data/uspto_filtered/uspto_filtered.md
[wikimedia_filtered]: data/wikimedia_filtered/wikimedia_filtered.md
[wikiteam_filtered]: data/wikiteam_filtered/wikiteam_filtered.md
[youtube_filtered]: data/youtube_filtered/youtube_filtered.md


[CC-0]: https://creativecommons.org/publicdomain/zero/1.0/legalcode.en
[CC-BY-SA 4.0]: https://creativecommons.org/licenses/by-sa/4.0/deed.en
[Apache 2.0]: https://www.apache.org/licenses/LICENSE-2.0
[DanNet 1.0]: ./data/dannet/dannet.md#license-information
[Gutenberg]: ./data/gutenberg/gutenberg.md#license-information
[Danish Copyright Law]: ./data/retsinformationdk/retsinformationdk.md#license-information
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
[Written agreement (public models, private data)]: ./data/plandata/plandata.md#license-information
[NLOD 2.0]: ./data/ncc_maalfrid/ncc_maalfrid.md#license-information
[NLOD 2.0]: ./data/ncc_parliament/ncc_parliament.md#license-information
[Written agreement (public models, private data)]: ./data/dbc-abstracts/dbc-abstracts.md#license-information
[Written agreement (public models, private data)]: ./data/dbc-faktalink/dbc-faktalink.md#license-information
[Written agreement (public models, private data)]: ./data/dbc-forfatterweb/dbc-forfatterweb.md#license-information
[Written agreement (public models, private data)]: ./data/dbc-reviews/dbc-reviews.md#license-information
[Public Domain]: ./data/danish-pd/danish-pd.md#license-information
[Verbal agreement]: ./data/cvr-reports/cvr-reports.md#license-information
[Danish Copyright Law]: ./data/domsdatabasen/domsdatabasen.md#license-information
[Various - MIT, BSD-3-Clause, Apache-2.0, etc.]: ./data/github_archive_filtered/github_archive_filtered.md#license-information
[Public Domain]: ./data/python_enhancement_proposals_filtered/python_enhancement_proposals_filtered.md#license-information
[Public Domain]: ./data/regulations_filtered/regulations_filtered.md#license-information
[Various - MIT, BSD-3-Clause, Apache-2.0, etc.]: ./data/stackv2_edu_filtered/stackv2_edu_filtered.md#license-information
[Public Domain]: ./data/ubuntu_irc_filtered/ubuntu_irc_filtered.md#license-information
[Open Parliament License]: ./data/uk_hansard_filtered/uk_hansard_filtered.md#license-information
[Public Domain]: ./data/usgpo_filtered/usgpo_filtered.md#license-information
[Public Domain]: ./data/uspto_filtered/uspto_filtered.md#license-information
<!-- END-MAIN TABLE -->
</details>

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
The following plot pr. dataset histograms displaying document lengths.

<details>
<summary>Per dataset histograms</summary>
<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dataset_size_plot.svg" width="800" style="margin-right: 10px;" />
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
