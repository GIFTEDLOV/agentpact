# AgentPact hardened release-candidate handoff

The repository is being prepared for a NEW corrected Intelligent Contract submission. Both previous deployments are historical:

- `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` — older rejected deployment.
- `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46` — corrected deployment, now historical; transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`.

The hardened source directly inherits `gl.contract.Contract`, keeps a zero-parameter constructor and the existing 11-method ABI, bounds all external text by UTF-8 bytes, strictly validates HTTPS URLs and SHA-256 commitments, rejects zero providers, evaluates the entire committed artifact up to `12,000` bytes, and fails closed on invalid evidence or model/consensus output.

The source uses only `gl.message.datetime` for transaction time. It does not use local wall-clock calls. The validator independently retrieves, verifies, evaluates, validates exact output shape, and compares the complete consensus result with the leader.

Before resubmission, complete the local gates and Studio-dev raw-source schema preflight, freeze the final source SHA, and perform exactly one separately authorized NEW deployment. Do not add a deployment address or call deployment tools in this preparation run.
