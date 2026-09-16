# AgentPact

AgentPact is an evidence-backed commitment adjudication contract for GenLayer. A requester creates a commitment, a provider submits a public HTTPS delivery with an exact SHA-256 digest and byte count, and either party can adjudicate after a dispute or deadline. Independent nondeterministic evaluation is validated by consensus and fails closed to `INCONCLUSIVE` when the artifact digest or evidence cannot be trusted.

## Final deployment

- Studio-dev chain: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: [`0xdA8781136eB4e59A5216e8891113222C42928a8C`](https://explorer-studio-dev.genlayer.com/address/0xdA8781136eB4e59A5216e8891113222C42928a8C)
- Deployment transaction: [`0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9`](https://explorer-studio-dev.genlayer.com/tx/0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9)
- Source SHA-256: `c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595`
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
