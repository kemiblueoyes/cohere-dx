# Writing Style Guide

These are technical writing guidelines that should be used for Cohere's developer documentation. They focus on tone and voice, sentence structure, terminology, capitalization, AI-writing fingerprints to avoid, audience considerations, and the like.

Some of the benefits of using this style guide are:

* Instructions are easier to read and understand.
* More professional feel to documentation.
* Documentation is easier to translate to multiple languages.

Paramount is technical accuracy, which overrides all else. In writing developer documentation technical writers and contributors should strive for:

* Technical accuracy
* Clarity
* Simplicity
* Consistency

Sometimes these objectives can conflict with each other, in which case the technical writer must use their experience and judgement to decide on the best approach.

> **NOTE:** As with most guidelines these are suggestions. Technical writers and contributors should always use their best judgement given the specific circumstances.

## Technical terms

It's important to be consistent with the use of technical terms. In order to provide consistency with technical terms, acronyms, and product names you should always refer to the Cohere Glossary.

## Use International English

The company standard is, as with most software companies, to use International English. This is [defined](https://www.star-ts.com/about/translation-faq/what-is-international-english) as US spelling, with Americanisms removed.

The industry standard dictionary is [Merriam Webster](https://www.merriam-webster.com/).

## Use inclusive language

Use inclusive language. Google has written extensively and thoughtfully on this subject, so there is no point in duplicating that here. See the [Google guide](https://developers.google.com/style/inclusive-documentation) for details on writing inclusive language.

## Empathy

Empathy for developers should always be a key factor in your writing.

## Use present tense

Use present tense. It's easier to read and translate.

Examples:

* *Avoid:* Command X will start the server.
* *Better:* Command X starts the server.

## Use simple language

For technical writing the best approach is to be simple, direct and technically accurate. To achieve this objective use clear, simple, accurate, and directive language.

Avoid being overly casual in developer documentation as this can lead to a sense of lack of professionalism.

Other things to avoid:

* Avoid verbose writing styles.
* Avoid attempts at humor.

Technical writing needs to be unapologetically accurate and precise, and use specific terminology wherever necessary to ensure that the correct and unambiguous meaning is conveyed.

## Avoid fillers

It's sometimes easy to get overly enthusiastic in technical documentation, and this shows itself by liberal use of superlatives. 

Avoid filler words and superfluous adjectives such as 'really nice feature', 'it may be that', 'and that's it'.

## Avoid subjective phrases

Avoid subjective phrases. "You can easily...". "it's simple to...". "It's as easy as that!"

Rather than say how simple it's to do something, show the developer through specific steps. Let the developer be the judge of whether something is simple or not.

## Contractions

It's fine to use common contractions, as long as the intent is clear. Where there may be the possibility for confusion, be explicit, for example, use "it's" or "it has" if using "it's" could lead to confusion. 

One common error is to use "it's" in the belief that the apostrophe is required if used in a possessive manner. This is never the case. For example:
* *Incorrect:* "Cohere persists it's data in memory for two minutes."
* *Correct:* "Cohere persists its data in memory for two minutes."

## Number words

For small numbers (less than 10) write the number as a word:

* *Avoid:* "Cohere persists messages in memory for 2 minutes."
* *Better:* "Cohere persists messages in memory for two minutes."

Larger numbers can stay as numerals, or where precision is required.

## Use active voice

To guide the developer accurately and in the most direct way possible, use the active voice. In active voice the *Subject* *Verbs* the *Object*. Remember SVO.

Examples:

* *Active voice:* The man ate the apple.
* *Passive voice:* The apple was eaten by the man.
* *Active voice:* The client creates the connection.
* *Passive voice:* The connection is created by the client.
* *Active voice:* Cohere provides an Asset Tracking SDK.
* *Passive voice:* An Asset Tracking SDK is provided by Cohere.

Active voice is simpler, more direct, and easier to translate.
If you drop into passive voice because it feels correct for the situation that's fine, but generally you want to keep things simple and use active voice.


## Paragraph breaks

You can be more generous with your use of paragraph breaks. Paragraph breaks make the text less overwhelming and easier to read. Generally, you want to avoid dense and cramped text because it's harder to read and digest.

## Parentheses

Generally avoid long sentences that have embedded parentheses as this makes the text harder to read. Break out the paranthetic text into a new sentence or rewrite the text to not require parentheses. Sometimes the paranthetic text might be better off as a note or tip admonition.

## Avoid vague and cautious language

Avoid words such as would, should, might, and maybe, as it does not inspire confidence.

Example:

* *Avoid:* When an inbound message arrives, you might receive it, or you might get an error, or something!
* *Better:* When an inbound message arrives, the message callback handler is invoked.
* *Avoid:* If you click the button, the alert box will probably be displayed.
* *Better:* When you click the `Submit` button, the alert box is displayed.

## Use second person

You should use 'you' rather than 'we' when referring to the reader, especially in task-based material such as tutorials.

The reason for generally avoiding 'we' is that it can potentially create confusion - who exactly is 'we'? 

Consider the following, for example:

* *Avoid:* We now configure the Time To Live (TTL).

Is that something Cohere configures on the developer's behalf, or does the developer have to do it, and if so how?

It's always best to be explicit: if the developer needs to do something, tell them directly what they need to do and how.

Examples:

* *Avoid:* We now need to enter an API Key.
* *Better:* You now need to enter your API Key in the `Create Application` dialog.
* *Avoid:* We can now click the button to create your Cohere account.
* *Better:* You can now click the button to create your Cohere account.
* *Best:* Click the `Create` button to create your Cohere account.

Use Cohere rather than 'we' when referring to the company.

Example:

* *Avoid:* We also provide a Ruby SDK.
* *Better:* Cohere also provides a Ruby SDK.

## Avoid Latin phrases and abbreviations

Latin abbreviations can occasionally cause confusion if not used correctly. For example, people can get confused between the meaning of "i.e." and "e.g." (and sometimes use them as equivalent).

Examples:

* Use 'for example', instead of 'e.g.'
* Use 'that is' rather than 'i.e.'

Instead of using 'etc.', be specficic. For example:

* *Avoid* The SDK supports common backend languages like Node.js, Python, Ruby, etc.
* *Better* The SDK supports Node.js, Python, Ruby, and other popular backend languages.
* *Better* The SDK supports backend languages like Node.js and Python.

Sometimes writers create variations of Latin abbreviations, such as 'eg', 'e.g', 'eg.' and so on. It's best to avoid this. When automated spell checkers are run, these variations can stop the doc build. 

Avoid Latin phrases such as "quid pro quo", "ad nauseum", "vis-a-vis". They can also be difficult to translate, and not everyone is familiar with their meaning.

## Avoid slang

Avoid slang as this can be hard for some developers to interpret.

For example:

* Don't use overly dramatic words like 'crash' or 'implode', use 'error'.
* Use 'launch' or 'start' rather than 'fire up'.
* Bear in mind the reader's daily language may not be English.
* A mouse is clicked and a keyboard is pressed. Avoid terms such as 'hit' or 'punch' when referring to the keyboard. Avoid: "Now punch in any key to continue."
* Avoid idiomatic language such as "You're good to go", "We'll run this by you", "You're all done".

## Avoid words that are rarely used

Avoid unusual words that have a more commonly used equivalent, unless doing so would compromise clarity and accuracy.

Some words are less frequently used, but have a more commonly used alternative word or phrase.

Some example suggested replacements:

* Use 'while' or 'during which' rather than 'whilst'.
* Use 'therefore' rather than 'ergo'.
* Use 'compatible' rather than 'concordant'.
* Use 'with regard to' rather than 'apropos' (if 'apropos' is being used as a preposition).

The aim is to keep things simple, avoid possible confusion, and aid translation, while retaining accuracy of meaning.

## Capitalization

Use sentence-style capitalization most of the time:

* Capitalize the first word of a sentence, heading, title, or standalone phrase.
* Capitalize proper nouns, which include job titles, and the names of brands, products, and services.
* Use lowercase for everything else.

## Heading forms

Use the imperative form for task headings. It's direct and action-oriented, making it clear what the developer needs to do. If a heading can naturally be prefixed with "How to," it's a task heading and should be imperative.

Examples:

* *Imperative (preferred):* Configure the API client
* *Gerund (avoid):* Configuring the API client
* *Imperative (preferred):* Install the SDK
* *Gerund (avoid):* Installing the SDK

Concept and reference headings are noun phrases, not commands. These may start with -ing terms when that's the established name of a feature or capability. The -ing word names the thing rather than instructing the reader to do something.

Examples:

* *Noun phrase (correct):* Streaming responses
* *Noun phrase (correct):* Grounding with RAG

Note that the same topic can take both forms depending on the page type: "Grounding with RAG" works as a concept heading, but a section that walks through implementation steps should use "Ground responses with RAG."

FAQ headings may be phrased as questions. In all other cases, follow the task/concept distinction above.

## Bulleted lists

A list should always have a piece of text introducing the list followed by a colon, and then a blank line, such as:

This is an example of a bulleted list:

* Precede a list with a sentence and a colon, followed by a blank line.
* Terminate each *sentence* in a list with a full stop.
* Use bulleted lists for lists of items that have no particular order.
* Use numbered lists for ordered sequences, such as procedures, tasks, a series of specific steps, items that are being enumerated, and so on.

Note the following points:

* Each sentence in the list is terminated by a full-stop (period).
* If each item in the list is a single word, a terminating period is not required.
* Don't use bold formatting for prefixes in bullet points (for example, avoid patterns like "**Feature name:** description").

## Acronyms

Define acronyms on first use on a page, in the form of "Oracle Cloud Infrastructure (OCI)". On subsequent use in a topic you don't need to redefine the acronym.

## Be explicit

Try to be explicit. Use precise terms where necessary to improve clarity and avoid ambiguity.

## Avoid genderized language

Avoid genderized language (use user/developer/client as appropriate).

Avoid using 'he or she' constructs. For example:

* *Avoid:* The developer can invoke the method, and then he or she can check the return code.
* *Better:* You can invoke the `connection_state()` method and then check the status code returned.

## Use correct case

Make sure you write the correct case for product names:

* JavaScript not Javascript
* GitHub not Github
* macOS not Mac OS

## Avoid AI-generated content fingerprints

Technical documentation should maintain a natural, human writing style and avoid patterns commonly associated with AI-generated content:

* don't use em-dashes (—) in technical writing. Prefer standard hyphens (-) or restructure the sentence for better clarity.
* Avoid bold prefixes in bullet points (for example, patterns like "**Feature:** Description" or "**Benefits:** Details"). This formatting style is a telltale sign of AI-generated content.
* Avoid formulaic patterns and overly structured prose that may appear mechanical or template-driven.

These guidelines help ensure documentation feels authentic and professionally written while maintaining readability and clarity.

The additional patterns below have been seen repeatedly in AI-assisted drafts and should be cut from final copy:

* Corrective antithesis. Avoid overusing corrective contrast patterns that create artificial insight or false binaries. Examples:
  * Patterns to avoid:
    * "It's not X. It's Y."
    * "It's not about X. It's about Y."
    * "The real challenge is Y."
    * "X isn't just A. It's B."
    * "It's not merely X; it's Y."
  * Instead, explain the relationship directly:
    * "X influences Y."
    * "X is one factor, but Y has a larger impact."
    * "In addition to X, organizations must consider Y."
    * "The decision affects both X and Y."
  * Use contrast only when it clarifies the argument, not as a substitute for analysis.
* Dramatic pivot phrases. Cut "But here's the thing", "Here's the catch", "Here's what most people miss", "Here's the bind". Fold the point into the sentence.
* Soft hedging. Cut "It's worth noting that", "Something we've observed", "This is where X really shines", "It's important to remember". State the thing directly.
* Throat-clearing intros. No "Let's explore", "Let's dive in", "Let's break it down", "In this article we'll", "First, let's understand". The page header is the title, and the first paragraph should land the reader in the middle of the topic.
* Gift-wrapped endings. Cut "In summary", "In conclusion", "Ultimately", "Moving forward", "At the end of the day". Pages end with related links or the last substantive paragraph; they don't restate themselves.
* Generic examples. "Imagine an e-commerce app" or "consider a chat application" with no specific behaviour is filler. Use concrete examples that name a real behaviour (for example, "a user closes their laptop and picks up their phone", "a tool that takes longer than the agent's runtime budget").
* Overexplaining the obvious. Developers know what an HTTP request, a WebSocket, a React hook, a JWT, and the `await` keyword are. Don't define them. State the specific behaviour the reader needs to know about this surface.
* Audience-aware cuts. Once the audience is established (developers, senior engineers, admins), cut explanations of things they already understand. Restating known concepts to fill space makes the writer look unsure of the reader.
* Copy-paste metaphors. If the same metaphor or framing phrase appears more than twice, vary it. "Drop-in", "the session as the anchor", and "the layer that fills the gap" each get used once and stay specific.
* Staccato runs. Avoid stacks of short sentences with no variation (for example, "Sessions are durable. They persist. They survive disconnects. They span devices"). Combine some, let others stretch. Rhythm should follow thinking, not a drumbeat.
* Abstract actors with generic verbs. Cut collective nouns ("participants", "consumers", "entities", "things") and generic verb pairs ("come and go", "happen at three points") when you can name the specific actors and the action they take. Example to cut: "Participants come and go; the session endures." Becomes: "Clients connect and disconnect, agents spin up and terminate, and the session endures." The specific actor + concrete verb reads as observation; the abstract version reads as filler.
* Summary scaffolds. Cut sentences that announce what's coming or restate what just happened: "Every other concept on this page operates on or within a session", "These properties combine to give you…", "All of these mean that…", "Putting it together…". If the connection is real, the prose makes it without saying so. Sister to "Gift-wrapped endings" — scaffolds happen mid-page, not just at the end.

## Patterns to keep

A few patterns are worth keeping when they earn their place. These are counter-rules to the patterns in "Avoid AI-generated content fingerprints":

* Fragments are fine when the rhythm asks for one. "No application code needed." is a complete-enough thought.
* Starting a sentence with "And" or "But" is fine sparingly.
* A comma splice that reads well is acceptable.
* Use judgment. If a sentence reads better with a "rule break", leave it. The goal is prose that sounds like a person wrote it.

## Layer-0 hook for opening prose

Every page should open with a hook that answers "what is this, why should I care?".

## Callouts

Use callouts sparingly:

* `Warning` only for production-blocking issues.
* `Info` for genuine context the reader would otherwise miss.
* `Note` for highlighting additional context or supplementary information.
* `Error` for indicating a potential error or missing information that must be added.

Default to no callout; let prose carry the emphasis. Decorative callouts get purged on review.

## API keys in client code

Never include real API keys in client-side code samples. As the placeholder, use `YOUR_API_KEY` (when a Cohere API key needed) or `SERVICE_NAME_API_KEY` (when an API key from a specific deployment service is needed; replace 'SERVICE_NAME'). And link out to the relevant authentication setup page once per document. This applies to every code sample on every page, with no exceptions.

## Other considerations

Some additional points to bear in mind:

* Explain the *why* to the developer. Rather than simply state what a feature or function does, also explain why it's needed.
* Avoid statements that predict the future, for example, "the next version will have feature X". There are good legal reasons for avoiding predicting the future.
* Avoid time sensitive information. Specify an exact version where possible, for example '1.1', rather than 'current version' as the current version may change. Sometimes though you do want to use the terms 'current version' or 'latest version', for example: "The latest version of the Ruby SDK can always be downloaded from its GitHub repository".
* Avoid using ampersand ('&') instead of 'and', unless you are specifying a programming language operator or similar.
* Avoid pricing information in *technical documentation* as it's subject to change, hard to maintain, and could lead to legal issues if wrong. Instead, direct developers to sales or pricing page.