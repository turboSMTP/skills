---
name: turbosmtp-send-email
description: >-
  Send a specific email requested by the user through their connected turboSMTP MCP account, including CC/BCC, inline images, attachments and a chosen sending region.
license: MIT
---

# Send a requested email

Identify the actual send request, sender, recipients, content and authorized account. A draft or a request for code produces a draft or code. If a real send is requested and sufficiently specified, use the connected `send_email` tool. Ask only for missing details that change the intended send.

Use the advertised schema. Preserve To/CC/BCC and separate personalized messages. Include the plain-text alternative when available. Pass an explicit `region` only for a requested global or EU route. Validate attachment fields and total encoded size. Do not infer region from recipient location.

Call once per intended message. Report the acceptance identifier and selected region if known. An uncertain mutation or timeout requires reconciliation in analytics or application records. Do not automatically resend or switch regions. If permission is denied, explain the SEND_API permission, key validity and allowed egress IP checks without asking for secrets.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
