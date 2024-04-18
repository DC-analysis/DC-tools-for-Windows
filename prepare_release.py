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
from pprint import pprint
import subprocess as sp
import sys
import time

here = pathlib.Path(__file__).parent


def get_import_name(pkg):
    if pkg == "scikit-image":
        return "skimage"
    return pkg.split("[")[0]


def get_packages():
    """read packages from requirements.txt"""
    data = (here / 'requirements.txt').read_text().split('\n')
    packages = []
    packages_pinned = []
    for line in data:
        pkg = line.split("==")[0].strip()
        if line.count("# no-upgrade"):
            packages_pinned.append(line.split("#")[0].strip())
        elif line.strip():
            packages.append(pkg)
    return packages, packages_pinned


def get_package_versions(packages, packages_pinned):
    """get versions of packages currently installed"""
    version_dict = {}
    for pkg in packages:
        mod = importlib.import_module(get_import_name(pkg))
        version_dict[pkg] = mod.__version__
    for pkgv in packages_pinned:
        pk, ver = pkgv.split("==")
        pmod = importlib.import_module(get_import_name(pk))
        pver = pmod.__version__
        if pver != ver:
            raise ValueError(
                f"Package {pk} should be {ver}, but is {pver}")
        version_dict[pk] = f"{ver}  # no-upgrade"
    return version_dict


def upgrade_packages(packages, packages_pinned):
    """upgrade all packages to latest version (resolving dependencies)"""
    print("Installing pins", packages_pinned)
    sp.check_output("pip install " + " ".join(packages_pinned), shell=True)
    print("Upgrading", packages)
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
        if iver:
            # the final version
            versions[iver] = idat
    # add the latest version (replacing anything we did today)
    nver = time.strftime("%Y.%m.%d")
    ndat = [f"  - Python {write_python_version()}"]
    for key in sorted(version_dict.keys()):
        pver = version_dict[key].split("#")[0].strip()
        ndat.append(f"  - {key} {pver}")
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
        text.append(pkg + "==" + version_dict[pkg])
    (here / 'requirements.txt').write_text("\n".join(text))


if __name__ == "__main__":
    packages, packages_pinned = get_packages()
    upgrade_packages(packages, packages_pinned)
    version_dict = get_package_versions(packages, packages_pinned)
    print("New versions:")
    pprint(version_dict)
    write_package_pins(version_dict)
    write_changelog_entry(version_dict)
