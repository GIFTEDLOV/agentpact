# AgentPact

AgentPact is an evidence-backed commitment adjudication contract for GenLayer. A requester creates a commitment, a provider submits a public HTTPS delivery with an exact SHA-256 digest and byte count, and either party can adjudicate after a dispute or deadline. Independent nondeterministic evaluation is validated by consensus and fails closed to `INCONCLUSIVE` when the artifact digest or evidence cannot be trusted.

## Final deployment

- Studio-dev chain: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: [`0xD9E8904920b23845ab1581fc4B4716B3B8be2101`](https://explorer-studio-dev.genlayer.com/address/0xD9E8904920b23845ab1581fc4B4716B3B8be2101)
- Deployment transaction: [`0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c`](https://explorer-studio-dev.genlayer.com/tx/0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c)
- Source SHA-256: `68781905e76686df967e1025bfada2f955db569b6c2e82bc956b56d85c72a64e`
- Public repository: https://github.com/GIFTEDLOV/agentpact

The deployed source is preserved byte-for-byte in [`contracts/agent_pact.py`](contracts/agent_pact.py). The source SHA is the SHA-256 of the UTF-8 bytes submitted in the deployment transaction.

## Safety properties

- Requester and provider must be different addresses.
- Deliveries require bounded HTTPS URLs, a lowercase 64-character SHA-256 digest, a positive byte count, and distinct evidence URLs.
- Adjudication re-fetches the artifact and verifies both digest and byte count before semantic evaluation.
- Artifact and evidence are wrapped as untrusted data in the classifier prompt.
- Any failed criterion produces `REJECTED`; any unknown criterion produces `INCONCLUSIVE`; only all-pass criteria produce `ACCEPTED`.

## Validation

The reproducible validation commands and the exact Studio-dev schema check are recorded in [`docs/VALIDATION.md`](docs/VALIDATION.md). Deployment and lifecycle operations are documented in [`docs/DEPLOYMENT_RUNBOOK.md`](docs/DEPLOYMENT_RUNBOOK.md). The release evidence is in [`docs/RELEASE_HANDOFF.md`](docs/RELEASE_HANDOFF.md).

