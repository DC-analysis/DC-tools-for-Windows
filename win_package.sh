#!/bin/bash
# This only works if you have git, bash, InnoSetup and Python3 installed.
# You should already have activated your environment before
# running this script.
set -e
set -x

cd $(dirname "$BASH_SOURCE[0]}")

# package executables as installer
ISCC.exe innosetup/dc_tools.iss
