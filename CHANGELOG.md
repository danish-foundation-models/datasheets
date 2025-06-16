
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [v0.0.7] - 2025-06-16

### Added

- Added all of the Danish Gigaword datasets
  - dagw-adl
  - dagw-botxt
  - dagw-dannet
  - dagw-depbank
  - dagw-ep
  - dagw-ft
  - dagw-gutenberg
  - dagw-hest
  - dagw-jvj
  - dagw-naat
  - dagw-relig
  - dagw-retsinformationdk
  - dagw-retspraksis
  - dagw-skat
  - dagw-spont
  - dagw-synne
  - dagw-tv2r
  - dagw-wiki
  - dagw-wikibooks
  - dagw-wikisource

## [v0.0.6] - 2025-06-13

### Added

- Added the rest of the DSK datasets
  - Alexandra Instittutet
  - ATP
  - cBrain
  - Dansk Erhverv
  - HOFOR
  - IDA
  - Odense Kommune
  - Plesner
  - Vitec
- Domain distribution plot to main datasheet
- Document length distribution plot to main datasheet
- Full dataset descriptive stats in main datasheet
- A minimal template + helper script used to more easily add datasets

### Changed

- Changed the logic of `src/datasheets/update_descriptive_statistics.py` to handle 
  - loading all datasets and calculating descriptive statistics
  - loading all dataset datasheets and adding main table to main datasheet

## [v0.0.5] - 2025-06-11

### Added

- Added third DSK dataset - Salling Group

### Changed

- Changed the name of this pryproject.toml package name from `dynaword` to `datasheets`. Should cause less confusion now. 

## [v0.0.4] - 2025-06-11

### Added

- Added small helper script to convert JSONL files to parquet, while adding a token_count column.
- Added second DSK dataset - Vejle Kommune

### Changed

- Fixed small error in `src/dynaword/update_descriptive_statistics.py` relating to loading the data

## [v0.0.3] - 2025-06-10

### Added

- Added scripts for building descriptive stats
- Added first DSK dataset - DKMedier

## [v0.0.2] - 2025-06-04

### Added

- Added changelog
- Added versioning to subdatasets
- For developers
  - Restructered CI codebase substantially
    - Added `DataSheet` to make CI for convenient


### Docs

- Restructured main readme to cover all DFM datasheets and restructured it to be in a more friendly GitHub format