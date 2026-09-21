# AgentPact release handoff

## Handoff status

This is the verified hardened Studio-dev release. The new deployment is the only address to use for resubmission evidence.

The two existing deployments are HISTORICAL only:

| Role | Contract | Deployment transaction | Source identity |
|---|---|---|---|
| Older rejected | `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` | historical rejected deployment | historical pre-direct-inheritance source |
| Corrected, now historical | `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46` | `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f` | `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8` |
| New hardened live deployment | `0xd8a44cc6D81eeb54A51071F790c242AE03e19157` | `0x338f0cccd6077a04be92ded0aabc80ac4584cfbf3f1631dd03707fdee28f11ae` | `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af` |

Do not use either historical address or its Explorer evidence. Use only the new address and its Explorer page: `https://explorer-studio-dev.genlayer.com/address/0xd8a44cc6D81eeb54A51071F790c242AE03e19157`.

## Source and toolchain freeze

```text
repository: https://github.com/GIFTEDLOV/agentpact
chain: 61997
rpc: https://studio-dev.genlayer.com/api
runner: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
genvm-linter: 0.11.1-rc.2
GenVM artifact: v0.6.0-rc5
```

The frozen hardened source SHA is `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`. The deployed source was retrieved and matched this SHA byte-for-byte. Deployment finalized with `FINISHED_WITH_RETURN` and `MAJORITY_AGREE`; fee value was `100000000000010352`.

## Security findings addressed

- Direct class discovery remains `AgentPact(gl.contract.Contract)` with an explicit zero-argument constructor and no `ContractBase` alias; the old E106 path is closed.
- Provider, requester, dispute, adjudication, zero-address, malformed-address, and canonical address comparisons are enforced with `Address` values.
- State transitions are terminal-safe, deadline checks use deterministic `gl.message.datetime`, and exact deadline boundaries are tested.
- Text and URL limits are UTF-8 byte bounds. HTTPS URLs reject malformed ports, credentials, fragments, controls, missing hosts, and non-HTTPS schemes.
- SHA-256 commitments are exactly 64 lowercase hexadecimal characters with no whitespace normalization.
- Evidence tuple shape is bounded, positive, contiguous, distinct, fully initialized, and fail-closed on all fetch, body, byte, digest, and UTF-8 failures.
- `MAX_ARTIFACT_BYTES` is `12,000`; the complete decoded artifact is passed to the semantic prompt with no silent truncation.
- Model output is exactly `{"criterion_results": [...]}`. Consensus output is exactly `{"criterion_results": [...], "evidence_valid": bool}`. The validator independently repeats retrieval, verification, semantic evaluation, shape validation, and complete-result comparison.

## Verified release evidence

The final handoff includes, from the NEW deployment:

1. raw-source schema preflight HTTP 200 and exact 11-method ABI;
2. deployed source retrieval and SHA-256 equality with the GitHub source;
3. finalized deployment and transaction status;
4. accepted, rejected, and inconclusive lifecycle proofs;
5. live unauthorized and terminal-reentry rejection checks;
6. Explorer evidence referencing the NEW address, never either historical address.

Lifecycle evaluation transactions:

```text
ACCEPTED:     0x5e7db2653384762c8704dab6bd175a8b2f6c873a4a0ec57fa6945879b3439e6f
REJECTED:     0x53b1b984460885fa996d5d5202959eb14720754d7c0565390fa0678c8ccd079f
INCONCLUSIVE: 0x70afc6e166012dff20a5fa2326bfdfea8bd79127b15201f7f9abcaa12449cfff
```

The live contract reports `AgentPact`, version `0.1.0`, 8 criteria, 3 evidence URLs, 12,000-byte artifact/evidence limits, and the expected seven statuses. The final local regression remained 52 passing tests with validation, check, schema, typecheck, and source SHA gates passing.

Submission evidence:

1. GitHub: `https://github.com/GIFTEDLOV/agentpact`
2. New Explorer contract: `https://explorer-studio-dev.genlayer.com/address/0xd8a44cc6D81eeb54A51071F790c242AE03e19157`
