# Validation record

## Verified release identity

The hardened source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its frozen source SHA-256 is `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`. The previous source SHA `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8` is HISTORICAL.

Both previous deployments are HISTORICAL and must not be used for submission:

- Older rejected: `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`.
- Corrected historical: `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`, deployment transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`.

The new deployment below is the only current AgentPact deployment to use for submission evidence.

## New live deployment

```text
contract: 0xd8a44cc6D81eeb54A51071F790c242AE03e19157
deployment transaction: 0x338f0cccd6077a04be92ded0aabc80ac4584cfbf3f1631dd03707fdee28f11ae
explorer: https://explorer-studio-dev.genlayer.com/address/0xd8a44cc6D81eeb54A51071F790c242AE03e19157
status: FINALIZED
execution: FINISHED_WITH_RETURN
consensus: MAJORITY_AGREE
source SHA-256: 2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af
SDK: genlayer-js 2.0.0-rc.1
feeValue: 100000000000010352
```

## Live lifecycle evidence

All live writes finalized with `FINISHED_WITH_RETURN` and `MAJORITY_AGREE` unless explicitly marked as a negative rejection.

| Proof | Commitment | Evaluation transaction | Result |
|---|---|---|---|
| Accepted | `pact-1` | `0x5e7db2653384762c8704dab6bd175a8b2f6c873a4a0ec57fa6945879b3439e6f` | `ACCEPTED`, score 100, `evidence_valid=true`, `PASS` |
| Rejected | `pact-2` | `0x53b1b984460885fa996d5d5202959eb14720754d7c0565390fa0678c8ccd079f` | `REJECTED`, `evidence_valid=true`, `FAIL` |
| Inconclusive | `pact-3` | `0x70afc6e166012dff20a5fa2326bfdfea8bd79127b15201f7f9abcaa12449cfff` | `INCONCLUSIVE`, `evidence_valid=false`, `UNKNOWN` |

The inconclusive proof used a validly shaped but intentionally incorrect evidence SHA-256 commitment.

`contract_info()` verified `name=AgentPact`, `version=0.1.0`, purpose `evidence-backed commitment adjudication`, `max_criteria=8`, `max_evidence_urls=3`, `max_artifact_bytes=12000`, `max_evidence_bytes=12000`, and the complete seven-status list.

Live negative checks:

```text
unauthorized provider submission: 0xd2c2cc2b87d30ffaa88251c20b216856a25841f3068e09fb707c783423e66064 — FINALIZED / FINISHED_WITH_ERROR
terminal re-adjudication: 0x50d7811c5fe7100c87fd7d50ada0942856f0f9dedd2517e07050cf32f69ff605 — FINALIZED / FINISHED_WITH_ERROR
```

No deployment transaction was rebroadcast after the single successful deployment.

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

Git history preserves the rejected pre-fix source. Its module-level `ContractBase` compatibility alias could be discovered before `AgentPact`, causing current semantic discovery to select `genlayer.contract.Contract` and report the historical E106 constructor error. The corrected historical source removed that alias and directly inherited from `gl.contract.Contract`, but that deployment is now historical too. The hardened source is a distinct revision and was deployed exactly once as the new live deployment recorded above.

The old rejected address is therefore not evidence for the hardened source. Explorer/source evidence must use only the new deployment address and the frozen SHA recorded above.

## Studio-dev raw-source preflight

Target:

```text
RPC: https://studio-dev.genlayer.com/api
CHAIN ID: 61997
RUNNER: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
METHOD: gen_getContractSchemaForCode
```

The preflight used the exact raw UTF-8 source bytes and the current supported Studio-dev schema request. It returned HTTP 200, selected `AgentPact`, reported zero constructor parameters and the exact 11-method ABI, with no E106, runner, import, or schema-drift errors.

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
deployment: PASS — exactly one broadcast; source and deployed bytes match
```
