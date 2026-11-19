# turboSMTP Agent Skills

Use turboSMTP with any agent that supports the [Agent Skills format](https://agentskills.io/specification). The skills guide your agent through email integration, message review and account operations. Each skill can be installed individually. A template review or code integration works locally. Sending through the agent requires a connected turboSMTP MCP account.

## Install

From your project directory, run the interactive installer and choose your skills and agents. See the [supported agents and installation paths](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) for client-specific setup.

```sh
npx skills add turboSMTP/skills
```

Optionally select a specific skill with `--skill`:

```sh
npx skills add turboSMTP/skills --skill turbosmtp-email-best-practices
```

To try a checkout, replace `turboSMTP/skills` with its local path. After installation, ask the agent a question such as “Review this receipt email and explain what still works with images disabled.”

## Choose a skill

| Skill | Use it to |
| --- | --- |
| [Account operations](skills/turbosmtp-account-operations/SKILL.md) | Review permissions, rotate keys or configure subaccount limits and alerts. |
| [Delivery debugging](skills/turbosmtp-delivery-debug/SKILL.md) | Trace a missing or bounced message using an ID, time window and delivery evidence. |
| [Domain setup](skills/turbosmtp-domain-setup/SKILL.md) | Set up a sender or tracking domain and verify its DNS records. |
| [Email best practices](skills/turbosmtp-email-best-practices/SKILL.md) | Review consent, sender authentication, reputation and unsubscribe handling. |
| [Template review](skills/turbosmtp-email-template-review/SKILL.md) | Repair HTML, plain text, personalization and inline images. |
| [Integration](skills/turbosmtp-integrate/SKILL.md) | Add SMTP or HTTP sending to an existing application. |
| [List hygiene](skills/turbosmtp-list-hygiene/SKILL.md) | Interpret validation results and reconcile suppressions with subscription preferences. |
| [Migration](skills/turbosmtp-migrate/SKILL.md) | Move SendGrid or Mailgun traffic with a tested cutover and rollback plan. |
| [Send email](skills/turbosmtp-send-email/SKILL.md) | Send a specific message through a connected account and report the result. |
| [Webhooks](skills/turbosmtp-webhooks/SKILL.md) | Implement an authenticated receiver that handles duplicate and out-of-order events. |

Live account workflows describe which steps use MCP and which require the dashboard or an authorized API connection. See the [MCP server](https://github.com/turboSMTP/mcp) and [developer documentation](https://serversmtp.com/docs).

[Contributing](CONTRIBUTING.md) · [Evaluation results](evals/README.md) · [Security reporting](SECURITY.md) · [MIT license](LICENSE)
