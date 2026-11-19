---
name: turbosmtp-integrate
description: >-
  Integrate turboSMTP sending into application code, a framework, CMS, monitor or mail client using its existing SMTP transport, SDK or HTTP API. Use for implementation and configuration.
license: MIT
---

# Integrate application sending

Identify where the application already builds and sends mail. Inspect its runtime, installed package versions, secret configuration and existing tests. Choose the smallest compatible transport. Prefer the existing SMTP mailer for fully formed MIME or existing frameworks. Use the regional HTTPS send endpoint for an application using JSON.

Keep secrets in server-side configuration. Grant only the relevant permission. Preserve the requested region and the application's envelope, sender, recipient privacy, headers and body parts. Use a fake SMTP sink or HTTP endpoint to verify the emitted request. Return the changed code/configuration and what the tests established. When diagnosing an uncertain send, query its status before considering another attempt.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
