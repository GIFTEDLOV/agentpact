# AgentPact release handoff

## Current corrected release coordinates

- Studio-dev chain: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`
- Deployment transaction: `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`
- Deployment status: `FINALIZED`; execution `FINISHED_WITH_RETURN`; consensus `MAJORITY_AGREE`
- Source SHA-256: `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`
- Public repository: https://github.com/GIFTEDLOV/agentpact
- `MAX_EVIDENCE_BYTES`: `12,000`

The former deployment `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` / transaction `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a` with source SHA `f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9` is HISTORICAL only. The earlier deployment `0xdA8781136eB4e59A5216e8891113222C42928a8C` / transaction `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9` is also historical.

## Historical disposable live proof table

The six-branch table below belongs to the historical hardened deployment listed above. Every listed transaction was independently checked through Studio-dev RPC as `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE`. The readback values below are from `get_commitment` after the terminal transaction. Each evidence commitment is shown as `SHA-256/bytes`.

| Branch | Commitment ID | Transaction hashes (create / submit / dispute / adjudicate or expire) | Finalized result | Final status and readback |
|---|---|---|---|---|
| accepted | `pact-1` | create [`0x7d850829321b52e229ebaf324eaf8afb11d23c2ad57aa772a02247639e7101c5`](https://explorer-studio-dev.genlayer.com/tx/0x7d850829321b52e229ebaf324eaf8afb11d23c2ad57aa772a02247639e7101c5); submit [`0xd5bf30460349dc82d04094b0940e8baf76974b2ee251c1628ff759c981c0b209`](https://explorer-studio-dev.genlayer.com/tx/0xd5bf30460349dc82d04094b0940e8baf76974b2ee251c1628ff759c981c0b209); dispute [`0xa52d825f7cb68631ec440a9e06e418832a3aa4465d031af350e753996a86af87`](https://explorer-studio-dev.genlayer.com/tx/0xa52d825f7cb68631ec440a9e06e418832a3aa4465d031af350e753996a86af87); adjudicate [`0x91d427ee44729b187b0294020d8bdb3511944d2f4344096a321cd65b1fccb97c`](https://explorer-studio-dev.genlayer.com/tx/0x91d427ee44729b187b0294020d8bdb3511944d2f4344096a321cd65b1fccb97c) | `MAJORITY_AGREE` | `ACCEPTED`; verdict `ACCEPTED`; `criterion_results=["PASS"]`; score `100`; passed/failed/unknown `1/0/0`; `evidence_valid=true`; artifact `81` bytes / `c64a0d...fd17d1`; evidence e1 `53b25c...0955c/107`, e2 `89fc15...eca31/115`, e3 `44e248...aadb/119`. |
| rejected | `pact-2` | create [`0x672074bc2b0e3ed4db021be40406bc760cf170fedb607f8e8cfec975a8190f21`](https://explorer-studio-dev.genlayer.com/tx/0x672074bc2b0e3ed4db021be40406bc760cf170fedb607f8e8cfec975a8190f21); submit [`0xa096fa9e240f5b4daf9ba876793326858df5a77ef9b6e22e6ec0e5d543d6b585`](https://explorer-studio-dev.genlayer.com/tx/0xa096fa9e240f5b4daf9ba876793326858df5a77ef9b6e22e6ec0e5d543d6b585); dispute [`0xe03854722e199a44c9808fca8477fc6042928099de456ef2417102a87df424df`](https://explorer-studio-dev.genlayer.com/tx/0xe03854722e199a44c9808fca8477fc6042928099de456ef2417102a87df424df); adjudicate [`0x6790577c6c9b478a80f8a4b9b0188f79ba64506c83fa6b64bc5d10814e2a6433`](https://explorer-studio-dev.genlayer.com/tx/0x6790577c6c9b478a80f8a4b9b0188f79ba64506c83fa6b64bc5d10814e2a6433) | `MAJORITY_AGREE` | `REJECTED`; verdict `REJECTED`; `criterion_results=["FAIL"]`; score `0`; passed/failed/unknown `0/1/0`; `evidence_valid=true`; artifact `93` bytes / `c0793418...11c082`; evidence e1 `89fc15...eca31/115`, e2 `53b25c...0955c/107`, e3 `44e248...aadb/119`. |
| artifact mismatch | `pact-3` | create [`0xa70a129b0d823dbb5209e1c69a936859c446aa62b46466d6f70ad34c80837b91`](https://explorer-studio-dev.genlayer.com/tx/0xa70a129b0d823dbb5209e1c69a936859c446aa62b46466d6f70ad34c80837b91); submit [`0xf51e80d5756d18439eb6ff248b12188015ad5c6cf77454972e28bcca3f893b03`](https://explorer-studio-dev.genlayer.com/tx/0xf51e80d5756d18439eb6ff248b12188015ad5c6cf77454972e28bcca3f893b03); dispute [`0x8ae1359816af60e2cd90d3777f879e09f9ae68c9643553f20e032669edd2df4a`](https://explorer-studio-dev.genlayer.com/tx/0x8ae1359816af60e2cd90d3777f879e09f9ae68c9643553f20e032669edd2df4a); adjudicate [`0xfc5178c4c5ca54ef8e6be96bbd4aaa930770f18f2914ed65a281bb196573c04b`](https://explorer-studio-dev.genlayer.com/tx/0xfc5178c4c5ca54ef8e6be96bbd4aaa930770f18f2914ed65a281bb196573c04b) | `MAJORITY_AGREE` | `INCONCLUSIVE`; verdict `INCONCLUSIVE`; `criterion_results=["UNKNOWN"]`; score `0`; passed/failed/unknown `0/0/1`; `evidence_valid=false`; submitted artifact digest deliberately `c64a0d...fd17d1` while served artifact was `108` bytes / SHA `39f7d765...9a7b3c`; evidence e1 `44e248...aadb/119`, e2 `53b25c...0955c/107`, e3 `89fc15...eca31/115`. |
| evidence unavailable | `pact-4` | create [`0xf6283604f77116327bb145f9599db9ebc778f81e5da4b58297f1507296ac8cc4`](https://explorer-studio-dev.genlayer.com/tx/0xf6283604f77116327bb145f9599db9ebc778f81e5da4b58297f1507296ac8cc4); submit [`0x0b0dc96996722dde4ac3e26ae7308da769273f12f3b3b2f18c691218eb8eedfd`](https://explorer-studio-dev.genlayer.com/tx/0x0b0dc96996722dde4ac3e26ae7308da769273f12f3b3b2f18c691218eb8eedfd); dispute [`0x26998bd4df5eb4279e5f6c1049929097fe23ca8b1e8b510d907fc0fc4694e6c6`](https://explorer-studio-dev.genlayer.com/tx/0x26998bd4df5eb4279e5f6c1049929097fe23ca8b1e8b510d907fc0fc4694e6c6); adjudicate [`0x7369c33ae3b877f14308cea795cdadce4cafd6cedea711b34fd365d6a2359269`](https://explorer-studio-dev.genlayer.com/tx/0x7369c33ae3b877f14308cea795cdadce4cafd6cedea711b34fd365d6a2359269) | `MAJORITY_AGREE` | `INCONCLUSIVE`; verdict `INCONCLUSIVE`; `criterion_results=["UNKNOWN"]`; score `0`; passed/failed/unknown `0/0/1`; `evidence_valid=false`; e1 was HTTP 404 `.../fixtures/mutable/missing.txt`, committed as `53b25c...0955c/107`; e2 `53b25c...0955c/107`; e3 `89fc15...eca31/115`. |
| mutable evidence attack | `pact-5` | create [`0x25dcd238ec26f413d254319fd5418f064a839f0baaa13835ea8964fad6155259`](https://explorer-studio-dev.genlayer.com/tx/0x25dcd238ec26f413d254319fd5418f064a839f0baaa13835ea8964fad6155259); submit [`0xee701fe0eee618a76f63c3c1a3be0a10dd4c7fb7de4c61b888830edfd5eb48ad`](https://explorer-studio-dev.genlayer.com/tx/0xee701fe0eee618a76f63c3c1a3be0a10dd4c7fb7de4c61b888830edfd5eb48ad); dispute [`0xb716b19238b2e9c4932a6d090fd8254256e54723f4ac686a3a2f106774810e7c`](https://explorer-studio-dev.genlayer.com/tx/0xb716b19238b2e9c4932a6d090fd8254256e54723f4ac686a3a2f106774810e7c); adjudicate [`0x605b8bc9b11c9dbe6d1d29977263629f4afa1d21d88550fd26270b25c30d2704`](https://explorer-studio-dev.genlayer.com/tx/0x605b8bc9b11c9dbe6d1d29977263629f4afa1d21d88550fd26270b25c30d2704) | `MAJORITY_AGREE` | `INCONCLUSIVE`; verdict `INCONCLUSIVE`; `criterion_results=["UNKNOWN"]`; score `0`; passed/failed/unknown `0/0/1`; `evidence_valid=false`; e1 was committed V1 `97` bytes / `d39983...e0e8`, then same public URL served V2 `102` bytes / `b5fcff...e82af`; e2 `53b25c...0955c/107`; e3 `89fc15...eca31/115`. |
| expired | `pact-6` | create [`0xbcf7234e1e8152824bd38921f8545390704f948689d73707d3eca6ae8bcfc619`](https://explorer-studio-dev.genlayer.com/tx/0xbcf7234e1e8152824bd38921f8545390704f948689d73707d3eca6ae8bcfc619); expire [`0x79a9adfa450b62cb8a9ee3f6136a6bf04e81282d73fecce0451c6f4ad8298d77`](https://explorer-studio-dev.genlayer.com/tx/0x79a9adfa450b62cb8a9ee3f6136a6bf04e81282d73fecce0451c6f4ad8298d77) | `MAJORITY_AGREE` | `EXPIRED`; no delivery; artifact URL/SHA empty, artifact bytes `0`, evidence URLs/SHA/bytes empty/zero, deadline `1789594510` passed before expiry, `resolved_at=0`. |

Exact fixture readback values referenced by the table:

- Accepted artifact: `81` bytes, SHA-256 `c64a0d022f3c0159af763ca39483752b950545cdc21cd4d32656ae4abbfd17d1`.
- Rejected artifact: `93` bytes, SHA-256 `c0793418d007e4baf10c55313f8b3bfe50e0a333424b17427f2f5c9a1e11c082`.
- Artifact-mismatch served artifact: `108` bytes, SHA-256 `39f7d765b31c529574367cba7a063ded0530eeeec1eb2a851b754f16d29a7b3c`; the submitted digest was deliberately the accepted digest above.
- Accepted evidence fixture: `107` bytes, SHA-256 `53b25c14405091d63c27db23cd5045015fd6845b7ba3bee3ff834c985580955c`.
- Rejected evidence fixture: `115` bytes, SHA-256 `89fc15b0fb14294e15cfd5d114ff3e1c362c49b21b956b7d81c300ef252eca31`.
- Inconclusive evidence fixture: `119` bytes, SHA-256 `44e24886aab7bf6dc858d75f3bbccb2e132286c980a20be8a4af125e7f29aadb`.
- Mutable evidence V1 at commitment: `97` bytes, SHA-256 `d39983d451b7fcf63e2e3d9fa4a7a3542682d9c30b26d607991171469d29e0e8`; mutated V2 served from the same URL: `102` bytes, SHA-256 `b5fcfff9ba609b42870474e226aaab6472919fb3968e0fb2ea659ef7e55e82af`.
- Evidence-failure URL `https://raw.githubusercontent.com/GIFTEDLOV/agentpact/main/fixtures/mutable/missing.txt` returned HTTP `404`, so no body was semantically used.

