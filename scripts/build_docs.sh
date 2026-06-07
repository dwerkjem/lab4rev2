#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

DOCS_DIR="$PROJECT_ROOT/docs"
DOCS_SOURCE="$DOCS_DIR/.source"
DOCS_BUILD="$DOCS_DIR/build"

HTML_OUT="$DOCS_BUILD/html"
MARKDOWN_OUT="$DOCS_BUILD/markdown"
PDF_OUT="$DOCS_BUILD/pdf"

# Clean old generated Markdown/PDF build output.
# Keep HTML rebuildable for preview, but still regenerate it cleanly.
rm -rf "$HTML_OUT" "$MARKDOWN_OUT" "$PDF_OUT"

# Build HTML for local preview
uv run sphinx-build -b html "$DOCS_SOURCE" "$HTML_OUT"

# Build Markdown
uv run sphinx-build -b markdown "$DOCS_SOURCE" "$MARKDOWN_OUT"

# Copy generated Markdown files into docs/, excluding .doctrees
rsync -av \
  --include="*/" \
  --include="*.md" \
  --exclude=".doctrees/" \
  --exclude="*" \
  "$MARKDOWN_OUT/" "$DOCS_DIR/"

# Build LaTeX source
uv run sphinx-build -b latex "$DOCS_SOURCE" "$PDF_OUT"

# Try to build PDF.
# If LaTeX fails after producing a PDF, still continue so the copy can happen.
make -C "$PDF_OUT" all-pdf || true

# Copy generated PDF files into docs/
find "$PDF_OUT" -name "*.pdf" -type f -exec cp {} "$DOCS_DIR/" \;

# Delete only non-preview build artifacts
rm -rf "$MARKDOWN_OUT" "$PDF_OUT" "$DOCS_DIR/.doctrees"