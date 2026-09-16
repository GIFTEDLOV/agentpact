# AgentPact deployment runbook

## Canonical deployment

Use the explicit Studio-dev network only:

```text
chain: 61997
rpc: https://studio-dev.genlayer.com/api
contract: 0xdA8781136eB4e59A5216e8891113222C42928a8C
deployment tx: 0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9
source sha256: c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595
repository: https://github.com/GIFTEDLOV/agentpact
```

The deployment is final and must not be rebroadcast while the source SHA remains unchanged. If the contract changes, recompute the SHA-256 over the exact UTF-8 source bytes, run every validation command, obtain deployment confirmation, deploy exactly once, and replace every canonical coordinate above and in the README/release handoff.

## Validation sequence

```bash
.venv/bin/pytest -q
GENVM_VERSION=v0.2.16 .venv/bin/genvm-lint lint contracts/agent_pact.py
python -m py_compile contracts/agent_pact.py
git diff --check
```

Then query `gen_getContractSchema` at the canonical RPC and verify the deployed schema has the exact methods in `docs/VALIDATION.md`. The public explorer URL is https://explorer-studio-dev.genlayer.com/address/0xdA8781136eB4e59A5216e8891113222C42928a8C.

## Lifecycle rules

Use only disposable Studio-dev accounts. Use separate commitments for accepted, rejected, inconclusive, and expired branches. For submitted branches, record create, submit, dispute, and adjudicate transaction hashes plus finalized receipts and read-only `get_commitment`/`get_verdict` state. For expiry, create with no delivery, wait past the deadline, expire, and record the final `EXPIRED` state.
