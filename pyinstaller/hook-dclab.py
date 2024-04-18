# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
# Hook for dclab: https://pypi.python.org/pypi/dclab
from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('dclab')

# Add the Zstandard library used by dclab by default
datas += collect_data_files("hdf5plugin", includes=["plugins/libh5zstd.*"])
