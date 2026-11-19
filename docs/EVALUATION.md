# Production acceptance specification

A documented catalog is not a production-ready skill release. Each of the ten skills in [CATALOG.md](CATALOG.md) must ship real instructions/references, supported execution paths, behavior evidence and a maintainer. All gates below apply to the complete production release; there is no reduced-quality starter tier.

## Required evidence per skill

| Evidence | Required result |
| --- | --- |
| Content provenance | Task rules link to current authoritative sources; changing provider requirements carry a checked date and applicability; conflicting docs/schema/runtime observations are resolved or constrain support explicitly |
| Standalone package | Valid standard frontmatter, correct names, included resources, all relative links resolving after ZIP extraction and no dependencies on an uninstalled sibling |
| Selection | Positive, paraphrased, ambiguous, multi-skill and unrelated-provider prompts activate the correct declared skills without forcing turboSMTP onto unrelated work |
| Workflow behavior | At least the six concrete cases for that skill pass against observable artifacts/tool traces; cover success, boundary, permission/access failure and unrequested-side-effect prevention |
| Runtime/host support | Clean installation and actual task completion in every advertised client/runtime; test supported versions and API-key access plus Auth account sign-in where the skill uses MCP |
| Authorization and data | No unintended send, DNS/config mutation, suppression removal, account creation, billing action or credential exposure; malicious tool/email/DNS data cannot expand the task |
| Operational behavior | Useful failures for missing tools, permissions, balance, retention, timeouts and uncertain writes; a user can recover without duplicate mutation or unsupported account access |
| Maintenance | Named responsible maintainer role, supported contract/version, current test evidence, report path, release/rollback procedure and trigger/reference refresh ownership |

Maintain at least 60 workflow cases, six for each skill, plus cross-skill routing and shared negative cases. Convert the case IDs in the catalog into machine-readable fixtures with the expected business outcome and artifact/call assertions. Assertions must verify behavior, not the presence of reassuring sentences in a SKILL.md.

## Shared adversarial and routing cases

- “Write code that sends” versus “send now”; “draft HTML” versus “publish/send a campaign.”
- Read-only DNS inspection versus register/verify/publish; one-message diagnosis versus bulk audience maintenance.
- General best-practice audit versus account settings versus a concrete delivery incident.
- Supplied fixtures containing another provider or an unrelated coding/writing task.
- Missing MCP connection, an older tool list, wrong account, insufficient service permissions and a restricted egress IP.
- Instructions hidden in HTML, callback fields, DNS TXT or log data requesting a secret or unrelated action.
- Large IDs, encoded/serialized attachment limits, pagination/timezone boundaries and incomplete retained data.
- Uncertain send/mutation outcomes, exhausted credits, reordered events and a process crash after accepting work.
- A complete, already-authorized request must not acquire an unnecessary second permission gate; missing consequential details still need clarification.

## Execution layers

1. **Static and contract checks:** validate frontmatter, links, references, scripts, examples, supported versions, content/archive secret scan and MCP/API tool schemas. Use pinned dependencies and lockfiles; do not add a paid model key just to check Markdown. Validate plugin manifests against their actual client schemas.
2. **Functional fixtures:** capture HTTP/SMTP requests, parse delivered MIME locally, exercise fake MCP/API/DNS failures and run generated integration/receiver code. Verify both Consumer headers, TLS selection, CID resolution, lossless identifiers, permission behavior, deduplication and no automatic uncertain-send retry.
3. **Clean-context agent evaluations:** run each recorded task with and without the skill in separate clean workspaces. Record client/model/version, skill/source commit, fixture version, expected and observed actions, failures, timing and tokens. Repeat critical cases and investigate inconsistent outcomes. All known critical safety/correctness cases must pass; an attractive average score cannot excuse a duplicate send or unauthorized write.
4. **Release environment acceptance:** install the exact signed candidate/tag/archive in the advertised clients, use an authorized non-customer test account and verify the real supported connection/tool paths. Live sends use privately configured allowlisted sender/recipient addresses and explicit authorization. Default CI stays fake/local and never contacts real recipients.
5. **Published artifact acceptance:** anonymous installation after authorized public visibility, extracted standalone ZIP checks, checksum/source verification, plugin installation/connection where advertised, and update/uninstall/rollback without overwriting unrelated skills.

## Specialized quality requirements

### Email expertise

Best-practice advice must separate observed facts, likely causes, recommendations and unknowns. Test both transactional and subscribed/marketing programs, with the correct mailbox-provider applicability. Verify unsubscribe behavior, not merely header text. A dashboard body-unsubscribe element does not establish all one-click requirements. Do not derive consent, legal compliance or end-to-end data residency from successful address validation, DNS authentication or an EU host.

### HTML and MIME

A browser screenshot is not an email-client rendering test. Define the supported client matrix before release and retain evidence for each advertised target. Exercise common Gmail, Outlook and Apple Mail environments according to the actual supported matrix, including mobile/image blocking and relevant dark-mode behavior. Unverified variants must not be advertised as verified.

Parse the actual MIME produced by the integration: plain-text/HTML alternatives, escaping/personalization, normal attachments, qualified inline CIDs and the whole serialized size. Validate that source fixes preserve destinations and do not expose BCC recipients. No universal design heuristic replaces this evidence.

### Webhooks and state

Run a real test receiver with authenticated/unauthenticated, chunked, duplicate and out-of-order payload fixtures. Kill/restart its processing around durable acceptance. Check that deduplication preserves distinct events for the same message/recipient and that business state is not incorrectly rolled back. Compare dashboard/API status vocabulary with webhook events; they are different contracts. No fabricated HMAC verifier or unlimited replay guarantee.

### Migration and administrative workflows

Prove preservation of personalization, privacy, suppression/preference scope and concurrent opt-outs. Include queued messages and a failed cutover/rollback. For administrative workflows, verify current account/access state before changes and preserve explicit permissions/IP restrictions on update. A dashboard-only handoff is a valid outcome when automation is unsupported, but must clearly say nothing was changed. It must not be presented as completed automated provisioning.

## CI and release evidence

Pull requests run static checks, contract/fixture tests and changed executable examples. Protect the release branch/tag path with required checks and review. Keep third-party actions pinned and token permissions scoped; PR jobs cannot publish or obtain live credentials. Group maintenance updates to prevent notification floods.

Behavior evaluations run on a selected candidate under a recorded budget and supported host/model set. Store the public case definitions and redacted aggregate results; keep raw account/model traces, personal data and live fixtures outside distributable artifacts. CI must detect stale/missing acceptance evidence when a skill's executable behavior or provider contract changes.

The release report names every included skill, supported clients/runtimes, API/MCP contract, source dates, case results, unresolved non-critical limits, rendered/template evidence where relevant and the exact artifact checksums. Do not claim independent security certification, universal client support or measured speed/token improvements without the corresponding evidence.

## Definition of production ready

A skill is production ready only for its explicitly tested tasks and environments when all required evidence above exists, every critical case passes, operational failure paths are useful, instructions are maintainable and the exact distributed package installs/updates correctly. Record actual results in [acceptance evidence](ACCEPTANCE.md).
