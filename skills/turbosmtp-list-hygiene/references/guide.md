# Maintain a sendable audience field guide

Valid addresses still require permission to receive the intended mail. Exclude invalid, abuse and spamtrap results. Review catch-all, unknown and do-not-mail separately with their sub_status. Preserve opt-outs and complaints even when validation says valid. A full mailbox alone can be a temporary failure.

The batch API accepts a multipart CSV/TXT upload at `/emailvalidation/upload`. Use its `list_id` for `/emailvalidation/lists/{Id}/validate` and subsequent progress/results. If a start times out, read list status before any second chargeable operation. If balance is insufficient, report that condition and the unresolved rows.

Before a suppression change preview the targeted records by date, recipient and source. An account-wide suppression can be broader than a list-specific preference. Keep the application's own preferences synchronized. A request to export or inspect a list does not imply authority to disclose its contents elsewhere.

## Sources

- [validation guide](https://serversmtp.com/docs/account/email-validation)
- [validation API](https://serversmtp.com/docs/api-reference/email-validation)
- [suppressions](https://serversmtp.com/docs/api-reference/suppressions)
- [bounce/opt-out handling](https://serversmtp.com/docs/deliverability/bounce-spam-management)
