# Migrate an existing integration field guide

**SendGrid.** Convert each personalization to the intended separate message when it has its own substitutions, subject or recipients. Combining all addresses into `to` may disclose recipients. Move typed content entries to `content` and `html_content`. Map SendGrid ASM group IDs to application preferences so a newsletter opt-out survives migration with its original scope. Apply that preference before queueing and retrying messages. Render templates in the application when there is no verified target equivalent. Map metadata to application records with a correlation UUID.

**Mailgun.** Replace per-domain form uploads and Basic auth with the regional JSON endpoint and both Consumer headers. Encode each attachment separately. Raw MIME goes through SMTP. Preserve group/domain-specific opt-outs at the appropriate scope in your application when an account-wide suppression is too broad.

**Callback cutover.** Map event meanings rather than spelling. Register the new callback via the dashboard, use HTTPS and separate receiver credentials, and accept concurrent old/new callbacks during the cutover. Check queue drain, final preference sync and an authenticated received sample before removing old-provider DNS. For other source providers verify their current contracts and document gaps explicitly.

## Sources

- [SendGrid migration](https://serversmtp.com/docs/migrate/from-sendgrid)
- [Mailgun migration](https://serversmtp.com/docs/migrate/from-mailgun)
- [comparisons](https://serversmtp.com/docs/compare/overview)
