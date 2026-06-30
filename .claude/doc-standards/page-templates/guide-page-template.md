# Guide page template

**Target audience:**  
Primary: Developer / Engineer, Enterprise Admin / Platform Operator, or Enterprise Architect / Technical Decision-Maker, depending on the task.

Secondary, if applicable: \[Audience\]

A guide should be written for the reader who understands the general area and now wants to complete a specific task or follow a recommended implementation path. For developer-facing guides, prioritize clear steps, working examples, and implementation choices. For admin/operator guides, prioritize configuration, validation, operational safety, and maintenance. For architect-facing guides, prioritize decision criteria, tradeoffs, and recommended approaches.

**Use when:**  
Use this page type when the reader needs to accomplish a specific task, configure a capability, implement a workflow, or follow a recommended approach.

A guide should answer how to do something and what choices to make along the way.

**Do not use when:**  
Do not use a guide to provide only a first successful API call, explain a concept from first principles, introduce a broad product area, document every parameter, or teach a complete project from start to finish. Use a Quickstart, Concept, Overview, Reference, or Tutorial page instead.

**Primary reader question:**  
“I understand the area. How do I do this correctly?”

**Planning checklist**

- What task is the reader trying to accomplish?
- What prerequisites are required?
- What is the expected outcome?
- What is the recommended workflow?

**Required sections:**

1. Short task summary  
   State what the guide helps the reader accomplish and when they would use this approach.  
2. Prerequisites  
   List what the reader needs before starting, such as account access, API keys, SDK installation, model availability, cloud platform setup, permissions, or required background knowledge.  
3. Recommended approach  
   Briefly explain the path the guide follows. If there are multiple valid approaches, name the one this guide uses and why.  
4. Implementation or usage pattern  
   Show the reader how to use the capability or complete the task. This may be a numbered procedure, a set of examples, a configuration pattern, an API usage pattern, or a sequence of related sections. Use numbered steps only when the task must be performed in order.  
5. Verify the result  
   Show how the reader can confirm that the task worked. This may be an expected response, console output, dashboard state, API result, deployment status, or validation check.  
6. Next steps  
   Link to related implementation paths, production considerations, reference material, or troubleshooting resources.

**Optional sections:**

* Before you start  
* Architecture or workflow diagram  
* Example request and response  
* Configuration options  
* Environment variables  
* Deployment-specific notes  
* Alternative approaches  
* Best practices  
* Troubleshooting  
* Security or compliance considerations  
* Performance considerations  
* Cleanup steps  
* Migration notes  
* Related concepts

**Content pattern:**  
Move from task context to successful completion.

Recommended pattern:

1. What the guide helps the reader do  
2. What the reader needs to know or have before starting  
3. Recommended approach or usage model  
4. Implementation details, examples, or configuration pattern  
5. Constraints, tradeoffs, or best practices  
6. How to verify, continue, or go deeper

The guide should be practical and task-oriented. It can explain why a step matters, but explanation should support the task rather than become the main focus.

**Code/table guidance:**  
Code is usually expected for developer-facing guides and optional for admin, platform, or architecture guides. Include code when it is necessary to complete or validate the task.

Code examples should be:

* Complete enough to run or adapt  
* Broken into meaningful steps  
* Annotated where decisions or non-obvious behavior matter  
* Consistent with the recommended approach  
* Supported by expected output or validation where possible

Tables are useful for prerequisites, configuration options, environment variables, supported platforms, implementation choices, and tradeoffs. Avoid exhaustive parameter tables; those belong in Reference pages.

**Links and next steps:**  
Next steps are required. These should help the reader continue after completing the task.

For example:

* To understand the underlying concept, read \[concept\].  
* To try the simplest version first, use \[quickstart\].  
* To look up parameters, limits, or supported values, use \[reference\].  
* To build a fuller example, follow \[tutorial\].  
* To prepare for production, read \[production/deployment guide\].  
* To troubleshoot issues, see \[troubleshooting or error reference\].

Adapt the links to the task. Do not include a long generic list of related pages.

**Common mistakes:**

* Writing the guide like a quickstart and skipping necessary context.  
* Writing the guide like a tutorial and adding too much teaching or narrative.  
* Omitting prerequisites.  
* Starting steps before explaining the recommended approach.  
* Mixing multiple unrelated tasks into one guide.  
* Providing code without expected output or validation.  
* Hiding important setup, permissions, or environment requirements.  
* Including exhaustive reference material in the guide.  
* Not explaining choices when there are multiple valid implementation paths.  
* Ending without a clear next step.

**Example pages:**

* Creating a client  
* AWS Private Deployment Guide (EC2 and EKS)  
* Cohere on the Microsoft Azure Platform  
* Qdrant and Cohere (Integration Guide)  
* Cohere Tools on LangChain (Integration Guide)

