# Production skill catalog

This is the required product scope, not a set of starter examples. All ten skills need the production evidence in [EVALUATION.md](EVALUATION.md) before release. Implementation order does not reduce this scope or its quality requirements.

Names are prefixed with `turbosmtp-` to avoid overwriting another provider's generic `email-best-practices` skill. The best-practices and template skills also work without a turboSMTP account. Each directory is independently installable, with no mandatory sibling-skill dependency.

## 1. turbosmtp-email-best-practices

**Job:** review a sending architecture or email program before production, explain an inbox-placement problem at the policy level, or produce an evidence-based remediation plan. This is reusable email expertise, not an API tutorial.

**Required knowledge:** transactional versus subscribed/marketing streams; recipient expectations and consent evidence; recognizable sender identity; SPF/DKIM/DMARC alignment; forward/reverse DNS and TLS ownership; appropriate domain/traffic separation; gradual changes in sending volume; shared versus dedicated infrastructure; bounce/complaint/opt-out handling; validation limits; provider-specific subscription/unsubscribe rules; tracking privacy/proxy effects; ongoing measurement and incident escalation.

Keep Gmail, Yahoo and Outlook requirements in separately dated references with applicability conditions. Verify changing thresholds and enforcement rules against primary sources. Distinguish technical sender requirements, product terms and jurisdiction-specific legal questions. An EU sending endpoint does not certify end-to-end residency or legal compliance.

**Output:** prioritized findings, supporting evidence, missing evidence, the party able to change each item, a safe sequence of improvements and a way to verify the result. Distinguish customer DNS/application work from provider-managed PTR, routing or IP-pool work. No invented fixed warm-up calendar, magic word blacklist, universal image/text ratio, guaranteed inbox placement or automatic `p=reject` recommendation.

**References:** sender architecture; authentication/identity; mailbox-provider requirements; reputation/volume; consent/unsubscribe; measurement. Review uses supplied artifacts and current public guidance; MCP is optional for evidence.

**Release cases BP1–BP6:** audit a mixed transactional/newsletter program; review a low-volume transactional service without imposing irrelevant bulk rules; detect SPF pass with unaligned identity; distinguish a body unsubscribe link from the applicable one-click mechanism; explain open-rate inflation without claiming human engagement; reject a request to bypass opt-outs or promise compliance/inbox placement.

