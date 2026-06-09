"""
Name: Derek R. Neilson
Description: A quick script to make the sources because I got tired of manually making them.
"""

import json
from pathlib import Path
from typing import Any


SOURCE_JSON_PATH = Path("docs/sources.json")


OUTPUT_FILE = "docs/.source/design/used-references.rst"


def rst_link(text: str, url: str) -> str:
    """Create an inline RST hyperlink."""
    return f"`{text} <{url}>`__"


def heading(title: str, symbol: str = "=") -> str:
    """Create an RST heading."""
    return f"{title}\n{symbol * len(title)}\n"


def load_sources(json_path: Path) -> list[dict[str, Any]]:
    """Load and validate sources from the JSON file path."""

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Error: JSON file not found: {json_path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Error: Invalid JSON in {json_path}: {error}")

    if not isinstance(data, list):
        raise SystemExit("Error: JSON file must contain a list of source objects.")

    for index, source in enumerate(data, start=1):
        if not isinstance(source, dict):
            raise SystemExit(f"Error: Source #{index} must be a JSON object.")

        if not source.get("title"):
            raise SystemExit(f"Error: Source #{index} is missing required field: title")

        if not source.get("url"):
            raise SystemExit(f"Error: Source #{index} is missing required field: url")

    return data


def get_categories(sources: list[dict[str, Any]]) -> list[str]:
    """Return categories in the order they first appear."""

    categories = []

    for source in sources:
        category = source.get("category") or "Other Sources"

        if category not in categories:
            categories.append(category)

    return categories


def field_line(name: str, value: Any) -> str:
    """Create an RST field-list line if the value exists."""

    if value is None or value == "":
        return ""

    return f"   :{name}: {value}\n"


def format_source_card(number: int, source: dict[str, Any]) -> str:
    """Format one source as an RST admonition card."""

    title = source["title"]
    url = source["url"]

    category = str(source.get("category", "")).lower()

    if "opentelemetry" in category or "observability" in category:
        card_class = "important"
    elif "python" in category or "tooling" in category:
        card_class = "hint"
    else:
        card_class = "note"

    card = f".. admonition:: {number}. {title}\n"
    card += f"   :class: {card_class}\n\n"

    card += field_line("Type", source.get("source_type"))
    card += field_line("Author", source.get("author"))
    card += field_line("Organization", source.get("organization"))
    card += field_line("Publisher", source.get("publisher"))
    card += field_line("Date", source.get("date"))
    card += field_line("Accessed", source.get("accessed"))
    card += field_line("URL", rst_link(url, url))
    card += field_line("Note", source.get("note"))

    return card


def format_table_for_category(
    category: str,
    sources: list[dict[str, Any]],
    start_number: int,
) -> str:
    """Create a list-table summary for one category."""

    output = ""

    output += heading(category, "-")
    output += "\n"

    output += ".. list-table::\n"
    output += "   :widths: 5 35 20 20 20\n"
    output += "   :header-rows: 1\n\n"

    output += "   * - #\n"
    output += "     - Source\n"
    output += "     - Creator\n"
    output += "     - Date\n"
    output += "     - Link\n"

    number = start_number

    for source in sources:
        creator = (
            source.get("author")
            or source.get("organization")
            or source.get("publisher")
            or "Unknown"
        )

        date = source.get("date") or source.get("accessed") or "No date listed"

        output += f"   * - {number}\n"
        output += f"     - **{source['title']}**\n"
        output += f"     - {creator}\n"
        output += f"     - {date}\n"
        output += f"     - {rst_link('Open source', source['url'])}\n"

        number += 1

    output += "\n"
    return output


def format_compact_citation(source: dict[str, Any]) -> str:
    """Create a compact citation-style entry."""

    creator = (
        source.get("author")
        or source.get("organization")
        or source.get("publisher")
        or "Unknown"
    )

    title = source["title"]
    organization = source.get("organization")
    publisher = source.get("publisher")
    date = source.get("date")
    accessed = source.get("accessed")
    url = source["url"]

    parts = [f"{creator}.", f"*{title}*."]

    if organization and organization != creator:
        parts.append(f"{organization}.")

    if publisher and publisher != creator and publisher != organization:
        parts.append(f"{publisher}.")

    if date:
        parts.append(f"{date}.")

    if accessed:
        parts.append(f"Accessed {accessed}.")

    parts.append(rst_link(url, url))

    return " ".join(parts)


def build_rst(sources: list[dict[str, Any]]) -> str:
    """Build the full RST document."""

    output = ""

    output += heading("Sources", "=")
    output += "\n"

    output += ".. epigraph::\n\n"
    output += "   A curated source list for reStructuredText, OpenTelemetry,\n"
    output += "   SQLAlchemy, and Python tooling.\n\n"

    output += ".. contents:: Source Categories\n"
    output += "   :depth: 2\n"
    output += "   :local:\n\n"

    output += heading("Quick Reference", "-")
    output += "\n"

    categories = get_categories(sources)
    source_number = 1

    for category in categories:
        category_sources = [
            source
            for source in sources
            if (source.get("category") or "Other Sources") == category
        ]

        output += format_table_for_category(
            category=category,
            sources=category_sources,
            start_number=source_number,
        )

        source_number += len(category_sources)

    output += heading("Detailed Source Cards", "-")
    output += "\n"

    for number, source in enumerate(sources, start=1):
        output += format_source_card(number, source)
        output += "\n"

    output += heading("Compact Works Cited", "-")
    output += "\n"

    for source in sources:
        output += f"#. {format_compact_citation(source)}\n\n"

    return output


def main() -> None:
    output_path = Path(OUTPUT_FILE)

    sources = load_sources(SOURCE_JSON_PATH)
    rst = build_rst(sources)

    output_path.write_text(rst, encoding="utf-8")

    print(f"Read sources from: {SOURCE_JSON_PATH}")
    print(f"Created RST file:  {output_path}")


if __name__ == "__main__":
    main()
