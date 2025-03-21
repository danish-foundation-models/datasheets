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

## Submitting a PR

Creating a PR on Huggingface is a bit different from creating one on Github.

1) Go to the community tab on huggingface press *new pull request* and choose *on your machine*. Specify the title of the your PR. Then you can simply:

```bash
git fetch origin refs/pr/{PR NUMBER}:pr/{PR NUMBER}
git checkout pr/{PR NUMBER}
# make your changes here 
# push to hub
git push origin pr/{PR NUMBER}:refs/pr/{PR NUMBER}
```

Before you make the PR do be sure to make sure that you have completed the following checklist. 

### Checklist

- [ ] I have run the test suite using `make test` and all tests pass
- [ ] I have added/changed a dataset and have
  - [ ] I have updated descriptive statistics using `make update-descriptive-statistics`
  - [ ] I have bumped the version use `make bump-version`
- [ ] If I have added a `create.py` script I have added the [script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) required to run that script.

### Examples of Previous PRs
To see example PR you can see the following:

- [Restructuring columns in the dataset](https://huggingface.co/datasets/danish-foundation-models/danish-dynaword/discussions/11)
- [Adding a new dataset](https://huggingface.co/datasets/danish-foundation-models/danish-dynaword/discussions/15)
- Updated [dataset description and metadata](https://huggingface.co/datasets/danish-foundation-models/danish-dynaword/discussions/20)

## Frequently asked questions

### Do you accept synthetic dataets

Yes we do generally accept synthetic datasets since it will likely be a promising research direction for low- to mid-resource languages.
However, you should be aware that synthetic dataset will probably require a more detailed examination and description.
We will for instance examine the quality of the synthetic subset and whether the model used for the creation permits resharing of the synthetic data under permissible licenses.

### Do you accept non-Danish data

Generally this repository is intended for Danish text, however quite broadly defined. For instance, we do accept data containing [code-switching](https://www.google.com/search?client=safari&rls=en&q=code+switching&ie=UTF-8&oe=UTF-8) and historical Danish text.