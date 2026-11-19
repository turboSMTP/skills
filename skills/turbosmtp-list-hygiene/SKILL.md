---
name: turbosmtp-list-hygiene
description: >-
  Review or validate turboSMTP recipient lists and reconcile suppressions, bounces, complaints and opt-outs. Use for list cleaning, validation costs/results and suppression changes.
license: MIT
---

# Maintain a sendable audience

Establish the list source, consent scope, requested action and whether processing incurs validation credits. A local inspection can normalize, deduplicate and identify obvious malformed entries without uploading the list. Keep suppression and subscription data associated with the right account/list.

For an authorized single check use `validate_email`. For lists use the documented batch API or dashboard with authorized access. Check validation balance, upload once, explicitly start the authorized run, poll its list ID, then retrieve results. Upload alone creates a list. Distinguish sending volume, included validation units and paid monetary balance.

Read suppressions with `list_suppressions`. Use `add_suppressions` or `remove_suppressions` only within the requested scope. Verify existing sources and permission to email before removal. Report classified results and remaining unknowns. Do not turn a cleanup, estimate or suppression removal into an unsolicited send.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
