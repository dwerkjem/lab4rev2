#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

DOCS_SOURCE="$PROJECT_ROOT/docs/source"
DOCS_BUILD="$PROJECT_ROOT/docs/build"

HTML_OUT="$DOCS_BUILD/html"
MARKDOWN_OUT="$DOCS_BUILD/markdown"
PDF_OUT="$DOCS_BUILD/pdf"

# Clean old documentation
rm -rf "$HTML_OUT" "$MARKDOWN_OUT" "$PDF_OUT"

# Build HTML
uv run sphinx-build -b html "$DOCS_SOURCE" "$HTML_OUT"

# Build markdown
uv run sphinx-build -b markdown "$DOCS_SOURCE" "$MARKDOWN_OUT"

# Build latex
uv run sphinx-build -b latex "$DOCS_SOURCE" "$PDF_OUT"

make -C "$PDF_OUT" all-pdf