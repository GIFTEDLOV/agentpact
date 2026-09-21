# Validation record

## Release-candidate identity

The hardened source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its frozen release-candidate SHA-256 is `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`. The previous source SHA `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8` is HISTORICAL.

Both existing deployments are HISTORICAL and must not be used for the next submission:

- Older rejected: `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`.
- Corrected historical: `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`, deployment transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`.

A NEW deployment of the exact final hardened source is required before resubmission. No deployment transaction is performed by this release-candidate run.

## Toolchain and local gates

- Runner pin: `py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng`.
- Installed linter: `genvm-linter 0.11.1-rc.2`.
- Pinned cached GenVM artifact used for semantic gates: `v0.6.0-rc5`.
- Python: `3.14.3`; pytest: `8.4.1`; Pyright: `1.1.410`.

Required commands:

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

The Windows runner uses UTF-8 console output and the installed Scripts directory on `PATH` for the official `genvm-lint` and `pyright` entry points. The contract keeps the runner pin as its first physical line, followed by a blank line before the Pyright directive so Studio-dev raw-source parsing sees a valid runner header. The directive only suppresses known dynamic GenLayer SDK alias diagnostics; no contract errors remain.

## Expected semantic discovery

The current validator must report all of the following:

```text
SELECTED_CLASS = AgentPact
DIRECT_BASE = gl.contract.Contract
CONSTRUCTOR_PARAMS = 0
PUBLIC_METHOD_COUNT = 11
E106 = absent
ContractBase = absent
genlayer.contract.Contract selected as contract = false
```

The exact public ABI is:

```text
create_commitment(provider:string, title:string, specification:string, acceptance_criteria:string, deadline:int, minimum_evidence:int) -> string [write]
submit_delivery(commitment_id:string, artifact_url:string, artifact_sha256:string, artifact_bytes:int, evidence_url_1:string, evidence_sha256_1:string, evidence_bytes_1:int, evidence_url_2:string, evidence_sha256_2:string, evidence_bytes_2:int, evidence_url_3:string, evidence_sha256_3:string, evidence_bytes_3:int) -> null [write]
open_dispute(commitment_id:string, reason:string) -> null [write]
adjudicate(commitment_id:string) -> null [write]
expire_unsubmitted(commitment_id:string) -> null [write]
get_commitment(commitment_id:string) -> any [view]
get_status(commitment_id:string) -> string [view]
get_verdict(commitment_id:string) -> any [view]
get_commitment_ids() -> DynArray[string] [view]
get_commitment_count() -> int [view]
contract_info() -> any [view]
```

## Hardened gates

The source now enforces UTF-8 byte limits for title, specification, criteria, dispute reason, and URLs; strict parsed HTTPS URLs; exact lowercase SHA-256 digests; canonical `Address` comparisons with zero-provider rejection; contiguous and fully consistent evidence tuples; deterministic GenLayer message time; and terminal-state protections.

`MAX_ARTIFACT_BYTES` is `12,000`, and the complete decoded artifact is passed to semantic evaluation. There is no `artifact_text[:12_000]` or equivalent silent truncation. The model result and consensus result use exact-key validation, and the validator independently retrieves, verifies, evaluates, validates, and compares its result with the leader.

## Historical E106 complaint

Git history preserves the rejected pre-fix source. Its module-level `ContractBase` compatibility alias could be discovered before `AgentPact`, causing current semantic discovery to select `genlayer.contract.Contract` and report the historical E106 constructor error. The corrected historical source removed that alias and directly inherited from `gl.contract.Contract`, but that deployment is now historical too. The hardened source is a distinct revision and must be deployed exactly once in a future run after this record is finalized.

The old rejected address is therefore not evidence for the hardened source. Explorer/source evidence for resubmission must use the future deployment address and the final frozen SHA recorded after deployment.

## Studio-dev raw-source preflight

Target:

```text
RPC: https://studio-dev.genlayer.com/api
CHAIN ID: 61997
RUNNER: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
METHOD: gen_getContractSchemaForCode
```

The preflight must use the exact raw UTF-8 source bytes and the current supported Studio-dev schema request. It must return HTTP 200, select `AgentPact`, report zero constructor parameters and the exact 11-method ABI, with no E106, runner, import, or schema-drift errors. This run does not deploy.

Recorded for the frozen candidate SHA above:

```text
pytest: 52 passed
py_compile: PASS
genvm-lint lint: PASS
genvm-lint validate: PASS (AgentPact, 11 methods, 0 constructor params)
genvm-lint check: PASS
genvm-lint schema: PASS (11 methods)
genvm-lint typecheck: PASS (0 errors, 0 warnings)
git diff --check: PASS
Studio-dev raw schema: HTTP 200, RPC error null, AgentPact, 0 constructor params, 11 methods
deployment: NOT RUN
```
