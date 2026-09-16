# AgentPact release handoff

## Canonical release coordinates

- Studio-dev chain: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: [`0xD9E8904920b23845ab1581fc4B4716B3B8be2101`](https://explorer-studio-dev.genlayer.com/address/0xD9E8904920b23845ab1581fc4B4716B3B8be2101)
- Deployment transaction: [`0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c`](https://explorer-studio-dev.genlayer.com/tx/0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c)
- Source SHA-256: `68781905e76686df967e1025bfada2f955db569b6c2e82bc956b56d85c72a64e`
- Public repository: https://github.com/GIFTEDLOV/agentpact

## Four disposable live proofs

The table below is the release gate. Every row must contain the exact commitment ID, all lifecycle transaction hashes, finalized result, and readback values from Studio-dev. Fixture URL, served byte count, and served SHA are recorded with the row.

| Branch | Commitment ID | Transaction hashes (create / submit / dispute / adjudicate or expire) | Finalized result | Final status and readback |
|---|---|---|---|---|
| accepted | `PENDING` | `PENDING` | `PENDING` | `PENDING` |
| rejected | `PENDING` | `PENDING` | `PENDING` | `PENDING` |
| inconclusive | `PENDING` | `PENDING` | `PENDING` | `PENDING` |
| expired | `PENDING` | `PENDING` | `PENDING` | `PENDING` |

## Validation gate

See [`VALIDATION.md`](VALIDATION.md) for the exact commands and deployed `gen_getContractSchema` contract. Do not call the release complete until the proof table has no `PENDING` entries, all hashes have public Studio-dev receipts, and the final independent audit is recorded.

