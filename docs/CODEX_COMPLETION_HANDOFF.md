# Codex completion handoff

AgentPact’s final hardening is complete on Studio-dev. The source now commits artifact and supporting-evidence SHA-256 digests with exact byte counts, bounds evidence to 12,000 bytes, verifies all committed bytes before semantic evaluation, and maps unavailable or unverifiable evidence to `UNKNOWN` / `INCONCLUSIVE`.

Canonical release coordinates:

- Chain `61997`
- RPC `https://studio-dev.genlayer.com/api`
- Contract `0x7Fef206fe3f14f01f01A1d18774F9Fcd3162FDCF`
- Deployment transaction `0xa32cda206de618c87655a06f11f1c8dc019b5b88262bd367cdade71114c6cb2a`
- Source SHA-256 `f231e6f24cb58c6ca73b3ffa99e33aaf703cf05dd7d6849f0a9e683f09e438a9`
- Repository `https://github.com/GIFTEDLOV/agentpact`

The previous deployment `0xdA8781136eB4e59A5216e8891113222C42928a8C` / `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9` is historical only. See `docs/RELEASE_HANDOFF.md` for the complete six-branch proof table, exact transactions, readbacks, and validation results.
