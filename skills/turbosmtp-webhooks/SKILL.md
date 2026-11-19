---
name: turbosmtp-webhooks
description: >-
  Implement or repair a turboSMTP delivery-event webhook receiver, including callback authentication, parsing, deduplication, durable acknowledgment and reconciliation.
license: MIT
---

# Process delivery webhooks

Configure the HTTPS callback and required event types in the dashboard. Check event availability on the account. Keep receiver credentials separate from sending credentials. Authenticate the request before processing. A sender-supplied JSON field cannot authenticate a callback.

Read the complete body with a bounded size and parse flat JSON losslessly. Validate status, message ID, recipient and timestamp. Atomically insert the authenticated event and deduplication identity into durable storage before returning a 2xx. Process application updates from that store. On a duplicate already committed event acknowledge it without repeating business effects.

Preserve independent delivery and engagement facts when events arrive out of order. Exercise a process restart after commit and before acknowledgment. Use analytics to reconcile gaps if delivery retries are exhausted. Report the remaining dashboard setup and which fixtures passed.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
