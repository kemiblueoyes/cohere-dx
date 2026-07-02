# author-docs — Worked Examples

## Example 1: New Quickstart page (Aya Vision)

**Input:** "Write a quickstart for Aya Vision. Here's the existing page: https://docs.cohere.com/docs/aya-vision"

### Step 1 — Outline stage

**Template confirmed:** Quickstart. Audience: Developer.

**Content-source check:** The existing `/docs/aya-vision` page already covers model variants, context length, and multimodal capabilities in table form — that's Feature-page content, not Quickstart content, so none of it is repeated here. The Quickstart links to it instead of restating it.

**Frontmatter draft:**

```yaml
---
title: "Aya Vision quickstart"
description: "Send an image and a text prompt to Aya Vision using the Chat API and get back a grounded multilingual response."
keywords: "Aya Vision quickstart, multimodal chat, image understanding, Cohere Chat API"
audience: "Developer"
---
```

**Section outline** (per the Quickstart template's five required sections):

1. **Short outcome statement** — By the end of this page, the reader sends an image and a question to Aya Vision and gets a text response back.
2. **Setup** — Install the SDK, set `COHERE_API_KEY`, note the two model options (`c4ai-aya-vision-8b`, `c4ai-aya-vision-32b`) with a one-line pointer to the Feature page for the tradeoff between them, not a repeated table.
3. **Minimal working example** — Per content-model.md's rule that quickstarts use all supported SDKs (code is meant to be copied and run), this is `<CodeBlocks>` with Python, TypeScript, and cURL tabs — not a single Python-only snippet.
4. **Expected response or output** — A sample response, with a short note that model output is non-deterministic.
5. **Further resources** — Link to the Aya Vision Feature page (model details), the Image Inputs concept page, and the Chat API reference.

Pause here and present this outline for approval before drafting.

### Step 2 — Draft stage (illustrative excerpt)

This shows the format the draft should follow once the outline above is approved — not the full page.

```markdown
## Send your first request

<CodeBlocks>
```python Python
import cohere

co = cohere.ClientV2("COHERE_API_KEY")

response = co.chat(
    model="c4ai-aya-vision-8b",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,<BASE64_IMAGE>"}}
            ]
        }
    ]
)

print(response.message.content[0].text)
```
```typescript TypeScript
import { CohereClientV2 } from "cohere-ai";

const cohere = new CohereClientV2({ token: "COHERE_API_KEY" });

const response = await cohere.chat({
  model: "c4ai-aya-vision-8b",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        { type: "imageUrl", imageUrl: { url: "data:image/jpeg;base64,<BASE64_IMAGE>" } }
      ]
    }
  ]
});

console.log(response.message.content[0].text);
```
```bash cURL
curl --request POST \
  --url https://api.cohere.com/v2/chat \
  --header "Authorization: Bearer COHERE_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "c4ai-aya-vision-8b",
    "messages": [
      {
        "role": "user",
        "content": [
          { "type": "text", "text": "What'\''s in this image?" },
          { "type": "image_url", "image_url": { "url": "data:image/jpeg;base64,BASE64_IMAGE" } }
        ]
      }
    ]
  }'
```
</CodeBlocks>
```

Notes on the excerpt above:

- Credential placeholder is `COHERE_API_KEY`, consistent with content-model.md's placeholder rules.
- Tab labels are auto-generated from the language fence label (`Python`, `TypeScript`, `cURL`) per fern-platform-rules.md — no manual titles needed since these snippets differ only by language.
- Field names shown (`image_url`, `imageUrl`) are illustrative for this worked example. Confirm exact request schema against the live API reference before publishing.

### Common mistake this example avoids

Duplicating the current page's existing code sample verbatim instead of upgrading it to the full SDK coverage a Quickstart requires, and re-explaining model capabilities that already live on the Feature page.
