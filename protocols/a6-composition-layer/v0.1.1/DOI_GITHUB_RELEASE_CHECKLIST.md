# DOI / GitHub Release Checklist

## Before GitHub release

- [ ] Confirm repository path.
- [ ] Confirm license choice; default package value is CC BY 4.0.
- [ ] Confirm author metadata.
- [ ] Confirm no private material is included.
- [ ] Confirm PDFs render correctly.
- [ ] Confirm `CITATION.cff` appears in GitHub citation UI.
- [ ] Confirm `.zenodo.json` is present in the package root.
- [ ] Create tag: `a6-composition-layer-v0.1.1`.
- [ ] Publish GitHub release using `GITHUB_RELEASE_BODY_v0.1.1.md`.

## Zenodo / DOI deposit

- [x] Canonical DOI: `10.5281/zenodo.20752182`.
- [x] Canonical DOI URL: https://doi.org/10.5281/zenodo.20752182.
- [ ] Enable repository in Zenodo, or upload ZIP manually.
- [ ] Confirm title and author.
- [ ] Confirm upload type: publication / technical note.
- [ ] Confirm version: `0.1.1`.
- [ ] Confirm license.
- [ ] Upload or let Zenodo ingest the release ZIP.
- [x] Record DOI.
- [x] Replace DOI placeholder in README, CITATION.bib, release notes, and repository description.
- [ ] Add DOI badge to README if desired.

## Post-release

- [ ] Archive GitHub release asset.
- [ ] Record concept DOI and version DOI separately if Zenodo provides both.
- [ ] Do not rewrite the tagged release after DOI minting unless publishing a new version.
