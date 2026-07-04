---
name: review-docs
description: Review documentation for compliance with the documentation standards, not to rewrite it.
---

#  Review Docs

##  Purpose

The value of this SKILL isn't just reviewing documentation. It's standardizing how documentation quality is evaluated.

"Does this documentation meet our documentation standards?" not "Review this documentation for me."

##  Common use cases

###  Content audits

Review one or more pages to identify:

- Incorrect page type
- Missing required sections
- Style guide violations
- Content model violations
- Fern authoring issues
- Inconsistent terminology
- Missing links
- Documentation gaps

###  Contributor pull requests

Review a contributor's pull request from Cohere's contributor workflow (`README.md`: *How to contribute to this repository*).

###  Existing documentation

Review existing documentation before publishing or as part of a documentation quality initiative.

##  Workflow

###  1. Determine the review scope
- User provides the page, pull request, or set of pages to review.
- Determine the page type and locate the corresponding template in `.claude/doc-standards/page-templates`.
- Load:
    - `.claude/doc-standards/writing-style-guide.md`
    - `.claude/doc-standards/content-model.md`
    - `.claude/doc-standards/fern-platform-rules.md`
- Determine whether this is:
    - A new page
    - An updated page
    - A content audit
    - A pull request review

###  2. Review against documentation standards

Review the page against:
- Page template
- Writing style
- Content model
- Fern platform rules
- Content quality:
    - Technical accuracy
    - Completeness
    - Clarity
    - Appropriate examples
    - Internal consistency
    - Duplicate or conflicting content

###  3. Summarize the review

Provide:
- Overall assessment:
    - Ready to publish
    - Ready with minor revisions
    - Requires significant revisions
- Summary
    - Briefly summarize the page's strengths.
    - Identify the highest-priority issues.
    - Highlight any documentation-wide concerns (for example, incorrect page type or duplicated content).

###  4. Report findings

Categorize findings as:

**Errors**\
Must be corrected before publishing.

**Warnings**\
Recommended improvements.

**Suggestions**\
Optional enhancements.

For each finding:
- Explain why it matters.
- Reference the relevant documentation standard.
- Suggest how to resolve it.
- **Do not rewrite the content unless the user explicitly requests revisions.**

###  5. Review documentation ecosystem impact

If applicable, identify:
- Related pages that should be updated
- Missing cross-links
- Pages that duplicate or contradict the reviewed content
- API reference descriptions that should be updated
- Navigation or information architecture changes to consider