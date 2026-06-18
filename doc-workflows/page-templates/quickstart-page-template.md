# Quickstart page template

**Target audience:**  
Primary: Developer / Engineer  
Secondary, if applicable: Enterprise Admin / Platform Operator

Use a secondary audience only when the quickstart helps someone configure or validate a deployment, environment, SDK, or platform setup.

**Use when:**  
Use this page type when the reader needs to get a capability working quickly with minimal setup and copy-pasteable code. A quickstart should help the reader reach a small, successful outcome without requiring them to understand the full concept, architecture, or production workflow first.

**Do not use when:**  
Do not use a quickstart to explain a concept in depth, compare options, teach a full end-to-end project, document every parameter, or describe production best practices in detail. Use a Concept, Overview, Guide, Tutorial, or Reference page instead.

**Primary reader question:**  
“How do I get this working right now?”

**Required sections:**

1. Short outcome statement  
   State what the reader will do and what they will have working by the end of the page.  
2. Setup  
   Include only the minimum requirements needed to run the example. This may include installing the SDK, creating a client, setting an API key, choosing a model, or preparing a small sample input.  
3. Minimal working example  
   Provide the shortest complete code path that demonstrates the capability. The example should be copy-pasteable and should avoid unnecessary abstraction.  
4. Expected response or output  
   Show the reader what success looks like. Include a sample response, returned object, generated text, ranking result, streamed output, citation output, or other visible confirmation.  
5. Further resources  
   End with links that help the reader continue after their first success.

**Optional sections:**

* Before you start  
* API key or authentication note  
* Sample input  
* Documents or test data  
* Environment variable setup  
* Response explanation  
* Streaming example  
* Error or troubleshooting note  
* SDK-specific tabs  
* Next step for production use

**Content pattern:**  
Move quickly from setup to working code to visible output.

Recommended pattern:

1. What you will build or run  
2. Minimal setup  
3. Input or test data, if needed  
4. Run the request  
5. Inspect the response  
6. Continue to deeper docs

The quickstart should prioritize momentum. Explain only what the reader needs to understand to run the example successfully.

**Code/table guidance:**  
Code is required. A quickstart should include a complete, runnable example or a short sequence of code blocks that build toward one working result.

Use code examples that are:

* Short  
* Copy-pasteable  
* Annotated only where needed  
* Focused on one primary success path  
* Free of production-only complexity unless required to make the example work

Avoid large tables. Use tables only for very small setup requirements or environment variables. Put detailed parameter tables, compatibility matrices, limits, and model support information in Reference pages.

**Links and next steps:**  
Further resources are required. Keep this section short and action-oriented.

Include links based on what the reader is likely to need after the first successful run, such as:

* A Guide for the recommended implementation pattern  
* A Concept page for the underlying mental model  
* API Reference for parameters and response fields  
* Related quickstarts for adjacent capabilities  
* Production or deployment guidance, if the quickstart is intentionally minimal

Do not include a long generic list of related links. Each link should help the reader take a clear next step.

**Common mistakes:**

* Starting with too much conceptual explanation.  
* Making the reader choose between too many options before they can run anything.  
* Hiding setup requirements or prerequisites.  
* Providing code that is incomplete or not copy-pasteable.  
* Omitting the expected response or output.  
* Turning the quickstart into a full guide or tutorial.  
* Including production architecture, edge cases, or optimization details too early.  
* Linking to many resources without explaining what to do next.  
* Assuming the reader already knows which model, endpoint, or SDK setup to use.

**Example pages:**

* Retrieval augmented generation (RAG) \- quickstart  
* Reranking \- quickstart  
* Semantic search \- quickstart  
* Text generation \- quickstart  
* Tool use & agents \- quickstart

