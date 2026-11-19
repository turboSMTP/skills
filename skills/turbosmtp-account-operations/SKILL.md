---
name: turbosmtp-account-operations
description: >-
  Review or configure turboSMTP account permissions, IP restrictions, credential rotation, subaccounts, sending limits, credit alerts and account-wide settings.
license: MIT
---

# Operate an account

Identify the account, role, requested scope and available administrative path. Use `get_account_info`, `list_subaccounts` and `get_subaccount` for supported MCP reads. Keep parent and child account identities explicit. For unsupported writes provide the documented dashboard steps or use an independently authorized administrative API connection.

For credential rotation inventory consumers, permissions, actual public egress addresses and available key slots. Create a replacement with explicit restrictions. Place the secret directly in the configured secret store, verify each application's new credential, then revoke the old one when authorized. Never collect a dashboard password or paste an integration secret into chat.

Report which settings were read, which authorized changes succeeded and how to verify or roll back. Keep billing purchases, changes in login availability and global BCC edits scoped to explicit user intent.

Consult the [field guide](references/guide.md) for examples, decision criteria and source documentation.
