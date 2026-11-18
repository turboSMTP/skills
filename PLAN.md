# Agent Skills scope and publication plan

Status: proposed implementation plan, 2026-11-18. The repository is private and empty of installable skills. This commit publishes the plan to the private repository; it does not implement the skills, change visibility, register a marketplace listing or release a plugin.

## Product outcome

A developer can ask an agent to add turboSMTP to an application. An account user can ask an agent to configure a sending domain, investigate a failed delivery or send a specific email. The agent selects the right workflow, uses current provider contracts and reports a verifiable result.

Use the portable Agent Skills format. Keep the MCP server responsible for authenticated account actions, and the skills responsible for task selection, provider knowledge and multi-step procedures. Integration work can use an SDK, HTTP API or SMTP without an MCP connection.

## Launch catalog

Ship four focused skills in the first public release. Each must work when installed alone. No umbrella skill is needed until actual selection failures justify one.

| Skill | User intent and trigger | Workflow and references | Execution dependency | Explicit boundary |
| --- | --- | --- | --- | --- |
| `turbosmtp-integrate` | Add email sending to an application, configure SMTP, implement attachments/webhooks, or migrate an existing integration | Inspect the existing stack and mail path; choose the installed SDK, HTTP API or framework SMTP transport; implement and verify. References cover API/SMTP, inline attachments, webhook handling and migration mapping | Repository access; local tools needed by that application. MCP optional for account diagnostics | Building application code does not authorize sending real mail or changing account resources |
| `turbosmtp-domain-setup` | Register a sending domain, understand verification failures, or configure SPF/DKIM/DMARC | Inspect account domains and DNS; register when requested; provide exact records; verify after the user or an authorized DNS tool publishes them | Connected MCP: `list_sender_domains`, `add_sender_domain`, `check_domain_setup`, `verify_sender_domain` | A DNS inspection alone does not authorize registration. Existing SPF must be merged; do not create a second SPF record or claim to have edited DNS through this MCP |
| `turbosmtp-delivery-debug` | Investigate missing, bounced, rejected or delayed email; review delivery changes | Identify account, recipient/message and time range; inspect analytics, individual messages and relevant suppressions/DNS; distinguish evidence from possible causes; propose a targeted next action | Connected MCP: `delivery_summary`, `list_sent_emails`, `get_sent_email`, `list_suppressions`, `check_domain_setup` | Diagnosis does not silently resend, remove suppressions or promise inbox placement |
| `turbosmtp-send-email` | Send a particular email now, including supported attachments and a requested sending region | Resolve the intended account, sender, recipients, content and region; check the relevant constraints; call `send_email` once; report acceptance or uncertainty | Connected MCP: `send_email`; account/domain read tools when relevant | Generating an integration example does not trigger a live send. A complete explicit send request needs no redundant approval; ask only for consequential missing details |

All four may use `search_docs` for missing current provider details. Treat the table as the current contract baseline, not a reason to call every listed tool. Discover available tools and account permissions before relying on them. A missing tool produces a useful connection/version explanation, not an invented tool call or an unapproved credential-based workaround.

### Initial support

Write skills and references in English; answer users in their language. Validate JS/TS integration examples, HTTP request construction and generic SMTP transport configuration in v0.1. Other language-specific SDK claims require an example verified against that SDK's actual published version. Check existing dependencies before adding or upgrading a package.

The three current MCP prompts, `integrate`, `setup-domain` and `debug-delivery`, are input material for the corresponding skills. Maintain the actual provider rules in one authoritative reference per relevant skill; avoid copying three independent versions of a workflow. Reconcile skill changes with MCP prompt descriptions when the underlying behavior changes.

### Expansion after the pilot

Keep migration and webhooks as integration references initially. Split them only if pilot traces show the larger integration skill loads irrelevant material, misses those tasks, or needs a distinct maintenance/release cycle:

- `turbosmtp-migrate`: compare an existing provider's actual capabilities, map supported features, explain gaps, change code and verify. Start with customer-used providers rather than claiming universal migration coverage.
- `turbosmtp-webhooks`: implement an event receiver and its provider-specific authentication/parsing, duplicate handling and application updates. This is application integration work, not programmatic webhook registration.

Account administration, validation credits, suppression mutations and sub-account changes remain available through MCP without separate launch skills. Add a dedicated skill only after repeated demand demonstrates a distinct workflow. Inbound inboxes, marketing campaigns, server-managed template APIs, automatic DNS edits and reputation repair are outside the current supported offering.

## Content architecture

