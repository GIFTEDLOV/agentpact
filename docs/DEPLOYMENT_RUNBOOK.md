# AgentPact deployment runbook

## Release-candidate rule

Do not deploy from this run. The next submission requires one NEW deployment of the exact final hardened GitHub source after all local and Studio-dev raw-source gates pass. Do not reuse either historical address.

Historical coordinates:

```text
older rejected contract: 0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF
corrected historical contract: 0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46
corrected historical deployment tx: 0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f
historical corrected source SHA: bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8
```

No future deployment address or transaction is written here until a separate deployment run completes and Explorer/source evidence matches the frozen hardened SHA byte-for-byte.

## Network and runner

```text
chain: 61997
rpc: https://studio-dev.genlayer.com/api
runner: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
repository: https://github.com/GIFTEDLOV/agentpact
```

## Validation before a future deployment

From the repository root, freeze the source hash and run every gate:

```text
sha256sum contracts/agent_pact.py
python -m pytest -q
python -m py_compile contracts/agent_pact.py
genvm-lint lint contracts/agent_pact.py
genvm-lint validate contracts/agent_pact.py
genvm-lint check contracts/agent_pact.py
genvm-lint schema contracts/agent_pact.py
genvm-lint typecheck contracts/agent_pact.py
git diff --check
```

Run raw-source `gen_getContractSchemaForCode` against the RPC and require HTTP 200, `AgentPact`, zero constructor parameters, the exact 11-method ABI, the pinned runner, and no E106/import/runner/schema error. Stop if the source changes after preflight.

Only after these checks should a separately authorized deployment run sign one transaction. Record the future deployment address, transaction, finalization state, Explorer source verification, and deployed-source SHA in a new handoff entry. Never blind-rebroadcast.

## Evidence commitments

`submit_delivery` commits the artifact URL/SHA/byte count and up to three evidence URL/SHA/byte-count triples. All populated URLs must be strict bounded HTTPS values. Evidence slots are contiguous; every empty optional slot has an empty digest and zero byte count; populated evidence URLs are distinct and differ from the artifact URL.

The hardened V1 artifact and evidence limits are both `12,000` bytes. At adjudication, the leader and validator independently fetch every committed body and verify HTTP success, nonempty body, exact byte count, exact lowercase SHA-256, and UTF-8 decoding. Any failure maps all criteria to `UNKNOWN`, `evidence_valid=false`, and `INCONCLUSIVE`.

## Lifecycle proof for the future deployment

Use disposable Studio-dev accounts and public HTTPS fixtures. Use separate commitments for accepted, rejected, artifact-mismatch inconclusive, evidence-failure inconclusive, mutable-evidence inconclusive, and expired branches. Record each transaction hash and verify `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE` through the RPC.

For submitted branches, record create, provider-only submit, requester-only dispute, adjudication, and read-only state. For expiry, create with no delivery, wait past the exact message-time deadline, expire, and record `EXPIRED`. All lifecycle evidence from the previous deployment is historical and cannot substitute for proof from the new deployment.
