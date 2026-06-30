# Reference page template

**Target audience:**  
Primary: Developer / Engineer, Enterprise Admin / Platform Operator, or Enterprise Architect / Technical Decision-Maker, depending on the reference material.

Secondary, if applicable: \[Audience\]

A reference page should be written for readers who already know what they are looking for and need accurate, scannable facts. For developer-facing reference, prioritize parameters, schemas, request/response fields, supported values, and examples. For admin/operator reference, prioritize limits, configuration values, support status, deprecations, and operational behavior. For architect-facing reference, prioritize compatibility, deployment support, availability, and constraints.

**Use when:**  
Use this page type when the reader needs to look up exact information, such as parameter names, supported values, limits, models, endpoints, compatibility, deprecations, schemas, error codes, or configuration options.

**Do not use when:**  
Do not use a reference page to introduce a broad product area, explain a concept from first principles, help readers choose between options, provide a task walkthrough, or teach a complete build. Use an Overview, Concept, Feature, Guide, or Tutorial page instead.

**Primary reader question:**  
“I know what I’m doing. What is the exact fact, value, parameter, limit, status, or supported behavior?”

**Planning checklist**

- What information is the reader looking up?
- What factual information must be complete and accurate?
- What related guides or concepts should be linked?

**Required sections:**

1. Short scope statement  
   State what the reference covers. Keep this brief and factual.  
2. Reference content  
   Provide the lookup material in the clearest format for the information type. This may be a table, schema, grouped list, endpoint section, parameter section, compatibility matrix, model list, deprecation history, or policy list.  
3. Definitions or field descriptions  
   Define each parameter, field, value, status, method, model, or configuration option clearly enough for the reader to use it correctly.  
4. Usage notes or constraints  
   Include important constraints, defaults, version notes, support boundaries, deprecations, or compatibility warnings.  
5. Related links  
   Link to the relevant guide, quickstart, concept, or API reference when the reader needs implementation context.

**Optional sections:**

* Endpoint summary  
* Request schema  
* Response schema  
* Parameter table  
* Supported values  
* Model support table  
* Platform or deployment support matrix  
* Limits and quotas  
* Error codes  
* Deprecation or migration notes  
* Version history  
* Examples  
* FAQ  
* Changelog-style entries

**Content pattern:**  
Optimize for lookup.

Recommended pattern:

1. What this reference covers  
2. The facts, values, fields, limits, or supported behavior  
3. Notes needed to interpret or use those facts correctly  
4. Links to implementation or conceptual context

The reference page should not require linear reading. Readers should be able to scan headings, tables, and labels to find the exact information they need.

**Code/table guidance:**  
Tables are often useful and should be used when they make lookup faster. Use tables for parameters, fields, supported values, limits, compatibility, model support, platform support, and deprecation history.

Code is optional. Include short examples only when they clarify usage of a parameter, schema, endpoint, or value. Avoid long workflows or multi-step examples; those belong in Guides, Quickstarts, or Tutorials.

Reference code examples should be minimal and directly tied to the reference material.

**Links and next steps:**  
Related links are required, but they should be brief. Reference pages do not need long guided next-step sections unless the reference material has important migration or implementation implications.

Use links such as:

* To implement this, follow \[guide\].  
* To try this quickly, start with \[quickstart\].  
* To understand the underlying concept, read \[concept\].  
* To migrate from a deprecated option, follow \[migration guide\].  
* To use this endpoint, see \[API reference\].

Adapt the links to the page. Do not include unrelated resources.

**Common mistakes:**

* Explaining too much before giving the lookup information.  
* Hiding exact values inside paragraphs.  
* Mixing conceptual explanation with reference material.  
* Turning the page into a guide or tutorial.  
* Omitting defaults, constraints, supported values, or version notes.  
* Including examples that are too long or not tied to the reference content.  
* Using prose when a table, schema, or list would be easier to scan.  
* Failing to explain deprecated, legacy, or removed behavior clearly.  
* Linking to broad docs instead of the most relevant implementation or migration page.

**Example pages:**

* Cohere’s Command R7B Model  
* Cohere’s Embed Models (Details and Application)  
* Parameter Types in Structured Outputs (JSON)  
* Deprecations  
* Cohere Labs Acceptable Use Policy  
* 

