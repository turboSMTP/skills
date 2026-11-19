# Set up and verify a domain field guide

For `receipts@mail.example.com` in zone `example.com`, check the actual envelope domain and DKIM signing domain. With aligned sending at `mail.example.com`, the SPF name is `mail` and the standard DKIM name is `turbo-smtp._domainkey.mail`. Many DNS editors append the zone automatically.

Add `include:spf.turbo-smtp.com` to the existing SPF record before its final all mechanism. Preserve other includes and evaluate the ten-lookup limit. Publishing two SPF records or changing an existing enforcement qualifier can break other senders. Check inherited DMARC and the alignment of passing identities before recommending a policy change.

Tracking domains use the two generated CNAME records shown in the dashboard. Use their exact names/targets and verify there. A custom tracking CNAME is different from a sending-domain verification record. PTR changes belong to the IP operator. Distinguish public DNS results, account verification and the authentication actually seen in a received message.

## Sources

- [SPF/DKIM/DMARC](https://serversmtp.com/docs/deliverability/spf-dkim-dmarc)
- [tracking domains](https://serversmtp.com/docs/deliverability/custom-tracking-domain)
- [MCP contract](https://github.com/turboSMTP/mcp)
