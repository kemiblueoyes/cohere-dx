# Outline: Deploy with the Cohere Platform

**Status:** Draft created in `cohere-platform-deployment.mdx`. Waiting for draft approval before the final polish pass.

**Target file:** `fern/pages/deployment-options/cohere-platform-deployment.mdx`

**Nav context:** Plan your deployment → Cohere Platform (only page in this section). Same file is referenced from `fern/v1.yml` and `fern/v2.yml`.

---

## Template

**Confirmed template:** Guide

**Why Guide, not another type:**

| Template | Why it does not fit |
|---|---|
| Overview | Deployment Options Overview already orients readers to the full set of options. Get Started → Cohere Platform overview already orients readers to models and use cases. This page is one deployment path, not a cluster of options. |
| Feature | The decision page already answers “what is this and when should I use it.” A feature page would re-introduce the Platform instead of getting the reader onto it. |
| Quickstart | Get Started already covers a first successful API call. This page needs the deployment path: account, keys, client, verification, and production follow-through. |
| Concept | The reader is not stuck on a mental model. They need to complete a setup task. |

**Primary reader question:** “I chose the Cohere Platform (or I am about to). How do I set it up correctly?”

**Primary audience:** Developer

**Secondary audience:** Technical Decision-Maker (arriving from the decision page; needs a short confirmation this is the right option, then a path to setup)

---

## Planning questions (Guide template)

| Question | Answer |
|---|---|
| What task is the reader trying to accomplish? | Stand up the Cohere Platform as their deployment: create an account and API key, authenticate an official SDK against `api.cohere.com`, send a request, and confirm it worked. |
| What prerequisites are required? | Ability to create a Cohere account. Optional: a preferred SDK language. No cloud account, VPC, or container registry. |
| What is the expected outcome? | An authenticated client that can call Cohere models on the hosted API, plus a clear path to a production key and enterprise settings. |
| What is the recommended workflow? | Sign up → create an API key → install the SDK → initialize the client → send a Chat request → inspect the response → upgrade to a production key when ready. |

---

## Content-source check

This page is the **setup guide for one deployment option**. It must not become a second platform overview or a second decision guide.

### Existing pages this outline must not duplicate

| Page | What it already owns | What this page does instead |
|---|---|---|
| [Cohere Platform overview](/docs/the-cohere-platform) (`get-started/the-cohere-platform.mdx`) | Product intro, first-call snippets in four languages, use-case cards, model families, community links | Link for “what you can build” and model families. Do not repeat use-case cards or the four-language chat sample. |
| [Choose a deployment option](/docs/choosing-deployment-option) | Five-option comparison, compliance deep-dives (FedRAMP, HIPAA, GDPR), scenario recommendations | One short “this option is a fit when…” paragraph. Link out for comparison and compliance. Do not copy the factor table. |
| [Cohere deployment options](/docs/deployment-options-overview) | Card list of every deployment option | Do not re-list Bedrock, SageMaker, Azure, OCI, private, or Model Vault as peer cards. |
| [Welcome to Cohere](/docs/welcome) | Product picker: Platform vs Model Vault vs North | Do not re-explain North or restage the product picker. |
| [Installation](/docs/get-started-installation) | Four-language SDK install commands | Link. Do not copy all install blocks. |
| [Creating a client](/docs/create-client) | Client initialization patterns | Link. Show one Platform client init in the steps; do not document every language. |
| [Authentication](/docs/authentication) | Auth across all deployments | Cover Platform keys only at the level needed to complete setup. Do not document Bedrock, Azure, OCI, or private auth. |
| [API keys and rate limits](/docs/rate-limits) | Full trial vs production rate-limit tables | Link. Do not copy tables. |
| [Upgrade to a production key](/docs/going-live) | Safety form, payment method, sensitive-use review | Link as the production next step. |
| [How Cohere pricing and billing works](/docs/how-does-cohere-pricing-work) | Billing units, trial vs production billing | Link. |
| [SDKs by deployment](/docs/cohere-works-everywhere) | Feature and SDK matrix by environment | One sentence: Platform has full feature support. Link for the matrix. |

### What this page uniquely owns

- The Cohere Platform as a **deployment option** in the Plan your deployment IA (the missing sibling to Model Vault, cloud AI services, and private deployment setup pages).
- The end-to-end hosted-API setup path: account → key → client → first request → verify.
- What Cohere controls vs what the reader controls, scoped to this option only.
- Production follow-through specific to this deployment: trial vs production keys (pointer), rate limits (pointer), training opt-out / ZDR (pointer), when to move to Model Vault.