Sources: [authentication](https://serversmtp.com/docs/deliverability/spf-dkim-dmarc), [spam-folder diagnosis](https://serversmtp.com/docs/troubleshooting/spam-folder), [routing](https://serversmtp.com/docs/deliverability/smart-routing), [tracking](https://serversmtp.com/docs/analytics/email-tracking), and the primary mailbox-provider references in [DOCUMENTATION-MAP.md](DOCUMENTATION-MAP.md).

## 2. turbosmtp-email-template-review

**Job:** create, review or repair email HTML/plain text and the message's visible identity before it is sent. Support application-rendered templates, including existing React Email output when present, without forcing a new framework.

**Required knowledge:** email-client HTML/CSS limitations, semantic and accessible content, image alternatives, useful link/button text, responsive layout, dark-mode/image-blocking behavior, plain-text alternatives, personalization escaping, missing variables, safe URLs, reply identity, unsubscribe elements, inline assets and serialized-message size. Check the actual target clients; a browser preview is not proof of Outlook/Gmail rendering.

**Output:** corrected template or review with specific changes, rendered/plain-text/MIME evidence for advertised clients, and remaining compatibility limits. Keep content generation separate from sending. Account dashboard templates/footers are documented UI features; do not invent template CRUD, a server-side template language or an automatic account-template upload API.

**References:** HTML/accessibility, personalization/security, client testing, provider content/MIME mapping. No MCP required. The authoring format stays the application's existing format; only the supported renderers/versions enter the compatibility table.

**Release cases TM1–TM6:** repair an image-only receipt with a text alternative; preserve layout and links when images are blocked; escape an injected personalization value; resolve a missing variable before release; distinguish inline CID assets from normal attachments; generate a review without a live send or fabricated rendering results.

Sources: [email elements](https://serversmtp.com/docs/account/email-settings), [tracking](https://serversmtp.com/docs/analytics/email-tracking), [attachments](https://serversmtp.com/docs/sending/attachments), [send contract](https://serversmtp.com/docs/api-reference/send-email). These support a template-quality skill, not a claim that the provider docs already contain a complete rendering standard; additional client/accessibility evidence is required.

## 3. turbosmtp-integrate

**Job:** add or repair sending in an application, CMS, framework, notification tool or supported email client. Preserve the existing mail abstraction and runtime rather than installing an SDK by habit.

Cover HTTP and SMTP, credentials/permissions/IP restrictions, TLS modes, Global/EU selection, attachments and correlation, errors/unknown outcomes, and configuration deployment without exposing secrets. Include references for the documented HTTP example languages, Nodemailer, Swoosh/Phoenix, WordPress/WooCommerce, CMS SMTP, Uptime Kuma, Symfony and the published SDK sources. Treat merged, development and released integrations differently.

**Output:** working code or precise configuration appropriate to the installed version, validated request/MIME behavior, configuration names and remaining operator actions. Do not claim an unpublished package is installable. Source availability of the C#/PHP SDKs is not evidence of a modern package/runtime release; the C# source target and direct HTTP example runtime differ.

**Access:** repository/local tool access or guided application configuration. MCP is optional. Raw MIME belongs on SMTP when the send endpoint does not use `mime_raw`. Subject requirements and accepted API fields come from the selected API/tool schema, not another client's assumptions.

**Release cases IN1–IN6:** integrate HTTP with both Consumer headers; configure SMTP with required STARTTLS and certificate checks; use an existing supported framework transport; choose a stable alternative to an unavailable bridge; preserve a requested EU route and configured key permissions; handle an uncertain result without retrying/switching providers automatically.

Sources: [SMTP](https://serversmtp.com/docs/sending/smtp-relay), [HTTP](https://serversmtp.com/docs/sending/email-api), [examples](https://serversmtp.com/docs/sending/code-examples), [integrations](https://serversmtp.com/docs/integrations/overview), [SDK status](https://serversmtp.com/docs/integrations/sdks).

## 4. turbosmtp-migrate

**Job:** move an existing sending integration to turboSMTP while preserving customer-visible behavior and the ability to stop/roll back a cutover. Migration is a full production workflow, not just replacing credentials.

Cover inventory, SMTP/API mapping, templates/personalization, recipient privacy, metadata/correlation, regional requirements, suppression/preferences transfer, webhook differences, parallel domain authorization, queued messages, staged traffic comparison and rollback. Maintain complete SendGrid and Mailgun playbooks because those are documented. Other sources require current provider evidence and a capability map before a migration claim; do not fabricate a Resend/Postmark/SES drop-in conversion.

**Output:** feature-gap map, application changes, suppression migration rules, verifiable cutover/rollback checkpoints and explicit remaining manual work. Multiple personalizations must not be flattened into a single visible recipient list. Preserve old-provider authorization until its queued mail and rollback needs are resolved. Reconcile opt-outs during coexistence, not only at the initial export.

**Access:** application repository and authorized provider export/connection paths. A diagnosis or plan does not authorize a production cutover. The user can authorize implementation/cutover explicitly without a second blanket approval ritual.

**Release cases MG1–MG6:** map one SendGrid personalization; preserve privacy and per-recipient substitutions across several messages; convert Mailgun form-data/Basic auth to the documented JSON/header contract; carry opt-outs with their correct scope; adapt webhook authentication/events and large IDs; abort/roll back on a failed acceptance checkpoint without duplicate sends or premature DNS cleanup.

Sources: [SendGrid migration](https://serversmtp.com/docs/migrate/from-sendgrid), [Mailgun migration](https://serversmtp.com/docs/migrate/from-mailgun), [comparisons](https://serversmtp.com/docs/compare/overview).

## 5. turbosmtp-domain-setup

**Job:** register or repair a sending-domain setup and explain authentication or custom-tracking-domain DNS changes. Own the actual DNS/setup procedure; best practices owns the higher-level policy review.

Cover existing-domain discovery, one merged SPF policy, lookup limits, exact DKIM selector/value, nested-subdomain placement, DMARC alignment/inheritance/reporting, verification and DNS cache effects. Keep sending identity, branded tracking links and provider-managed PTR distinct. Custom tracking uses the account's exact generated CNAME records and configured rotation/availability; do not invent targets or assume the sending-domain API configures tracking domains.

**Output:** record changes preserving other senders, evidence from DNS/received headers, verification flags and the remaining action/owner. A diagnostic query alone does not authorize registration or DNS edits. Do not generate a per-domain DKIM key when the provider uses its standard shared record; custom-key provisioning is separate. A root-domain record does not automatically apply to every sending subdomain.

**Access:** MCP `list_sender_domains`, `add_sender_domain`, `check_domain_setup`, `verify_sender_domain` for the supported sending-domain operations. DNS publication requires an authorized DNS tool/user handoff. Custom tracking setup currently uses documented dashboard guidance.

**Release cases DN1–DN6:** inspect DNS without a write; merge existing SPF without authorizing unrelated hosts; place DKIM correctly for a nested subdomain; respect effective DMARC alignment/policy before proposing enforcement; verify an existing domain without duplicate registration; explain tracking-domain CNAMEs/PTR ownership without claiming unsupported MCP writes.

Sources: [SPF/DKIM/DMARC](https://serversmtp.com/docs/deliverability/spf-dkim-dmarc), [tracking domains](https://serversmtp.com/docs/deliverability/custom-tracking-domain), [MCP contract](https://github.com/turboSMTP/mcp).

## 6. turbosmtp-webhooks

**Job:** implement, secure, test and operate an application's delivery-event receiver. Include event interpretation, state transitions and reconciliation, not just an example HTTP route.

Cover dashboard configuration, event availability/propagation, HTTPS and endpoint authentication, flat payloads, timestamp casing, nullable/optional fields, lossless IDs, chunked request bodies, duplicate/out-of-order events, durable acceptance, asynchronous processing, bounded retries and analytics reconciliation. Never copy SendGrid/Mailgun/Resend signature verification into an unsigned turboSMTP callback.

**Output:** executable receiver and fixtures, authenticated failure behavior, durable handling/idempotency strategy, observable state transitions and a dashboard setup checklist. Deduplicate distinct events rather than only `mid`; do not regress a delivered state because an older event arrives later. An open/click event is not proof of a human action. Preserve message-recipient scope.

**Access:** code/HTTP test environment and an authorized operator for dashboard callback configuration. There is no current MCP webhook-registration tool or documented public registration API. Callback authentication is separate from API credentials. Raw results must not leak credentials, recipient content or full callback URLs.

**Release cases WH1–WH6:** accept authenticated chunked JSON; reject missing/wrong receiver authentication; handle `Timestamp`/`timestamp` and large IDs; distinguish duplicate callbacks from different events on the same message; durably accept before acknowledgment and survive an application restart; process out-of-order events and reconcile an exhausted callback retry through analytics.

Sources: [webhooks](https://serversmtp.com/docs/analytics/webhooks), [analytics](https://serversmtp.com/docs/api-reference/analytics), [migration guides](https://serversmtp.com/docs/migrate/from-sendgrid).

## 7. turbosmtp-send-email

**Job:** execute a particular user-requested send through a connected MCP account. Keep explicit sending separate from writing code, drafting a template or diagnosing delivery.

Resolve account/sender/recipients/content/attachments/region and the scope of any batch. Preserve recipient privacy, check the actual supported size/schema, call the send tool once for an authorized message and report acceptance or uncertainty. Use provider/template advice when relevant without forcing every message through every other skill.

**Output:** the result and correlation/message identifier, selected region and a truthful next verification step. Never call acceptance “delivered” or “in the inbox.” Ask for consequential missing fields, not a redundant confirmation after a complete authorized request. A multi-recipient string is not automatically personalized campaign sending.

**Access:** MCP `send_email`, with relevant account/domain reads when needed. `SEND_API` permission/IP restrictions still matter upstream. A missing connection does not authorize extracting credentials from a broker or using another account.

**Release cases SE1–SE6:** send one complete explicit request exactly once; request a genuinely missing recipient/account; honor EU for that call only; preserve BCC/privacy and inline/normal attachments; reject an oversized/invalid request before sending; handle timeout/unknown outcome without automatic resend or region failover.

Sources: [sending](https://serversmtp.com/docs/api-reference/send-email), [attachments](https://serversmtp.com/docs/sending/attachments), [MCP contract](https://github.com/turboSMTP/mcp).

## 8. turbosmtp-delivery-debug

**Job:** investigate a specific missing/bounced/deferred/dropped message or a change in delivery performance, using attributable evidence rather than generic spam advice.

Cover date/timezone/retention bounds, exact large IDs, status groups, API/webhook vocabulary differences, failure reasons, permissions, suppressions, received authentication headers, tracking limits and account/routing escalation. Support aggregate comparisons with documented denominators, pagination and data-availability caveats. Account provisioning/credit management belongs to account operations; a general pre-production audit belongs to best practices.

**Output:** evidence-backed findings, what remains unproven, a targeted next action and a redacted support bundle when needed. Delayed delivery, suppression and spam-folder placement are different outcomes. Do not infer an incident from scanner-driven opens or an empty out-of-retention query. Do not silently resend or delete suppressions.

**Access:** MCP `delivery_summary`, `list_sent_emails`, `get_sent_email`, `list_suppressions`, `check_domain_setup`, plus account reads where relevant. CSV exports and account tracking controls are documented API/dashboard features, not additional MCP tools.

**Release cases DE1–DE6:** correlate recipient/time/message evidence; preserve an ID above JavaScript's safe range; explain a suppressed versus deferred message; distinguish analytics statuses from webhook names; report an incomplete window/denominator or missing permission honestly; identify privacy-proxy/link-scanner effects without changing tracking settings.

Sources: [analytics API](https://serversmtp.com/docs/api-reference/analytics), [statistics](https://serversmtp.com/docs/analytics/statistics-dashboard), [tracking](https://serversmtp.com/docs/analytics/email-tracking), [common errors](https://serversmtp.com/docs/troubleshooting/common-errors).

## 9. turbosmtp-list-hygiene

**Job:** validate an address/list, interpret risk categories, reconcile bounces/complaints/opt-outs and maintain a safe sendable audience. This is independent from diagnosing one message.

Cover syntax/duplicates, consent and preference provenance, validation categories/sub-status, catch-all/unknown risk, separate validation credits and monetary balances, batch upload/start/progress/results/export, suppressions, scoped imports and targeted removal criteria. Validation cannot create consent or guarantee delivery. An uploaded list is not yet validated. A credit purchase amount is not a count of addresses.

**Output:** categorized results and an explainable audience/suppression action plan, including uncertain entries and the operations actually completed. Credit-consuming validation and destructive changes require authorization at the requested scope; a cost estimate or list inspection is not permission to validate/purchase/delete. Never clear complaints/unsubscribes just to make a send succeed.

**Access:** MCP `validate_email`, `list_suppressions`, `add_suppressions`, `remove_suppressions` for their current operations. Batch lifecycle, credit balance and CSV exports use documented API/dashboard paths with a separately authorized connection. No invented MCP batch tool and no reuse of hidden broker credentials.

**Release cases HY1–HY6:** classify a small mixed list without sending; keep consent separate from a `valid` result; explain catch-all/unknown results; distinguish upload from an authorized paid validation start; preserve complaint/unsubscribe scope on import/removal; handle credit/permission/unknown-result failures without purchasing, deleting or spending again automatically.

Sources: [validation guide](https://serversmtp.com/docs/account/email-validation), [validation API](https://serversmtp.com/docs/api-reference/email-validation), [suppressions](https://serversmtp.com/docs/api-reference/suppressions), [bounce/opt-out handling](https://serversmtp.com/docs/deliverability/bounce-spam-management).

## 10. turbosmtp-account-operations

**Job:** configure or review credentials, permissions, IP restrictions, sub-account isolation/limits, credit alerts and account feature settings. Own the account lifecycle and operational configuration, rather than payment execution or per-message diagnosis.

Cover least-privilege service permissions, public egress IPs, secret-once creation, safe credential rotation, plan-aware key allowances, sub-account provisioning/profile/limits/status, separate sub-account keys, usage versus validation balance, credit alert semantics, tracking/BCC settings and meaningful escalation. Prefer current account evidence to hardcoded pricing/features. Explain when administrative operations require different authentication.

**Output:** reviewed configuration, targeted authorized actions where a supported connection exists, verification/rollback steps and explicit dashboard/operator work. Sub-account creation does not automatically create its sending key; setting a profile is distinct from changing its limit/status. Omitted key-update fields can broaden permissions or clear IP restrictions, so preserve explicit state. Global BCC changes expose message copies and need deliberate scope.

**Access:** MCP `get_account_info`, `list_subaccounts`, `get_subaccount` provide supported reads. Provisioning/alerts/tracking use documented API or dashboard workflows only through an authorized administrative path. Credential management has session-authenticated exceptions; MCP bearer tokens and Consumer credentials are not interchangeable with those sessions. Never collect a dashboard password in chat, loop login requests or impersonate another account to bypass missing access.

**Release cases AC1–AC6:** identify a sending permission/IP problem without exposing secrets; rotate while preserving an active integration and key allowance; explain sub-account creation versus separate keys/limits/status; distinguish daily usage alerts from remaining-credit thresholds; preserve permissions/IP restrictions on a partial-looking key edit; hand off unavailable/session-only/billing operations without fabricating MCP writes or making purchases.

Sources: [API keys](https://serversmtp.com/docs/get-started/api-keys), [authentication](https://serversmtp.com/docs/api-reference/authentication), [subaccounts](https://serversmtp.com/docs/api-reference/subaccounts), [alerts](https://serversmtp.com/docs/api-reference/alerts), [email settings](https://serversmtp.com/docs/account/email-settings).

## Routing and ownership

| User task | Primary skill | Boundary to preserve |
| --- | --- | --- |
| “Review our sending program before production” | Best practices | No account mutations or guaranteed compliance |
| “Fix this receipt's HTML” | Template review | No live send or claimed client render without evidence |
| “Wire our app/WordPress/monitor to turboSMTP” | Integrate | Preserve the current stack and actual stable integration status |
| “Move our existing SendGrid flow” | Migrate | Preserve semantics, preferences, queues and rollback |
| “Set up this sending/tracking domain” | Domain setup | Separate sending-domain MCP operations from DNS/dashboard work |
| “Build the delivery callback receiver” | Webhooks | Provider-specific event contract and durable handling |
| “Send this email now” | Send email | The user has requested an actual send, not code generation |
| “Why did this message fail?” | Delivery debug | Evidence first; no resend or suppression deletion |
| “Clean/validate this recipient list” | List hygiene | Respect credits, consent and uncertain outcomes |
| “Manage customer accounts/keys/alerts” | Account operations | Administrative auth and current plan/access remain explicit |

A task can legitimately use several skills. Prefer the most specific task description, load only useful references and preserve the original user scope across transitions. Do not make activation of every sibling a prerequisite for a simple task.
