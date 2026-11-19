# Worked Example — privacy-tool-review

> **Sample data.** The app below ("QuietNotes") is fictional, invented
> for this example. Findings are illustrative, not a real audit.

## Input

- **Tool:** QuietNotes (fictional) — a browser note app claiming
  "end-to-end encrypted notes, zero-knowledge".
- **Threat model:** a curious stranger with the device, and the hosting
  provider. What must stay secret: note text. Metadata (that notes exist)
  is acceptable to leak.

## Findings

| Severity | Finding | Evidence (file:line) | Fix |
|----------|---------|----------------------|-----|
| Critical | None | — | — |
| Minor | Note titles are stored in plaintext | `app.js:84` — titles sent unencrypted alongside encrypted bodies | Encrypt titles, or warn users titles are visible |
| Minor | No security headers on the demo host | `netlify.toml` — no Content-Security-Policy set | Add CSP, HSTS, X-Frame-Options |
| Note | Vault IDs are random, but reads are public | `rules.json` — `".read": true` on the vault | Restrict reads, or state the limit in the README |

## Verified claims

- "AES-256-GCM" — confirmed: `crypto.js:31` uses
  `crypto.subtle.encrypt({name: "AES-GCM", iv})` with a 256-bit key.
- "PBKDF2" — confirmed: `crypto.js:22` derives the key with PBKDF2,
  210,000 SHA-256 iterations.
- No real secrets found in the repo: config uses placeholders only, and
  `.gitignore` covers `.env`.

## Verdict: Ship with notes

- Threat model: note text stays secret from the provider and from a
  stranger without the password; note titles do not.
- Critical findings: 0. Minor findings: 2 (listed above).
- Not verified: the hosted demo's server logs were not inspected.
