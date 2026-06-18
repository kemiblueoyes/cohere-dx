# Fern platform rules

## Callouts

```html
<Info>For genuine context the reader would otherwise miss.</Info>

<Warning>Only for production-blocking issues where user action may cause failure and might be irreversible.</Warning>

<Note>For highlighting helpful context or supplementary information.</Note>

<Error>This callout should only be used in API reference docs for indicating a potential error or missing information that must be added.</Error>
```

## Code

Choose between `<CodeBlocks>` and `<Tabs>` based on what varies between the grouped snippets.

**Use `<CodeBlocks>` when the snippets differ by programming language.** Tab names are generated automatically from the language label after the fence, so you don't write titles. This is the default for showing the same operation across SDKs.

````html
<CodeBlocks>
```python Python
    ...
```
```typescript TypeScript
    ...
```
</CodeBlocks>
````

**Use `<Tabs>` when the snippets differ by anything other than (just) language** (deployment platform, ecosystem, concept), or when the tabs share one language and so can't be distinguished by a language label. Titles are free text that you write.

```html
<Tabs>
    <Tab title="Cohere Platform">
    ...
    </Tab>
    <Tab title="Azure">
    ...
    </Tab>
</Tabs>
```

```html
<Tabs>
    <Tab title="Python">
        ```python
            ...
        ```
        Some other content such as a table
        
    </Tab>
    <Tab title="TypeScript">
        ```typescript
            ...
        ```
        Some other content such as a table
    </Tab>
</Tabs>
```

Additional conventions:

- Don't wrap a single snippet in `<CodeBlocks>` just for styling; use a plain fenced code block.
- Keep the platform axis consistent: when grouping by deployment platform, use `<Tabs>` rather than splitting platforms across markdown headings.

## Cards

For card groups, use:

```html
<CardGroup cols={2}>
    <Card>
    ...
    </Card>
</CardGroup>
```

## Tables

Use regular markdown for tables with 20 or fewer rows.

For tables with over 20 rows, use a searchable table:

```html
<SearchableTable>
...
</SearchableTable>
```