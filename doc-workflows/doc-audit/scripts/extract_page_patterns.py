#!/usr/bin/env python3
"""Extract structural patterns from Cohere documentation pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, Tag

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
REQUEST_TIMEOUT_SECONDS = 30

STRUCTURAL_LABELS = [
    "Overview",
    "Prerequisites",
    "Setup",
    "Install",
    "Example",
    "Usage",
    "Response",
    "Parameters",
    "Best practices",
    "Limitations",
    "Troubleshooting",
    "Next steps",
]

ENDING_HEADING_PATTERNS = [
    ("next steps", "Next steps section"),
    ("related resources", "Related resources section"),
    ("related guides", "Related guides section"),
    ("further resources", "Further resources section"),
    ("related", "Related content section"),
    ("see also", "See also section"),
]

ENDING_LINK_PATTERNS = [
    ("/reference/", "Links to API reference"),
    ("/docs/", "Links to other documentation pages"),
    ("tutorial", "Links to tutorials"),
    ("guide", "Links to guides"),
    ("quickstart", "Links to quickstarts"),
]


@dataclass
class PageAnalysis:
    url: str
    h1: str = ""
    word_count: int = 0
    code_blocks: int = 0
    tables: int = 0
    ordered_lists: int = 0
    unordered_lists: int = 0
    links: int = 0
    heading_structure: list[dict[str, Any]] = field(default_factory=list)
    structural_labels: list[str] = field(default_factory=list)
    ending_patterns: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def page_title(self) -> str:
        if self.h1:
            return self.h1
        slug = urlparse(self.url).path.rstrip("/").split("/")[-1]
        return slug.replace("-", " ").title() if slug else self.url


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def load_pages_by_type(input_path: Path) -> dict[str, list[str]]:
    with input_path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object mapping page types to URL lists.")

    pages_by_type: dict[str, list[str]] = {}
    for page_type, urls in data.items():
        if not isinstance(urls, list):
            raise ValueError(f"Page type '{page_type}' must map to a list of URLs.")
        pages_by_type[str(page_type)] = [str(url) for url in urls]
    return pages_by_type


def find_fern_streamed_content(soup: BeautifulSoup) -> Tag | None:
    """Return the Fern RSC streamed body div (e.g. div#S:5) when present."""
    candidates = [
        div
        for div in soup.find_all("div", id=True)
        if re.fullmatch(r"S:\d+", div.get("id", ""))
    ]
    if not candidates:
        return None

    return max(
        candidates,
        key=lambda div: (
            len(div.find_all(["h2", "h3"])),
            len(div.find_all("pre")),
            len(div.find_all("p")),
            len(div.get_text(strip=True)),
        ),
    )


def extract_h1(soup: BeautifulSoup) -> str:
    for selector in ("article h1", ".fern-layout-guide h1", "main h1", "h1"):
        element = soup.select_one(selector)
        if isinstance(element, Tag):
            text = extract_heading_text(element)
            if text:
                return text

    title_element = soup.find("title")
    if isinstance(title_element, Tag):
        return normalize_whitespace(title_element.get_text(" ", strip=True))

    return ""


def find_main_content(soup: BeautifulSoup) -> Tag:
    """Combine page header (article) with streamed MDX body when available."""
    streamed = find_fern_streamed_content(soup)
    article = soup.find("article")

    if streamed is not None or isinstance(article, Tag):
        combined_html = ""
        if isinstance(article, Tag):
            combined_html += str(article)
        if streamed is not None:
            combined_html += str(streamed)

        combined = BeautifulSoup(combined_html, "html.parser")
        wrapper = combined.new_tag("div")
        for child in list(combined.children):
            if isinstance(child, Tag):
                wrapper.append(child)
        return wrapper

    main = soup.find("main")
    if isinstance(main, Tag):
        return main

    body = soup.find("body")
    if isinstance(body, Tag):
        return body

    return soup


def extract_heading_text(element: Tag) -> str:
    return normalize_whitespace(element.get_text(" ", strip=True))


def extract_heading_structure(content: Tag) -> list[dict[str, Any]]:
    structure: list[dict[str, Any]] = []
    current_h2: dict[str, Any] | None = None

    for heading in content.find_all(["h2", "h3"]):
        text = extract_heading_text(heading)
        if not text:
            continue

        if heading.name == "h2":
            current_h2 = {"h2": text, "h3": []}
            structure.append(current_h2)
        elif heading.name == "h3":
            if current_h2 is None:
                current_h2 = {"h2": "(no preceding H2)", "h3": []}
                structure.append(current_h2)
            current_h2["h3"].append(text)

    return structure


def count_code_blocks(content: Tag) -> int:
    pre_blocks = content.find_all("pre")
    if pre_blocks:
        return len(pre_blocks)

    return len(content.find_all("code"))


def count_data_tables(content: Tag) -> int:
    tables = content.find_all("table")
    count = 0
    for table in tables:
        classes = " ".join(table.get("class", []))
        if "code-block-line-group" in classes:
            continue
        count += 1
    return count


def approximate_word_count(content: Tag) -> int:
    content_copy = BeautifulSoup(str(content), "html.parser")
    root = content_copy.find() or content_copy
    for element in root.find_all(["script", "style", "nav", "aside"]):
        element.decompose()

    text = normalize_whitespace(root.get_text(" ", strip=True))
    if not text:
        return 0
    return len(text.split())


def detect_structural_labels(content: Tag) -> list[str]:
    headings = [
        extract_heading_text(heading)
        for heading in content.find_all(["h2", "h3"])
    ]
    detected: list[str] = []

    for label in STRUCTURAL_LABELS:
        label_lower = label.lower()
        for heading in headings:
            heading_lower = heading.lower()
            if heading_lower == label_lower or label_lower in heading_lower:
                detected.append(label)
                break

    return detected


def detect_ending_patterns(content: Tag, heading_structure: list[dict[str, Any]]) -> list[str]:
    patterns: list[str] = []

    h2_headings = [section["h2"] for section in heading_structure if section.get("h2")]
    for heading in h2_headings[-3:]:
        heading_lower = heading.lower()
        for pattern, label in ENDING_HEADING_PATTERNS:
            if pattern in heading_lower and label not in patterns:
                patterns.append(label)

    link_elements = content.find_all("a", href=True)
    if not link_elements:
        return patterns

    tail_start = max(0, len(link_elements) - max(5, len(link_elements) // 3))
    tail_links = link_elements[tail_start:]

    for link in tail_links:
        href = link.get("href", "")
        href_lower = href.lower()
        link_text = extract_heading_text(link).lower()
        combined = f"{href_lower} {link_text}"

        for pattern, label in ENDING_LINK_PATTERNS:
            if pattern in combined and label not in patterns:
                patterns.append(label)

    return patterns


def build_page_notes(analysis: PageAnalysis) -> list[str]:
    notes: list[str] = []

    if analysis.code_blocks >= 3:
        notes.append("Contains multiple code examples.")
    elif analysis.code_blocks == 0:
        notes.append("No code blocks detected.")

    if analysis.structural_labels:
        notes.append(
            "Detected structural sections: "
            + ", ".join(analysis.structural_labels)
            + "."
        )

    if analysis.ending_patterns:
        notes.append(
            "Ending patterns detected: " + ", ".join(analysis.ending_patterns) + "."
        )

    if not analysis.heading_structure:
        notes.append("No H2/H3 heading structure detected in main content.")

    if analysis.word_count >= 1500:
        notes.append("Long-form explanatory content.")
    elif analysis.word_count <= 400:
        notes.append("Short, focused page.")

    return notes


def analyze_page(url: str, html: str) -> PageAnalysis:
    soup = BeautifulSoup(html, "html.parser")
    content = find_main_content(soup)
    h1 = extract_h1(soup)
    heading_structure = extract_heading_structure(content)

    analysis = PageAnalysis(
        url=url,
        h1=h1,
        word_count=approximate_word_count(content),
        code_blocks=count_code_blocks(content),
        tables=count_data_tables(content),
        ordered_lists=len(content.find_all("ol")),
        unordered_lists=len(content.find_all("ul")),
        links=len(content.find_all("a", href=True)),
        heading_structure=heading_structure,
        structural_labels=detect_structural_labels(content),
        ending_patterns=detect_ending_patterns(content, heading_structure),
    )
    analysis.notes = build_page_notes(analysis)
    return analysis


def fetch_page(url: str, session: requests.Session) -> tuple[str | None, str | None]:
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, str(exc)

    return response.text, None


def analyze_url(url: str, session: requests.Session) -> PageAnalysis:
    html, error = fetch_page(url, session)
    if error:
        return PageAnalysis(url=url, error=error)

    try:
        return analyze_page(url, html or "")
    except Exception as exc:  # noqa: BLE001 - keep script resilient for manual review
        return PageAnalysis(url=url, error=f"Parse error: {exc}")


def normalize_heading_for_comparison(heading: str) -> str:
    normalized = normalize_whitespace(heading).lower()
    normalized = re.sub(r"[^\w\s]", "", normalized)
    return normalized


def summarize_page_type(page_type: str, pages: list[PageAnalysis]) -> list[str]:
    successful = [page for page in pages if not page.error]
    failed = [page for page in pages if page.error]
    lines: list[str] = []

    lines.append(f"- Pages analyzed: {len(successful)}")
    if failed:
        lines.append(f"- Pages skipped due to errors: {len(failed)}")

    if not successful:
        lines.append("- Common heading patterns: (none — no pages fetched successfully)")
        lines.append("- Common content blocks: (none)")
        lines.append("- Common ending patterns: (none)")
        lines.append("- Typical use of code: unknown")
        lines.append("- Typical use of tables: unknown")
        return lines

    h2_counter: Counter[str] = Counter()
    ending_counter: Counter[str] = Counter()
    label_counter: Counter[str] = Counter()
    pages_with_code = sum(1 for page in successful if page.code_blocks > 0)
    pages_with_tables = sum(1 for page in successful if page.tables > 0)
    pages_with_prerequisites = sum(
        1 for page in successful if "Prerequisites" in page.structural_labels
    )
    pages_with_next_steps = sum(
        1
        for page in successful
        if "Next steps" in page.structural_labels
        or any("Next steps" in pattern for pattern in page.ending_patterns)
    )

    for page in successful:
        for section in page.heading_structure:
            h2 = section.get("h2", "")
            if h2 and h2 != "(no preceding H2)":
                h2_counter[normalize_heading_for_comparison(h2)] += 1
        for label in page.structural_labels:
            label_counter[label] += 1
        for pattern in page.ending_patterns:
            ending_counter[pattern] += 1

    common_h2 = [
        heading
        for heading, count in h2_counter.most_common()
        if count >= 2
    ]
    common_labels = [label for label, count in label_counter.items() if count >= 2]
    common_endings = [pattern for pattern, count in ending_counter.items() if count >= 2]

    lines.append(
        "- Common heading patterns: "
        + (", ".join(common_h2) if common_h2 else "(no H2 headings repeated across pages)")
    )
    lines.append(
        "- Common content blocks: "
        + (", ".join(common_labels) if common_labels else "(no repeated structural labels)")
    )
    lines.append(
        "- Common ending patterns: "
        + (", ".join(common_endings) if common_endings else "(no repeated ending patterns)")
    )
    lines.append(
        f"- Typical use of code: code blocks appear in {pages_with_code} of {len(successful)} pages."
    )
    lines.append(
        f"- Typical use of tables: tables appear in {pages_with_tables} of {len(successful)} pages."
    )

    if pages_with_prerequisites >= max(1, len(successful) // 2):
        lines.append("- Most pages include prerequisites.")
    else:
        lines.append("- Prerequisites sections are uncommon for this page type.")

    if pages_with_next_steps >= max(1, len(successful) // 2):
        lines.append("- Most pages end with next steps or related links.")
    else:
        lines.append("- Next steps / related-resource endings are uncommon for this page type.")

    orientation = classify_page_type_orientation(successful)
    lines.append(f"- Overall orientation: {orientation}.")

    return lines


def classify_page_type_orientation(pages: list[PageAnalysis]) -> str:
    if not pages:
        return "unknown"

    avg_code = sum(page.code_blocks for page in pages) / len(pages)
    avg_words = sum(page.word_count for page in pages) / len(pages)
    example_labels = sum(1 for page in pages if "Example" in page.structural_labels)
    instructional_labels = sum(
        1
        for page in pages
        if any(label in page.structural_labels for label in ("Setup", "Install", "Prerequisites"))
    )
    lookup_labels = sum(
        1
        for page in pages
        if any(label in page.structural_labels for label in ("Parameters", "Response"))
    )

    scores = {
        "example-driven": (avg_code >= 2, example_labels >= len(pages) // 2),
        "instructional": (instructional_labels >= len(pages) // 2, avg_code >= 1),
        "lookup-oriented": (lookup_labels >= len(pages) // 2, avg_words <= 1200),
        "explanatory": (avg_words >= 800, avg_code < 2),
    }

    ranked = sorted(
        scores.items(),
        key=lambda item: sum(item[1]),
        reverse=True,
    )
    best_name, best_signals = ranked[0]
    if sum(best_signals) == 0:
        return "mixed"
    return best_name


def render_heading_structure(heading_structure: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    if not heading_structure:
        lines.append("- (none detected)")
        return lines

    for section in heading_structure:
        lines.append(f"- {section.get('h2', '(missing H2)')}")
        for h3 in section.get("h3", []):
            lines.append(f"  - {h3}")
    return lines


def render_page_section(page: PageAnalysis) -> list[str]:
    lines = [
        f"#### Page: {page.page_title}",
        "",
        f"- URL: {page.url}",
    ]

    if page.error:
        lines.extend(
            [
                "- Status: fetch/parse error",
                f"- Error: {page.error}",
                "",
            ]
        )
        return lines

    lines.extend(
        [
            f"- H1: {page.h1 or '(not found)'}",
            f"- Word count: {page.word_count}",
            f"- Code blocks: {page.code_blocks}",
            f"- Tables: {page.tables}",
            f"- Ordered lists: {page.ordered_lists}",
            f"- Unordered lists: {page.unordered_lists}",
            f"- Links: {page.links}",
            "",
            "##### Heading structure",
            "",
        ]
    )
    lines.extend(render_heading_structure(page.heading_structure))
    lines.extend(
        [
            "",
            "##### Detected structural labels",
            "",
        ]
    )

    if page.structural_labels:
        lines.extend(f"- {label}" for label in page.structural_labels)
    else:
        lines.append("- (none detected)")

    if page.ending_patterns:
        lines.extend(["", "##### Ending patterns", ""])
        lines.extend(f"- {pattern}" for pattern in page.ending_patterns)

    lines.extend(["", "##### Notes", ""])
    if page.notes:
        lines.extend(f"- {note}" for note in page.notes)
    else:
        lines.append("- (none)")
    lines.append("")
    return lines


def render_markdown(pages_by_type_results: dict[str, list[PageAnalysis]]) -> str:
    sections = ["# Cohere Documentation Page Pattern Extraction", ""]

    for page_type, pages in pages_by_type_results.items():
        sections.extend(
            [
                f"## Page Type: {page_type}",
                "",
                "### Summary",
                "",
            ]
        )
        sections.extend(summarize_page_type(page_type, pages))
        sections.extend(["", "### Pages", ""])

        for page in pages:
            sections.extend(render_page_section(page))

    markdown = "\n".join(sections)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    return markdown


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract structural patterns from Cohere documentation pages "
            "and write the results to a Markdown file."
        )
    )
    parser.add_argument(
        "input_json",
        type=Path,
        help="JSON file mapping page types to example documentation URLs.",
    )
    parser.add_argument(
        "output_md",
        type=Path,
        help="Path for the generated Markdown report.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.input_json.is_file():
        print(f"Input file not found: {args.input_json}", file=sys.stderr)
        return 1

    try:
        pages_by_type = load_pages_by_type(args.input_json)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Failed to read input JSON: {exc}", file=sys.stderr)
        return 1

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    results: dict[str, list[PageAnalysis]] = {}
    for page_type, urls in pages_by_type.items():
        results[page_type] = [analyze_url(url, session) for url in urls]

    markdown = render_markdown(results)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(markdown, encoding="utf-8")

    print(f"Wrote pattern report to {args.output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