### Downstream link fix (after the page ships)

[Choose a deployment option](/docs/choosing-deployment-option) currently links “Set up the Cohere Platform” to `/docs/the-cohere-platform`. That destination should change to this page once it is published.

---

## Frontmatter draft

```yaml
---
title: "Deploy with the Cohere Platform"
description: "Set up the Cohere Platform: create an API key, authenticate the SDK, and send a request on Cohere's hosted API."
keywords: "Cohere Platform, hosted API, managed deployment, API key, Cohere SaaS"
audience: "Developer, Technical Decision-Maker"
---
```

| Field | Value | Notes |
|---|---|---|
| title | Deploy with the Cohere Platform (32 chars) | Imperative is allowed: this page is task-oriented. Matches the current stub title and the user request. |
| description | 118 chars | States the task and the outcome. Stays under 160. |
| keywords | Four short phrases | Deployment-scoped; does not repeat Get Started keywords like Command / Embed / Rerank. |
| audience | Developer, Technical Decision-Maker | Developer is primary. Decision-Maker is secondary because this page sits under Plan your deployment. |

**Slug recommendation:** `docs/cohere-platform-deployment` (or `docs/deploy-cohere-platform` if we want the URL to match the title). Confirm before drafting.

---

## Section outline

Follows the Guide template’s required section order. Optional sections are marked.

### 1. Short task summary

State what the guide helps the reader do and when they would use this approach.

**Draft intent:**

- The Cohere Platform is Cohere’s fully managed hosted API (`api.cohere.com`).
- Cohere hosts the models, manages availability and updates, and you call the API with a key. No infrastructure to provision.
- Use this guide after you have chosen the Platform (or confirmed it is the right starting point) and need to get a working, authenticated client.

**One-paragraph fit check (do not expand into a comparison):**

- Best when you want the fastest path to Cohere models and your data-sensitivity requirements are met by Cohere’s enterprise data commitments.
- If you need dedicated isolation, no rate limits, or confidential computing, go to [Model Vault](/docs/model-vault). If you are still choosing, go to [Choose a deployment option](/docs/choosing-deployment-option).

**Do not include:** Model family list, use-case cards, five-option table.

### 2. Prerequisites

What the reader needs before starting.

