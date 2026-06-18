# Content Format Guidelines

These are content formatting and model guidelines that focus on fern published pages 

Page types
Required sections
Heading hierarchy
Code block conventions
Table conventions
Admonition usage rules
Image and diagram conventions
Link patterns

## Frontmatter / metadata

Frontmatter is required for all published and public mdx pages. 

* title: required. between 30 and 60 characters
* description: required. up to 160 characters
* keywords: required. comma separated list of at least 2 short keyword phrases
* audience: required. comma separated list of target audiences. Must be 1 or more of: Developer, Technical Decison-Maker, Platform Operator

```yaml
---
title: "Choose a deployment option for Cohere models"
description: "Compare Cohere's deployment options across data residency, compliance, and infrastructure requirements to choose the right fit for your organization."
keywords: "deploy Cohere, enterprise deployment, cloud deployment, private deployment, security, compliance, infrastructure requirements"
---
```
Add 'hidden: true' when you want to completely remove a page or section from your sidebar navigation while keeping it accessible via direct URL.

## Code blocks

Code block tab labels use title case, not all caps: Python, JavaScript, cURL, Go. Not PYTHON, JAVASCRIPT, CURL, GO.

Code example language selection depends on what the reader needs to do with the example, not which languages are technically supported:

* Use Python alone for long tutorials or conceptual walkthroughs
* Use Python + TypeScript when async, streaming, or frontend patterns are involved
* Use cURL alone when deliberately showing API shape
* Use all supported SDKs in auto-generated references or when code is meant to be copied and run, such as in quickstarts, install, and authentication pages.

## Tables

For tables with 20 rows or less, use default table markdown.

For long tables of 20 rows or more, follow these rules:

* Use the fern <SearchableTable> component to make it a searchable table
* Don't put essential content after a long table, because users who find what they need will stop reading.
* If content, such as next steps or a ling to a guide, must follow a large table, give it a distinct heading so it reads as a new section, not an afterthought.

## Cards

Use cards for navigation and orientation, not for content. Every place cards appear, the reader's job is to choose or locate, not to read and understand. 

Use cards when:

* The page is a hub or overview whose primary job is navigation
* Each card represents a distinct destination the reader will choose between
* The items are the same type of thing (all deployment options, all model families, all cookbook entries)

Don't use cards when:

* The page is explaining, instructing, or referencing
* The items aren't genuinely comparable items
* A table or prose would communicate the same information with less visual weight

## Steps

Use the fern's `<Steps>` component for short, linear success paths where the reader's only goal is task completion, such as in quickstarts.

Use numbered headings for longer guides where steps are part of a broader explanation, the page needs a ToC, or readers are likely to scan and jump rather than follow sequentially.

## Callouts

Use the following fern callouts like so:

```html
<Info>For genuine context the reader would otherwise miss.</Info>
<Warning>Only for production-blocking issues where user action may cause failure and might be irreversible.</Warning>
<Note>For highlighting helpful context or supplementary information.</Note>
<Error>This callout should only be used in API reference docs for indicating a potential error or missing information that must be added.</Error>
```

## Lists

For unordered lists, use * for consistency.
* JavaScript
* Go
* Python

For ordered lists, use standard Markdown syntax with ascending numbers for readability and consistency.
1. First
2. Second
3. Third

# Images

