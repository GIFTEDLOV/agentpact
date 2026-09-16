# Validation record

## Canonical source

The contract source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its exact UTF-8 bytes hash to:

```text
68781905e76686df967e1025bfada2f955db569b6c2e82bc956b56d85c72a64e
```

This equals the source embedded in the finalized deployment transaction `0xf4fe13133e8fb7a5f86781baf0717db27b2ce04ac63abef968b07fb69326f77c`.

## Required local checks

Run from the repository root:

```bash
.venv/bin/pytest -q
GENVM_VERSION=v0.2.16 .venv/bin/genvm-lint lint contracts/agent_pact.py
python -m py_compile contracts/agent_pact.py
git diff --check
```

## Exact Studio-dev semantic/schema check

The strongest available deployed-source check is the Studio-dev JSON-RPC method `gen_getContractSchema` against chain `61997`, RPC `https://studio-dev.genlayer.com/api`, and contract `0xD9E8904920b23845ab1581fc4B4716B3B8be2101`. The expected public methods are:

```text
create_commitment(provider:string, title:string, specification:string, acceptance_criteria:string, deadline:int, minimum_evidence:int) -> string [write]
submit_delivery(commitment_id:string, artifact_url:string, artifact_sha256:string, artifact_bytes:int, evidence_url_1:string, evidence_url_2:string, evidence_url_3:string) -> null [write]
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

The live schema check returned all 11 methods with the exact parameter types, read-only flags, and return shapes above. The public explorer responded HTTP 200 for the canonical contract and deployment transaction pages.

