# Send a requested email field guide

Example tool arguments for a single plain-text message (reserved example addresses):

```json
{"from":"Orders <orders@example.com>","to":"buyer@example.org","subject":"Receipt","content":"We received your payment for order 1042.","region":"eu"}
```

Use an attachment object with `name`, `type` and Base64 `content`. Add bare `content_id` only for inline media. If the sender domain is example.com and the ID is logo, use `cid:logo@example.com`. The entire encoded message must fit under 24 MB.

`region` is a tool argument selecting the endpoint. It does not go in an upstream HTTP JSON body. A `reference_id` lets the application correlate later records and gives no deduplication guarantee. Distinguish an upstream rejection with an actionable error from a call whose outcome is unknown.

## Sources

- [sending](https://serversmtp.com/docs/api-reference/send-email)
- [attachments](https://serversmtp.com/docs/sending/attachments)
- [MCP contract](https://github.com/turboSMTP/mcp)