- A Cohere account, or the ability to [create one](https://dashboard.cohere.com/welcome/register).
- Access to the [API keys page](https://dashboard.cohere.com/api-keys) after sign-up.
- A supported SDK language if they will call the API from code: Python, TypeScript, Java, or Go. Point to [Installation](/docs/get-started-installation) rather than repeating install commands.
- No cloud subscription, VPC, IAM role, or container license.

Optional note: readers who want to try the API without code can use the [Playground](https://dashboard.cohere.com/playground/generate). This guide covers the API path.

### 3. Recommended approach

Name the path this guide uses and why.

- **Path:** Official Cohere SDK → `api.cohere.com` → API key in the client.
- **Why:** This is the default Platform path. It gives full feature support and matches the rest of the Get Started and API docs.
- **Not covered here:** Cloud-provider clients (Bedrock, SageMaker, Azure, OCI), Model Vault endpoints, or private-deployment base URLs. Those have their own setup guides.

Short control split (keep to a few lines; the decision page owns the long version):

- **Cohere controls:** Infrastructure, model hosting, availability, updates.
- **You control:** API keys, which models you call, and how you integrate the API.

### 4. Implementation or usage pattern

Numbered procedure. Use Fern `<Steps toc={true}>` in the eventual draft. Python only for the runnable example (Guide default; Platform overview already has four-language samples).

#### Step 1 — Create a Cohere account

- Register at the dashboard.
- Trial access is enough to complete this guide.

#### Step 2 — Create an API key

- Open the API keys page and create a **trial** key for evaluation.
- One sentence on the two key types: trial (free, rate-limited) vs production (paid, higher limits). Link [Authentication](/docs/authentication) and [API keys and rate limits](/docs/rate-limits) for details.
- Store the key as `COHERE_API_KEY`. Do not commit it.

#### Step 3 — Install the SDK

- Link to [Installation](/docs/get-started-installation) for the install command in the reader’s language.
- In the draft, show the Python install only (`pip install -U cohere`) so the steps stay runnable without copying all four language blocks.

#### Step 4 — Initialize the client

- Short Python example: `cohere.Client(api_key="COHERE_API_KEY")` (v1 page) or `cohere.ClientV2(...)` (if this page is treated as v2-canonical — confirm which client the published v1/v2 shared file should show).
- Note the default base URL: `https://api.cohere.com`.
- Link [Creating a client](/docs/create-client) for other languages.

#### Step 5 — Send a request

- One Chat call with a current Command model (confirm the model ID against the live models page at draft time; do not hardcode a stale ID in this outline).
- Keep the prompt trivial. This is a connectivity check, not a Chat tutorial.
- Link [Cohere Platform overview](/docs/the-cohere-platform) and the Chat API reference for richer examples.

### 5. Verify the result

How the reader knows setup worked.

- Print or inspect `response` (or `response.message` / equivalent, depending on client version confirmed at draft time).
- Success looks like a non-empty model reply, not an auth or rate-limit error.
- Short note that model output is non-deterministic; the check is “the call succeeded,” not a specific string.
- If the call fails: point to invalid/missing key, trial rate limits, and [API keys and rate limits](/docs/rate-limits). Do not add a full troubleshooting section unless review asks for one.

### 6. Security and compliance considerations (optional, recommended)

Keep this to a short list with links. The decision page owns the deep-dive.

- Prompts and completions are processed on Cohere’s infrastructure.
- Enterprise customers can opt out of model training in the dashboard.
- Zero Data Retention (ZDR) is available if approved; Cohere does not log prompts or completions under ZDR.
- A Data Processing Agreement (DPA) is available for enterprise customers.
- Do not submit PHI through the Platform SaaS service. Link the HIPAA section of the decision page.
- Point to [Enterprise Data Commitments](https://cohere.com/enterprise-data-commitments) and the [Trust Center](https://trustcenter.cohere.com).

### 7. Production considerations (optional, recommended)

What to do after the first successful call, without turning this into the going-live page.

- Upgrade from a trial key to a production key: [Upgrade to a production key](/docs/going-live).
- Review [rate limits](/docs/rate-limits) and [pricing](/docs/how-does-cohere-pricing-work).
- Subscribe to the [status page](https://status.cohere.ai).
- If you later need dedicated capacity, no rate limits, or single-tenant isolation, move to [Model Vault](/docs/model-vault). Do not expand into a migration guide.

### 8. Next steps (required)

Guided links, each with a one-line “this is for…” clause. Not a dump of every related page.

- To see what you can build on the Platform, read [Cohere Platform overview](/docs/the-cohere-platform).
- To compare this option with Model Vault, cloud AI services, or private deployment, read [Choose a deployment option](/docs/choosing-deployment-option).
- To look up endpoints and parameters, use the [API reference](/reference/about).
- To initialize a client in another language, see [Creating a client](/docs/create-client).
- To go to production, follow [Upgrade to a production key](/docs/going-live).

---

## Code and component notes (for the later draft)

- Use `<Steps toc={true}>` for the setup procedure. Supporting explanation (fit check, control split) stays outside Steps.
- Python only in the runnable path. No TypeScript / Java / Go / cURL tabs on this page.
- Credential placeholder: `COHERE_API_KEY` (ALL_CAPS), consistent with `content-model.md`.
- Single-language snippets use a plain fenced block, not `<CodeBlocks>`.
- No rate-limit tables, model-family tables, or five-option comparison tables.
- Default to no callouts. If one is needed: a `Note` that trial keys are rate-limited, or a `Warning` only if we must say not to send PHI.

---

## Open questions for review

1. **Client version on this shared v1/v2 file.** `v1.yml` and `v2.yml` both point at this one MDX file. `the-cohere-platform.mdx` (v1) uses `cohere.Client`; the v2 counterpart uses `cohere.ClientV2`. Which client should this page show?
2. **Slug.** Keep a new slug (`docs/cohere-platform-deployment`) or reuse something readers already know?
3. **Playground.** Mention as an optional no-code path in Prerequisites, or leave it off so the page stays API-only?
4. **Security / production sections.** Recommended here so the page is a complete deployment landing page. Cut them if you want a shorter setup-only guide.

---

## Out of scope

- Model catalogs, capability descriptions, or use-case cards.
- Fine-tuning, RAG, tool use, or any workload tutorial.
- Cloud, private, or Model Vault setup steps.
- Full compliance matrices (FedRAMP, HIPAA, GDPR).
- Full rate-limit or pricing tables.
- Four-language install or chat samples.
