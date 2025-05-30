---
name: PyGMT release checklist
about: Checklist for a new PyGMT release. [For project maintainers only!]
title: Release PyGMT vX.Y.Z
labels: maintenance
assignees: ''

---

**Release**: [v0.x.x](https://github.com/GenericMappingTools/pygmt/milestones/?)
**Scheduled Date**: 20YY/MM/DD
**Pull request due date**: 20YY/MM/DD
**DOI**: `10.5281/zenodo.XXXXXXX`
**Announcement draft**: https://hackmd.io/@pygmt/xxxxxxxx

**Priority PRs/issues to complete prior to release**

- [ ] Wrap X ()
- [ ] Wrap Y ()

**Before release**:

- [ ] Check [SPEC 0](https://scientific-python.org/specs/spec-0000/) to see if we need to bump the minimum supported versions of GMT, Python and core package dependencies (NumPy, pandas, Xarray)
- [ ] Review the ["PyGMT Team" page](https://www.pygmt.org/dev/team.html)
- [ ] README looks good on TestPyPI. Visit [TestPyPI](https://test.pypi.org/project/pygmt/#history), click the latest pre-release, and check the homepage.
- [ ] Check to ensure that:
  - [ ] Deprecated workarounds/codes/tests are removed. Run `grep "# TODO" **/*.py` to find all potential TODOs.
  - [ ] All tests pass in the ["GMT Legacy Tests" workflow](https://github.com/GenericMappingTools/pygmt/actions/workflows/ci_tests_legacy.yaml)
  - [ ] All tests pass in the ["GMT Dev Tests" workflow](https://github.com/GenericMappingTools/pygmt/actions/workflows/ci_tests_dev.yaml)
  - [ ] All tests pass in the ["Doctests" workflow](https://github.com/GenericMappingTools/pygmt/actions/workflows/ci_doctests.yaml)
- [ ] Update warnings in `pygmt/_show_versions.py` as well as notes in [Not working transparency](https://www.pygmt.org/dev/install.html#not-working-transparency) regarding GMT-Ghostscript incompatibility
- [ ] Reserve a DOI on [Zenodo](https://zenodo.org) by clicking on "New Version"
- [ ] Finish up the "Changelog entry for v0.x.x" Pull Request (Use the previous changelog PR as a reference)
- [ ] Run `make codespell` to check common misspellings. If there are any, either fix them or add them to `ignore-words-list` in `pyproject.toml`
- [ ] Draft the announcement on https://hackmd.io/@pygmt

**Release**:

- [ ] At the [PyGMT release page on GitHub](https://github.com/GenericMappingTools/pygmt/releases):
  - [ ] Edit the draft release notes with the finalized changelog
  - [ ] Set the tag version and release title to vX.Y.Z
  - [ ] Make a release by clicking the 'Publish Release' button, this will automatically create a tag too
- [ ] Verify that [all workflows triggered by the release](https://github.com/GenericMappingTools/pygmt/actions?query=event%3Arelease) pass
  - [ ] The latest version is correct on [PyPI](https://pypi.org/project/pygmt/)
  - [ ] The latest version is correct on https://www.pygmt.org/latest/
  - [ ] The [release page](https://github.com/GenericMappingTools/pygmt/releases) has five assets, including `baseline-images.zip`, `pygmt-docs.zip` and `pygmt-docs.pdf`
- [ ] Download pygmt-X.Y.Z.zip (rename to pygmt-vX.Y.Z.zip) and baseline-images.zip from the release page, and upload the two zip files to https://zenodo.org/deposit, ensure that they are filed under the correct reserved DOI

**After release**:

- [ ] Update conda-forge [pygmt-feedstock](https://github.com/conda-forge/pygmt-feedstock) (Done automatically by conda-forge's bot. If you don't want to wait, open a new issue in the `conda-forge/pygmt-feedstock` repository with the title `@conda-forge-admin, please update version`. This will trigger the bot immediately. Remember to pin GMT, Python and SPEC0 versions)
- [ ] Bump PyGMT version on https://github.com/GenericMappingTools/try-gmt (after conda-forge update)
- [ ] Announce the release on:
  - [ ] GMT [forum](https://forum.generic-mapping-tools.org/c/news/) (do this announcement first! Requires moderator status)
  - [ ] [ResearchGate](https://www.researchgate.net) (after forum announcement; download the ZIP file of the new release from the release page and add it as research item via the **code** category, be sure to include the corresponding new Zenodo DOI)
- [ ] Update release checklist template with any additional bullet points that may have arisen during the release

---

- [ ] Party :tada: (don't tick before all other checkboxes are ticked!)
