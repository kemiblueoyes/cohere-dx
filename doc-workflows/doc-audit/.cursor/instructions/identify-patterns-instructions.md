Create a Python script that extracts structural patterns from Cohere documentation pages and outputs the results to a Markdown file.

The goal is not to generate page templates yet. The goal is to extract repeatable content patterns from examples of each page type.

## Input

I will provide a JSON file with page types and 3–5 example URLs per page type.

Example JSON structure:

```json
{
  "Quickstart": [
    "https://docs.cohere.com/docs/rag-quickstart",
    "https://docs.cohere.com/docs/reranking-quickstart"
  ],
  "Guide": [
    "https://docs.cohere.com/docs/get-started-installation",
    "https://docs.cohere.com/docs/reranking-best-practices"
  ],
  "Concept": [
    "https://docs.cohere.com/docs/tokens-and-tokenizers",
    "https://docs.cohere.com/docs/embeddings"
  ]
}
```

The script should accept:

```bash
python extract_page_patterns.py input.json output.md
```

## What the script should do

For each page type in the JSON file:

1. Fetch each URL.
2. Parse the HTML.
3. Extract useful structural information from each page.
4. Group the results by page type.
5. Write the output to a Markdown file.

## Extract for each page

For each URL, extract:

* Page title / H1
* URL
* H2 headings, in order
* H3 headings, grouped under the nearest H2 when possible
* Number of code blocks
* Number of tables
* Number of ordered lists
* Number of unordered lists
* Number of links
* Approximate word count
* Repeated structural labels, if present:

  * Overview
  * Prerequisites
  * Setup
  * Install
  * Example
  * Usage
  * Response
  * Parameters
  * Best practices
  * Limitations
  * Troubleshooting
  * Next steps
* Any obvious “page ending” pattern, such as:

  * Next steps
  * Related resources
  * Links to API reference
  * Links to tutorials or guides

## Markdown output format

The Markdown file should be organized by page type.

Use this structure:

```md
# Cohere Documentation Page Pattern Extraction

## Page Type: Guide

### Summary

- Pages analyzed: 5
- Common heading patterns:
- Common content blocks:
- Common ending patterns:
- Typical use of code:
- Typical use of tables:

### Pages

#### Page: Installation

- URL:
- H1:
- Word count:
- Code blocks:
- Tables:
- Ordered lists:
- Unordered lists:
- Links:

##### Heading structure

- H2
  - H3
  - H3
- H2
  - H3

##### Detected structural labels

- Prerequisites
- Install
- Code examples
- Next steps

##### Notes

- Add any automatically detected observations here.
```

Repeat this for every page under every page type.

## Page type summary logic

After processing all pages in a page type, generate a simple summary based on repeated patterns.

For each page type, include:

* headings that appear across multiple pages
* whether code blocks are common
* whether tables are common
* whether pages tend to include prerequisites
* whether pages tend to include next steps
* whether pages are mostly explanatory, instructional, example-driven, or lookup-oriented

This can be rule-based. Do not use an LLM.

For example:

```md
### Summary

- Common headings: Overview, Setup, Example, Next steps
- Code blocks appear in 4 of 5 pages.
- Tables appear in 1 of 5 pages.
- Most pages include implementation examples.
- Most pages end with links to related guides or API reference.
```

## Technical requirements

Use:

* `requests` for fetching pages
* `beautifulsoup4` for parsing HTML
* standard Python libraries for JSON, argparse, collections, and Markdown string generation

Add a `extract-page-patterns-requirements.txt` file with :

```txt
requests
beautifulsoup4
```

## Script requirements

The script should:

* Handle failed requests gracefully.
* Skip pages that cannot be fetched, but include an error note in the Markdown.
* Use a browser-like User-Agent header.
* Avoid crashing if a page is missing an H1, H2, code block, or table.
* Normalize whitespace.
* Remove duplicate empty lines.
* Keep heading order intact.
* Keep output readable and useful for manual review.

## Files to create

Create:

```text
scripts/extract_page_patterns.py
extract-page-patterns-requirements.txt
data/pages-by-type-sample.json
output/cohere-page-patterns.md
```

## Important

Do not generate final templates. This script is only for extracting patterns from real Cohere documentation examples so I can use the output to create page type templates later.