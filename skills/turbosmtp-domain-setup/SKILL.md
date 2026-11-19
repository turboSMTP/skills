---
name: turbosmtp-domain-setup
description: >-
  Inspect DNS or set up and verify a turboSMTP sender domain, SPF, DKIM, DMARC or custom tracking domain. Use for DNS record values, domain alignment or verification failures.
license: MIT
---

# Set up and verify a domain

Identify the exact sender domain, DNS zone and purpose (sending or link tracking). For an inspection, call `check_domain_setup` or inspect supplied records. For an explicit registration, use `list_sender_domains` first and reuse an existing ID. Call `add_sender_domain` once if missing.

Give the DNS administrator the record type, relative host, full name and value. Preserve existing authorized senders and enforcement policy. Use the standard DKIM value returned by diagnostics for the standard selector. Custom selectors require their provisioned key. Wait for publication/TTL as appropriate before calling `verify_sender_domain` for the existing ID. Report the actual verification flags and any outstanding DNS work.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
