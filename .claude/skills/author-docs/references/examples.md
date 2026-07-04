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
3. **Minimal working example** — Per quickstart-page-template.md, Python only, since Python is the default Quickstart language and Cohere Platform is the default deployment path. No TypeScript or cURL tabs, and no deployment-specific variants, unless this were a Python-specific or deployment-specific quickstart.
4. **Expected response or output** — A sample response, with a short note that model output is non-deterministic.
5. **Further resources** — Link to the Aya Vision Feature page (model details), the Image Inputs concept page, and the Chat API reference. Each link is followed by a colon and a short sentence about what it covers, per the template's Further Resources format.

Pause here and present this outline for approval before drafting.

### Step 2 — Draft stage (illustrative excerpt)

This shows the format the draft should follow once the outline above is approved — not the full page.

```markdown
<Steps toc={true}>
  ### Install the SDK and set your API key
  
    ```bash
    pip install cohere
    ```
    ```python
    import cohere

    co = cohere.ClientV2("COHERE_API_KEY")
    ```
  ### end a request with an image and a question
    ```python
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
    ```
  ### Inspect the response
    ```python
    print(response.message.content[0].text)
    ```
    Sample output: a short text description of the image, grounded in what the model observed.
</Steps>
```

Notes on the excerpt above:

- Single Python path throughout, no `<CodeBlocks>` wrapper — per fern-platform-rules.md, `<CodeBlocks>` is for grouping snippets that differ by language; a single language gets a plain fenced block instead.
- Credential placeholder is `COHERE_API_KEY`, consistent with content-model.md's placeholder rules.
- The runnable path (install, request, inspect response) lives inside [`<Steps>`](https://buildwithfern.com/learn/docs/writing-content/components/steps), per quickstart-page-template.md. Supporting explanation — like the note on model options in Setup — sits outside the Steps block, not inside it.
- `<Steps>` requires `toc={true}` so the step headings appear in the page's table of contents.
- Each step is a ### heading inside <Steps toc={true}>, per Fern docs and current live-docs usage — not a <Step> component wrapper.
- Field names shown (`image_url`) are illustrative for this worked example. Confirm exact request schema against the live API reference before publishing.

### Common mistakes this example avoids

- Duplicating the current page's existing code sample verbatim instead of re-scoping it to the Quickstart template's single-Python, single-deployment-path default.
- Including TypeScript or cURL tabs "for completeness," which the updated template explicitly flags as a mistake for Quickstarts.
- Using a plain heading for the runnable flow instead of Fern's `<Steps>` component.
- Re-explaining model capabilities that already live on the Feature page.