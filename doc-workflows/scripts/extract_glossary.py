#!/usr/bin/env python3
"""Build the Cohere developer glossary from the docs corpus.

This is a rerunnable extractor. It scans the MDX documentation corpus under
fern/pages and produces a glossary of Cohere product and ML/AI terms with
dev-facing definitions.

How it decides what belongs:

* The curated vocabulary file (glossary_vocabulary.json) is the source of
  truth. Its term list (with curated definitions) keeps the output focused on
  real Cohere product and ML/AI vocabulary.
* The docs corpus supplies evidence: occurrence counts, source pages, and a
  candidate definition sentence for each term (used when a term has no curated
  definition).
* Some subdirectories are skipped by default (see DEFAULT_EXCLUDED_DIRS), as is
  the glossary page itself, so its own content never feeds back into the counts.

Outputs:

* Always: a candidates report (default doc-workflows/glossary-candidates.md)
  with the curated definitions table, the terms still missing a definition, and
  a paste-ready block.
* With --write-glossary: the Definitions section is also published into the
  glossary page (default fern/pages/resources/glossary.mdx), preserving that
  file's frontmatter and any intro text before the first heading. That section
  is regenerated on every run; do not hand-edit it - edit
  glossary_vocabulary.json instead.

Usage:
    # Dry run: scan the docs and (re)write the candidates report only. Use
    # this first, after editing glossary_vocabulary.json or the docs corpus,
    # to review new/missing terms before touching the published glossary.
    python3 doc-workflows/scripts/extract_glossary.py

    # Publish: same scan, but also regenerate the Definitions section of
    # fern/pages/resources/glossary.mdx. Use this once you're happy with the
    # candidates report and want the glossary page updated.
    python3 doc-workflows/scripts/extract_glossary.py --write-glossary

    # Custom paths/excludes: override any default location, or change which
    # subdirectories are skipped. Use this for one-off runs against a
    # different checkout layout, a subset of pages, or an adjusted exclude
    # list (the values shown here are the script's defaults).
    python3 doc-workflows/scripts/extract_glossary.py \\
        --pages fern/pages \\
        --vocab doc-workflows/scripts/glossary_vocabulary.json \\
        --output doc-workflows/glossary-candidates.md \\
        --glossary fern/pages/resources/glossary.mdx \\
        --exclude-dirs -ARCHIVE- changelog api-reference llm-university cookbooks

Paths default to locations relative to the repository root (the parent of the
doc-workflows directory), so the script can be run from anywhere.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Subdirectories of the pages tree to skip. These hold archived, time-stamped,
# auto-generated, or example-heavy content whose vocabulary is not representative
# of the curated developer glossary.
DEFAULT_EXCLUDED_DIRS = (
    "-ARCHIVE-",
    "changelog",
    "api-reference",
    "llm-university",
    "cookbooks",
)

# Definition-cue verbs used to mine a candidate sentence for a known term.
DEFINITION_CUES = (
    " is ", " are ", " refers to ", " describes ", " lets you ",
    " allows you ", " enables ", " provides ", " represents ",
)


@dataclass
class TermHit:
    term: str
    definition: str = ""
    source: str = ""
    occurrences: int = 0
    curated: bool = False


def load_vocabulary(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def iter_mdx_files(pages_dir: Path, excluded_dirs: tuple[str, ...] = ()) -> list[Path]:
    excluded = set(excluded_dirs)
    return sorted(
        path
        for path in pages_dir.rglob("*.mdx")
        if not excluded.intersection(path.relative_to(pages_dir).parts)
    )


def strip_mdx(raw: str) -> str:
    """Reduce MDX to readable prose for sentence-level analysis."""
    text = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.DOTALL)  # frontmatter
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)  # fenced code
    text = re.sub(r"`[^`]*`", " ", text)  # inline code
    text = re.sub(r"<[^>]+>", " ", text)  # JSX / HTML tags
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links -> link text
    text = re.sub(r"[*_#>|]", " ", text)  # markdown punctuation
    return text


def split_sentences(text: str) -> list[str]:
    flat = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", flat)
    return [p.strip() for p in parts if p.strip()]


def find_definition(term: str, files_text: list[tuple[str, list[str]]]) -> tuple[str, str, int]:
    """Find the best candidate definition sentence for a term across the corpus.

    Returns (definition, source, occurrences).
    """
    term_re = re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
    occurrences = 0
    best: tuple[str, str] | None = None

    for rel, sentences in files_text:
        for sentence in sentences:
            if not term_re.search(sentence):
                continue
            occurrences += 1
            if best is not None:
                continue
            lower = sentence.lower()
            term_pos = lower.find(term.lower())
            if any(cue in lower[term_pos:] for cue in DEFINITION_CUES) and len(sentence) <= 320:
                best = (sentence, rel)

    if best is None:
        return "", "", occurrences
    return best[0], best[1], occurrences


def collect_terms(files: list[Path], vocab: dict) -> list[TermHit]:
    files_text: list[tuple[str, list[str]]] = []
    for path in files:
        raw = path.read_text(encoding="utf-8", errors="ignore")
        rel = str(path.relative_to(REPO_ROOT))
        files_text.append((rel, split_sentences(strip_mdx(raw))))

    results: list[TermHit] = []
    for term, curated_def in sorted(vocab.get("terms", {}).items(), key=lambda item: item[0].lower()):
        mined_def, source, occurrences = find_definition(term, files_text)
        definition = curated_def or mined_def
        results.append(
            TermHit(
                term=term,
                definition=definition,
                source=source,
                occurrences=occurrences,
                curated=bool(curated_def),
            )
        )
    return results


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").strip()


def render_definition_table(terms: list[TermHit]) -> list[str]:
    lines = ["<SearchableTable>", "| Term | Definition |", "|------|------------|"]
    lines += [
        f"| {md_escape(hit.term)} | {md_escape(hit.definition)} |"
        for hit in terms
        if hit.definition
    ]
    lines.append("</SearchableTable>")
    return lines


def render_report(terms: list[TermHit]) -> str:
    lines: list[str] = [
        "# Cohere glossary candidates",
        "",
        "Generated by `doc-workflows/scripts/extract_glossary.py`. Refine "
        "`glossary_vocabulary.json` and rerun to adjust. Run with `--write-glossary` "
        "to publish into the glossary page.",
        "",
        "## Definitions",
        "",
        "Cohere product and ML/AI terms with dev-facing definitions. Curated "
        "definitions come from the vocabulary file; occurrence counts and sources "
        "are mined from the docs.",
        "",
        "| Term | Definition | Source | Occurrences |",
        "|------|------------|--------|-------------|",
    ]
    for hit in terms:
        src = hit.source if hit.source else "-"
        definition = hit.definition if hit.definition else "(needs definition)"
        lines.append(
            f"| {md_escape(hit.term)} | {md_escape(definition)} | {src} | {hit.occurrences} |"
        )

    missing = [hit.term for hit in terms if not hit.definition]
    if missing:
        lines += [
            "",
            "### Terms needing a definition",
            "",
            "These curated terms had no curated or mined definition. Add one to the "
            "vocabulary file:",
            "",
        ]
        lines += [f"- {term}" for term in missing]

    lines += [
        "",
        "## Glossary-ready output",
        "",
        "Paste the block below into the glossary page after review.",
        "",
    ]
    lines += render_definition_table(terms)

    return "\n".join(lines).rstrip() + "\n"


GLOSSARY_NOTE_SENTINEL = "extract_glossary.py --write-glossary"
GLOSSARY_GENERATED_NOTE = (
    "{/* The glossary table below is generated by "
    "doc-workflows/scripts/extract_glossary.py --write-glossary. "
    "Edit glossary_vocabulary.json and rerun; do not hand-edit. */}"
)
# Anchors for the generated region, stripped before regeneration so they never
# accumulate. Matches the legacy "## Definitions" heading too, for older files.
SEARCHABLE_TABLE_RE = re.compile(r"\n*<SearchableTable>.*?</SearchableTable>\s*", re.DOTALL)
LEGACY_HEADING_RE = re.compile(r"^##\s+Definitions\b.*$", re.MULTILINE)


def write_glossary(path: Path, terms: list[TermHit]) -> None:
    """Publish the curated glossary table into the glossary page.

    Preserves everything in the file except the generated region: the title,
    frontmatter, and any hand-written intro are kept, while the prior note line
    and SearchableTable block are stripped and regenerated. This keeps the
    output idempotent regardless of whether the page uses a section heading.
    """
    if path.is_file():
        existing = path.read_text(encoding="utf-8")
        stripped = SEARCHABLE_TABLE_RE.sub("\n", existing)
        stripped = LEGACY_HEADING_RE.sub("", stripped)
        preamble = "\n".join(
            line for line in stripped.splitlines() if GLOSSARY_NOTE_SENTINEL not in line
        )
        preamble = re.sub(r"\n{3,}", "\n\n", preamble).rstrip()
    else:
        preamble = "# Cohere glossary"

    lines = [preamble, "", GLOSSARY_GENERATED_NOTE, ""]
    lines += render_definition_table(terms)

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--pages",
        type=Path,
        default=REPO_ROOT / "fern" / "pages",
        help="Directory of MDX docs to scan (default: fern/pages).",
    )
    parser.add_argument(
        "--vocab",
        type=Path,
        default=REPO_ROOT / "doc-workflows" / "scripts" / "glossary_vocabulary.json",
        help="Curated vocabulary JSON file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "doc-workflows" / "glossary-candidates.md",
        help="Path for the generated candidates report.",
    )
    parser.add_argument(
        "--exclude-dirs",
        nargs="*",
        default=list(DEFAULT_EXCLUDED_DIRS),
        metavar="DIR",
        help=(
            "Subdirectory names under --pages to skip "
            f"(default: {', '.join(DEFAULT_EXCLUDED_DIRS)}). Pass with no values to scan everything."
        ),
    )
    parser.add_argument(
        "--write-glossary",
        action="store_true",
        help="Also publish the curated Definitions section into the glossary page.",
    )
    parser.add_argument(
        "--glossary",
        type=Path,
        default=REPO_ROOT / "fern" / "pages" / "resources" / "glossary.mdx",
        help=(
            "Target glossary file for --write-glossary "
            "(default: fern/pages/resources/glossary.mdx). Always excluded from scanning."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.pages.is_dir():
        print(f"Pages directory not found: {args.pages}", file=sys.stderr)
        return 1
    if not args.vocab.is_file():
        print(f"Vocabulary file not found: {args.vocab}", file=sys.stderr)
        return 1

    vocab = load_vocabulary(args.vocab)
    files = iter_mdx_files(args.pages, tuple(args.exclude_dirs))
    # Never mine the glossary page itself, or its terms feed back into the counts.
    glossary_resolved = args.glossary.resolve()
    files = [path for path in files if path.resolve() != glossary_resolved]
    if not files:
        print(f"No .mdx files found under {args.pages}", file=sys.stderr)
        return 1

    terms = collect_terms(files, vocab)

    report = render_report(terms)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")

    if args.write_glossary:
        write_glossary(args.glossary, terms)

    print(
        f"Scanned {len(files)} pages. "
        f"Terms: {sum(1 for t in terms if t.definition)}/{len(terms)} defined."
    )
    print(f"Wrote candidates report to {args.output}")
    if args.write_glossary:
        print(f"Published curated sections to {args.glossary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