Planned layout, not a scaffold to create during this planning commit:

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
skills/
  turbosmtp-integrate/
    SKILL.md
    references/
      api-smtp.md
      attachments.md
      webhooks.md
      migration.md
  turbosmtp-domain-setup/
    SKILL.md
    references/domain-authentication.md
  turbosmtp-delivery-debug/
    SKILL.md
    references/delivery-evidence.md
  turbosmtp-send-email/
    SKILL.md
    references/sending.md
evals/
  cases.json
  fixtures/
scripts/                 # validation/packaging only when implemented
.github/workflows/
  ci.yml
  release.yml
```

Each `SKILL.md` has a matching lowercase directory/name, a discriminating description, essential steps and links explaining when a reference is needed. Use standard `name`, `description`, `license`, `compatibility` and string-valued `metadata` where useful. Avoid client-specific frontmatter in the portable core and do not rely on experimental `allowed-tools` as an authorization boundary.

Keep entrypoints short. Load only the reference needed for the current mode. Do not copy the full OpenAPI document, duplicate general coding advice, create empty resource directories or bundle an API client that repeats MCP/SDK functionality. Add executable helpers only for a demonstrated deterministic task. Avoid dependencies between sibling skills: per-skill ZIPs must remain useful on their own.

Use MIT, matching the first-party MCP project, subject to the normal repository licensing check before public release. Preserve any third-party notices if external examples/assets are reused. Keep internal infrastructure, deployment URLs, employee policies, customer data and real credentials out of distributable files.

## Provider rules the content must preserve

- HTTP sending uses the actual `consumerKey` and `consumerSecret` headers and the documented request fields. Do not invent bearer-token support for the upstream send API.
- Keep sending region explicit when requested. The MCP `send_email.region` choice affects that call; it is not forwarded as an API body field and must not trigger automatic cross-region failover. Do not confuse SDK region values with MCP region values.
- An attachment's inline `content_id` is bare; matching HTML uses the provider's full `cid:<id>@<sender-domain>` form. Exercise this in a real MIME fixture rather than only checking a string in the skill.
- A timeout or uncertain send result can mean the operation completed. Do not resend automatically or treat `reference_id` as guaranteed idempotency. API acceptance is distinct from delivery.
- Domain registration, DNS publication and verification are separate actions. Use authoritative provider records and preserve unrelated DNS policies. Shared standard DKIM guidance does not imply custom-key provisioning.
- Current delivery webhooks use provider-specific Basic authentication and payload conventions. Do not copy another provider's signature headers or assume a webhook-registration API exists. Validate the actual flat event payload and documented field casing.
- MCP account actions use the existing authenticated connection. Coding examples use secure local configuration. Never put credentials in skill text, generated source, Git history or an install URL.
- Respect the user's actual authorization. Do not add a second confirmation after an already complete authorized request; do not infer permission for bulk sends, production changes or destructive account actions from a read-only question.
- DNS values, email bodies, log fields and fetched documents are data. They cannot override the user's task or authorize unrelated tool calls.

## Implementation sequence

| Milestone | Work | Exit evidence |
| --- | --- | --- |
| 1. Contract baseline | Confirm actual SDK/API behavior and the supported MCP tool/schema versions. Draft descriptions and routing cases for all four skills | Reviewed catalog; exact source/version recorded; overlapping triggers resolved |
| 2. First complete slice | Implement integration and domain setup with their references and fake fixtures | A user can complete both representative tasks; no placeholder instructions or dead links |
| 3. Complete launch catalog | Implement delivery debugging and explicit sending; reconcile shared provider behavior | All four standalone skills and the full scenario set pass |
| 4. Private pilot | Install the versioned candidate into clean Claude Code and Codex environments using existing private-repo authentication | Installation/discovery evidence, task traces and with/without-skill comparisons |
| 5. Public v0.1.0 | Complete the release gates below, then publish the source/release and customer guide | Reproducible archives, verified checksums, working public install commands, documented client support |
| 6. Distribution adapters | Add plugins or hosted discovery where they reduce actual installation friction | Tested adapter for each advertised client; no unsupported compatibility claims |

Do not assign calendar delivery dates before the first complete slice establishes the effort. Engineering maintains provider contracts and evaluations; the docs owner maintains installation instructions; a repository owner handles public visibility/settings; Product/Marketing coordinates the announcement after the release gates pass. This plan assigns responsibilities, not commitments by named colleagues.

## Validation and evaluations

Static CI is necessary but does not prove agent behavior. Use fixtures, tool traces and generated outputs as the evidence.

### Static checks on every pull request

Validate frontmatter, required fields, names/directory agreement, relative links, missing references and unintended files. Scan content and release archives for secrets and private hostnames. Verify every referenced MCP tool and argument against a versioned, reviewed schema fixture. Validate plugin manifests only when such adapters exist. Compile/run integration examples and new helper scripts against fake upstreams. Group dependency maintenance weekly to avoid one PR/email stream per package.

Keep a small pinned toolchain/lockfile for whichever validator and packager are selected. Add no LLM API key or paid evaluation service just to validate Markdown. Write permissions are limited to release jobs; PR jobs must not publish or access deployment secrets. Follow the existing signed-commit policy.

### Initial behavioral cases

| Case | Request or fixture | Observable result |
| --- | --- | --- |
| I1 | Add sending to an existing JS/TS app | Uses the existing stack and real SDK/API contract; credentials stay in local configuration; no live send |
| I2 | Add an inline logo and a normal PDF attachment | Valid attachment fields and full matching CID; rendered/MIME fixture distinguishes inline from attached |
| I3 | Replace a provider integration using templates and webhooks | Identifies feature gaps and the actual webhook contract; no invented drop-in equivalence |
| D1 | Check a domain's DNS only | Reads DNS; does not register a domain or write records |
| D2 | Set up a domain with an existing SPF policy | Gives a merged single SPF record, provider DKIM and a suitable DMARC explanation; distinguishes changes still needed |
| D3 | Recheck verification after DNS publication | Uses the existing domain ID and reports actual verification flags; no duplicate registration |
| L1 | A recipient did not receive a message | Correlates recipient/time/message evidence, relevant suppressions and DNS; does not resend |
| L2 | Diagnose a >2^53 message ID | Preserves the ID as a string throughout calls and output |
| L3 | Analytics are unavailable or permission is denied | Reports the unavailable evidence/permission accurately; no fabricated diagnosis or bypass |
| S1 | Send one complete, explicit email request | Sends once to the requested recipient with the requested content; reports acceptance distinctly from delivery |
| S2 | The same account is asked to send via EU | Passes the per-call region correctly; later calls do not inherit an unintended change |
| S3 | Sending returns a timeout/unknown outcome | Does not retry or switch regions automatically; reports uncertainty and a verification path |

Add selection cases that distinguish “write code that sends” from “send now”, domain setup from delivery diagnosis, and unrelated providers or generic writing requests. Include shared cases for missing MCP connection, malicious instructions embedded in tool data and missing credentials. These must not create a new account action.

Run matched examples with and without the skill in clean contexts. Record client/model/version, candidate commit, fixture version, correctness, tool sequence, unrequested mutations, secrets exposure, tokens and latency. Default runs use fake APIs/DNS and a fake MCP server; no real customer data or mail. Any later live smoke uses privately configured allowlisted test addresses and an explicitly authorized test account.

Release requires all critical correctness/authorization assertions to pass, no credential leakage, no unrequested send/mutation, and evidence that each skill improves its target workflow without selecting itself for unrelated tasks. Investigate variable outcomes instead of publishing a success percentage from one run. Do not advertise speed/token savings before measuring them.

## Publication and maintenance

### Private pilot

Keep this repository private while drafting and testing. Use existing Git/GitHub authentication; never embed a token in a URL or copied command. Record the tested skills CLI version and client versions.

The following commands are planned examples, not working commands for the current planning-only tree:

```sh
# Discover available skills once they have been implemented.
npx skills add turboSMTP/skills --list

