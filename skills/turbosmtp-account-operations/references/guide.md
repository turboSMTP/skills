# Operate an account field guide

HTTP sending needs SEND_API, SMTP needs SEND_SMTP, and supported management operations use APIS. Key management is a session-authenticated exception. Prefer the dashboard when a suitable session is unavailable. On a key update, preserve the full intended permissions and IP list: omission can reset permissions or clear IP restrictions.

New subaccounts need their own sending key. The parent's sending IP must already be assigned. Creating a profile, changing the sending limit and changing active status are distinct operations. Check the current parent limit and the period before interpreting a child limit. A daily percentage-of-credit-usage alert is different from an alert on remaining validation credits.

Tracking settings and global BCCs apply to more than one message. Review the current setting and identify the affected traffic before making an authorized change. For billing, feature availability and retention, consult the user's current account and terms. Use a redacted order or message reference when escalating.

## Sources

- [API keys](https://serversmtp.com/docs/get-started/api-keys)
- [authentication](https://serversmtp.com/docs/api-reference/authentication)
- [subaccounts](https://serversmtp.com/docs/api-reference/subaccounts)
- [alerts](https://serversmtp.com/docs/api-reference/alerts)
- [email settings](https://serversmtp.com/docs/account/email-settings)
