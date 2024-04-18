#!/bin/env/python
"""Prepare a new release of the DC tools for Windows

This script performs the following steps:

- upgrade dclab, dcnum, dcoraid, and chipstream to the latest version
- determine the version of each of those packages
- modify the following files for the new release:
  - CHANGELOG: add a new entry with today's date
  - requirements.txt: update the version pins for all packages
"""
import importlib
import pathlib
import subprocess as sp
import sys
import time

here = pathlib.Path(__file__).parent


def get_packages():
    """read packages from requirements.txt"""
    data = (here / 'requirements.txt').read_text().split('\n')
    packages = [ll.split("=")[0].strip() for ll in data if ll.strip()]
    return packages


def get_package_versions(packages):
    """get versions of packages currently installed"""
    version_dict = {}
    for pkg in packages:
        mod = importlib.import_module(pkg)
        version_dict[pkg] = mod.__version__
    return version_dict


def upgrade_packages(packages):
    """upgrade all packages to latest version (resolving dependencies)"""
    sp.check_output("pip install --upgrade " + " ".join(packages), shell=True)


def write_changelog_entry(version_dict):
    """Add a new entry to CHANGELOG"""
    # parse the changelog
    data = (here / "CHANGELOG").read_text().split('\n')
    versions = {}
    idat = []
    iver = ""
    for line in data:
        if line.startswith("-"):
            if iver:
                versions[iver] = idat
                idat = []
            # set new version identifier
            iver = line.strip(" -")
        elif line:
            # version data
            idat.append(line)
    else:
        # the final version
        versions[iver] = idat
    # add the latest version (replacing anything we did today)
    nver = time.strftime("%Y.%m.%d")
    ndat = [f"  - Python {write_python_version()}"]
    for key in sorted(version_dict.keys()):
        ndat.append(f"  - {key} {version_dict[key]}")
    versions[nver] = ndat
    # write everything to CHANGELOG
    text = []
    for vv in sorted(versions.keys())[::-1]:
        text.append(f"- {vv}")
        text += versions[vv]
    (here / "CHANGELOG").write_text("\n".join(text))


def write_python_version():
    pv = ".".join(f"{v}" for v in sys.version_info[:2])
    (here / "python_version.txt").write_text(pv)
    return pv


def write_package_pins(version_dict):
    """write package pins to requirements.txt"""
    text = []
    for pkg in version_dict:
        text.append(pkg + "=" + version_dict[pkg])
    (here / 'requirements.txt').write_text("\n".join(text))


if __name__ == "__main__":
    packages = get_packages()
    upgrade_packages(packages)
    version_dict = get_package_versions(packages)
    write_package_pins(version_dict)
    write_changelog_entry(version_dict)
