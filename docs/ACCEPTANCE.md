# Private acceptance record

The checkout contains ten installable skills. Maintainers can build ten standalone ZIPs, the catalog ZIP and SHA256SUMS with Python 3.11 or newer. CI uploads these as private workflow artifacts. This record covers checks on 2026-11-19.

| Exercise | Result |
| --- | --- |
| Skill Creator validation | All ten entrypoints passed the author's installed quick validator. |
| Local install | Skills CLI 1.7.4 discovered all ten in a clean project. Project-local installation for Claude Code and Codex included the entrypoints and their relative field guides. |
| Artifact integrity | Built the archives and compared each packaged file to its source, checked local reference paths inside the skill boundary, verified checksums and confirmed that the bundle contains the same files. |
| Independent task trials | One qualitative pass for each of ten requests. The evaluator picked the intended skill from its description for each request and used its packaged instructions. No credentials or live account actions were involved. |

## Observed decisions

| Request | Skill selected | Observed result |
| --- | --- | --- |
| Order receipt and one-click opt-out | Email best practices | Distinguished receipt-only and subscription mail. Added the receipt example explicitly after review. |
| Scoped discounts and opt-outs on migration | Migrate | Preserved per-recipient content and scoped preferences across cutover. Added explicit SendGrid group guidance after review. |
| Diagnose a dropped message using only a large ID | Delivery debug | Preserved the ID and requested the missing event evidence. |
| Write an inline-logo HTTP example | Integrate | Used both Consumer headers and the qualified CID without sending mail. |
| Review a template with an absent reset URL | Template review | Identified the required-value failure and escaped untrusted markup. Restricted fallbacks to optional fields after review. |
| Inspect DNS for a nested sender | Domain setup | Preserved existing SPF authorizations and used zone-relative subdomain names in a read-only diagnosis. |
| Duplicate callback and distinct open after restart | Webhooks | Recommended durable deduplication and separate recording of the open. |
| An EU send timed out | Send email | Preserved the unknown outcome without replay or failover. Fixed an unrelated plain-text example that promised an attachment. |
| Uploaded CSV and a valid but unsubscribed contact | List hygiene | Kept the opt-out and recognized the cost boundary between uploading and starting validation. |
| Change the label of an IP-restricted key | Account operations | Preserved the existing complete permission and egress restrictions on update. |

The 60 cases in [the evaluation set](../evals/cases.json) are inputs and expected outcomes. The ten qualitative trials above cover a subset and lack a matched no-skill baseline. The installed paths were checked locally. Full client sessions, independent actual email-client rendering, generated-code runtime tests, live authorized account acceptance and a tagged public release still require evidence under [the evaluation specification](EVALUATION.md).
