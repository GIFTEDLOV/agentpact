# Validation record

## Canonical source

The contract source is [`contracts/agent_pact.py`](../contracts/agent_pact.py). Its exact UTF-8 bytes hash to:

```text
c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595
```

This equals the source fetched from the finalized replacement deployment `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9` at `0xdA8781136eB4e59A5216e8891113222C42928a8C`.

## Required local checks

Run from the repository root:

```bash
.venv/bin/pytest -q
GENVM_VERSION=v0.2.16 .venv/bin/genvm-lint lint contracts/agent_pact.py
python -m py_compile contracts/agent_pact.py
git diff --check
```

## Exact Studio-dev semantic/schema check

The strongest available deployed-source check is the Studio-dev JSON-RPC method `gen_getContractSchema` against chain `61997`, RPC `https://studio-dev.genlayer.com/api`, and contract `0xdA8781136eB4e59A5216e8891113222C42928a8C`. The expected public methods are:

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

The final `gen_getContractSchemaForCode` preflight returned HTTP 200 and all 11 expected methods before deployment. The final live schema check returned the same 11 methods with the exact parameter types, read-only flags, and return shapes above. The deployed source fetched with `gen_getContractCode` hashes exactly to the local SHA above. The public explorer responded HTTP 200 for the canonical contract and deployment transaction pages.
