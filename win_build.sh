#!/bin/bash
# This only works if you have git, bash, InnoSetup and Python3 installed.
# You should already have activated your environment before
# running this script.
set -e
set -x

cd $(dirname "$BASH_SOURCE[0]}")

# cleanup
rm -rf dist build

# install/upgrade dependencies
python3 -m pip install --upgrade pip wheel

# upgrade build environment
python3 -m pip install --upgrade pyinstaller
python3 -m pip install msvc-runtime

# upgrade packages
# Note that torch and torchvision are not in the requirements file,
# because the CI or user has to install the correct versions (e.g. CUDA).
pip install -r requirements.txt

# build executables
pyinstaller pyinstaller/dc_tools.spec
