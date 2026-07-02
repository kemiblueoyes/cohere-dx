# Tutorial page template

**Target audience:**  
Primary: Developer / Engineer  
Secondary, if applicable: Enterprise Admin / Platform Operator

A tutorial should be written for readers who want to learn by building something real from start to finish. For developer-facing tutorials, prioritize a complete working example, explanations along the way, and a finished outcome. For admin/operator tutorials, use this page type only when the reader is walking through a complete setup or workflow in a learning-oriented sequence.

**Use when:**  
Use this page type when the reader needs to learn a capability, workflow, or pattern by building a complete example.

A tutorial should walk the reader through a realistic scenario from setup to finished result. It should teach through sequence, not just provide isolated code snippets or task instructions.

**Do not use when:**  
Do not use a tutorial for a first quick success, a short task, a conceptual explanation, a feature introduction, or factual lookup. Use a Quickstart, Guide, Concept, Feature, or Reference page instead.

**Primary reader question:**  
“Can you walk me through building something so I understand how this works?”

**Planning checklist**

- What will the reader build?
- What skills will they learn?
- What is the finished outcome?

**Required sections:**

1. Tutorial outcome  
   State what the reader will build, what the finished result will do, and what they will learn.  
2. Before you start  
   List prerequisites, required access, SDKs, API keys, sample data, dependencies, and assumed knowledge.  
3. Scenario or use case  
   Briefly explain the realistic scenario the tutorial uses. This gives the sequence a purpose and helps the reader understand why each step matters.  
4. Setup  
   Help the reader prepare the environment, client, data, tools, or configuration needed for the tutorial.  
5. Build steps  
   Walk through the example in a clear sequence. Each section should add one meaningful part of the final result.  
6. Run the completed example  
   Show how to run the full workflow or final version.  
7. Review the result  
   Show the expected output and explain what happened. Connect the output back to the tutorial goal.  
8. Summary and next steps  
   Recap what the reader built, what they learned, and where to go next.

**Optional sections:**

- Architecture or workflow diagram  
- Sample dataset  
- Full final code  
- Intermediate checkpoints  
- Expected output after each major step  
- Troubleshooting  
- Variations or extensions  
- Cleanup steps  
- Production considerations  
- Related guides  
- Related concepts  
- API reference links

**Content pattern:**  
Teach by building.

Recommended pattern:

1. What you will build  
2. What you need before starting  
3. The scenario  
4. Initial setup  
5. Build part one  
6. Build part two  
7. Build part three, as needed  
8. Run the complete example  
9. Explain the result  
10. Continue or adapt the example

A tutorial should have a clear beginning, middle, and end. The reader should finish with something complete enough to understand the workflow, not just a disconnected set of examples.

**Code/table guidance:**  
Code is usually required for developer-facing tutorials. The code should build progressively toward a complete working example.

Use code examples that are:

- Sequential  
- Runnable or easy to adapt  
- Explained in context  
- Connected to the scenario  
- Supported by expected output  
- Consolidated at the end when useful

Tables are optional. Use tables for sample data, tool definitions, configuration values, or comparison points that support the tutorial. Do not use large lookup tables or exhaustive parameter tables; those belong in Reference pages.

**Links and next steps:**  
Next steps are required. They should help the reader continue after completing the tutorial.

For example:

- To understand the underlying concept, read \[concept\].  
- To implement this pattern in your application, follow \[guide\].  
- To try a shorter first-success path, use \[quickstart\].  
- To look up parameters, limits, or supported values, use \[reference\].  
- To extend this example, follow \[related tutorial or advanced guide\].

Adapt the links to the tutorial. Do not include a long generic list of related pages.

**Common mistakes:**

- Writing a tutorial as a loose collection of examples.  
- Skipping the scenario or finished outcome.  
- Assuming the reader knows why each step matters.  
- Providing code without explaining what changed or why.  
- Ending without showing the complete result.  
- Turning the tutorial into a quickstart by making it too shallow.  
- Turning the tutorial into a guide by focusing only on task completion.  
- Turning the tutorial into reference by listing parameters or options.  
- Omitting prerequisites, setup, or expected output.  
- Adding production complexity before the reader understands the basic workflow.

**Example pages:**

- Routing Queries to Data Sources  
- Generate Parallel Queries for Better RAG Retrieval  
- Performing Tasks Sequentially with Cohere’s RAG  
- Generating Multi-Faceted Queries  
- Querying Structured Data (Tables)

