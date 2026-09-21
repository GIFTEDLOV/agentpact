# AgentPact hardened release handoff

The hardened AgentPact source is deployed and live on Studio-dev. Both previous deployments remain historical:

- `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` — older rejected deployment.
- `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46` — corrected deployment, now historical; transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`.

The hardened source directly inherits `gl.contract.Contract`, keeps a zero-parameter constructor and the existing 11-method ABI, bounds all external text by UTF-8 bytes, strictly validates HTTPS URLs and SHA-256 commitments, rejects zero providers, evaluates the entire committed artifact up to `12,000` bytes, and fails closed on invalid evidence or model/consensus output.

The source uses only `gl.message.datetime` for transaction time. It does not use local wall-clock calls. The validator independently retrieves, verifies, evaluates, validates exact output shape, and compares the complete consensus result with the leader.

Live release identity:

- Contract: `0xd8a44cc6D81eeb54A51071F790c242AE03e19157`.
- Deployment transaction: `0x338f0cccd6077a04be92ded0aabc80ac4584cfbf3f1631dd03707fdee28f11ae`.
- Explorer: `https://explorer-studio-dev.genlayer.com/address/0xd8a44cc6D81eeb54A51071F790c242AE03e19157`.
- Source SHA-256: `2775e9d26a664601616e3a59a89b876cb1de444758dc8479ca71a8794509c0af`.
- Status: `FINALIZED`, `FINISHED_WITH_RETURN`, `MAJORITY_AGREE`.

The live schema is zero-constructor/11-method, `contract_info()` reports the hardened 12,000-byte artifact limit, and accepted, rejected, inconclusive, unauthorized, and terminal-reentry proofs are recorded in the release handoff and validation documents.
