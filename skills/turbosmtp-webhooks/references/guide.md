# Process delivery webhooks field guide

Callback bodies can arrive chunked. Use `Timestamp` in seconds and accept lowercase `timestamp` as a fallback. Preserve `mid` as an opaque value with a lossless JSON parser when the sender encodes it as a large JSON number. A conversion to string after JavaScript's JSON.parse may already have lost digits.

Prefer the event ID when present. Otherwise use the message, recipient, event type and timestamp as a fallback and document the collision limits. Two recipients or two distinct events can share a message ID. For example, receiving DELIVERED after OPENED still adds delivery evidence without deleting the observed open. A click can come from a scanner.

Requests are unsigned. Use HTTPS and verify Basic auth against separate configured callback credentials. Redact callback credentials and URL from logs. Reject bad authentication, handle unknown fields, and do not treat payload IP as callback source IP. Configure the receiver before enabling events. Documented delivery retries are finite.

## Sources

- [webhooks](https://serversmtp.com/docs/analytics/webhooks)
- [analytics](https://serversmtp.com/docs/api-reference/analytics)
- [migration guides](https://serversmtp.com/docs/migrate/from-sendgrid)

## Transaction boundary

For a relational receiver, give the event ledger a unique key scoped to the provider account and event identity. In one transaction, insert the authenticated event and enqueue its pending processing record. If the event is already durably recorded, a retry can receive 2xx. A failed commit must return a failure response so the sender can retry. Let a worker claim pending rows on restart and make its downstream state updates idempotent. Avoid doing email or other non-transactional side effects inside a retried database transaction.

Test two distinct records sharing a message ID and then replay the first after restarting the worker:

```json
[
  {"id":"evt-701","mid":"9007199254740993","status":"DELIVERED","email":"buyer@example.org","Timestamp":1710000000},
  {"id":"evt-702","mid":"9007199254740993","status":"OPENED","email":"buyer@example.org","Timestamp":1710000002}
]
```

Submit each object as its own HTTP request. Expect two durable events and one delivery transition. If the receiver accepts numeric IDs, repeat the test with an unquoted numeric mid and verify the exact decimal value survives input parsing.
