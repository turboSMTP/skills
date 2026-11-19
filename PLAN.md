# Production Agent Skills specification and publication plan

Status: production product specification, revised 2026-11-18. The required deliverable is a complete, tested ten-skill product with maintainable expertise and working workflows. The ten skill directories are implemented. See [acceptance evidence](docs/ACCEPTANCE.md) for verification status.

## Product scope

The product covers email-program quality, message/template quality, application integration, provider migration, domain setup, event processing, explicit sending, delivery diagnosis, audience hygiene and account operations. These are customer jobs and areas of expertise, not one skill per API endpoint.

The [catalog](docs/CATALOG.md) defines the required content, outputs, supported execution paths, boundaries and six acceptance cases for each skill. The [documentation map](docs/DOCUMENTATION-MAP.md) connects that scope to the official docs and identifies gaps that must not be papered over with invented capabilities. The [production acceptance specification](docs/EVALUATION.md) defines what evidence is required before release.

## Required catalog

| Skill | Product outcome | Works without MCP? |
| --- | --- | --- |
| `turbosmtp-email-best-practices` | Evidence-based production review of sending architecture, authentication/alignment, reputation, subscriptions, volume and measurement | Yes; MCP can supply account evidence |
| `turbosmtp-email-template-review` | Safe, accessible, client-tested HTML/plain-text templates, personalization and inline assets | Yes |
| `turbosmtp-integrate` | Working API/SMTP/framework/CMS/application integration matching the actual installed versions | Yes |
| `turbosmtp-migrate` | Behavior-preserving migration with suppression/preferences, queue coexistence, cutover and rollback | Yes; needs authorized source/target access for actual actions |
| `turbosmtp-domain-setup` | Correct sending/tracking-domain records, preserved DNS policies and verified account/DNS state | DNS advice can; supported account actions need MCP or authorized operator paths |
| `turbosmtp-webhooks` | Authenticated, durable, idempotent receiver with correct event semantics and reconciliation | Yes; callback setup uses the documented dashboard path |
| `turbosmtp-send-email` | One explicitly requested send with correct account, recipients, content and region, plus a truthful result | Connected MCP required for this skill's send workflow |
| `turbosmtp-delivery-debug` | Attributable per-message or aggregate delivery diagnosis, with uncertainty and next steps | Supplied-artifact review can; live account investigation uses MCP |
| `turbosmtp-list-hygiene` | Consent-preserving validation/suppression handling with explicit cost and mutation scope | Guided/documented API mode can; current MCP covers only part of the workflow |
| `turbosmtp-account-operations` | Least-privilege credentials, client isolation, quotas, alerts and feature settings with correct administrative access | Guided/API workflows can; current MCP provides supported account reads |

All ten are part of the production scope. Webhooks and migrations are full skills, not deferred references. Best practices and template quality are first-class knowledge products. Their usefulness is independent of whether a user wants to call an API.

Do not add an umbrella router that must be installed for the others to work. A multi-step request can select several relevant skills. Task descriptions and selection evaluations determine when each applies. Existing MCP prompts `integrate`, `setup-domain` and `debug-delivery` provide material to reconcile with the corresponding skills; they do not replace the broader content or evaluation work.

## Documentation-led design

The review covered the 48-page live developer-docs export, the public OpenAPI artifact with 43 paths, and the current MCP source contract. Read the snapshot/provenance and page-by-page coverage in [DOCUMENTATION-MAP.md](docs/DOCUMENTATION-MAP.md). The review is content/contract analysis; it did not execute every published code example or verify every account feature live.

Keep four levels distinct:

1. A product feature is documented.
2. An API endpoint exposes a particular operation with specific authentication.
3. A current MCP tool exposes a supported subset of that operation.
4. A skill can complete the requested job through the user's actual authorized tools, configuration and account entitlement.

Do not infer level 3 or 4 from level 1. In particular, batch validation, tracking-domain/settings changes, key administration and sub-account provisioning are not all current MCP tools. A precise dashboard/operator handoff is an honest supported path when automation is absent; it is not an automated success report.

