# Investigate delivery evidence field guide

| Observation | Interpretation / next evidence |
| --- | --- |
| NEW or DEFER | Queue or temporary deferral. Inspect reason and retry history. |
| FAIL or SYSFAIL | Permanent rejection or system drop. Match recipient, timestamp and suppression reason. |
| SUCCESS | Receiving server accepted the message. Ask about folder/filtering if inbox placement is disputed. |
| OPEN or CLICK | Image loaded or link requested. A proxy or automated checker may be responsible. |
| REPORT or UNSUB | Complaint or unsubscribe. Preserve the corresponding preference. |

Analytics vocabulary differs from webhook vocabulary (e.g. SUCCESS versus DELIVERED). State which dataset and aggregation rule produced a rate. A date filter uses YYYY-MM-DD and the retention window depends on the account. An empty window or insufficient APIS access leaves the diagnosis open. Preserve IDs such as `9007199254740993` through lookup and reporting.

## Sources

- [analytics API](https://serversmtp.com/docs/api-reference/analytics)
- [statistics](https://serversmtp.com/docs/analytics/statistics-dashboard)
- [tracking](https://serversmtp.com/docs/analytics/email-tracking)
- [common errors](https://serversmtp.com/docs/troubleshooting/common-errors)
