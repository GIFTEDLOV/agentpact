# AgentPact

AgentPact is an evidence-backed commitment adjudication contract for GenLayer. A requester creates a commitment, a provider submits a public HTTPS delivery, and either legitimate party can adjudicate after a dispute or deadline. Consensus evaluates the complete committed artifact and evidence, failing closed to `INCONCLUSIVE` when bytes cannot be recovered or verified.

## Release-candidate status

This repository contains a new hardened source revision for a future deployment. A NEW deployment of the exact final source is required before resubmission. This run performs no deployment and does not claim release completion.

Both existing AgentPact deployments are HISTORICAL only:

- Older rejected deployment: `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`.
- Corrected but now historical deployment: `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`, transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`, source SHA `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`.
- Hardened release-candidate source SHA: `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`.

The historical source identity is not the identity for the next deployment. The only source identity to use after all gates pass is the SHA-256 of the final hardened `contracts/agent_pact.py` bytes.

## E106 and contract discovery

The contract directly inherits from `gl.contract.Contract`, declares an explicit zero-argument `__init__`, and exposes no `ContractBase` compatibility alias. Current semantic discovery must select `AgentPact`; the historical rejected revision selected the SDK base through that alias and produced E106.

## Security model

AgentPact commits the artifact and each evidence source with lowercase exact SHA-256 digests and positive exact byte counts. Externally supplied text bounds are measured in UTF-8 bytes. URLs require strict HTTPS parsing, a hostname, valid port syntax, no credentials, no fragments, no controls, and a bounded UTF-8 length.

The hardened V1 artifact limit is `MAX_ARTIFACT_BYTES = 12,000`. The complete decoded artifact within that bound is passed to semantic evaluation; there is no silent prompt truncation. Evidence is also bounded at `MAX_EVIDENCE_BYTES = 12,000` and every verified body must decode as UTF-8.

The model response must contain exactly `{"criterion_results": [...]}`. The consensus result must contain exactly `{"criterion_results": [...], "evidence_valid": bool}`. The validator independently fetches and verifies the artifact and all evidence, independently evaluates the material, validates the exact result shape, and compares the complete consensus-critical result with the leader.

Unavailable, malformed, oversized, mutated, or digest-mismatched artifact/evidence never becomes `ACCEPTED`; all criteria become `UNKNOWN` and the result is `INCONCLUSIVE`. Transaction time comes only from `gl.message.datetime`; no local wall clock is used.

## Validation

Run the complete local and semantic gates from the repository root:

```text
python -m pytest -q
python -m py_compile contracts/agent_pact.py
genvm-lint lint contracts/agent_pact.py
genvm-lint validate contracts/agent_pact.py
genvm-lint check contracts/agent_pact.py
genvm-lint schema contracts/agent_pact.py
genvm-lint typecheck contracts/agent_pact.py
git diff --check
```

The expected public ABI remains 11 methods with a zero-parameter constructor. Studio-dev raw-source schema preflight must pass before any future deployment. See [`docs/VALIDATION.md`](docs/VALIDATION.md), [`docs/DEPLOYMENT_RUNBOOK.md`](docs/DEPLOYMENT_RUNBOOK.md), and [`docs/RELEASE_HANDOFF.md`](docs/RELEASE_HANDOFF.md).

Financial settlement, payments, and frontend logic remain outside AgentPact.
