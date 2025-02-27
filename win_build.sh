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

# Install CPU versions of torch (smaller file size)
pip install torch==2.3.1+cpu torchvision==0.18.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

# upgrade packages
pip install -r requirements.txt

# build executables
pyinstaller pyinstaller/dc_tools.spec
