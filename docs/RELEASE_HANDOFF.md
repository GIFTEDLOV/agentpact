# AgentPact release handoff

## Canonical release coordinates

- Studio-dev chain: `61997`
- RPC: `https://studio-dev.genlayer.com/api`
- Contract: [`0xdA8781136eB4e59A5216e8891113222C42928a8C`](https://explorer-studio-dev.genlayer.com/address/0xdA8781136eB4e59A5216e8891113222C42928a8C)
- Deployment transaction: [`0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9`](https://explorer-studio-dev.genlayer.com/tx/0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9)
- Source SHA-256: `c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595`
- Public repository: https://github.com/GIFTEDLOV/agentpact

## Four disposable live proofs

The table below is the release gate. Every row must contain the exact commitment ID, all lifecycle transaction hashes, finalized result, and readback values from Studio-dev. Fixture URL, served byte count, and served SHA are recorded with the row.

| Branch | Commitment ID | Transaction hashes (create / submit / dispute / adjudicate or expire) | Finalized result | Final status and readback |
|---|---|---|---|---|
| accepted | `pact-1` | create [`0xf1998a54ca69cf333056612cc99876fd59a52750aea5495bf8fa47ecbf313732`](https://explorer-studio-dev.genlayer.com/tx/0xf1998a54ca69cf333056612cc99876fd59a52750aea5495bf8fa47ecbf313732); submit [`0x352e8694a58cf8eb328d981cdcc6d3d752fab7c965d7629bb3b4b18408dc2df3`](https://explorer-studio-dev.genlayer.com/tx/0x352e8694a58cf8eb328d981cdcc6d3d752fab7c965d7629bb3b4b18408dc2df3); dispute [`0x079b2a1c5f565bfb3ea5e812d031187911f92394fd2b06dba16eab552cdabee7`](https://explorer-studio-dev.genlayer.com/tx/0x079b2a1c5f565bfb3ea5e812d031187911f92394fd2b06dba16eab552cdabee7); adjudicate [`0xeeb0bb4d212168e5921fbcc3c88a9454385612d1ffc7529ac4259a264401b8fe`](https://explorer-studio-dev.genlayer.com/tx/0xeeb0bb4d212168e5921fbcc3c88a9454385612d1ffc7529ac4259a264401b8fe) | all `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE` | `ACCEPTED`; `criterion_results=["PASS"]`, score `100`, passed `1`, failed `0`, unknown `0`, `evidence_valid=true`; served artifact `81` bytes, SHA-256 `c64a0d022f3c0159af763ca39483752b950545cdc21cd4d32656ae4abbfd17d1`; [artifact](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/accepted/artifact.txt) and [evidence](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/accepted/evidence.txt) HTTP 200 |
| rejected | `pact-2` | create [`0xb1d6e6a3cd35b958ef31a48d7694f699b2c351f278ed36553f2d0ab4515b0d76`](https://explorer-studio-dev.genlayer.com/tx/0xb1d6e6a3cd35b958ef31a48d7694f699b2c351f278ed36553f2d0ab4515b0d76); submit [`0xcf1e94f0396d1e4a33d521c9f6003720504b2a90b4919b17ee668094733a572c`](https://explorer-studio-dev.genlayer.com/tx/0xcf1e94f0396d1e4a33d521c9f6003720504b2a90b4919b17ee668094733a572c); dispute [`0x02654d83b1e356d90b00b503bc726ba28ac43f98ef63aec2187dab8ab7c7084b`](https://explorer-studio-dev.genlayer.com/tx/0x02654d83b1e356d90b00b503bc726ba28ac43f98ef63aec2187dab8ab7c7084b); adjudicate [`0x3fbe486e411ac1a3b340d95ac767d52842ab107440311d0c033db13a91c1e748`](https://explorer-studio-dev.genlayer.com/tx/0x3fbe486e411ac1a3b340d95ac767d52842ab107440311d0c033db13a91c1e748) | all `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE` | `REJECTED`; `criterion_results=["FAIL"]`, score `0`, passed `0`, failed `1`, unknown `0`, `evidence_valid=true`; served artifact `93` bytes, SHA-256 `c0793418d007e4baf10c55313f8b3bfe50e0a333424b17427f2f5c9a1e11c082`; [artifact](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/rejected/artifact.txt) and [evidence](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/rejected/evidence.txt) HTTP 200 |
| inconclusive | `pact-3` | create [`0x8d88398f7108e70c7c77f8de81d05e4009eb2fc739eaad2f08244556919709b2`](https://explorer-studio-dev.genlayer.com/tx/0x8d88398f7108e70c7c77f8de81d05e4009eb2fc739eaad2f08244556919709b2); submit [`0xf1506e92ce688e931a00fbbb8ffd1331e414fe230f12f09dd7817d9ec24aef0c`](https://explorer-studio-dev.genlayer.com/tx/0xf1506e92ce688e931a00fbbb8ffd1331e414fe230f12f09dd7817d9ec24aef0c); dispute [`0xea3f1adea926825dd8e47dcc6788c45c0bf8287006087d3223cf813a47c3e040`](https://explorer-studio-dev.genlayer.com/tx/0xea3f1adea926825dd8e47dcc6788c45c0bf8287006087d3223cf813a47c3e040); adjudicate [`0x1f7b453c74c84dd3ad8d02d33dd3100561141a63ec6134691681f482daaac0bf`](https://explorer-studio-dev.genlayer.com/tx/0x1f7b453c74c84dd3ad8d02d33dd3100561141a63ec6134691681f482daaac0bf) | all `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE` | `INCONCLUSIVE`; `criterion_results=["UNKNOWN"]`, score `0`, passed `0`, failed `0`, unknown `1`, `evidence_valid=false`; submitted digest `c64a0d022f3c0159af763ca39483752b950545cdc21cd4d32656ae4abbfd17d1` deliberately mismatched served 108-byte artifact SHA-256 `39f7d765b31c529574367cba7a063ded0530eeeec1eb2a851b754f16d29a7b3c`; [artifact](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/inconclusive/artifact.txt) and [evidence](https://raw.githubusercontent.com/GIFTEDLOV/agentpact/89bada7d20813b0e071e3a038f318efe1e2207d2/fixtures/inconclusive/evidence.txt) HTTP 200 |
| expired | `pact-4` | create [`0xd237c47b585862062bc244aafa7c89ba681b6066de7d95d330b11f979aa7912a`](https://explorer-studio-dev.genlayer.com/tx/0xd237c47b585862062bc244aafa7c89ba681b6066de7d95d330b11f979aa7912a); expire [`0xc4e3297ca31014cb03b72c6cea97f4371a971c02d5dd277c023a1d62d22c0f54`](https://explorer-studio-dev.genlayer.com/tx/0xc4e3297ca31014cb03b72c6cea97f4371a971c02d5dd277c023a1d62d22c0f54) | both `FINALIZED / FINISHED_WITH_RETURN / MAJORITY_AGREE` | `EXPIRED`; no delivery, `artifact_url=""`, `artifact_bytes=0`, `resolved_at=0`, exact deadline `1789588801` passed before expiry |

The disposable requester/provider/reader accounts used for these proofs were `0x61f10cc252ed98ce7596c73fc557cca4cc600c82`, `0x8c896e5a32885f162d938c2bca80604c4d59e481`, and `0x0291e33706b7cae6ad332a28f66e7f3e6f634d58`. No private key is included in the repository.

## Validation gate

## Final independent audit

- Direct tests: `6 passed`.
- GenVM lint: `✓ Lint passed (3 checks)` with `GENVM_VERSION=v0.2.16`.
- Python compilation: passed.
- `git diff --check`: passed.
- `gen_getContractSchemaForCode`: HTTP 200, exact 11-method schema before deployment.
- Live `gen_getContractSchema`: exact same 11-method schema after deployment.
- `gen_getContractCode`: fetched source SHA exactly `c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595`.
- Public GitHub repository: https://github.com/GIFTEDLOV/agentpact.

See [`VALIDATION.md`](VALIDATION.md) for the exact commands and deployed schema. The proof table above contains no placeholders; every listed transaction and fixture URL was independently checked through public/Studio interfaces.
