# AgentPact

AgentPact is an evidence-backed commitment adjudication contract for GenLayer. A requester creates a commitment, a provider submits a public HTTPS delivery, and either party can adjudicate after a dispute or deadline. Independent nondeterministic evaluation is validated by consensus and fails closed to `INCONCLUSIVE` when committed bytes cannot be recovered or verified.

## Current corrected deployment

- Network: Studio-dev
- Chain ID: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`
- Deployment transaction: `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`
- Deployment status: `FINALIZED`; execution `FINISHED_WITH_RETURN`; consensus `MAJORITY_AGREE`
- Source SHA-256: `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`
- Public repository: https://github.com/GIFTEDLOV/agentpact

The deployed source is preserved byte-for-byte in [`contracts/agent_pact.py`](contracts/agent_pact.py). The source SHA is the SHA-256 of the exact UTF-8 bytes submitted in the deployment transaction. The previous deployment `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` / `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a` is HISTORICAL because its source predates the semantic-validator correction.

## Semantic-validator E106 remediation

`AgentPact` always declared its own `__init__(self)`. The former module-level `ContractBase` compatibility alias could be discovered as the contract class before `AgentPact`, so schema extraction inspected the SDK base class and reported `__init__ is absent`. The alias was removed and `AgentPact` now directly inherits from `gl.contract.Contract`. Current SDK semantic validation and schema extraction pass, and the exact corrected source was redeployed with a matching on-chain source hash.

## Evidence trust model

AgentPact cryptographically commits both the delivered artifact and every required supporting evidence input using SHA-256 plus the exact byte count. URLs are transport locations, not evidence identity. At adjudication, validators independently retrieve the public HTTPS bytes, verify HTTP success, exact byte count, SHA-256, and UTF-8 decoding before semantic evaluation.

Supporting evidence is bounded by `MAX_EVIDENCE_BYTES = 12,000`. If committed bytes cannot be recovered or verified—including a non-200 response, missing body, invalid UTF-8, changed content, wrong digest, or wrong byte count—every criterion becomes `UNKNOWN`, `evidence_valid` is `false`, and the terminal verdict is `INCONCLUSIVE`. No availability failure is silently accepted as `ACCEPTED` or `REJECTED`.

## Safety properties

- Requester and provider must be different addresses.
- Deliveries require bounded HTTPS URLs, lowercase SHA-256 digests, positive bounded byte counts, and distinct evidence URLs.
- Provider-only delivery, requester-only dispute, deadline checks, terminal-status checks, and independent validator reevaluation are enforced on-chain.
- Artifact and evidence are verified before being wrapped as untrusted data in the classifier prompt.
- Validator output is restricted to `PASS`, `FAIL`, or `UNKNOWN` with the exact criterion count.
- Any failed criterion produces `REJECTED`; any unknown criterion produces `INCONCLUSIVE`; only all-pass criteria with verified evidence produce `ACCEPTED`.
- Financial settlement remains outside AgentPact.

## Validation

The reproducible validation commands and the exact Studio-dev schema check are recorded in [`docs/VALIDATION.md`](docs/VALIDATION.md). Deployment and lifecycle operations are documented in [`docs/DEPLOYMENT_RUNBOOK.md`](docs/DEPLOYMENT_RUNBOOK.md). The release evidence is in [`docs/RELEASE_HANDOFF.md`](docs/RELEASE_HANDOFF.md).
