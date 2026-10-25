# Rebuilding the reading PDFs

The complete six English editorial manuscripts, the preserved Russian manuscript, and PDF_EDITION.json are in editorial_sources/. English is the primary publication language. The Russian supplement retains its original edition 1 front matter; the six English volumes are edition 2. The renderer uses ReportLab, Pandoc and DejaVu fonts; it does not run CI qualification experiments.

Requires Python 3.10+, ReportLab as pinned in requirements-pdf.txt, Pandoc on PATH, and the DejaVu serif/sans/mono font family with regular, bold, italic and bold-italic faces. The fonts are not redistributed as separate binaries; use your platform's DejaVu font package. FONT_LICENSE.txt preserves their terms.

From the outer package root, on Linux/macOS:

    python -m pip install -r build/requirements-pdf.txt
    python build/render_academic.py . --font-dir /path/to/dejavu-fonts

To render only the six English volumes, add --language en. The optional --only argument accepts an exact PDF filename from PDF_EDITION.json. The Russian supplement was copied byte-for-byte from the preceding edition for this release. Rebuilding it is optional and is not required to use the English publication route.

The --font-dir argument is a user-supplied directory containing DejaVuSerif.ttf, DejaVuSerif-Italic.ttf and the related family files. On this build host the complete font set was provided by the existing Matplotlib installation; the renderer can detect it if present. Matplotlib is not required when --font-dir is supplied.

The source date is fixed to 25 October 2026 for reproducible PDF metadata. Byte equality of a rebuilt PDF depends on the exact tool and font versions; cross-platform PDF byte identity is not claimed. The output text, pagination, fonts, metadata and visual rendering must be checked before creating a new frozen package.

The source_original/ directory is never modified by the renderer. Rebuilding a PDF changes the outer package's integrity state; rebuild its inventory and checksum index as a separately identified edition if you intend to distribute different bytes. Do not edit the original _02 source archive.

Text: CC BY 4.0. Rendering code: Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.
