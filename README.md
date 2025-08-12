---
license: other
configs:
- config_name: default
- config_name: adl
- config_name: botxt
- config_name: dannet
- config_name: depbank
- config_name: ep
- config_name: ft
- config_name: gutenberg
- config_name: hest
- config_name: jvj
- config_name: naat
- config_name: relig
- config_name: retsinformationdk
- config_name: retspraksis
- config_name: skat
- config_name: spont
- config_name: synne
- config_name: tv2r
- config_name: wiki
- config_name: wikibooks
- config_name: wikisource
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
- config_name: plandata
- config_name: ai-aktindsigt
- config_name: danske-taler
- config_name: fm-udgivelser
- config_name: eur-lex-sum-da
- config_name: memo
- config_name: miljoeportalen
- config_name: nordjyllandnews
- config_name: nota
- config_name: opensubtitles
- config_name: cellar
- config_name: ncc_books
- config_name: ncc_maalfrid
- config_name: ncc_newspaper
- config_name: ncc_parliament
- config_name: dbc-abstracts
- config_name: dbc-faktalink
- config_name: dbc-forfatterweb
- config_name: dbc-reviews
- config_name: danish-pd
- config_name: cvr-reports
- config_name: health_hovedstaden
- config_name: grundtvig
- config_name: domsdatabasen
- config_name: enevaeldens_nyheder
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

# DFM Datasheets

This repository contains the datasheets for DFM. This repostory documents.

<!-- START README TABLE -->
|             |                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Version** | 0.0.15 ([Changelog](/CHANGELOG.md)) |
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
- **Number of samples**: 16.23M
- **Number of tokens (Llama 3)**: 10.58B
- **Average document length in tokens (min, max)**: 651.9848074000665 (2, 13.35M)
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


### Domains

