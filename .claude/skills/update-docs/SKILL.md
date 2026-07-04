---
name: update-docs
description: Update a Cohere documentation page in fern/pages in this repo. Use when updating an MDX page. Ensures principles, page-type templates, writing standards, and code format checks are applied.
---

# Update Docs

##  Purpose

The value of this SKILL isn't just updating documentation. It's ensuring documentation evolves consistently over time. 

"How do we update documentation here?" not "Update documentation for me."

##  Workflow

###  1. Assess the scope of the update:
- User provides the page to update and the requested change.
- Determine the page type and locate the corresponding template in `.claude/doc-standards/page-templates`.
- Review the template's **Planning questions** to confirm the page's core intent still matches the requested update. Flag if the requested change changes the page's purpose, audience, or page type.
- Preserve existing frontmatter; check for missing required fields and title/description length violations per `.claude/doc-standards/content-model.md` (see Frontmatter / metadata section).
- Identify which sections need updating vs. preserving.
- Flag if the request implies structural changes (new sections, reordering, page-type change) beyond the requested edit.
- Suggest related pages in fern/pages to update if needed (ignore all hidden: true pages referenced in `fern/v1.yml`, `fern/v2.yml`, and page frontmatter; ignore `fern/pages/-ARCHIVE-`).
- Suggest updates to API endpoints content in cohere-openapi.yaml as needed.
- Pause here and confirm the scope with the user before drafting.

###  2. Based on the confirmed scope, create a draft:
- Update only the requested sections unless structural changes were confirmed in step 1.
- Validate updated sections against the page template's structure and section order.
- Implement `.claude/doc-standards/content-model.md` and `.claude/doc-standards/fern-platform-rules.md` for any new or changed content (headings, callouts, code block components, tables, cards/steps).
- Apply .claude/doc-standards/writing-style-guide.md to new or edited prose, keeping voice consistent with unedited sections.
- Pause here and present the draft to the user for approval before the final pass.

###  3. Based on the approved draft, create the final draft:
- Polish pass against `.claude/doc-standards/writing-style-guide.md` (AI-writing fingerprints, active voice, simplicity) on new or edited prose.
- Code format check against `.claude/doc-standards/content-model.md` and `.claude/doc-standards/fern-platform-rules.md` (credential placeholders, tab labels, CodeBlocks vs. Tabs usage).
- Confirm page template structure is still intact after edits.
- Present the final draft to the user for approval.
