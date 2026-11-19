---
name: turbosmtp-email-template-review
description: >-
  Build or review an email template, including responsive HTML, text fallback, personalization, links, inline images and accessibility. Use for message artifacts and rendering issues.
license: MIT
---

# Review an email template

Render the actual template with representative data in its existing engine. Include a missing value, a long value and punctuation in a name. Compare the result to the message purpose and the requested action. A receipt should still communicate the amount, order identifier and next step with images disabled.

Keep the plain-text part useful on its own. Give links descriptive text and a visible destination in the text version. Preserve intentional query parameters, tracking and recipient-specific links. Escape dynamic text and attributes for their output context and allow only expected URL schemes in links. Use fallbacks only for optional fields. Fail rendering before sending when a required value, especially a recipient-specific reset URL, is missing.

Inspect the generated MIME and, where available, actual target-client renders. Check narrow widths, dark mode, long labels, missing images and keyboard/screen-reader reading order. Return the edited source plus which client/version and fixture were exercised. Drafting and reviewing require no account action.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
