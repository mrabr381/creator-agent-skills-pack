---
name: privacy-tool-review
description: Review a privacy tool before recommending or shipping it — threat model, data flow, secrets handling, encryption claims, permissions and licensing — and return a verdict with evidence. Use when a chat app, vault, encoder or privacy feature is about to be recommended, linked, or released. Hidden-Chat is the worked reference implementation.
---

# Privacy Tool Review

## When to Use

- A privacy tool (chat, vault, encoder, steganography app) is about to be
  recommended, linked in a post, or shipped.
- A "secure / encrypted / private" claim needs checking before it is
  repeated.
- Do **not** use this skill to declare something "unhackable" or "100%
  secure". The output is a verdict with evidence and limits, never a
  guarantee.

## Workflow

1. **Write the threat model first.** Who is the adversary (a curious
   stranger? the hosting provider? someone with the device?), and what
   exactly must stay secret (message text? metadata? the fact that a
   secret exists?). A tool that hides text but leaks metadata is fine for
   one model and useless for another — name the model before judging.
2. **Map the data flow.** Trace a secret from input to storage to output:
   where is it encrypted, where does it travel, what is stored, and what
   does the server see? Draw it as a short list. Any step you cannot trace
   is a finding ("cannot verify"), not a pass.
3. **Check secrets handling.** Search the repo for hardcoded keys,
   tokens, passwords, and Firebase/API config with real values
   (`AIza`, `sk-`, private keys). Placeholders and `.env.example` files
   are fine; real values in a public repo are a critical failure. Check
   `.gitignore` covers `.env` and that the README explains key setup.
4. **Verify the encryption claims.** For each claim ("AES-256-GCM",
   "PBKDF2 210,000 iterations", "zero-knowledge"), find the code that
   does it: algorithm name, key derivation, iteration count, IV/nonce
   handling, and what is (and is not) encrypted. A claim with no matching
   code is a fail. Note honestly what is *not* covered: e.g. "message
   text is encrypted; room names in the URL hash never reach the server;
   media IDs are random but the vault read rule is public."
5. **Check the boring defences.** Input validation and length limits,
   HTML escaping of user content, file-type checks by magic bytes (not
   extension), blocked upload types (SVG/HTML/scripts), HTTPS-only
   connections, and security headers (CSP, HSTS, X-Frame-Options).
   Privacy tools fail on boring things more often than on cryptography.
6. **Check permissions and scope.** What does the app ask for (microphone,
   camera, notifications, storage)? Is each permission needed for a named
   feature, and can the app run without it? Excess permissions are a
   finding.
7. **Check the licence and the claims on the box.** Does the licence match
   how the tool is distributed? Does the README promise anything the code
   cannot do ("zero-metadata" while analytics or logging is enabled)?
   Quote the promise and the contradicting evidence side by side.
8. **Verdict.** One of: **Ship** (no blocking findings), **Ship with notes**
   (minor findings listed, none blocking), or **Do not ship** (a critical
   finding: real secret, false encryption claim, or data the threat model
   requires secret reaching a server in plaintext). List every finding
   with file, line, and evidence.

## Checklist

- [ ] Threat model written (adversary + what must stay secret)
- [ ] Data flow traced end to end; untraceable steps marked "cannot verify"
- [ ] Repo searched for real secrets; placeholders only (or a critical finding)
- [ ] Every encryption claim matched to code (algorithm, KDF, IV, coverage)
- [ ] What is NOT encrypted / NOT private stated explicitly
- [ ] Input validation, escaping, file-type checks, HTTPS, headers checked
- [ ] Permissions listed with a reason for each
- [ ] Licence matches distribution; README promises checked against code
- [ ] Verdict given (Ship / Ship with notes / Do not ship) with findings

## Templates

### Finding

```markdown
| Severity | Finding | Evidence (file:line) | Fix |
|----------|---------|----------------------|-----|
| Critical | Real API key in repo | `config.js:12` — `apiKey: "AIza..."` | Move to `.env`, rotate the key, purge history |
| Minor | Media vault reads are public | `database.rules.json` — `".read": true` on `media_vault` | Restrict reads to room members or note the limit |
```

### Verdict

```markdown
## Verdict: Ship with notes
- Threat model: ...
- Critical findings: 0
- Minor findings: 2 (listed above)
- Not verified: ...
```

## Anti-Patterns

- **Never declare "100% secure" or "unhackable".** Security is a set of
  properties with limits; state the limits.
- **Never trust a claim without code.** "Military-grade encryption" in a
  README is marketing until the algorithm, KDF, and IV handling are found.
- **Never ignore metadata.** Hiding the message while leaking who talked
  to whom, when, and how often is a partial job — say so.
- **Never pass a tool you could not trace.** "Cannot verify" is a finding,
  not a shrug.
- **Never skip the boring checks.** Secrets, escaping, and file uploads
  cause more real harm than weak ciphers.

## Output Format

A Markdown review: threat model, data-flow list, findings table (severity,
evidence with file:line, fix), and a verdict. Keep the evidence so a
second reviewer can re-check it without re-doing the whole audit.

## Related Repos

- `Hidden-Chat` — worked reference: zero-knowledge encrypted steganography
  chat (Web Crypto AES-256-GCM + PBKDF2, LSB image hiding, Firebase
  Realtime DB). Review it with this skill to see a filled-in example.
- `repurpose-episode` — do not use a privacy review as content; if a
  review finds a critical issue, fix it first, then talk about the tool.
