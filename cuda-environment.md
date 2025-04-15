# Setting up with a CUDA GPU

Below is an example recipe for setting up a CUDA environment
for our DeepLabCut/TensorFlow specification to work.

Only conda-based, UNIX-shell specification is described here:

```bash
# replace the name of the environment
# from BDBC as you wish
# for tensorflow version compatibilities, please see:
# https://www.tensorflow.org/install/source#tested_build_configurations
conda create -n BDBC -c conda-forge -y "python=3.10" "cudatoolkit=11.2" "cudnn=8"
conda activate BDBC

# install DeepLabCut
# numpy 1.x is necessary to work with the
# corresponding tensorflow version
pip install "numpy<2" "deeplabcut[tf]==2.3.10"

# specify LD_LIBRARY_PATH so that
# tensorflow looks up the CUDA libraries
# within the conda environment
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"

# but in some cases, you may need to _prepend_
# the system library path so that the other libraries
# won't get affected:
#
# export LD_LIBRARY_PATH="/lib/x86_64-linux-gnu:/$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"

# check that tensorflow recognizes the GPU
python -c "from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())"
```

Note that **`LD_LIBRARY_PATH` needs to be specified every time you open the**
**terminal console**.
Consider setting up a script, e.g. in the form of `.bashrc`.