For changing facts, retain the source, checked date, applicable account/runtime/client and resolution of any discrepancy. Recheck sender requirements, plan allowances, SDK/framework release status and the selected tool schemas when preparing a release. Consumer credentials, MCP connection tokens and privileged account sessions are separate authentication mechanisms.

## Content and package architecture

Each skill is a standalone directory containing a valid `SKILL.md`, concise essential instructions and linked references for its actual modes. Follow the open Agent Skills core: matching lowercase directory/name, meaningful description, license and supported optional fields. Keep descriptions discriminating and metadata string-valued; client-specific extensions belong in distribution adapters. Experimental tool allowlists are not an authorization boundary.

Planned authoring layout:

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
PLAN.md
docs/
  CATALOG.md
  DOCUMENTATION-MAP.md
  EVALUATION.md
skills/
  turbosmtp-email-best-practices/SKILL.md
  turbosmtp-email-template-review/SKILL.md
  turbosmtp-integrate/SKILL.md
  turbosmtp-migrate/SKILL.md
  turbosmtp-domain-setup/SKILL.md
  turbosmtp-webhooks/SKILL.md
  turbosmtp-send-email/SKILL.md
  turbosmtp-delivery-debug/SKILL.md
  turbosmtp-list-hygiene/SKILL.md
  turbosmtp-account-operations/SKILL.md
  # Each directory contains its own needed references/assets/helpers.
evals/
  cases.json
  fixtures/
scripts/
  # Implemented validators/packagers only, with tests.
.github/workflows/
  ci.yml
  release.yml
