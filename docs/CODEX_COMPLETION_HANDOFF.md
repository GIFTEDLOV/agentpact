# Codex completion handoff

AgentPact’s final hardening is complete on Studio-dev. The source now commits artifact and supporting-evidence SHA-256 digests with exact byte counts, bounds evidence to 12,000 bytes, verifies all committed bytes before semantic evaluation, and maps unavailable or unverifiable evidence to `UNKNOWN` / `INCONCLUSIVE`.

Current corrected release coordinates:

- Chain `61997`
- RPC `https://studio-dev.genlayer.com/api`
- Contract `0xa339d64338cb561c9140fc5D1fd5F6eF010d3d46`
- Deployment transaction `0xf6971beb416d81ce171de96eed9986ee1e546bc473da964bbaa489bdc0d2c54f`
- Source SHA-256 `bcea163d516058011e823cd9db422344eb9d4e3009bf95cbea24bc007834aea8`
- Repository `https://github.com/GIFTEDLOV/agentpact`

The prior deployments `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF` / `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a` and `0xdA8781136eB4e59A5216e8891113222C42928a8C` / `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9` are historical only. See `docs/RELEASE_HANDOFF.md` for the semantic-validator remediation, corrected lifecycle proof, complete historical six-branch table, exact transactions, readbacks, and validation results.
