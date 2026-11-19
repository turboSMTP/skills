---
name: turbosmtp-migrate
description: >-
  Move an existing SendGrid or Mailgun SMTP/API integration to turboSMTP. Use for compatibility mapping, suppression transfer, webhook conversion, cutover and rollback.
license: MIT
---

# Migrate an existing integration

Inventory sending paths, per-recipient substitutions, templates, domains, queue owners, webhook consumers, tracking region and preference scopes. For each feature record an equivalent, an application-owned replacement or an unresolved gap. Resolve any gap affecting privacy or opt-outs before shifting traffic.

Keep the old provider authorized while its queue drains. Merge the new sender into the existing SPF policy. Import suppressions and keep collecting new opt-outs from both providers during coexistence. Render/test each message variant against a fixture. Route a bounded cohort to a single provider and compare acceptance, failure and deferral by recipient domain.

If a checkpoint fails, stop moving new traffic. Preserve both providers' queued message identities and reconcile accepted or uncertain sends rather than replaying the cohort. Roll back only unsent work, retain preferences and retire unused DNS entries/credentials after confirming dependencies and queue drain.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
