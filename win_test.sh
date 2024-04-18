#!/bin/bash
# This script is run as part of the CI pipeline to test whether
# the binaries created with pyinstaller work.
set -e
set -x

# Test whether we can print the version
./dist/chipstream-cli --version
./dist/dclab-compress --version
./dist/dclab-verify-dataset --version
./dist/dcoraid-upload-task --version
