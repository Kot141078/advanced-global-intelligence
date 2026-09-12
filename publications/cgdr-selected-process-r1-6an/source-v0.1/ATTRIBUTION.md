# Source origin, notices and coverage

This is an exact snapshot of the 93-file accepted current-AK tree, not a new
release of any entire upstream repository. The three included profile files
are separately identified. SOURCE_LICENCE_INDEX.json maps all 96 payload files
by path, byte hash, origin category and applicable notices.

The included CGAM protocol and SER arbitration document are credited to Ivan
Kotov and retain CC BY 4.0. The c-hardening-pack subset retains its original
license and commercial/non-implementation notice, with the independent
research permission in LICENSE.md for material Ivan controls. That supplement
permits research implementation and necessary verification changes; it does
not rewrite old notices, revoke existing CC rights, or authorize production.

Pinned references:
- CGAM: https://github.com/Kot141078/c-governed-cli-agent-mesh/tree/c3b004d7439a8c608f08233fc17be1150c442b44
- c Hardening Pack: https://github.com/Kot141078/c-hardening-pack/tree/47fed105d7b1df1df7375aa203a551b0f684c13d
- SER: https://github.com/Kot141078/sovereign-entity-recursion/tree/94dcab585b5c179cf4f4e0da4ebf63261c7fb984
- CC BY 4.0: https://creativecommons.org/licenses/by/4.0/legalcode
- CC BY-NC-ND 4.0: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode

Important path qualification: 18 CGDR scenario fixtures occur beneath the
c-hardening-pack-named directory but are CGDR-local overlay artifacts, not
files at that upstream commit. A pinned directory name does not prove byte
identity or original authorship. The other upstream-origin entries are
identified by their accepted source hashes and source reference; a fresh
full upstream byte-comparison is not asserted by this local inventory.
The fixture MANIFEST.json describes a wider upstream fixture set than this
selected subset. Missing files outside the selected profile are not silently
claimed to be included.

The four reproduced upstream notice files are byte-checked against their Git
blob identities; the SER notice supplies creator, exact source and a link to
the applicable full CC license and disclaimer. CGAM code is not included;
its MIT text is therefore not imported as though it licensed the selected
CGAM document or CGDR.

The 12 locked external Python distributions remain external, not bundled.
Their exact-version public license declarations are recorded in
DEPENDENCY_LICENCES.json. This source-only package does not relicense those
projects. Bundling wheels or system libraries later requires their own notices
and a new distribution-scope review.

The source/attribution review inspected package membership, source text and
static import/notice/secret indicators. It establishes a finite publication
inventory, not forensic proof of exclusive copyright title, a patent search,
or a professional legal opinion. Unidentified rights are not purported to be
granted by Ivan's permission.
