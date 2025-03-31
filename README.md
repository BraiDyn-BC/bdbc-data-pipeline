# bdbc-data-pipeline

A super-repository for managing a set of packages used for processing the BraiDyn-BC data files.

## Documentation

For a brief overview of the packages, please refer to the [docs](./docs) directory.

## Prerequisites

Before installing, please make sure you prepare an environment with Python 3.10+, by running e.g.

```shell
# in case you have (Ana)conda; for venv etc., the shell command must be different
conda create -n bdbc "python==3.10"
```

>
> [!NOTE]
> In addition, in case you want to run atlas registration (i.e. DeepLabCut/Tensorflow),
> Please make sure you install CUDA Toolkit in accodance with
> [this version compatibility info](https://www.tensorflow.org/install/source#tested_build_configurations).
> 
> At the time of writing, DeepLabCut uses Tensorflow 2.0–2.12.
> 

## Installation

First, clone the repository along with its [submodules](https://gist.github.com/gitaarik/8735255):

```shell
git clone --recurse-submodules https://github.com/BraiDyn-BC/bdbc-data-pipeline.git
cd bdbc-data-pipeline
```

Then you can run `install.py`, e.g. as follows:

```shell
python install.py
```

By running the above command, the script attempts to install everything
in this repository (along with all the external dependencies).

For more detailed instructions about `install.py`, please refer to
[the documentation](./docs/README.md#how-to-use-the-installation-script).

The resulting package versions (in a python 3.10 environment) may be found
under the [requirements-python3.10](./requirements-python3.10) directory. 

## Citation

When using the code from this repository (and any of the sub-repositories), please cite:

[Kondo, Sehara, Harukuni, Aoki et al. (2025) A multimodal dataset linking wide-field calcium imaging to behavior changes in mice during an operant lever-pull task. _BioRxiv_ 2025.02.03.631599](https://doi.org/10.1101/2025.02.03.631599)
