# Review a sending program field guide

**Aligned identity.** For a visible From of `orders@example.com`, an SPF pass for an unrelated return path is insufficient by itself. Inspect DKIM's passing signing domain and the effective DMARC alignment mode. A pending DNS record, a verified provider domain and the headers on an actual delivered sample answer different questions.

**Recipient consent.** A valid mailbox and an address supplied for a receipt do not establish newsletter consent. Keep the source and scope of opt-in with the contact. Process opt-outs in the sending application as well as provider suppressions. A provider switch must preserve them.

**Receiver requirements.** Gmail distinguishes personal Gmail traffic and bulk senders. An order-only receipt ordinarily falls outside the marketing/subscription one-click requirement. Reassess if promotional content is added. For applicable marketing/subscription mail, inspect both the visible unsubscribe link and the RFC 8058 flow. Inspect the signed headers and test a synthetic POST with a test subscription. A GET from a link scanner must not unsubscribe a recipient. Review Yahoo's sender requirements separately. Outlook.com's high-volume requirements concern consumer domains. Check these primary sources at review time: [Gmail](https://support.google.com/mail/answer/81126), [Yahoo](https://senders.yahooinc.com/best-practices/), [Outlook.com](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/4399730), [RFC 8058](https://www.rfc-editor.org/rfc/rfc8058).

**Evidence quality.** Compare similar periods and volumes. Image proxies can load pixels and scanners can follow links. An observed open cannot establish human engagement. A dedicated IP requires enough consistent wanted traffic to build reputation. Verify entitlement and routing with the provider. No fixed warm-up schedule or placement guarantee follows from these checks.

## Sources

- [authentication](https://serversmtp.com/docs/deliverability/spf-dkim-dmarc)
- [spam-folder diagnosis](https://serversmtp.com/docs/troubleshooting/spam-folder)
- [routing](https://serversmtp.com/docs/deliverability/smart-routing)
- [tracking](https://serversmtp.com/docs/analytics/email-tracking)