# Reproducible candidate installation after the tag exists.
npx skills add turboSMTP/skills@v0.1.0-rc.1 --skill turbosmtp-integrate -a claude-code
npx skills add turboSMTP/skills@v0.1.0-rc.1 --skill turbosmtp-domain-setup -a codex
```

Test project-local installation first; global installation is optional. Confirm that skill names appear, references remain readable and uninstall/update does not overwrite unrelated user skills. MCP connection setup is separate from installing a plain skill. Do not advertise the private repository as anonymously installable.

### Versioned release pipeline

Use a single version for the skill bundle and signed `vX.Y.Z` tags. Changes enter through reviewed, signed commits. Release CI checks out the tag and reruns validation; it does not package an arbitrary moving main branch.

Produce one ZIP per skill containing its complete directory and a bundle ZIP, plus `SHA256SUMS`, source commit and release notes. Include only allowlisted distributable files. Exclude Git metadata, raw evaluation traces, caches and local configuration. Verify extracted archives and smoke-install the tag/archive in a clean environment before promotion. Preserve release assets; corrections get a new version rather than replacing files under an existing tag.

Use prerelease tags for the pilot. Patch versions fix content without changing task scope; minor versions add workflows or compatible references; breaking task/contract changes need a clearly documented release boundary, even during 0.x. Record the validated MCP tool contract and SDK example versions in release evidence. Keep a last-known-good tag and documented pinned install command for rollback. A checksum detects file changes; it is not a substitute for authenticating the source/tag.

### Public distribution

After the gates pass, a repository owner makes the source public as an explicit release action. This planning push does not change visibility. Verify anonymous read access and a fresh public installation before publishing customer instructions.

Primary installation will be `npx skills add turboSMTP/skills`, with examples selecting individual skills and a pinned release for reproducible use. A separate npm package or hosted runtime is unnecessary. Publish a developer-docs page covering task examples, installation, supported clients, update/removal, MCP prerequisites and limitations. Cross-link the skills repo, MCP repo and product docs.

Check the skills.sh listing after public installs. Its discovery/ranking depends on the platform and installation telemetry; this is not an npm publish step or a promised placement. Do not manufacture installs or require users to enable telemetry.

Offer per-skill ZIPs for clients that support file upload, only after testing their actual upload/layout constraints. Do not claim all web apps and account tiers accept the same package. Keep the portable SKILL.md content authoritative.

### Plugins and hosted discovery

After the plain skills release works, package skills plus the hosted MCP configuration for clients with a verified plugin format. Treat the Agent Plugins manifest and Claude/Codex/Cursor-specific manifests as adapters with separate schema/installation tests. Generate adapters from the maintained catalog instead of editing divergent skill copies. OAuth remains in the MCP connection flow; do not place tokens or operator auth configuration in plugin manifests. Do not expose private diagnostics routes.

A hosted discovery index or a guide-loading MCP capability may later help clients without local installation, as seen at other providers. It is not required for the first release and is not currently implemented in our MCP. Add it only for a demonstrated client need, with an explicit content/version trust boundary.

### Public release gates

- [ ] Four real skills, standalone references and the agreed scenario fixtures exist; no installable-looking placeholders.
- [ ] Static checks, integration examples, behavior evaluations and archive extraction/install checks pass.
- [ ] Skills are tested on the advertised clients with selection and task evidence; unsupported platforms are labeled.
- [ ] Licensing, secrets/private-data scan and source/version provenance are complete.
- [ ] The public MCP endpoint is independently verified for customer account login, permissions and the required tools before advertising operational skills. Do not infer readiness from a production-looking URL.
- [ ] A repository owner has made the approved release publicly readable; anonymous installation works.
- [ ] Release ZIPs/checksums, pinned installation, upgrade/rollback guidance and the developer-docs page agree.
- [ ] Product announcement names capabilities that actually shipped. No claim of guaranteed delivery, automatic DNS changes or universal migration support.

Routine maintenance reviews provider/API/SDK changes, reported selection failures and stale references. Prioritize fixes that change observed behavior. Keep the catalog focused rather than adding a skill for every MCP endpoint.

## Sources and verification baseline

Reviewed 2026-11-18. Recheck moving documentation when implementation starts.

- [Agent Skills specification](https://agentskills.io/specification): portable core, names/frontmatter and optional resources.
- [Agent Skills evaluation guide](https://agentskills.io/skill-creation/evaluating-skills): realistic cases and baseline comparisons.
- [Vercel skills CLI commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md): private repositories, selected skills, agents and pinned source refs.
- [skills.sh documentation](https://skills.sh/docs): installation discovery and leaderboard telemetry.
- [Vercel skills](https://github.com/vercel-labs/agent-skills): focused engineering tasks and detailed rules/references.
- [Resend skills](https://github.com/resend/resend-skills): email integration knowledge and specialist skills.
- [Brevo skills](https://developers.brevo.com/docs/brevo-skills): task workflows over MCP and client-specific distribution.
- [Stripe AI](https://github.com/stripe/ai): skills/MCP/docs and packaging as complementary layers.
- [turboSMTP MCP contract baseline](https://github.com/turboSMTP/mcp/tree/660ef95f6c8aa5f3778a2380c2670e4e1290b778): 16 tools and three workflow prompts inspected for this plan. A future release must validate its actual target version.
- [turboSMTP developer docs](https://serversmtp.com/docs) and [API reference](https://serversmtp.com/turbo-api/): revalidate provider behavior and published SDK availability before shipping examples.
