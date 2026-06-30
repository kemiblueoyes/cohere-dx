---
name: author-docs
description: Write or refresh a Cohere documentation page in fern/pages in this repo. Use when creating a new MDX page, rewriting an existing one, or applying the page-design principles to docs work. Ensures principles, page-type templates, writing standards, and code format checks are applied.
---

# Purpose

The value for this SKILL isn't just AI generating docs. It's standardizing how documentation gets written.

"How do we write documentation here?" not "Write documentation for me."

# Workflow

## 1. Write an outline for the new page, based on:
- Suggested template: confirm the user-suggested template from `.claude/doc-standards/page-templates` is appropriate for the content, or recommend a better fit.
- Review the selected page template's **Planning questions** to validate the page's purpose, audience, and scope before drafting the outline. If the proposed content doesn't align with the template, recommend a more appropriate page type.
- Frontmatter: draft title (30-60 chars), description (≤160 chars), keywords, and audience per .claude/doc-standards/content-model.md, since these constrain page scope.
- Content sources: Cohere context, specific pages published in fern/pages, or provided files. Check related/existing pages to avoid duplicating or contradicting published content.
- Draft a section-by-section outline based on the selected page template.
- Pause here and present the outline to the user for approval before drafting.

## 2. Based on the approved outline, create a draft:
- Aligns with the specified page template's structure and section order.
- Implements `.claude/doc-standards/content-model.md` and `.claude/doc-standards/fern-platform-rules.md` (frontmatter, headings, callouts, code block components, tables, cards/steps).
- Written using .claude/doc-standards/writing-style-guide.md (tone, voice, terminology).
- Pause here and present the draft to the user for approval before the final pass.

## 3. Based on the approved draft, create the final draft:
- Polish pass against `.claude/doc-standards/writing-style-guide.md` (AI-writing fingerprints, active voice, simplicity).
- Code format check against `.claude/doc-standards/content-model.md` and `.claude/doc-standards/fern-platform-rules.md` (credential placeholders, tab labels, CodeBlocks vs. Tabs usage).
- Confirm page template structure is still intact after edits.
- Present the final draft to the user for approval.

## 4. Suggest linked pages:
- Suggest related pages in fern/pages that should link to this new page if needed (ignore all hidden: true pages referenced in `fern/v1.yml`, `fern/v2.yml`, and page frontmatter; ignore `fern/pages/-ARCHIVE-`).
- Suggest related API endpoint description copy in cohere-openapi.yaml that shold link to this new page, if needed.
