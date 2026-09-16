# Validation record

## Canonical source

The contract source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its exact UTF-8 bytes hash to:

```text
f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9
```

This equals the source fetched from the finalized hardened deployment `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a` at `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`.

## Required local checks

Run from the repository root:

```bash
.venv/bin/pytest -q
GENVM_VERSION=v0.2.16 .venv/bin/genvm-lint lint contracts/agent_pact.py
python -m py_compile contracts/agent_pact.py
git diff --check
```

## Exact Studio-dev semantic/schema check

The strongest available deployed-source check is the Studio-dev JSON-RPC method `gen_getContractSchema` against chain `61997`, RPC `https://studio-dev.genlayer.com/api`, and contract `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`. The expected public methods are:

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

The final `gen_getContractSchemaForCode` preflight returned HTTP 200 and all 11 expected methods before deployment, including the 13-parameter evidence-commitment form of `submit_delivery`. The final live `gen_getContractSchema` check returned the same 11 methods with the exact parameter types, read-only flags, and return shapes above. The deployed source fetched with `gen_getContractCode` hashes exactly to the local SHA above, and bytecode is present at the new address.

## Recorded release gates

- Runner: GenVM `v0.2.16`; contract dependency runner `py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng`.
- Direct tests: `20 passed`.
- GenVM lint: `Lint passed (3 checks)`.
- Python compilation: passed.
- `git diff --check`: passed.
- Source SHA-256: `f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9`.
- `MAX_EVIDENCE_BYTES`: `12,000`; all submitted evidence commitments use positive exact byte counts within this bound.
- Public explorer pages for the canonical contract and deployment transaction returned HTTP 200.
