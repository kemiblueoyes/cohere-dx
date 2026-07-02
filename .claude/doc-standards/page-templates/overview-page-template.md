# Overview page template

**Target audience:**

Define the primary audience for the page. Add a secondary audience only if the page also needs to support another reader type.

Primary: \[Developer / Engineer | Enterprise Architect / Technical Decision-Maker | Enterprise Admin / Platform Operator\]

Secondary, if applicable: \[Audience\]

**Use when:**  
Use this page type to orient readers to a product area, documentation section, capability group, or set of related options. An overview page should help readers understand what the area includes, how the pieces relate, and where to go next.

- **Doc set / platform overview**  
  Use when the page orients users to the whole platform or docs experience.  
  Emphasis: broad mental map, major product areas, audience paths, “start here” routing.  
- **Product area overview**  
  Use when the page introduces a major product area, such as models, deployment options, or text generation.  
  Emphasis: what the area includes, key components/options, how to choose, links to quickstarts/guides/reference.  
- **Capability cluster overview**  
  Use when the page introduces a set of related capabilities, such as RAG, agents/tool use, private deployment, or search/retrieval.  
  Emphasis: when to use the capability, related concepts, common workflows, recommended next steps.

**Do not use when:**  
Do not use an overview page to provide a full implementation walkthrough, explain a concept in depth, document every parameter or limit, or teach a complete build from start to finish. Use a Quickstart, Concept, Guide, Tutorial, or Reference page instead.

**Primary reader question:**  
“I’m here, but I need to understand what this area contains, what my options are, and where I should go next.”

**Planning checklist**

- What area of the product is being introduced?
- What options or capabilities does it contain?
- Where should different audiences go next?

**Required sections:**

1. Short orientation  
   Briefly explain what the page covers and why the reader should care. Keep this practical and reader-centered.

2. What this area includes  
   Name the major options, components, capabilities, or subtopics included in this area. This can be a short paragraph, table, list, or card layout.

3. Key options, components, or concepts  
   Give each major option enough context for the reader to understand what it is, when it matters, and whether it applies to them. Keep explanations short. Link to deeper pages instead of expanding too much on the overview page.

4. Recommended next steps  
   End with guided routing. Help readers choose the next page based on their goal, level of readiness, or deployment need.

**Optional sections:**

- When to use each option

- Comparison table

- Feature support table

- Common use cases

- Audience-specific paths

- Architecture or workflow diagram

- Related concepts

- Prerequisites or assumptions, if the overview introduces implementation paths

**Content pattern:**  
Start broad, then help the reader narrow.

**Recommended pattern:**

1. What this area is

2. What options or components are available

3. How those options differ

4. Which option or page to choose next

The overview should provide enough context to support a decision, but not enough detail to replace the deeper pages it links to.

**Code/table guidance:**  
Use code sparingly. Include code only if a short example helps readers understand the shape of the API or capability. Do not include full workflows or multi-step implementation examples; those belong in Quickstarts, Guides, or Tutorials.

Use tables when readers need to compare options, features, support levels, platforms, models, or use cases. Tables should help the reader choose or orient, not serve as exhaustive reference material.

**Links and next steps:**  
Recommended next steps are required. These should be guided, not just listed. 

For example:

- To compare options before choosing, read \[decision guide\].

- To get started quickly, use \[quickstart\].

- To implement a specific path, follow \[setup or implementation guide\].

- To look up exact parameters, limits, or supported values, use \[reference\].

Adapt the links to the page. Do not include all of these categories unless they are relevant.

For pages with cards or comparison tables, the final next step should not duplicate every card. Instead, it should help undecided readers choose a decision guide and help decided readers continue to the relevant setup or implementation path.

**Common mistakes:**

- Turning the overview into a long concept explanation.

- Adding too much implementation detail.

- Listing links without explaining which reader should choose which link.

- Mixing several page types into one page.

- Assuming all readers have the same goal.

- Making the page too marketing-oriented and not useful for developer navigation.

- Creating a broad list of capabilities without explaining how they differ.

- Including large code samples that belong in a Quickstart or Guide.

- Omitting a clear next step.

**Example pages:**

- Deployment Options \- Overview

- An Overview of The Cohere Platform

- An Overview of Cohere’s Models

- Introduction to Text Generation at Cohere