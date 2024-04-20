|Build Status|

DC tools for Windows
====================

DC tools for Windows are a set of precompiled binaries for Windows users to
automate deformability cytometry (DC) data analysis without having
to install a Python distribution:

- ``dclab-compress``: https://dclab.readthedocs.io/en/stable/sec_cli.html#dclab-compress
- ``dclab-verify-dataset``: https://dclab.readthedocs.io/en/stable/sec_cli.html#dclab-verify-dataset
- ``dcoraid-upload-task``: https://github.com/DCOR-dev/DCOR-Aid/blob/master/dcoraid/cli.py
- ``chipstream-cli``: https://github.com/DC-analysis/ChipStream/tree/main/chipstream/cli


Installation
------------
At the `release page <https://github.com/DC-analysis/DC-tools-for-Windows/releases/latest>`_,
you can download an installer.


For developers
--------------
If you would like to make a release, create and activate a virtual environment
and run `prepare_release.py` (see docstring for more information). Then
modify the `CHANGELOG` if needed, push all the changes made and create a git
tag with the current date (as in `CHANGELOG`).


.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/DC-Analysis/DC-tools-for-Windows/check.yml
   :target: https://github.com/DC-Analysis/DC-tools-for-Windows/actions?query=workflow%3AChecks