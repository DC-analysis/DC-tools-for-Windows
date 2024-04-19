# -*- mode: python ; coding: utf-8 -*-

my_hidden_imports = [x for x in collect_submodules("skimage") if "tests" not in x]
my_datas = collect_data_files("skimage")

block_cipher = None


# chipstream
chipstream_a = Analysis(
    ['run-chipstream-cli.py'],
    pathex=[],
    binaries=[],
    datas=my_datas,
    hiddenimports=my_hidden_imports,
    hookspath=[".", "pyinstaller"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
chipstream_pyz = PYZ(chipstream_a.pure, chipstream_a.zipped_data, cipher=block_cipher)
chipstream_exe = EXE(
    chipstream_pyz,
    chipstream_a.scripts,
    [],
    exclude_binaries=True,
    name='chipstream-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


# dclab-compress
dclab_compress_a = Analysis(
    ['run-dclab-compress.py'],
    pathex=[],
    binaries=[],
    datas=my_datas,
    hiddenimports=my_hidden_imports,
    hookspath=[".", "pyinstaller"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
dclab_compress_pyz = PYZ(dclab_compress_a.pure, dclab_compress_a.zipped_data, cipher=block_cipher)
dclab_compress_exe = EXE(
    dclab_compress_pyz,
    dclab_compress_a.scripts,
    [],
    exclude_binaries=True,
    name='dclab-compress',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


# dclab-verify-dataset
dclab_verify_a = Analysis(
    ['run-dclab-verify-dataset.py'],
    pathex=[],
    binaries=[],
    datas=my_datas,
    hiddenimports=my_hidden_imports,
    hookspath=[".", "pyinstaller"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
dclab_verify_pyz = PYZ(dclab_verify_a.pure, dclab_verify_a.zipped_data, cipher=block_cipher)
dclab_verify_exe = EXE(
    dclab_verify_pyz,
    dclab_verify_a.scripts,
    [],
    exclude_binaries=True,
    name='dclab-verify-dataset',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


# dcoraid
dcoraid_a = Analysis(
    ['run-dcoraid-upload-task.py'],
    pathex=[],
    binaries=[],
    datas=my_datas,
    hiddenimports=my_hidden_imports,
    hookspath=[".", "pyinstaller"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
dcoraid_pyz = PYZ(dcoraid_a.pure, dcoraid_a.zipped_data, cipher=block_cipher)
dcoraid_exe = EXE(
    dcoraid_pyz,
    dcoraid_a.scripts,
    [],
    exclude_binaries=True,
    name='dcoraid-upload-task',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


coll = COLLECT(
    chipstream_exe,
    chipstream_a.binaries,
    chipstream_a.zipfiles,
    chipstream_a.datas,
    dclab_compress_exe,
    dclab_compress_a.binaries,
    dclab_compress_a.zipfiles,
    dclab_compress_a.datas,
    dclab_verify_exe,
    dclab_verify_a.binaries,
    dclab_verify_a.zipfiles,
    dclab_verify_a.datas,
    dcoraid_exe,
    dcoraid_a.binaries,
    dcoraid_a.zipfiles,
    dcoraid_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DC-tools-for-Windows',
)
