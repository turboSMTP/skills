# Review an email template field guide

Use a presentation table only for layout and label it as presentational. Keep essential text and calls to action as real text. Use alt text for informative images and empty alt text for purely decorative ones. A receipt number must remain visible outside its image.

For the turboSMTP send API, attach the inline image with a bare `content_id` such as `logo`. For sender `orders@example.com` reference `cid:logo@example.com` in the HTML. A downloadable invoice should have no inline ID. Verify the MIME's Content-ID and the decoded attachment bytes. A data URI prefix does not belong in an attachment's Base64 data.

Build the entire encoded message before estimating the size limit (under 24 MB). Include the text and HTML alternatives, attachment encoding and envelope overhead. Dashboard footers or unsubscribe elements can change what recipients receive. Report differences between the source preview and the received test MIME. A browser rendering alone covers neither Outlook desktop nor Apple Mail.

## Sources

- [email elements](https://serversmtp.com/docs/account/email-settings)
- [tracking](https://serversmtp.com/docs/analytics/email-tracking)
- [attachments](https://serversmtp.com/docs/sending/attachments)
- [send contract](https://serversmtp.com/docs/api-reference/send-email)

## Receipt fixture

Render these two alternatives from the same data and compare their meaning. Both should show the order number, amount and support link when remote images are blocked.

```html
<div lang="en">
  <h1>Your receipt for order 1042</h1>
  <p>We received your payment of EUR 19.00.</p>
  <p><a href="https://shop.example.com/help">Contact order support</a></p>
  <img src="cid:logo@example.com" width="96" height="32" alt="">
</div>
```

```text
Your receipt for order 1042
We received your payment of EUR 19.00.
Contact order support: https://shop.example.com/help
```

Try a long translated order label, narrow viewport, image blocking and a dark background. Verify the support action in the actual target client. A reset-link fixture also needs an expired or missing token case. Reject a required URL missing at render time and preserve its intended host. Use the template engine's escaping for user-supplied values.
