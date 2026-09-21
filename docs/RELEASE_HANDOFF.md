# AgentPact release handoff

## Handoff status

This is a hardened release candidate, not a deployed release. A NEW deployment is required before resubmission. This run must not deploy or add a new deployment address.

The two existing deployments are HISTORICAL only:

| Role | Contract | Deployment transaction | Source identity |
|---|---|---|---|
| Older rejected | `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` | historical rejected deployment | historical pre-direct-inheritance source |
| Corrected, now historical | `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46` | `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f` | `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8` |

Do not use either address or its Explorer evidence for the next submission. The future deployment must be created from the final GitHub source bytes, and its deployed-source SHA must match exactly.

## Source and toolchain freeze

```text
repository: https://github.com/GIFTEDLOV/agentpact
chain: 61997
rpc: https://studio-dev.genlayer.com/api
runner: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
genvm-linter: 0.11.1-rc.2
GenVM artifact: v0.6.0-rc5
```

The frozen hardened release-candidate source SHA is `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`. Use only that SHA for the one future deployment. Do not claim release completion until Explorer/source verification is byte-for-byte equal.

## Security findings addressed

- Direct class discovery remains `AgentPact(gl.contract.Contract)` with an explicit zero-argument constructor and no `ContractBase` alias; the old E106 path is closed.
- Provider, requester, dispute, adjudication, zero-address, malformed-address, and canonical address comparisons are enforced with `Address` values.
- State transitions are terminal-safe, deadline checks use deterministic `gl.message.datetime`, and exact deadline boundaries are tested.
- Text and URL limits are UTF-8 byte bounds. HTTPS URLs reject malformed ports, credentials, fragments, controls, missing hosts, and non-HTTPS schemes.
- SHA-256 commitments are exactly 64 lowercase hexadecimal characters with no whitespace normalization.
- Evidence tuple shape is bounded, positive, contiguous, distinct, fully initialized, and fail-closed on all fetch, body, byte, digest, and UTF-8 failures.
- `MAX_ARTIFACT_BYTES` is `12,000`; the complete decoded artifact is passed to the semantic prompt with no silent truncation.
- Model output is exactly `{"criterion_results": [...]}`. Consensus output is exactly `{"criterion_results": [...], "evidence_valid": bool}`. The validator independently repeats retrieval, verification, semantic evaluation, shape validation, and complete-result comparison.

## Required evidence before resubmission

The final handoff must include, from the NEW deployment:

1. raw-source schema preflight HTTP 200 and exact 11-method ABI;
2. deployed source retrieval and SHA-256 equality with the final GitHub source;
3. finalized deployment and transaction status;
4. accepted, rejected, inconclusive, mutable-evidence, and expired lifecycle proofs;
5. Explorer source evidence referencing the NEW address, never either historical address.

No deployment, push, or resubmission is authorized by this handoff document itself.
