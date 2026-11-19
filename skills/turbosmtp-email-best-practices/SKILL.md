---
name: turbosmtp-email-best-practices
description: >-
  Review email sending practices, consent, sender reputation, volume ramp-up, unsubscribe handling and authentication alignment. Use for a pre-launch or program audit, including reviews without account access.
license: MIT
---

# Review a sending program

Identify the streams involved (receipts, password resets, alerts, newsletters), the audience source, promised frequency, recipient providers and typical and peak volume. Work from a sample message with received headers, a description of signup and unsubscribe, and available bounce/complaint trends. If some evidence is missing, return the findings that can already be supported.

1. Trace each stream from collection of permission through suppression at send time. Check whether marketing preferences and complaints survive imports, migrations and retries.
2. Compare the visible From domain with the authenticated identities in received headers. Record which aligned mechanism passed. Assign DNS changes to the domain owner and reverse DNS or pool issues to the sending infrastructure operator.
3. Review a sample with images disabled. Check the identity, promise in the subject, plain-text alternative, links and applicable unsubscribe mechanism.
4. Use observed deferrals and complaints by stream and mailbox provider to decide whether to hold or increase volume. Treat a spike as a reason to investigate acquisition, audience and frequency.
5. Report each finding with evidence, affected stream, priority, owner and one verification step. Check current receiver guidance before quoting thresholds.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
