#!/bin/bash
# This script is run as part of the CI pipeline to test whether
# the binaries created with pyinstaller work.
set -e
set -x

# Test whether we can print the version
./dist/DC-tools-for-Windows/chipstream-cli --version
./dist/DC-tools-for-Windows/dclab-compress --version
./dist/DC-tools-for-Windows/dclab-verify-dataset --version
./dist/DC-tools-for-Windows/dcoraid-upload-task --version
