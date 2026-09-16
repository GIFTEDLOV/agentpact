# AgentPact deployment runbook

## Canonical deployment

Use the explicit Studio-dev network only:

```text
chain: 61997
rpc: https://studio-dev.genlayer.com/api
contract: 0xD9E8904920b23845ab1581fc4B4716B3B8be2101
deployment tx: 0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c
source sha256: 68781905e76686df967e1025bfada2f955db569b6c2e82bc956b56d85c72a64e
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

Then query `gen_getContractSchema` at the canonical RPC and verify the deployed schema has the exact methods in `docs/VALIDATION.md`. The public explorer URL is https://explorer-studio-dev.genlayer.com/address/0xD9E8904920b23845ab1581fc4B4716B3B8be2101.

## Lifecycle rules

Use only disposable Studio-dev accounts. Use separate commitments for accepted, rejected, inconclusive, and expired branches. For submitted branches, record create, submit, dispute, and adjudicate transaction hashes plus finalized receipts and read-only `get_commitment`/`get_verdict` state. For expiry, create with no delivery, wait past the deadline, expire, and record the final `EXPIRED` state.

