# Validation record

## Current corrected source and deployment

The contract source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its exact UTF-8 bytes hash to:

```text
bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8
```

This equals the source fetched from the finalized corrected deployment `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f` at `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`.

The former deployment `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` / `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a` with source SHA `f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9` is HISTORICAL only.

## Required local checks

Run from the repository root:

```bash
python -m pytest -q
python -m py_compile contracts/agent_pact.py
genvm-lint lint contracts/agent_pact.py
genvm-lint validate contracts/agent_pact.py
genvm-lint check contracts/agent_pact.py
genvm-lint schema contracts/agent_pact.py
git diff --check
```

On the release machine, `genvm-lint` was invoked through the installed
`genvm_linter.cli` entry point with UTF-8 console output because the Windows
console script was not on PATH. This is the same official CLI implementation.

## Exact Studio-dev semantic/schema check

The strongest available deployed-source check is the Studio-dev JSON-RPC method `gen_getContractSchema` against chain `61997`, RPC `https://studio-dev.genlayer.com/api`, and contract `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`. The expected public methods are:

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

The final `gen_getContractSchemaForCode` preflight returned HTTP 200 and all 11 expected methods before deployment, including the 13-parameter evidence-commitment form of `submit_delivery`. The final live `gen_getContractSchema` check returned the same 11 methods with the exact parameter types, read-only flags, and return shapes above. The deployed source fetched with `gen_getContractCode` returned 24,344 nonempty bytes and hashes exactly to the local SHA above. GenLayer source/code is present at the new address.

## Recorded release gates

- GenVM linter: `0.11.1-rc.2`; GenVM artifact: `v0.6.0-rc5`; py-genlayer runner: `5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng`.
- Direct and semantic regression tests: `21 passed`.
- GenVM lint: `Lint passed (3 checks)`.
- Semantic validation: passed; contract `AgentPact`; constructor params `0`; 11 methods.
- Combined check: passed.
- Schema extraction: passed; exact documented ABI comparison passed.
- Typecheck: passed with `0 error(s), 0 warning(s)`.
- Python compilation: passed.
- `git diff --check`: passed.
- Schema preflight: HTTP 200, exact 11 methods and exact 13-parameter `submit_delivery`.
- Live schema: exact preflight/local match; 24,344 deployed source bytes present.
- Source SHA-256: `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`.
- Deployment receipt: `FINALIZED`, `MAJORITY_AGREE`, `FINISHED_WITH_RETURN`; leader execution `SUCCESS`.
- `contract_info()`: name `AgentPact`, version `0.1.0`, purpose `evidence-backed commitment adjudication`, statuses `COMMITTED`, `SUBMITTED`, `DISPUTED`, `ACCEPTED`, `REJECTED`, `INCONCLUSIVE`, `EXPIRED`.
- Lifecycle proof on the corrected deployment: create `0x9ffeeb241c1b768d6e95c247c8da21e437b41cf22e446311d503acf9f1623378`; submit `0x8e74c76df2e1e9c99020977a75a14be10e5b54edc24033388e9599922d8cc52b`; dispute `0xbf9f6a789f70d00eef253f44d31a0dab41a1f792c16dfab27f26a377ac00e106`; adjudicate `0xc606bec2752a6a0f546733321878dd542a0163456217d1a448e87d9e3183e50d`. All four finalized with `MAJORITY_AGREE` and `FINISHED_WITH_RETURN`; readback was `ACCEPTED`, score `100`, `evidence_valid=true`.
- `MAX_EVIDENCE_BYTES`: `12,000`; all submitted evidence commitments use positive exact byte counts within this bound.

## Semantic-validator E106 remediation

`AgentPact` always declared `__init__(self)`. Before the correction, the module-level `ContractBase` compatibility alias was encountered first by current semantic discovery, selecting `genlayer.contract.Contract`; that SDK base class has no user-defined `__init__` in its own class dictionary, producing E106. The alias was removed and `AgentPact` now directly inherits from `gl.contract.Contract`. After the correction, discovery selected `AgentPact`, its constructor schema had zero parameters, and current semantic validation plus schema extraction passed. The corrected exact source was redeployed and its on-chain source SHA matches the repository SHA above.
