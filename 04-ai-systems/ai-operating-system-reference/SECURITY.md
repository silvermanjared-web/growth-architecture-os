# Security Policy

This reference is intentionally local, synthetic, and public-safe.

## Security properties

- no network calls are required for validation;
- no credentials are required;
- write examples are restricted to caller-supplied sandbox roots;
- path traversal outside the sandbox is refused;
- capability names are allowlisted;
- mutation requires explicit confirmation;
- receipts do not include secret values.

Run `npm run test:security` for the security test path.

Report security issues privately rather than opening a public issue containing sensitive details.