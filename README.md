# turboSMTP Agent Skills

Install the skills for the jobs you need. Best practices and template review work from supplied material. Integration, migration and webhook development work in an application repository. Live account actions use a connected turboSMTP MCP client with the appropriate permissions.

From a project with read access to this repository:

```sh
npx skills add turboSMTP/skills --list
npx skills add turboSMTP/skills --skill turbosmtp-email-best-practices -a claude-code
npx skills add turboSMTP/skills --skill turbosmtp-integrate -a codex
```

For a checked-out copy, replace the repository name with the checkout path. Select project-local installation unless you need the skills across projects. Use the CLI's `skills check`, `skills update` and `skills remove` commands to manage installed copies.

Browse the [ten skill directories](skills/) and their [catalog](docs/CATALOG.md). To build standalone ZIPs with license text and checksums, run `python3 scripts/package.py dist` with an empty output directory. The private CI workflow packages the same files.

The collection is in private acceptance. The [60 evaluation prompts](evals/cases.json) specify expected behavior. See [acceptance evidence](docs/ACCEPTANCE.md) for the checks performed and the [release plan](PLAN.md) for the remaining requirements.