The disposable requester/provider/reader accounts were `0x61f10cc252ed98ce7596c73fc557cca4cc600c82`, `0x8c896e5a32885f162d938c2bca80604c4d59e481`, and `0x0291e33706b7cae6ad332a28f66e7f3e6f634d58`. No private key or token is committed.

## Security result

Supporting evidence is cryptographically committed with SHA-256 and exact byte count. URLs are transport locations only. Non-200, missing-body, invalid-UTF-8, wrong-SHA, wrong-byte-count, and post-submission mutation cases all fail closed to `INCONCLUSIVE`; valid exact bytes still permit normal semantic `ACCEPTED`/`REJECTED` evaluation. Terminal commitments cannot be adjudicated again, expired commitments cannot be adjudicated, and unauthorized adjudication is rejected.

## Corrected release validation gate

- GenVM linter: `0.11.1-rc.2`; GenVM artifact: `v0.6.0-rc5`; py-genlayer runner: `5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng`.
- Direct and semantic regression tests: `21 passed`.
- AST lint: `Lint passed (3 checks)`; semantic validation, combined check, and schema extraction passed with contract `AgentPact`, constructor params `0`, and `11` public methods.
- Typecheck: `0 error(s), 0 warning(s)`.
- Python compilation and `git diff --check`: passed.
- Schema preflight: HTTP 200; live schema matched exactly; `gen_getContractCode` returned `24,344` nonempty bytes.
- Deployment receipt: `FINALIZED`, `FINISHED_WITH_RETURN`, `MAJORITY_AGREE`; leader execution `SUCCESS`.
- On-chain source SHA: `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`, exactly matching the repository source.
- `contract_info()`: `AgentPact`, version `0.1.0`, purpose `evidence-backed commitment adjudication`, with the seven documented statuses.

