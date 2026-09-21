# AgentPact deployment runbook

## Verified release record

The hardened source has been deployed once through the direct `genlayer-js 2.0.0-rc.1` path. Do not reuse either historical address and do not rebroadcast the deployment transaction.

Historical coordinates:

```text
older rejected contract: 0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF
corrected historical contract: 0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46
corrected historical deployment tx: 0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f
historical corrected source SHA: bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8
```

New live deployment:

```text
contract: 0xd8a44cc6D81eeb54A51071F790c242AE03e19157
deployment tx: 0x338f0cccd6077a04be92ded0aabc80ac4584cfbf3f1631dd03707fdee28f11ae
explorer: https://explorer-studio-dev.genlayer.com/address/0xd8a44cc6D81eeb54A51071F790c242AE03e19157
source SHA-256: 2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af
status: FINALIZED
execution: FINISHED_WITH_RETURN
consensus: MAJORITY_AGREE
```

## Network and runner

```text
chain: 61997
rpc: https://studio-dev.genlayer.com/api
runner: py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng
repository: https://github.com/GIFTEDLOV/agentpact
```

## Validation gates used for deployment

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

The checks above passed before the single deployment. The submitted fee value was `100000000000010352`, equal to the explicit SDK estimate and nonzero. The deployed source was fetched with `gen_getContractCode` and matched the frozen bytes exactly. Never blind-rebroadcast.

## Evidence commitments

`submit_delivery` commits the artifact URL/SHA/byte count and up to three evidence URL/SHA/byte-count triples. All populated URLs must be strict bounded HTTPS values. Evidence slots are contiguous; every empty optional slot has an empty digest and zero byte count; populated evidence URLs are distinct and differ from the artifact URL.

The hardened V1 artifact and evidence limits are both `12,000` bytes. At adjudication, the leader and validator independently fetch every committed body and verify HTTP success, nonempty body, exact byte count, exact lowercase SHA-256, and UTF-8 decoding. Any failure maps all criteria to `UNKNOWN`, `evidence_valid=false`, and `INCONCLUSIVE`.

## Lifecycle proof for the new deployment

The live proof used disposable funded Studio-dev accounts and immutable raw GitHub fixtures. The exact acceptance proof used commit `464868b` with README artifact SHA/bytes `73f443027862400f8ee5e12d25ea5b108c7b971f91a1c7cbe565d8a87366d19b` / `4063` and validation evidence SHA/bytes `a99244a2dcc9c99f0f624c8398576a6006fbebb0a57332fcdb91ca6beb85b26a` / `7390`. The acceptance criterion was `AGENTPACT-HARDENED-RELEASE-PASS`.

Exact accepted transaction chain: create `0xec71479ae77d367f3e91ec152a8388b59ae6cd37bcd3fb771749c4bbddfdc399`, submit `0x8242cb67dcf7ba853d878a29c18d5e97df7237e3fcae6281e5290a33f82081b0`, dispute `0x5d21a93723d3e2c400e0f26585ad24991ba90968a05d972813009cf4e4094355`, adjudicate `0xf3db7dfe28beb6f521c11bc1ea01e00f79dad32cdf73265295018ed644185903` (`pact-4`).

Rejected transaction chain: create `0xbd0086bcf40f69271cf259528f988475d24892439807c24ca0dc38765760572d`, submit `0x747d51e034cd271667e550769c327111487f722bddc2055a29383420fc6e561a`, dispute `0x7374d36d6494593ceb8713600d3b9c1772af9eee412764970be9a2f99928fe81`, adjudicate `0x53b1b984460885fa996d5d5202959eb14720754d7c0565390fa0678c8ccd079f`.

Inconclusive transaction chain: create `0x9a6f1e9fd14d3c2ef7f20ca5647d6ff893c2b11367a9172732f37301fbe8852d`, submit `0x66f7e092de8e7cc2259675b74fb43b89db8b8fe648b2a4e786b800c1819e4ea5`, dispute `0xafafd79cf23015d37c736aced45959715c8298d194f7736dd56a5c79509154cd`, adjudicate `0x70afc6e166012dff20a5fa2326bfdfea8bd79127b15201f7f9abcaa12449cfff`.

Negative checks: unauthorized submission `0xd2c2cc2b87d30ffaa88251c20b216856a25841f3068e09fb707c783423e66064`; terminal re-adjudication `0x50d7811c5fe7100c87fd7d50ada0942856f0f9dedd2517e07050cf32f69ff605`. Both finalized with `FINISHED_WITH_ERROR`.

Mutable-evidence and expiry branches were not needed for this final release proof; all prior lifecycle evidence remains historical and cannot substitute for proof from the new deployment.
