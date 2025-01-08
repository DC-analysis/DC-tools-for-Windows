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
You can download the installer from the
`release page <https://github.com/DC-analysis/DC-tools-for-Windows/releases/latest>`_.

Code Signing Policy
...................
The DC tools for Windows use free code signing provided by `SignPath.io <https://about.signpath.io/>`_,
certificate by `SignPath Foundation <https://signpath.org/>`_.

Project Integrity
-----------------
To verify the integrity of the DC tools for Windows, we manage access this
repository via GitHub Team roles:

- **Triage**: The `Members team of DC-Analysis <https://github.com/orgs/DC-analysis/teams/triage>`_
  has permission to triage (e.g. modify issues).
- **Core**: The `Core team of DC-Analysis <https://github.com/orgs/DC-analysis/teams/core>`_
  consists of people who are trusted to modify the source code in the project's
  version control system without additional reviews.
- There is no special role for *Commiters*. External contributors or members
  of the *Triage* team must create a pull request which is reviewed by a
  *Core* team member.
- Furthermore, we enforce 2FA for every member of the DCOR-dev GitHub
  organization.


For developers
--------------
If you would like to make a release, create and activate a virtual environment
and run `prepare_release.py` (see docstring for more information). Then
modify the `CHANGELOG` if needed, push all the changes made and create a git
tag with the current date (as in `CHANGELOG`).


.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/DC-Analysis/DC-tools-for-Windows/check.yml
   :target: https://github.com/DC-Analysis/DC-tools-for-Windows/actions?query=workflow%3AChecks