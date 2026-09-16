# AgentPact deployment runbook

## Canonical hardened deployment

Use the explicit Studio-dev network only:

```text
chain: 61997
rpc: https://studio-dev.genlayer.com/api
contract: 0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF
deployment tx: 0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a
source sha256: f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9
repository: https://github.com/GIFTEDLOV/agentpact
```

This replacement was required because the source changed. It was broadcast exactly once, then verified as `FINALIZED`, `FINISHED_WITH_RETURN`, and `MAJORITY_AGREE`; the address has contract code, the live schema matches the preflight schema, and `gen_getContractCode` matches the source SHA above. Never rebroadcast this deployment.

The prior deployment `0xdA8781136eB4e59A5216e8891113222C42928a8C` with transaction `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9` is historical only and is not a current coordinate.

## Validation before deployment

Run from the repository root and record the exact source hash:

```bash
sha256sum contracts/agent_pact.py
.venv/bin/pytest -q
GENVM_VERSION=v0.2.16 .venv/bin/genvm-lint lint contracts/agent_pact.py
python -m py_compile contracts/agent_pact.py
git diff --check
```

Run `gen_getContractSchemaForCode` against `https://studio-dev.genlayer.com/api` and require HTTP 200. The exact 11-method schema is recorded in [`VALIDATION.md`](VALIDATION.md); `submit_delivery` must include the artifact URL/SHA/bytes and three URL/SHA/bytes evidence triples. Check requester balance, latest nonce, pending nonce, and the deployment fee profile before signing. If source changes after a deployment, stop and obtain a new deployment confirmation; never blind-rebroadcast.

## Evidence commitments

`submit_delivery` commits:

```text
commitment_id, artifact_url, artifact_sha256, artifact_bytes,
evidence_url_1, evidence_sha256_1, evidence_bytes_1,
evidence_url_2, evidence_sha256_2, evidence_bytes_2,
evidence_url_3, evidence_sha256_3, evidence_bytes_3
```

All URLs must be public HTTPS transport locations. Each required evidence byte count must be greater than zero and no greater than `MAX_EVIDENCE_BYTES = 12,000`; evidence URLs must be distinct and different from the artifact URL. At adjudication, every response is checked for HTTP success, a body, exact committed byte count, exact committed SHA-256, and UTF-8 decoding before semantic use. Any failure maps all criteria to `UNKNOWN`, `evidence_valid=false`, and `INCONCLUSIVE`.

## Lifecycle proof procedure

Use only disposable Studio-dev accounts and public HTTPS fixtures. Use a separate commitment for accepted, rejected, artifact-mismatch inconclusive, evidence-failure inconclusive, mutable-evidence attack, and expired branches. Record every transaction hash and verify each through the RPC as `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE`.

For submitted branches, record create, provider-only submit, requester-only dispute, adjudicate, and read-only `get_commitment`/`get_verdict` state. For expiry, create with no delivery, read the exact deadline, wait until it has passed, expire, and record `EXPIRED`. The complete final evidence is in [`RELEASE_HANDOFF.md`](RELEASE_HANDOFF.md).
