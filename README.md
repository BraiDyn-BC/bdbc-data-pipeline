# bdbc-data-pipeline

A super-repository for managing a set of packages used for processing the BraiDyn-BC data files.

## Installation

First, clone the repository, and initialize it with submodules:

```shell
git clone https://github.com/BraiDyn-BC/bdbc-data-pipeline.git
cd bdbc-data-pipeline
git submodule init && git submodule update  # clones the submodules

# within an appropriate (virtual) python environment
python install.py --help

# running `install.py` with particular
# installation targets will install
# the required libraries
```

If you intend to perform DeepLabCut-based atlas registration,
**we recommend installing DeepLabCut/Tensorflow first**, before
installation of the libraries in this repository.

In case you encounter issues building up a CUDA-aware environment,
please refer to [this document](./cuda-environment.md).


## Documentation

For a brief overview of the packages, please refer to the [docs](./docs) directory.


## Citation

When using the code from this repository (and any of the sub-repositories), please cite:

[Kondo, Sehara, Harukuni, Aoki et al. (2025) A multimodal dataset linking wide-field calcium imaging to behavior changes in mice during an operant lever-pull task. _BioRxiv_ 2025.02.03.631599](https://doi.org/10.1101/2025.02.03.631599)