## Corrected deployment lifecycle proof

The corrected deployment lifecycle used create `0x9ffeeb241c1b768d6e95c247c8da21e437b41cf22e446311d503acf9f1623378`, submit `0x8e74c76df2e1e9c99020977a75a14be10e5b54edc24033388e9599922d8cc52b`, dispute `0xbf9f6a789f70d00eef253f44d31a0dab41a1f792c16dfab27f26a377ac00e106`, and adjudicate `0xc606bec2752a6a0f546733321878dd542a0163456217d1a448e87d9e3183e50d`. All four were verified as `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE`; readback was `ACCEPTED`, score `100`, and `evidence_valid=true`.

## Semantic-validator E106 remediation

`AgentPact` always declared `__init__(self)`. A module-level `ContractBase` compatibility alias could be discovered before `AgentPact`, causing current semantic discovery to select `genlayer.contract.Contract`; schema extraction then inspected the SDK base class and reported `__init__ is absent`. The alias was removed and `AgentPact` now directly inherits from `gl.contract.Contract`. Current SDK semantic validation and schema extraction select `AgentPact` and pass, and the exact corrected source was redeployed with a matching on-chain source SHA.

The public source, fixtures, validation record, runbook, and this handoff are published at https://github.com/GIFTEDLOV/agentpact.