This dynaword consist of data from various domains (e.g., legal, books, social media). The following table and figure give an overview of the relative distributions of these domains. To see a full overview of the source check out the [source data section](#source-data)

<div style="display: flex; gap: 20px; align-items: flex-start;">

<div style="flex: 1;">


<!-- START-DOMAIN TABLE -->
<style>
table {
    border-collapse: collapse;
}
th, td {
    border: 1px solid #ddd;
    padding: 6px 10px;
}
th {
    background-color: #f9f9f9;
}
</style>

<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>Domain</th>
      <th>Sources</th>
      <th>N. Tokens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Legal</td>
      <td><a href="data/retsinformationdk/retsinformationdk.md">retsinformationdk</a>, <a href="data/retspraksis/retspraksis.md">retspraksis</a>, <a href="data/skat/skat.md">skat</a>, <a href="data/fm-udgivelser/fm-udgivelser.md">fm-udgivelser</a>, <a href="data/eur-lex-sum-da/eur-lex-sum-da.md">eur-lex-sum-da</a>, <a href="data/miljoeportalen/miljoeportalen.md">miljoeportalen</a>, <a href="data/cellar/cellar.md">cellar</a>, <a href="data/domsdatabasen/domsdatabasen.md">domsdatabasen</a></td>
      <td>2.44B</td>
    </tr>
    <tr>
      <td>Financial</td>
      <td><a href="data/cvr-reports/cvr-reports.md">cvr-reports</a></td>
      <td>2.32B</td>
    </tr>
    <tr>
      <td>Books</td>
      <td><a href="data/adl/adl.md">adl</a>, <a href="data/gutenberg/gutenberg.md">gutenberg</a>, <a href="data/jvj/jvj.md">jvj</a>, <a href="data/relig/relig.md">relig</a>, <a href="data/wikibooks/wikibooks.md">wikibooks</a>, <a href="data/memo/memo.md">memo</a>, <a href="data/ncc_books/ncc_books.md">ncc_books</a>, <a href="data/dbc-abstracts/dbc-abstracts.md">dbc-abstracts</a>, <a href="data/dbc-reviews/dbc-reviews.md">dbc-reviews</a>, <a href="data/danish-pd/danish-pd.md">danish-pd</a>, <a href="data/grundtvig/grundtvig.md">grundtvig</a></td>
      <td>2.01B</td>
    </tr>
    <tr>
      <td>News</td>
      <td><a href="data/tv2r/tv2r.md">tv2r</a>, <a href="data/dsk-danskerhverv/dsk-danskerhverv.md">dsk-danskerhverv</a>, <a href="data/dsk-dkmedier/dsk-dkmedier.md">dsk-dkmedier</a>, <a href="data/dsk-ida/dsk-ida.md">dsk-ida</a>, <a href="data/dsk-odense/dsk-odense.md">dsk-odense</a>, <a href="data/nordjyllandnews/nordjyllandnews.md">nordjyllandnews</a>, <a href="data/ncc_newspaper/ncc_newspaper.md">ncc_newspaper</a>, <a href="data/enevaeldens_nyheder/enevaeldens_nyheder.md">enevaeldens_nyheder</a></td>
      <td>1.16B</td>
    </tr>
    <tr>
      <td>Governmental</td>
      <td><a href="data/plandata/plandata.md">plandata</a></td>
      <td>1.03B</td>
    </tr>
    <tr>
      <td>Conversation</td>
      <td><a href="data/ep/ep.md">ep</a>, <a href="data/ft/ft.md">ft</a>, <a href="data/naat/naat.md">naat</a>, <a href="data/spont/spont.md">spont</a>, <a href="data/danske-taler/danske-taler.md">danske-taler</a>, <a href="data/opensubtitles/opensubtitles.md">opensubtitles</a></td>
      <td>497.09M</td>
    </tr>
    <tr>
      <td>Social Media</td>
      <td><a href="data/hest/hest.md">hest</a></td>
      <td>389.32M</td>
    </tr>
    <tr>
      <td>Other</td>
      <td><a href="data/dannet/dannet.md">dannet</a>, <a href="data/depbank/depbank.md">depbank</a>, <a href="data/synne/synne.md">synne</a>, <a href="data/dsk-cbrain/dsk-cbrain.md">dsk-cbrain</a>, <a href="data/dsk-hofor/dsk-hofor.md">dsk-hofor</a>, <a href="data/dsk-plesner/dsk-plesner.md">dsk-plesner</a>, <a href="data/dsk-vitec/dsk-vitec.md">dsk-vitec</a>, <a href="data/ncc_parliament/ncc_parliament.md">ncc_parliament</a></td>
      <td>346.36M</td>
    </tr>
    <tr>
      <td>Web</td>
      <td><a href="data/dsk-alexandra/dsk-alexandra.md">dsk-alexandra</a>, <a href="data/dsk-atp/dsk-atp.md">dsk-atp</a>, <a href="data/dsk-salling/dsk-salling.md">dsk-salling</a>, <a href="data/dsk-vejle/dsk-vejle.md">dsk-vejle</a>, <a href="data/ai-aktindsigt/ai-aktindsigt.md">ai-aktindsigt</a>, <a href="data/ncc_maalfrid/ncc_maalfrid.md">ncc_maalfrid</a></td>
      <td>209.72M</td>
    </tr>
    <tr>
      <td>Encyclopedic</td>
      <td><a href="data/wiki/wiki.md">wiki</a>, <a href="data/wikisource/wikisource.md">wikisource</a>, <a href="data/dbc-faktalink/dbc-faktalink.md">dbc-faktalink</a>, <a href="data/dbc-forfatterweb/dbc-forfatterweb.md">dbc-forfatterweb</a></td>
      <td>130.76M</td>
    </tr>
    <tr>
      <td>Medical</td>
      <td><a href="data/health_hovedstaden/health_hovedstaden.md">health_hovedstaden</a></td>
      <td>27.07M</td>
    </tr>
    <tr>
      <td>Readaloud</td>
      <td><a href="data/nota/nota.md">nota</a></td>
      <td>7.30M</td>
    </tr>
    <tr>
      <td>Dialect</td>
      <td><a href="data/botxt/botxt.md">botxt</a></td>
      <td>847.97K</td>
    </tr>
    <tr>
      <td><b>Total</b></td>
      <td></td>
      <td>10.58B</td>
    </tr>
  </tbody>
</table>
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
<style>
table {
    border-collapse: collapse;
}
th, td {
    border: 1px solid #ddd;
    padding: 6px 10px;
}
th {
    background-color: #f9f9f9;
}
</style>

<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>License</th>
      <th>Sources</th>
      <th>N. Tokens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CC-0</td>
      <td><a href="data/adl/adl.md">adl</a>, <a href="data/botxt/botxt.md">botxt</a>, <a href="data/ep/ep.md">ep</a>, <a href="data/ft/ft.md">ft</a>, <a href="data/hest/hest.md">hest</a>, <a href="data/naat/naat.md">naat</a>, <a href="data/relig/relig.md">relig</a>, <a href="data/retspraksis/retspraksis.md">retspraksis</a>, <a href="data/skat/skat.md">skat</a>, <a href="data/spont/spont.md">spont</a>, <a href="data/synne/synne.md">synne</a>, <a href="data/wiki/wiki.md">wiki</a>, <a href="data/wikibooks/wikibooks.md">wikibooks</a>, <a href="data/wikisource/wikisource.md">wikisource</a>, <a href="data/danske-taler/danske-taler.md">danske-taler</a>, <a href="data/miljoeportalen/miljoeportalen.md">miljoeportalen</a>, <a href="data/nordjyllandnews/nordjyllandnews.md">nordjyllandnews</a>, <a href="data/nota/nota.md">nota</a>, <a href="data/opensubtitles/opensubtitles.md">opensubtitles</a>, <a href="data/ncc_books/ncc_books.md">ncc_books</a>, <a href="data/ncc_newspaper/ncc_newspaper.md">ncc_newspaper</a>, <a href="data/health_hovedstaden/health_hovedstaden.md">health_hovedstaden</a>, <a href="data/grundtvig/grundtvig.md">grundtvig</a>, <a href="data/enevaeldens_nyheder/enevaeldens_nyheder.md">enevaeldens_nyheder</a></td>
      <td>3.04B</td>
    </tr>
    <tr>
      <td>Verbal agreement</td>
      <td><a href="data/cvr-reports/cvr-reports.md">cvr-reports</a></td>
      <td>2.32B</td>
    </tr>
    <tr>
      <td>Written agreement (public models, private data)</td>
      <td><a href="data/plandata/plandata.md">plandata</a>, <a href="data/dbc-abstracts/dbc-abstracts.md">dbc-abstracts</a>, <a href="data/dbc-faktalink/dbc-faktalink.md">dbc-faktalink</a>, <a href="data/dbc-forfatterweb/dbc-forfatterweb.md">dbc-forfatterweb</a>, <a href="data/dbc-reviews/dbc-reviews.md">dbc-reviews</a></td>
      <td>1.78B</td>
    </tr>
    <tr>
      <td>CC-BY-SA 4.0</td>
      <td><a href="data/depbank/depbank.md">depbank</a>, <a href="data/jvj/jvj.md">jvj</a>, <a href="data/tv2r/tv2r.md">tv2r</a>, <a href="data/fm-udgivelser/fm-udgivelser.md">fm-udgivelser</a>, <a href="data/eur-lex-sum-da/eur-lex-sum-da.md">eur-lex-sum-da</a>, <a href="data/memo/memo.md">memo</a>, <a href="data/cellar/cellar.md">cellar</a></td>
      <td>1.37B</td>
    </tr>
    <tr>
      <td>Other (No attribution required)</td>
      <td><a href="data/retsinformationdk/retsinformationdk.md">retsinformationdk</a>, <a href="data/domsdatabasen/domsdatabasen.md">domsdatabasen</a></td>
      <td>904.61M</td>
    </tr>
    <tr>
      <td>Public Domain</td>
      <td><a href="data/danish-pd/danish-pd.md">danish-pd</a></td>
      <td>532.43M</td>
    </tr>
    <tr>
      <td>Other (Attribution required)</td>
      <td><a href="data/dannet/dannet.md">dannet</a>, <a href="data/gutenberg/gutenberg.md">gutenberg</a>, <a href="data/ai-aktindsigt/ai-aktindsigt.md">ai-aktindsigt</a>, <a href="data/ncc_maalfrid/ncc_maalfrid.md">ncc_maalfrid</a>, <a href="data/ncc_parliament/ncc_parliament.md">ncc_parliament</a></td>
      <td>515.61M</td>
    </tr>
    <tr>
      <td>DSK-1</td>
      <td><a href="data/dsk-alexandra/dsk-alexandra.md">dsk-alexandra</a>, <a href="data/dsk-atp/dsk-atp.md">dsk-atp</a>, <a href="data/dsk-cbrain/dsk-cbrain.md">dsk-cbrain</a>, <a href="data/dsk-danskerhverv/dsk-danskerhverv.md">dsk-danskerhverv</a>, <a href="data/dsk-dkmedier/dsk-dkmedier.md">dsk-dkmedier</a>, <a href="data/dsk-hofor/dsk-hofor.md">dsk-hofor</a>, <a href="data/dsk-ida/dsk-ida.md">dsk-ida</a>, <a href="data/dsk-odense/dsk-odense.md">dsk-odense</a>, <a href="data/dsk-plesner/dsk-plesner.md">dsk-plesner</a>, <a href="data/dsk-salling/dsk-salling.md">dsk-salling</a>, <a href="data/dsk-vejle/dsk-vejle.md">dsk-vejle</a>, <a href="data/dsk-vitec/dsk-vitec.md">dsk-vitec</a></td>
      <td>113.35M</td>
    </tr>
    <tr>
      <td><b>Total</b></td>
      <td></td>
      <td>10.58B</td>
    </tr>
  </tbody>
</table>
<!-- END-LICENSE TABLE -->

### Source Data

Below follows a brief overview of the sources in the corpus along with their individual license. To get more information about the individual dataset click the hyperlink in the table.

<details>
<summary><b>Overview Table (click to unfold)</b></summary>

You can learn more about each dataset by pressing the link in the first column.

<!-- START-MAIN TABLE -->
<table class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>Source</th>
      <th>Description</th>
      <th>Domain</th>
      <th>N. Tokens</th>
      <th>License</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="data/cvr-reports/cvr-reports.md">cvr-reports</a></td>
      <td>Annual reports from danish companies in the period 2010-2025</td>
      <td>Financial</td>
      <td>2.32B</td>
      <td><a href="data/cvr-reports/cvr-reports.md#license-information">Verbal agreement</a></td>
    </tr>
    <tr>
      <td><a href="data/cellar/cellar.md">cellar</a></td>
      <td>The official digital repository for European Union legal documents and open data</td>
      <td>Legal</td>
      <td>1.15B</td>
      <td><a href="data/cellar/cellar.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/enevaeldens_nyheder/enevaeldens_nyheder.md">enevaeldens_nyheder</a></td>
      <td>High quality OCR'd texts from Danish and Norwegian newspapers during the period of constitutional absolutism in Denmark (1660–1849)</td>
      <td>News</td>
      <td>1.03B</td>
      <td><a href="data/enevaeldens_nyheder/enevaeldens_nyheder.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/plandata/plandata.md">plandata</a></td>
      <td>A comprehensive dataset consisting of municipal planning documents from across Denmark, including local development plans, municipal plans, planning strategies, and related document types</td>
      <td>Governmental</td>
      <td>1.03B</td>
      <td><a href="data/plandata/plandata.md#license-information">Written agreement (public models, private data)</a></td>
    </tr>
    <tr>
      <td><a href="data/retsinformationdk/retsinformationdk.md">retsinformationdk</a></td>
      <td>[retsinformation.dk](https://www.retsinformation.dk) (legal-information.dk) the official legal information system of Denmark</td>
      <td>Legal</td>
      <td>818.25M</td>
      <td><a href="data/retsinformationdk/retsinformationdk.md#license-information">Danish Copyright Law</a></td>
    </tr>
    <tr>
      <td><a href="data/dbc-abstracts/dbc-abstracts.md">dbc-abstracts</a></td>
      <td>dbc-abstracts consists of more than 11.6 million abstracts of books and other materials collected and created by [DBC D1G1TAL](https://dbcdigital.dk/) (former Dansk Bibliotekscenter)</td>
      <td>Books</td>
      <td>694.42M</td>
      <td><a href="data/dbc-abstracts/dbc-abstracts.md#license-information">Written agreement (public models, private data)</a></td>
    </tr>
    <tr>
      <td><a href="data/danish-pd/danish-pd.md">danish-pd</a></td>
      <td>**PleIAs - Danish Public Domain** is a large collection aiming to aggregate all Danish monographies and periodicals in the public domain</td>
      <td>Books</td>
      <td>532.43M</td>
      <td><a href="data/danish-pd/danish-pd.md#license-information">Public Domain</a></td>
    </tr>
    <tr>
      <td><a href="data/ncc_books/ncc_books.md">ncc_books</a></td>
      <td>Danish books extracted from the [Norwegian Colossal Corpus](https://huggingface.co/datasets/NbAiLab/NCC) derived from OCR</td>
      <td>Books</td>
      <td>531.97M</td>
      <td><a href="data/ncc_books/ncc_books.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/hest/hest.md">hest</a></td>
      <td>Samples from the Danish debate forum www.heste-nettet.dk</td>
      <td>Social Media</td>
      <td>389.32M</td>
      <td><a href="data/hest/hest.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/ncc_parliament/ncc_parliament.md">ncc_parliament</a></td>
      <td>Collections from the Norwegian parliament in Danish. Extracted from the [Norwegian Colossal Corpus](https://huggingface.co/datasets/NbAiLab/NCC) derived from ocr</td>
      <td>Other</td>
      <td>338.87M</td>
      <td><a href="data/ncc_parliament/ncc_parliament.md#license-information">NLOD 2.0</a></td>
    </tr>
    <tr>
      <td><a href="data/opensubtitles/opensubtitles.md">opensubtitles</a></td>
      <td>Danish subsection of [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles)</td>
      <td>Conversation</td>
      <td>271.60M</td>
      <td><a href="data/opensubtitles/opensubtitles.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/ai-aktindsigt/ai-aktindsigt.md">ai-aktindsigt</a></td>
      <td>Multiple web scrapes from municipality websites collected as a part of the [AI-aktindsigt](https://ai-aktindsigt.dk) project</td>
      <td>Web</td>
      <td>139.23M</td>
      <td><a href="data/ai-aktindsigt/ai-aktindsigt.md#license-information">Apache 2.0</a></td>
    </tr>
    <tr>
      <td><a href="data/miljoeportalen/miljoeportalen.md">miljoeportalen</a></td>
      <td>Data from [Danmarks Miljøportalen](https://www.miljoeportal.dk/om-danmarks-miljoeportal/) (Denmark's Environment Portal)</td>
      <td>Legal</td>
      <td>127.38M</td>
      <td><a href="data/miljoeportalen/miljoeportalen.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/skat/skat.md">skat</a></td>
      <td>Skat is the Danish tax authority. This dataset contains content from its website skat.dk</td>
      <td>Legal</td>
      <td>122.11M</td>
      <td><a href="data/skat/skat.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/wiki/wiki.md">wiki</a></td>
      <td>The Danish subsection of [wikipedia](https://en.wikipedia.org/wiki/Main_Page)</td>
      <td>Encyclopedic</td>
      <td>122.00M</td>
      <td><a href="data/wiki/wiki.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/ft/ft.md">ft</a></td>
      <td>Records from all meetings of The Danish parliament (Folketinget) in the parliament hall</td>
      <td>Conversation</td>
      <td>114.09M</td>
      <td><a href="data/ft/ft.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/memo/memo.md">memo</a></td>
      <td>The MeMo corpus comprising almost all Danish novels from the period 1870-1899, known as the Modern Breakthrough</td>
      <td>Books</td>
      <td>113.74M</td>
      <td><a href="data/memo/memo.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/ep/ep.md">ep</a></td>
      <td>The Danish subsection of [Europarl](https://aclanthology.org/2005.mtsummit-papers.11/)</td>
      <td>Conversation</td>
      <td>100.84M</td>
      <td><a href="data/ep/ep.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/domsdatabasen/domsdatabasen.md">domsdatabasen</a></td>
      <td>[Domsdatabasen.dk](https://domsdatabasen.dk/) is a public database containing selected judgments from the Danish courts</td>
      <td>Legal</td>
      <td>86.35M</td>
      <td><a href="data/domsdatabasen/domsdatabasen.md#license-information">Danish Copyright Law</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-dkmedier/dsk-dkmedier.md">dsk-dkmedier</a></td>
      <td>A collection of ~100K news articles from [DK Medier](https://dkmedier.dk), written in the period 2000-2024</td>
      <td>News</td>
      <td>63.64M</td>
      <td><a href="data/dsk-dkmedier/dsk-dkmedier.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/adl/adl.md">adl</a></td>
      <td>Danish literature from 1700-2023 from the [Archive for Danish Literature](https://tekster.kb.dk/text?editorial=no&f%5Bsubcollection_ssi%5D%5B%5D=adl&match=one&search_field=Alt) (ADL)</td>
      <td>Books</td>
      <td>58.49M</td>
      <td><a href="data/adl/adl.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/retspraksis/retspraksis.md">retspraksis</a></td>
      <td>Case law or judical practice in Denmark derived from [Retspraksis](https://da.wikipedia.org/wiki/Retspraksis)</td>
      <td>Legal</td>
      <td>56.26M</td>
      <td><a href="data/retspraksis/retspraksis.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dbc-reviews/dbc-reviews.md">dbc-reviews</a></td>
      <td>dbc-reviews consists of more than 214 thousand reviews of books and other materials collected and created by DBC D1G1TAL (former Dansk Bibliotekscenter)</td>
      <td>Books</td>
      <td>53.96M</td>
      <td><a href="data/dbc-reviews/dbc-reviews.md#license-information">Written agreement (public models, private data)</a></td>
    </tr>
    <tr>
      <td><a href="data/fm-udgivelser/fm-udgivelser.md">fm-udgivelser</a></td>
      <td>The official publication series of the Danish Ministry of Finance containing economic analyses, budget proposals, and fiscal policy documents</td>
      <td>Legal</td>
      <td>50.34M</td>
      <td><a href="data/fm-udgivelser/fm-udgivelser.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/nordjyllandnews/nordjyllandnews.md">nordjyllandnews</a></td>
      <td>Articles from the Danish Newspaper [TV2 Nord](https://www.tv2nord.dk)</td>
      <td>News</td>
      <td>37.90M</td>
      <td><a href="data/nordjyllandnews/nordjyllandnews.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/eur-lex-sum-da/eur-lex-sum-da.md">eur-lex-sum-da</a></td>
      <td>The Danish subsection of EUR-lex SUM consisting of EU legislation paired with professionally written summaries</td>
      <td>Legal</td>
      <td>31.37M</td>
      <td><a href="data/eur-lex-sum-da/eur-lex-sum-da.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/ncc_maalfrid/ncc_maalfrid.md">ncc_maalfrid</a></td>
      <td>Danish content from Norwegian institutions websites</td>
      <td>Web</td>
      <td>29.26M</td>
      <td><a href="data/ncc_maalfrid/ncc_maalfrid.md#license-information">NLOD 2.0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-vejle/dsk-vejle.md">dsk-vejle</a></td>
      <td>A collection of crawled webpages that is managed by Vejle Kommune. Contains various information, covering everything from tourists to garbage collection to historical knowledge of the area</td>
      <td>Web</td>
      <td>27.99M</td>
      <td><a href="data/dsk-vejle/dsk-vejle.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/health_hovedstaden/health_hovedstaden.md">health_hovedstaden</a></td>
      <td>Guidelines and informational documents for healthcare professionals from the Capital Region</td>
      <td>Medical</td>
      <td>27.07M</td>
      <td><a href="data/health_hovedstaden/health_hovedstaden.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/tv2r/tv2r.md">tv2r</a></td>
      <td>Contemporary Danish newswire articles published between 2010 and 2019</td>
      <td>News</td>
      <td>21.67M</td>
      <td><a href="data/tv2r/tv2r.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/grundtvig/grundtvig.md">grundtvig</a></td>
      <td>The complete collection of [Grundtvig](https://en.wikipedia.org/wiki/N._F._S._Grundtvig) (1783-1872) one of Denmark’s most influential figures</td>
      <td>Books</td>
      <td>10.53M</td>
      <td><a href="data/grundtvig/grundtvig.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-salling/dsk-salling.md">dsk-salling</a></td>
      <td>A collection of crawled webpages that is managed by Salling Group. The dataset consists mainly of product pages from online stores such as bilka.dk, br.dk and such. The data consists of ~24K webpages</td>
      <td>Web</td>
      <td>9.79M</td>
      <td><a href="data/dsk-salling/dsk-salling.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/danske-taler/danske-taler.md">danske-taler</a></td>
      <td>Danish Speeches from [dansketaler.dk](https://www.dansketaler.dk)</td>
      <td>Conversation</td>
      <td>8.72M</td>
      <td><a href="data/danske-taler/danske-taler.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/nota/nota.md">nota</a></td>
      <td>The text only part of the [Nota lyd- og tekstdata](https://sprogteknologi.dk/dataset/nota-lyd-og-tekstdata) dataset</td>
      <td>Readaloud</td>
      <td>7.30M</td>
      <td><a href="data/nota/nota.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/gutenberg/gutenberg.md">gutenberg</a></td>
      <td>The Danish subsection from Project [Gutenberg](https://www.gutenberg.org)</td>
      <td>Books</td>
      <td>6.76M</td>
      <td><a href="data/gutenberg/gutenberg.md#license-information">Gutenberg</a></td>
    </tr>
    <tr>
      <td><a href="data/wikibooks/wikibooks.md">wikibooks</a></td>
      <td>The Danish Subsection of [Wikibooks](https://www.wikibooks.org)</td>
      <td>Books</td>
      <td>6.24M</td>
      <td><a href="data/wikibooks/wikibooks.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/wikisource/wikisource.md">wikisource</a></td>
      <td>The Danish subsection of [Wikisource](https://en.wikisource.org/wiki/Main_Page)</td>
      <td>Encyclopedic</td>
      <td>5.34M</td>
      <td><a href="data/wikisource/wikisource.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-cbrain/dsk-cbrain.md">dsk-cbrain</a></td>
      <td>A collection of Marketing material, product guides, and datasheets produced by cBrain for their products</td>
      <td>Other</td>
      <td>4.19M</td>
      <td><a href="data/dsk-cbrain/dsk-cbrain.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/jvj/jvj.md">jvj</a></td>
      <td>The works of the Danish author and poet, [Johannes V. Jensen](https://da.wikipedia.org/wiki/Johannes_V._Jensen)</td>
      <td>Books</td>
      <td>3.55M</td>
      <td><a href="data/jvj/jvj.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-atp/dsk-atp.md">dsk-atp</a></td>
      <td>A collection of crawled webpages that is managed by ATP</td>
      <td>Web</td>
      <td>2.86M</td>
      <td><a href="data/dsk-atp/dsk-atp.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/dbc-faktalink/dbc-faktalink.md">dbc-faktalink</a></td>
      <td>dbc-faktalink consists of more than 5 hundred articles created by [DBC D1G1TAL](https://dbcdigital.dk/) (former Dansk Bibliotekscenter)</td>
      <td>Encyclopedic</td>
      <td>1.99M</td>
      <td><a href="data/dbc-faktalink/dbc-faktalink.md#license-information">Written agreement (public models, private data)</a></td>
    </tr>
    <tr>
      <td><a href="data/spont/spont.md">spont</a></td>
      <td>Conversational samples collected as a part of research projects at Aarhus University</td>
      <td>Conversation</td>
      <td>1.56M</td>
      <td><a href="data/spont/spont.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dannet/dannet.md">dannet</a></td>
      <td>[DanNet](https://cst.ku.dk/projekter/dannet) is a Danish WordNet</td>
      <td>Other</td>
      <td>1.48M</td>
      <td><a href="data/dannet/dannet.md#license-information">DanNet 1.0</a></td>
    </tr>
    <tr>
      <td><a href="data/dbc-forfatterweb/dbc-forfatterweb.md">dbc-forfatterweb</a></td>
      <td>dbc-forfatterweb consists of more than 1 thousand articles created by DBC D1G1TAL (former Dansk Bibliotekscenter)</td>
      <td>Encyclopedic</td>
      <td>1.42M</td>
      <td><a href="data/dbc-forfatterweb/dbc-forfatterweb.md#license-information">Written agreement (public models, private data)</a></td>
    </tr>
    <tr>
      <td><a href="data/relig/relig.md">relig</a></td>
      <td>Danish religious text from the 1700-2022</td>
      <td>Books</td>
      <td>1.24M</td>
      <td><a href="data/relig/relig.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-odense/dsk-odense.md">dsk-odense</a></td>
      <td>A set of newsletters stories, covering events in Odense Municipality. Have been published on their website</td>
      <td>News</td>
      <td>1.18M</td>
      <td><a href="data/dsk-odense/dsk-odense.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-danskerhverv/dsk-danskerhverv.md">dsk-danskerhverv</a></td>
      <td>A set of newsletters written by Dansk Erhverv, primarily focusing on financials and companies world wide</td>
      <td>News</td>
      <td>1.12M</td>
      <td><a href="data/dsk-danskerhverv/dsk-danskerhverv.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/ncc_newspaper/ncc_newspaper.md">ncc_newspaper</a></td>
      <td>OCR'd Newspapers derived from [NCC](https://huggingface.co/datasets/NbAiLab/NCC)</td>
      <td>News</td>
      <td>1.05M</td>
      <td><a href="data/ncc_newspaper/ncc_newspaper.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-plesner/dsk-plesner.md">dsk-plesner</a></td>
      <td>A combination of crawled webpages from Plesners own website, and a series of internal documents outlining procedures</td>
      <td>Other</td>
      <td>896.33K</td>
      <td><a href="data/dsk-plesner/dsk-plesner.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/botxt/botxt.md">botxt</a></td>
      <td>The Bornholmsk Ordbog Dictionary Project</td>
      <td>Dialect</td>
      <td>847.97K</td>
      <td><a href="data/botxt/botxt.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-alexandra/dsk-alexandra.md">dsk-alexandra</a></td>
      <td>A collection of crawled webpages that is managed by Alexandra Institutet</td>
      <td>Web</td>
      <td>584.35K</td>
      <td><a href="data/dsk-alexandra/dsk-alexandra.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-vitec/dsk-vitec.md">dsk-vitec</a></td>
      <td>A collection of documents covering product descriptions, to newsletters, to internal documentation</td>
      <td>Other</td>
      <td>537.07K</td>
      <td><a href="data/dsk-vitec/dsk-vitec.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-ida/dsk-ida.md">dsk-ida</a></td>
      <td>A collection of newsletters, articles and other texts produced by IDA</td>
      <td>News</td>
      <td>417.32K</td>
      <td><a href="data/dsk-ida/dsk-ida.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/naat/naat.md">naat</a></td>
      <td>Danish speeches from 1930-2022</td>
      <td>Conversation</td>
      <td>286.68K</td>
      <td><a href="data/naat/naat.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/depbank/depbank.md">depbank</a></td>
      <td>The Danish subsection of the [Universal Dependencies Treebank](https://github.com/UniversalDependencies/UD_Danish-DDT)</td>
      <td>Other</td>
      <td>185.45K</td>
      <td><a href="data/depbank/depbank.md#license-information">CC-BY-SA 4.0</a></td>
    </tr>
    <tr>
      <td><a href="data/dsk-hofor/dsk-hofor.md">dsk-hofor</a></td>
      <td>A collection of articles, guides and newsletters written by HOFOR for their customers</td>
      <td>Other</td>
      <td>143.49K</td>
      <td><a href="data/dsk-hofor/dsk-hofor.md#license-information">DSK-1</a></td>
    </tr>
    <tr>
      <td><a href="data/synne/synne.md">synne</a></td>
      <td>Dataset collected from [synnejysk forening's website](https://www.synnejysk.dk), covering the Danish dialect sønderjysk</td>
      <td>Other</td>
      <td>52.02K</td>
      <td><a href="data/synne/synne.md#license-information">CC-0</a></td>
    </tr>
    <tr>
      <td><a href="data/<b>Total</b>/<b>Total</b>.md"><b>Total</b></a></td>
      <td></td>
      <td></td>
      <td>10.58B</td>
      <td><a href="data/<b>Total</b>/<b>Total</b>.md#license-information"></a></td>
    </tr>
  </tbody>
</table>
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
