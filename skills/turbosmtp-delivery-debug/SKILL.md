---
name: turbosmtp-delivery-debug
description: >-
  Investigate a missing, bounced, deferred or dropped turboSMTP message or compare delivery trends using analytics, DNS, suppression records and received headers.
license: MIT
---

# Investigate delivery evidence

Anchor the investigation to account, time range/timezone and recipient or exact message ID. Use an exact ID with `get_sent_email` when available. Otherwise filter `list_sent_emails` and inspect pagination. Keep IDs as strings. Use `delivery_summary` to compare similar windows and denominators when the question concerns a trend.

Follow the evidence. For a drop, inspect matching `list_suppressions` records and reason. For a domain rejection, read the remote response, use `check_domain_setup` and inspect Authentication-Results on an available received sample. For apparent missing opens, check HTML/tracking conditions and measurement limits.

Report the observed state, likely cause with confidence, evidence still missing and a targeted next action. Keep recipient details and credentials out of support exports. Diagnosis itself should not change account settings, suppressions or delivery attempts.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
