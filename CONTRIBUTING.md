## Working with this repository locally

This repo follows a similar structure to [Danish Dynaword](https://huggingface.co/datasets/danish-foundation-models/danish-dynaword).
However it does not include the datasets themselves.


## Adding a new datasheet

To add a new dataset you will have to create a folder under `data/{dataset_name}/`, which should look as follows:

```
  data/dataset_name
  |- dataset_name.md
```

Optionally the folder might include script and similar for filtering the datasets.

## Installing dependencies

This repo comes with a few dependencies you need to install to make this run. It uses a [makefile](https://opensource.com/article/18/8/what-how-makefile) to run commands and a [uv](https://docs.astral.sh/uv/) for package management. Once you have uv installed you can install the dependencies using:

```bash
make install
```

These dependencies are only used for testing the structure of the repository.

## Running tests

This repository comes with a test suite to ensure that the datasheets follows the right format. You can run it using:

```bash
make test
```

### Checklist

- [ ] I have run the test suite using `make test` and all tests pass
- [ ] I have added/changed a dataset and have
  - [ ] I have bumped the version use `make bump-version`
- [ ] If I have added a `create.py` script I have added the [script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) required to run that script.