```

Author in English and respond to users in their language. References carry the substantive domain expertise: concrete decisions, examples, limitations and verification procedures, not just links saying “read the docs.” Use public primary sources; keep employee policies, private deployment details, credentials and customer data out of distributed material.

Maintain shared provider facts from one reviewed source and check consistency across the relevant skills. Each final per-skill artifact must contain every resource it needs with working relative links; do not rely on a file outside its package. Avoid hand-maintained divergent copies. Optional shared authoring/build input must resolve into complete standalone distributions.

Add scripts only where deterministic verification or repeated processing justifies them, such as validating a generated MIME fixture. Do not ship another API client just to duplicate an installed SDK or MCP. Add template assets only when they are actually used and tested.

MIT is the intended license, matching the first-party MCP project, with provenance/license checks for reused content and preserved third-party notices. The actual LICENSE and contribution/security policy belong to implementation before public release.

## Production support contract

Production readiness applies to declared tasks and tested environments. It does not mean claiming every feature, runtime or client exists.

- Include API/SMTP and the documented integration families. For any advertised executable example, record supported runtime/package versions and run it. The public docs cover HTTP examples in cURL, Python, Node.js, PHP, Ruby, Go, Java and C#, plus framework/application paths. Do not silently replace this scope with a JS-only pack.
- Preserve existing mail abstractions and dependencies. Prefer a stable built-in transport when a provider bridge is not yet released. Verify source-only SDKs and package releases separately. The documentation review is not a package-installation certification.
- For CMS, notification tools and desktop clients, verify the actual supported configuration path/version. If no safe automation exists, provide accurate guided setup and a verification result rather than inventing UI/API automation.
- Knowledge/template workflows must work from supplied artifacts without requiring an account. Operative workflows must identify the real connected account, required permissions and current tools before a mutation.
- Match the user's authorization: complete an already authorized task without redundant approval, and ask only for missing consequential information or genuinely new scope. Inspection/code generation does not authorize a live send, paid validation, suppression deletion, DNS write, account creation or purchase.
- Production skills must handle failure and uncertainty. Sending acceptance is not delivery; delivered status is not inbox placement; validation is not consent; open/click events are not verified human attention. Preserve unknown outcomes rather than inventing guarantees or retrying writes blindly.

The detailed failure cases, privacy boundaries, client-rendering evidence and administrative limitations are release requirements in [EVALUATION.md](docs/EVALUATION.md).

## Implementation and acceptance sequence

Implementation is sequenced for dependency management; every sequence item retains the same production quality bar and the full catalog remains the target.

| Stage | Deliverable | Required completion evidence |
| --- | --- | --- |
| Contract and content design | Resolve documentation/runtime differences, assign source ownership and define the ten skill descriptions/reference structures | Documentation map, current contract fixtures, supported-version matrix and cross-skill selection cases |
| Complete expertise layer | Best practices and template-review skills with substantive references and verification assets | Dated mailbox-provider rules, actionable findings, personalization/MIME tests and actual advertised-client render evidence |
| Complete integration layer | Integration, migration and webhook skills and executable fixtures | Tested supported transports/framework examples, migration privacy/queue/rollback evidence and durable receiver tests |
| Complete account workflows | Domain setup, explicit sending, delivery diagnosis, hygiene and account operations | Actual tool/access maps and success/failure evidence, including unsupported-operation handoffs |
| Pre-production acceptance | Exact candidate installed in clean advertised clients and authorized test environments | Full case results, baseline comparisons, source/package scans, account/permission checks and redacted live acceptance where required |
| Production release | Complete validated catalog, source, artifacts and customer installation/update documentation | All release gates below, signed provenance and fresh-install/update/rollback evidence |

Assign a responsible maintainer for each skill and its contracts. Engineering owns execution correctness and evaluations, documentation ownership covers sources/install guidance, a repository owner controls visibility/settings, and Product/Marketing announces only completed capabilities. These are responsibilities, not unapproved commitments by named colleagues. Estimate delivery after the contract/content workload is established rather than promising a calendar date without evidence.

## CI, evaluations and maintenance

Follow [EVALUATION.md](docs/EVALUATION.md). Static Markdown/schema checks alone cannot establish production readiness. The baseline is 60 specific workflow cases plus selection/adversarial/failure cases, functional code/MIME/receiver fixtures, and clean-context agent evaluations in each advertised host.

Pin validation/packaging tools and third-party actions, use lockfiles, group dependency updates, restrict workflow permissions and keep live secrets out of PR jobs. CI must check links/resources, source freshness where relevant, tool/schema compatibility, example compilation/execution, script behavior and the extracted release contents. Do not place raw customer/model traces in skill ZIPs or public artifacts.

Record the skill version/commit, test client/model/runtime versions, source/contract versions, observed business outcomes, tool traces, tokens/timing and unresolved limits. Critical authorization/correctness failures block release; average success rates do not override them. Re-run the affected evidence after relevant content or provider changes. Publish performance claims only after measurement.

Routine ownership includes mailbox-provider requirement changes, source/API drift, integration releases, customer selection failures, incident reports and deprecation/rollback guidance. A release with stale instructions must be fixable through a versioned update without breaking unrelated installed skills.

## Distribution and publication

### Private acceptance

Keep the repository private during development and acceptance. Use existing Git/GitHub authentication; never embed credentials in an install URL. Record the tested skills CLI/client versions. The version-pinned examples below target a future release candidate. Use the README commands for the current private checkout.

```sh
npx skills add turboSMTP/skills --list
npx skills add turboSMTP/skills@v1.0.0-rc.1 --skill turbosmtp-email-best-practices -a claude-code
npx skills add turboSMTP/skills@v1.0.0-rc.1 --skill turbosmtp-integrate -a codex
```

Test independent and whole-catalog installs, project-local/global scope where advertised, selection, references, updates, removal and rollback. A plain skill install does not establish an authenticated MCP connection. Private repository access is a preparation mechanism, not anonymous public availability.

### Reproducible release assets

Use a single bundle version and signed `vX.Y.Z` tags. Release CI checks out the exact tag, validates the complete required catalog and packages an explicit allowlist. Produce one complete ZIP per skill and a complete bundle ZIP, `SHA256SUMS`, source commit and release notes. Verify extraction and exact tag/archive installs before promotion. Keep release assets immutable; a correction gets a new version.

Use `v1.0.0-rc.*` only as acceptance candidates for the full production specification. Publish `v1.0.0` after the gates pass. Patch versions fix compatible content; minor versions add compatible supported workflows; breaking task/contract changes require an explicit version boundary and migration notes. Record actual MCP/API/SDK/client compatibility and keep a last-known-good pinned release for rollback. Checksums prove content integrity, not source identity by themselves.

No separate npm package or hosted skill runtime is needed for the portable core. Skills can be installed from the vendor Git repository or a tested complete release artifact.

### Customer-facing release

Public visibility is an explicit owner-controlled release action after acceptance, not an automatic effect of a planning push. Verify anonymous read/download and installation before publishing instructions.

Primary distribution is `npx skills add turboSMTP/skills`, with selective and pinned-version examples. Publish an installation/task guide in the developer docs, a truthful catalog/compatibility table, upgrade/removal/rollback guidance, support/reporting links and cross-links from MCP/product docs. Verify skills.sh discovery after public installs; its telemetry-based ranking is neither an npm publish step nor a promised placement. Do not manufacture install counts or require telemetry.

Provide ZIP-upload instructions only for clients and account tiers where the exact artifacts have passed installation and task tests. Label available installation paths and execution dependencies precisely.

### Plugin distribution

Offer skills plus public MCP configuration in an Agent Plugins package and client-specific adapters where supported. Each advertised adapter must have manifest validation and actual install/connect/update tests for its target client. Generate adapters from maintained content/catalog input to avoid divergent copies. No tokens, account bindings, private routes or operator auth settings belong in these manifests.

The portable skills and tested ZIP/CLI paths remain usable independently. An adapter may be omitted from the advertised support table until it passes; that does not lower the quality bar of the actual production skills. Hosted discovery indexes or a guide-loading MCP capability are optional distribution features, not existing MCP capabilities or substitutes for the full knowledge content.

## Release gates

- [ ] All ten skills in [CATALOG.md](docs/CATALOG.md) are implemented with substantive, independently packaged resources and assigned ownership.
- [ ] Each skill meets [EVALUATION.md](docs/EVALUATION.md), including its six cases, selection boundaries, failure paths and the advertised host/runtime matrix.
- [ ] API/MCP/product/primary-source differences are resolved or explicitly constrain supported behavior; references and changing requirements have current evidence.
- [ ] Executable examples, MIME, template rendering, webhook restart/idempotency, migration rollback and account-operation boundaries have actual evidence where applicable.
- [ ] No known critical correctness, secret/privacy or unauthorized-action case fails. No installable-looking placeholders or unsupported capabilities are advertised.
- [ ] Licensing, content/archive scans, immutable package contents, signatures/checksums and provenance are complete.
- [ ] Customer MCP login/account permissions and required tools are verified at the intended public endpoint before operative skills are advertised. A production-looking URL alone is insufficient.
- [ ] A repository owner has authorized public visibility, and anonymous installation plus independent ZIP/CLI and advertised-plugin tests pass.
- [ ] Documentation, release assets, compatibility statements, update/removal/rollback and support handling agree.
- [ ] Product communication reports the accepted scope and remaining documented limits accurately, without calling the current specification an implemented production release.

## Primary references

- [Documentation audit and source map](docs/DOCUMENTATION-MAP.md)
- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills)
- [Skills CLI commands and private/pinned installation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [skills.sh documentation](https://skills.sh/docs)
- [Vercel's skill collection](https://github.com/vercel-labs/agent-skills)
- [Resend's email expertise collection](https://github.com/resend/resend-skills)
- [Brevo skills and MCP distribution](https://developers.brevo.com/docs/brevo-skills)
- [Stripe's skills/MCP distribution](https://github.com/stripe/ai)
