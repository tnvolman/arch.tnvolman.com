# arch.tnvolman.com

Public marketing and docs home for **Arch API** — the pay-per-call theological review product for AI developers.

Live site: https://arch.tnvolman.com

## What Arch API is

Submit AI-generated theological content. Receive **APPROVED**, **FLAGGED**, or **REJECTED** verdicts grounded in Hebrew, Greek, and Aramaic — with KJV as the working translation.

- Endpoint: `POST /v1/review`
- Auth: `X-API-Key` header
- Pricing: Starter **$2.00** / Growth **$1.75** (100+/mo) / Scale **$1.50** (500+/mo) / Enterprise custom
- No subscription — pay per call

## What this is not

**Arch in the Forge** (Sanctuary’s internal theological review gate) is a separate product surface. It lives in `tnvolman/the-forge` and must not be conflated with this public API.

Until the landing page is extracted here, production HTML is still served from the Forge Railway service (`templates/arch_landing.html`). This repo owns public marketing/docs once that cutover happens.

## Ownership

| Surface | Owner |
|---------|--------|
| Arch API public marketing/docs | this repo (`arch.tnvolman.com`) |
| Arch API + Sanctuary Arch platform code | `tnvolman/the-forge` |
