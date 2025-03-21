---
pretty_name: AI4WELFARE KB Data
language:
  - da
  - en
license: other
license_name: danish
task_categories:
  - text-generation
  - fill-mask
task_ids:
  - language-modeling
---

# Dataset Card for AI4WELFARE KB Data

<!-- START-SHORT DESCRIPTION -->
The Danish Web Archive (Netarkivet) collected by The Royal Danish Library
<!-- END-SHORT DESCRIPTION -->
Text extracted from objects harvested primarily on the '.dk' Top Level Domain from 2005 until 20024 by The Royal Danish Library and archived in The Danish Web Archive (Netarkivet).

The Danish Web Archive describes themselves as:

> Since 2005, we have collected material from the Danish part of the Internet and preserved it in our web archive. More precisely, this means material published on the Internet in Danish, by Danes or addressed to Danes. The material is part of Denmark's cultural heritage, which the library must preserve for posterity according to the Danish Legal Deposit Act.
> 
> The collection takes place automatically with so-called crawlers, which are software developed to be able to collect Internet material.
> 
> We only collect publicly available material from the Internet. Private content (with limited access) such as password protected family websites or corporate intranets are not in the public domain and we do not collect them.
> 
> *Source: [Netarkivet](https://www.kb.dk/en/find-materials/collections/netarkivet)*

[Danish Foundation Models](https://www.foundationmodels.dk) (DFM) has entered into an agreement with The Royal Danish Library under which DFM can use this data collection for research.

In order to reduce resource requirements, the data extraction is based on the Solr index of the Web Archive and thereby limited by the content of that index. The provenance of the extracted data is described in the following 

## Dataset Description

- **Language**: Estimated 56% Danish, 38% English and the rest distributed over the rest of the worlds languages.
- **Number of samples**:  18B
- **Estimated number of tokens**: 1,200B
- **Period**: 2005-2024


## Dataset Structure
The data is distributed over 173 gzip files of CSV data, where each file is between 100GB and 180GB.

An example from the dataset looks as follows.

```
"sha1:2222AWKN4MZTM5NQX2GTS5F74ADBL77M","20241127055747","200","da","visesangere.dk","https://visesangere.dk/baand.php?order=12&bid=49","application/xhtml+xml; charset=UTF-8; version=1.0","1179","Sønderjyder synger Hop forbi menuen Forside Viser   :: :: Viser Sangere   :: :: Sangere Temaer Indsamlinger Søg Baggrund Bånd 49 Hele båndet som lydfil:Højkvalitet lydfilHøjkvalitet lydfil (128kbit). Download evt. med højreklik og 'Gem destination som' Hvis du ikke har læst ""NB om lydfiler"" bør du gøre det først! (5.9mb ).   Lavkvalitet lydfilLavkvalitet lydfil (32kbit). Download evt. med højreklik og 'Gem destination som' Hvis du ikke har læst ""NB om lydfiler"" bør du gøre det først! (1.5mb ).   NB! om lydfilerne her !Vigtig information om lydfiler Sorter efter:  Sanger Optagelsessted Titel Lydfil Position Længde Optagelsestype Optagelsesdato Sanger Optagelsessted Titel Lydfil Position Længde Optagelsestype Optagelsesdato Nielsen, Ebbe Egebjerg Den sjæl som Gud i sandhed kender 2:10 Sang 11-8-1966 Nielsen, Ebbe Egebjerg Har du ej lyst til i himmelen at komme 1:45 Sang 11-8-1966 Denne sides indhold er opdateret 16. maj 2015. Publikationen her er tilknyttet Sanghistorisk Arkiv på Institut for Æstetiske Fag - Afdeling for Musikvidenskab ved Aarhus Universitet. Udskrevet fra Sønderjyder Synger, http://visesangere.dk/baand.php%3Forder%3D12%26bid%3D49 den 27/11/2024."
```

### Data Fields

An entry in the dataset consists of the following fields:
- `hash`(`str`):
- `wayback_date`(`str`):
- `status_code`(`str`):
- `content_language`(`str`):
- `domain`(`str`):
- `url`(`str`):
- `content_type_full`(`str`):
- `content_text_length`(`str`):
- `content`(`str`):


## Usage restrictions
This dataset can be used for research by <a href="https://www.foundationmodels.dk">DFM</a> under an agreement with The Royal Danish Library that covers May 2024 until December 2030. 


## Additional Information


### Citation Information

There is currently no citation for this dataset.