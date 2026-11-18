# Documentation audit and capability map

Reviewed 2026-11-18. The scope is grounded in the live developer documentation, not just the MCP tool list or competitor skill names.

## Corpus and evidence boundary

- Downloaded the official [index](https://serversmtp.com/docs/llms.txt) and [full developer-docs export](https://serversmtp.com/docs/llms-full.txt), containing 48 pages across setup/sending, deliverability, account features, analytics/webhooks, integrations, migration and API references.
- Parsed the current [OpenAPI artifact](https://serversmtp.com/docs/turbo-smtp.yaml): OpenAPI 3.1.0, 43 paths and 58 HTTP operations. Read the substantive documentation for authentication, sending/MIME, SMTP, domain authentication, tracking, suppressions, validation, webhooks, migrations, framework availability, account/sub-account administration and reporting.
- Cross-checked against the [MCP source contract](https://github.com/turboSMTP/mcp/tree/660ef95f6c8aa5f3778a2380c2670e4e1290b778), which exposes 16 tools and three workflow prompts. Those are a different, smaller surface than the full product/API.
- Supplemented the email-expertise scope with current primary Gmail, Yahoo and Outlook sender requirements and RFC 8058. Template rendering/accessibility claims need additional target-client evidence during implementation; the provider docs alone do not establish them.
- This is documentation/content/contract analysis. Published code examples were inventoried, not all executed; package versions, sender rules, plan entitlements and actual customer-account behavior must be rechecked in production acceptance. No live send, account mutation, legal compliance certification or migration was performed.

[Source snapshot metadata](source-snapshot.json) records the export/schema hashes and per-page hashes/URLs. The hashes make this review reproducible; they do not imply the current live pages will stay unchanged. The export's hosted-origin links are normalized to the canonical serversmtp.com/docs URLs below.

## Capability and access findings

| Documented area | What the skills can cover | Actual access boundary |
| --- | --- | --- |
| Sending architecture and sender requirements | Best-practice review, stream separation, authentication/alignment, volume changes, measurement and remediation | Knowledge/supplied artifacts; provider/IP settings may require support, not a customer DNS write |
| Templates, footers and unsubscribe elements | HTML/plain-text/personalization review and guided account configuration | Dashboard features do not establish template CRUD or an email design API |
| API/SMTP and integrations | Working code/configuration, runtime/TLS/permission checks and current integration selection | Use the application's actual version; documented/merged/source-only is not automatically a stable installed package |
| Domains and tracking domains | DNS policy, sending-domain registration/verification and tracking-domain setup guidance | MCP has sending-domain list/add/verify/DNS diagnostics; tracking CNAME values/settings require the documented dashboard path or an independently verified authorized API |
| Delivery and engagement | Per-message/aggregate diagnosis, status interpretation, reporting and reconciliation | MCP analytics tools cover supported reads; CSV export and tracking settings are additional API/dashboard features |
| Delivery webhooks | Authenticated receiver, flat payload parsing, lossless IDs, durable processing/deduplication and reconciliation | Dashboard callback setup; no webhook-registration MCP tool/public API established by this review |
| Validation and suppressions | Risk classification, paid/batch workflow, opt-outs and bounded suppression changes | MCP supports individual validation and suppression tools. Batch upload/start/progress/export/credit balance are separate API/dashboard operations |
| Accounts, keys and alerts | Credential rotation/least privilege, isolation/limits/status, usage alerts, plan/access checks | MCP has account/sub-account reads. Administrative writes need the documented auth path; some key operations require a separate privileged session |
| Migration | Behavior-preserving conversion, preferences/suppressions, queued mail, gradual cutover and rollback | Full SendGrid/Mailgun guides exist; other providers require their own current source/feature mapping before claiming support |
| Billing, marketing add-ons and account recovery | Accurate handoff, entitlement explanation and support escalation | Do not infer a campaign API, password automation or authorization to purchase from a docs menu or support question |

### Details that materially change skill behavior

1. **`mime_raw` is not an API MIME transport.** The send schema accepts the property, but the sending docs say the endpoint does not use it. Route pre-built MIME through SMTP and verify content, rather than treating schema acceptance as delivery behavior.
2. **Identity is more than green DNS checks.** SPF uses the envelope domain, DMARC needs alignment and a nested sender has its own DNS placement. Preserve existing senders/policies. Re-enveloped sending is not proof of visible-From alignment.
3. **Tracking has a distinct setup and uncertain measurements.** Custom tracking uses generated account-specific DNS records. Privacy proxies and link scanners affect opens/clicks. A body unsubscribe link does not by itself prove the applicable one-click behavior.
4. **Hygiene needs a complete lifecycle.** A list upload does not start validation. Validation and sending credits are separate; paid balance fields are not necessarily address counts. Suppression removal can resume delivery and must preserve the original complaint/opt-out reasoning.
5. **Account writes have sharp edges.** Creating a sub-account does not create its key, and profile, status and limits are separate. Key-management calls need the documented session authentication. Omitted permission/IP update fields can broaden access or clear restrictions.
6. **Webhooks differ from analytics.** Callback event names and analytics status names are not interchangeable. `mid` identifies a message, not one event. Respect casing/optional fields, exact IDs, retry limits and out-of-order delivery.
7. **Framework/SDK release status is evidence, not a label.** The docs distinguish released adapters, merged work and source repositories; recheck registries before advertising an installation. C# source SDK targeting .NET Framework and modern direct HTTP examples are different options.
8. **Docs locations and contracts need verification.** The older `/turbo-api/turbo-smtp.yaml` link returned 404 during review; `/docs/turbo-smtp.yaml` returned the live schema. Sending-domain MCP operations also need their own tool/runtime contract because the reviewed public schema does not list that surface.
9. **A provider's retry is not a client resend policy.** Smart Routing may retry temporary delivery through provider infrastructure. It does not justify a skill repeating a timed-out send or switching the requested region.
10. **Pricing and legal facts are conditional.** Read current account/plan evidence and authoritative terms where relevant. Do not freeze commercial allowances into timeless skill instructions or equate a technical check with legal compliance.

## Primary sender-rule supplements

- [Gmail sender guidelines](https://support.google.com/mail/answer/81126?hl=en), checked 2026-11-18: distinguish all-sender requirements from higher-volume personal-Gmail requirements and the applicability of subscription/marketing one-click unsubscribe. The skill must retain those conditions, not impose every bulk requirement on every transactional message.
- [Yahoo sender requirements](https://senders.yahooinc.com/best-practices/), checked 2026-11-18 via direct HTTPS: distinguish all versus bulk senders, authentication/alignment, complaint measurement and opt-out behavior. Public fetch-tool rate limiting was not treated as evidence that requirements were absent.
- [Outlook high-volume sender requirements](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730), checked 2026-11-18: the updated post describes rejection for authentication noncompliance; do not repeat superseded text about junk-folder-only handling or treat Outlook.com and every Microsoft mail environment as identical.
- [RFC 8058](https://www.rfc-editor.org/rfc/rfc8058), reviewed 2026-11-18: verify the actual one-click mechanism and its required message/authentication properties, rather than adding a decorative header and claiming success.

Maintain exact, dated requirements in the implemented references. The review does not certify any customer's current compliance with these rules.

## Page-to-skill coverage

Abbreviations: **BP** Best practices; **TM** Template review; **IN** Integrate; **MG** Migrate; **DN** Domain setup; **WH** Webhooks; **SE** Send email; **DE** Delivery debug; **HY** List hygiene; **AC** Account operations. Rows map product knowledge to ownership, not a promise that each page's operations are exposed over MCP. No page is turned automatically into a separate skill.

| Official developer-doc page | Skill ownership |
| --- | --- |
| [Email Elements, BCCs, and Marketing Tools](https://serversmtp.com/docs/account/email-settings) | TM, BP, AC |
| [Validate Email Addresses Before Sending](https://serversmtp.com/docs/account/email-validation) | HY, BP, DE |
| [turboSMTP Plans and Billing](https://serversmtp.com/docs/account/plans-billing) | AC, IN, BP |
| [Account Security and Two-Factor Authentication](https://serversmtp.com/docs/account/security) | AC, IN, BP |
| [Manage turboSMTP Sub-Accounts](https://serversmtp.com/docs/account/subaccounts) | AC, IN, BP |
| [Track Email Opens and Clicks](https://serversmtp.com/docs/analytics/email-tracking) | BP, TM, DE, AC |
| [Email Analytics in the turboSMTP Dashboard](https://serversmtp.com/docs/analytics/statistics-dashboard) | DE, AC, WH |
| [Receive Email Delivery and Engagement Webhooks](https://serversmtp.com/docs/analytics/webhooks) | WH, MG, DE |
| [Credit Usage Alerts API](https://serversmtp.com/docs/api-reference/alerts) | AC, IN, BP |
| [Analytics API](https://serversmtp.com/docs/api-reference/analytics) | DE, AC, WH |
| [Authenticate turboSMTP API Requests](https://serversmtp.com/docs/api-reference/authentication) | AC, IN, SE |
| [turboSMTP API Hosts and SMTP Settings](https://serversmtp.com/docs/api-reference/base-urls) | IN, SE, AC |
| [Consumer Keys API](https://serversmtp.com/docs/api-reference/consumer-keys) | AC, IN, BP |
| [Email Validation API](https://serversmtp.com/docs/api-reference/email-validation) | HY, BP, DE |
| [turboSMTP REST API v2 Reference](https://serversmtp.com/docs/api-reference/overview) | IN, BP, AC |
| [Send Transactional Email: POST /mail/send Reference](https://serversmtp.com/docs/api-reference/send-email) | IN, SE, TM, MG |
| [Sub-Accounts API](https://serversmtp.com/docs/api-reference/subaccounts) | AC, IN, BP |
| [Suppressions API](https://serversmtp.com/docs/api-reference/suppressions) | HY, BP, DE |
| [turboSMTP Alternatives: Compare Email Providers Side by Side](https://serversmtp.com/docs/compare/overview) | MG, IN |
| [turboSMTP vs Mailgun: Compare EU Email Delivery Options](https://serversmtp.com/docs/compare/turbosmtp-vs-mailgun) | MG, IN |
| [turboSMTP vs SendGrid: A European SendGrid Alternative](https://serversmtp.com/docs/compare/turbosmtp-vs-sendgrid) | MG, IN |
| [Manage Bounces, Spam Complaints, and Unsubscribes](https://serversmtp.com/docs/deliverability/bounce-spam-management) | BP, HY, DE, WH |
| [Configure a Custom Tracking Domain](https://serversmtp.com/docs/deliverability/custom-tracking-domain) | DN, BP, TM, AC |
| [turboSMTP Smart Routing](https://serversmtp.com/docs/deliverability/smart-routing) | BP, DE, AC |
| [Configure SPF, DKIM, and DMARC for Maximum Deliverability](https://serversmtp.com/docs/deliverability/spf-dkim-dmarc) | BP, DN, DE |
| [Create and Manage turboSMTP API Keys](https://serversmtp.com/docs/get-started/api-keys) | AC, IN, SE |
| [Start Your turboSMTP Free Trial](https://serversmtp.com/docs/get-started/free-trial) | IN, SE, AC |
| [Configure Your Email Client with turboSMTP SMTP Settings](https://serversmtp.com/docs/get-started/smtp-configuration) | IN, SE, AC |
| [turboSMTP Guides: Integrations, Comparisons, Migrations](https://serversmtp.com/docs/guides/overview) | IN, BP, AC |
| [Connect Drupal, Joomla, and Magento to turboSMTP via SMTP](https://serversmtp.com/docs/integrations/cms-platforms) | IN, SE, AC |
| [Send from Outlook and Thunderbird with turboSMTP SMTP](https://serversmtp.com/docs/integrations/email-clients) | IN, SE, AC |
| [Send Email from Node.js with Nodemailer and turboSMTP](https://serversmtp.com/docs/integrations/nodemailer) | IN, SE, AC |
| [turboSMTP Integrations: Frameworks, Libraries, and Apps](https://serversmtp.com/docs/integrations/overview) | IN, SE, AC |
| [Official turboSMTP SDKs for C# and PHP Applications](https://serversmtp.com/docs/integrations/sdks) | IN, SE, AC |
| [Send Email from Elixir with the turboSMTP Swoosh Adapter](https://serversmtp.com/docs/integrations/swoosh) | IN, SE, AC |
| [Send Email from Symfony with the turboSMTP Mailer Bridge](https://serversmtp.com/docs/integrations/symfony-mailer) | IN, SE, AC |
| [Send Uptime Kuma Monitor Alerts by Email with turboSMTP](https://serversmtp.com/docs/integrations/uptime-kuma) | IN, SE, AC |
| [Send WordPress and WooCommerce Email Through turboSMTP](https://serversmtp.com/docs/integrations/wordpress) | IN, SE, AC |
| [Start Sending Email with turboSMTP](https://serversmtp.com/docs/introduction) | IN, BP, AC |
| [Migrate from Mailgun to turboSMTP: SMTP and API Guide](https://serversmtp.com/docs/migrate/from-mailgun) | MG, IN |
| [Migrate from SendGrid to turboSMTP: SMTP and API Guide](https://serversmtp.com/docs/migrate/from-sendgrid) | MG, IN |
| [How to Send Email Attachments with the turboSMTP API](https://serversmtp.com/docs/sending/attachments) | IN, TM, SE, MG |
| [Code Examples: Send Email with turboSMTP in Any Language](https://serversmtp.com/docs/sending/code-examples) | IN, SE, AC |
| [Send Transactional Email via the turboSMTP REST API](https://serversmtp.com/docs/sending/email-api) | IN, SE, TM, MG |
| [Send Email Through the turboSMTP SMTP Relay](https://serversmtp.com/docs/sending/smtp-relay) | IN, SE, AC |
| [turboSMTP Common Errors: API, SMTP, and Account Issues](https://serversmtp.com/docs/troubleshooting/common-errors) | DE, IN, AC |
| [turboSMTP FAQ: Accounts, Plans, Sending & Deliverability](https://serversmtp.com/docs/troubleshooting/faq) | DE, IN, AC |
| [Why Emails Land in Spam and How to Fix Inbox Placement](https://serversmtp.com/docs/troubleshooting/spam-folder) | BP, DE, HY, DN |

## Remaining implementation evidence

The production release must supply the behavior/rendering/runtime evidence in [EVALUATION.md](EVALUATION.md), validate current sender rules and fix unsupported or stale installation claims. Planning coverage, a source hash or a valid Markdown file does not satisfy those gates. Product capabilities absent from MCP remain explicitly guided/API modes unless separately implemented and tested.
