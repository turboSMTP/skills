# Integrate application sending field guide

| Transport | Configuration | Check |
| --- | --- | --- |
| SMTP | `pro.turbo-smtp.com` or `pro.eu.turbo-smtp.com`, username = Consumer Key, password = Consumer Secret, permission `SEND_SMTP` | Require STARTTLS on 587 or 2525, implicit TLS on 465 or 25025. Keep certificate verification enabled. |
| HTTP | Global `https://api.turbo-smtp.com/api/v2/mail/send` or EU `https://api.eu.turbo-smtp.com/api/v2/mail/send`, permission `SEND_API` | POST JSON with both `consumerKey` and `consumerSecret` headers. The management host is separate. |
| Framework/application | Inspect the installed version and the corresponding [integration guide](https://serversmtp.com/docs/integrations/overview). Check Nodemailer presets, Swoosh adapter, Symfony bridge release, Uptime Kuma provider or WordPress plugin before recommending installation. | For older or unsupported versions use the documented generic SMTP path. A source repository alone does not establish package availability. |

A minimal JSON payload uses `from`, comma-separated `to`, `subject` and `content`. HTML uses `html_content`. Attachments use `name`, MIME `type` and standard Base64 `content`. A bare inline `content_id` of `logo` corresponds to HTML `cid:logo@sender-domain`. Keep the entire message under 24 MB including overhead. Use SMTP for prebuilt MIME. For a 401 check permission, key pair and application egress IP. A successful `mid` records provider acceptance. Preserve the ID without floating-point conversion.

## Sources

- [SMTP](https://serversmtp.com/docs/sending/smtp-relay)
- [HTTP](https://serversmtp.com/docs/sending/email-api)
- [examples](https://serversmtp.com/docs/sending/code-examples)
- [integrations](https://serversmtp.com/docs/integrations/overview)
- [SDK status](https://serversmtp.com/docs/integrations/sdks)

## Pick the existing integration

| Application | Decision and verification |
| --- | --- |
| Nodemailer | Inspect the installed service list for `TurboSMTP` or `TurboSMTP-EU`. Otherwise set host and TLS explicitly. On port 587 use `secure: false` and `requireTLS: true`. |
| Swoosh / Phoenix | Check the installed adapter's provider options. Some versions qualify inline CIDs for the application. Inspect generated HTML to avoid appending the sender domain twice. |
| Symfony | Verify the bridge package and application's compatible stable version. If unavailable, use the existing SMTP transport. Percent-encode reserved characters in DSN credentials. |
| WordPress / WooCommerce | Select the existing mailer's API or SMTP mode, and the matching key permission. Verify the actual order/form email flow in the test environment. |
| Uptime Kuma | Check that the installed version includes the turboSMTP notification provider and that the notification is assigned to the intended monitors. |
| Drupal, Joomla, Magento or mail clients | Configure the outbound mailer. Keep incoming IMAP settings independent. Check the version-specific mail extension before changing application code. |
| PHP, C#, or other HTTP clients | Check package/runtime requirements in the published source and registry. If direct HTTPS is more appropriate, use the documented JSON schema and test against a capture server. |

[Official example languages](https://serversmtp.com/docs/sending/code-examples) · [Nodemailer](https://serversmtp.com/docs/integrations/nodemailer) · [Swoosh](https://serversmtp.com/docs/integrations/swoosh) · [Symfony](https://serversmtp.com/docs/integrations/symfony-mailer) · [WordPress](https://serversmtp.com/docs/integrations/wordpress) · [Uptime Kuma](https://serversmtp.com/docs/integrations/uptime-kuma).
