#!/bin/bash
# This script is run as part of the CI pipeline to test whether
# the binaries created with pyinstaller work.
./dist/chipstream-cli --version
./dist/dclab-compress --version
./dist/dclab-verify-dataset --version
./dist/dcoraid-upload-task --version
