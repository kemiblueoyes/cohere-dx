# Concept page template

**Target audience:**  
Primary: Developer / Engineer, Enterprise Architect / Technical Decision-Maker, or Enterprise Admin / Platform Operator, depending on the concept.

Secondary, if applicable: \[Audience\]

Concept pages can serve different audiences, but each page should be written for one primary reader need. A developer concept may explain how a technical mechanism works. An enterprise architect concept may explain a system model, deployment tradeoff, or architectural constraint. An admin/operator concept may explain behavioral controls, operational boundaries, or lifecycle implications.

**Use when:**  
Use this page type when the reader needs to understand an idea, mental model, mechanism, architecture, terminology, or tradeoff before they can use the product effectively.

A concept page should answer what something is, why it exists, how it works, and when it matters.

**Do not use when:**  
Do not use a concept page to provide a full task walkthrough, get the reader to first success, compare a full set of product options, document parameters, or teach a complete build from start to finish. Use a Guide, Quickstart, Overview, Reference, or Tutorial page instead.

**Primary reader question:**  
“I don’t understand this thing. What is it, why does it exist, how does it work, and when would I use it?”

**Required sections:**

1. Short explanation  
   Define the concept in plain language. Start with what the thing is and why it matters to the reader.  
2. Why it exists  
   Explain the problem, need, or product context that makes the concept necessary. This section should answer why the reader should care.  
3. How it works  
   Explain the mechanism, flow, architecture, or logic behind the concept. Use diagrams, examples, or short code snippets only if they make the explanation clearer.  
4. When to use it  
   Explain the situations where the concept applies. Include boundaries, tradeoffs, or decision points when relevant.  
5. Related implementation paths  
   End by linking to the relevant quickstart, guide, tutorial, or reference page so the reader can move from understanding to action.

**Optional sections:**

* Key terminology  
* Example scenario  
* Architecture diagram  
* Workflow diagram  
* Comparison with related concepts  
* Tradeoffs  
* Limitations  
* Common misconceptions  
* Interaction with other Cohere features  
* Security, compliance, or operational considerations  
* Short code proof, if useful

**Content pattern:**  
Move from explanation to application.

Recommended pattern:

1. What the concept is  
2. Why it matters  
3. How it works  
4. When to use it  
5. What to read or do next

The concept page should give readers enough understanding to make sense of the related quickstarts, guides, tutorials, and reference docs. It should not become the implementation path itself.

**Code/table guidance:**  
Code is optional. Use code only when it helps prove or clarify the concept. Keep code examples short and focused on the idea being explained.

Do not include full implementation workflows. Those belong in Guides, Quickstarts, or Tutorials.

Tables are optional. Use tables when comparing terms, tradeoffs, related concepts, or behavior across options. Avoid large compatibility or parameter tables; those belong in Reference pages.

**Links and next steps:**  
End with links that help the reader apply the concept.

For example:

* To try this in code, start with \[quickstart\].  
* To implement this in an application, follow \[guide\].  
* To understand a related idea, read \[related concept\].  
* To look up exact fields, limits, or parameters, use \[reference\].

Adapt the links to the page. Do not include all categories unless they are relevant.

**Common mistakes:**

* Starting with implementation steps before explaining the idea.  
* Treating the concept page like a guide.  
* Defining the term but not explaining why it matters.  
* Explaining how something works without saying when to use it.  
* Adding too much code.  
* Adding reference-level parameter detail.  
* Assuming the reader already understands related terminology.  
* Omitting tradeoffs or boundaries.  
* Ending without a path to implementation or deeper reference.

**Example pages:**

* Advanced Generation Parameters  
* A Guide to Tokens and Tokenizers  
* Understanding Retrieval Augmented Generation (RAG) \[new page\]

