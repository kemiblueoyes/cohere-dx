# Content Format Guidelines

These are content formatting and model guidelines that focus on: 

- Page types structure
- Required frontmatter
- Heading conventions
- Code block conventions
- Table conventions
- Callouts usage rules
- Image and diagram conventions
- Link conventions

## Frontmatter / metadata

Frontmatter is required for all published and public mdx pages. 

- title: required. between 30 and 60 characters
- description: required. up to 160 characters
- keywords: required. comma separated list of at least 2 short keyword phrases
- audience: required. comma separated list of target audiences. Must be 1 or more of: Developer, Technical Decison-Maker, Platform Operator

**Note**: The `audience` field is an editorial aid only. It is not used for content filtering, AI search, or personalization. Use it to keep  page scope aligned with the intended reader when writing, reviewing, or updating content.

```yaml
---
title: "Choose a deployment option for Cohere models"
description: "Compare Cohere's deployment options across data residency, compliance, and infrastructure requirements to choose the right fit for your organization."
keywords: "deploy Cohere, enterprise deployment, cloud deployment, private deployment, security, compliance, infrastructure requirements"
audience: "Technical Decision-Maker"
---
```

## Page types

Consult the page-templates/ for how to structure the following page types:

- Concept
- Feature
- Guide
- Overview
- Quickstart
- Reference
- Tutorial

## Headings

### Page titles (H1)

Use the title form appropriate for the page type.

Examples:
- Text Generation Quickstart
- Streaming Responses
- Grounding with RAG
- Parameter Types in JSON

Avoid imperative (direct command, instruction, or call to action to the reader) H1 titles unless the page is explicitly task-oriented.

### Section headings (H2-H6)

#### Task-oriented
Task-oriented sections use the imperative form. If a heading can naturally be prefixed with "How to," it's a task heading and should be imperative.

Examples:
- Install the SDK
- Configure the client
- Ground responses with RAG


#### Concept and reference
Concept and reference sections use noun phrases. Use noun phrases rather than commands. These may start with -ing terms when that's the established name of a feature or capability. The -ing word names the thing rather than instructing the reader to do something.

Examples:
- Streaming responses
- Grounding with RAG
- Rate limits
- Authentication methods

#### FAQ

FAQ headings may be written as questions.

## Callouts

Use callouts sparingly:

- `Warning` only for production-blocking issues.
- `Info` for genuine context the reader would otherwise miss.
- `Note` for highlighting additional context or supplementary information.
- `Error` for indicating a potential error or missing information that must be added.

Default to no callout; let prose carry the emphasis. Decorative callouts get purged on review.

## Code blocks

Code block tab labels use title case: Python, JavaScript, cURL, Go. Not all caps: PYTHON, JAVASCRIPT, CURL, GO.

Code example language selection depends on what the reader needs to do with the example, not which languages are technically supported:

- Use Python alone for long tutorials or conceptual walkthroughs
- Use Python + TypeScript when async, streaming, or frontend patterns are involved
- Use cURL alone when deliberately showing API shape
- Use all supported SDKs in auto-generated references or when code is meant to be copied and run, such as in quickstarts, install, and authentication pages.

### Code credentials

For API keys, tokens, credentials, base urls, and so forth, placeholders should be in `ALL_CAPS_WITH_UNDERSCORES` such as:

- co = cohere.Client("`COHERE_API_KEY`")
- token: "`AZURE_INFERENCE_CREDENTIAL`"
- base_url="`AZURE_MODEL_ENDPOINT`"
- aws_region="`AWS_REGION`"
- aws_access_key="`AWS_ACCESS_KEY_ID`"
- aws_secret_key="`AWS_SECRET_ACCESS_KEY`"
- aws_session_token="`AWS_SESSION_TOKEN`"

Make sure to use the eact same labeling for the exact same placeholder throughout docs. Exceptions:

- In tutorials and guides that use specific models or endpoints, such as /docs/cohere-on-azure/azure-ai-sem-search: api_key="`AZURE_EMBED_INFERENCE_CREDENTIAL`" and  base_url="`AZURE_EMBED_ENDPOINT`". Event then, be consistent in using the same alternative labeling throughout docs.

## Tables

For tables with 20 rows or less, use default table markdown.

For long tables of 20 rows or more, follow these rules:

- Wrap markdown in [`<SearchableTable>`](https://buildwithfern.com/learn/docs/writing-content/components/tables#searchable-tables) component to make it a searchable table
- Don't put essential content after a long table, because users who find what they need will stop reading.
- If content, such as next steps or a ling to a guide, must follow a large table, give it a distinct heading so it reads as a new section, not an afterthought.

## Cards

Use cards for navigation and orientation, not for content. Every place cards appear, the reader's job is to choose or locate, not to read and understand. 

Use cards when:

- The page is a hub or overview whose primary job is navigation
- Each card represents a distinct destination the reader will choose between
- The items are the same type of thing (all deployment options, all model families, all cookbook entries)

Don't use cards when:

- The page is explaining, instructing, or referencing
- The items aren't genuinely comparable items
- A table or prose would communicate the same information with less visual weight

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

A list should have a piece of text introducing the list followed by a colon, and then a blank line, such as:

This is an example of a bulleted list:

- Use bulleted lists for lists of items that have no particular order.
- Precede a list with a sentence and a colon, followed by a blank line.
- Terminate each *sentence* in a list with a full stop.

This is an example of an ordered list:

1. Use numbered lists for ordered sequences, such as procedures, tasks, a series of specific steps, items that are being enumerated, and so on.
2. This is the next step in this task.
3. This is the last step in this task.

Note the following points:

- Each sentence in the lists are terminated by a full-stop (period).
- If each item in the list is a single word, a terminating period is not required.
- Don't use bold formatting for prefixes (for example, avoid patterns like "**Feature name:** description").

## Links

Use standard link markdown, such as the example below, where possible instead of HTML `<a></a>`.

Standard link markdown: 
- `[Cohere Docs](https://docs.cohere.com/)`
- `Email link: [support+aws@cohere.com](mailto:support+aws@cohere.com)`
- Anchor on same page: [Link text](#anchor)`
- `Link with title: [Cohere Docs](https://docs.cohere.com/, "Cohere docs home")`

## Images

Use standard image markdown:

 - Image with alt tag: `![Cohere logo](/../assets/logo.svg)`
 - Linked image: `[![Cohere logo](/../assets/logo.svg)]](https://docs.cohere.com/)`

 ## Diagrams

 Use HTML to display captions with diagram images:

 ```html
<figure>
    <img src="/../assets/diagram.jpg"
         alt="diagram alt text">
    <figcaption>Short diagram description.</figcaption>
</figure>
 ```

