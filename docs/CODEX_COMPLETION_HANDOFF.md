# Codex completion handoff

AgentPact was recovered and audited from the finalized Studio-dev deployment transaction because the requested scratch path was not mounted in the active workspace. Hosted validation then exposed two real GenVM compatibility defects (`gl.message_raw` and `gl.vm.run_nondet_unsafe`); the minimal fixes were applied, validated, and deployed once per changed source revision. The final deployed source was fetched back from Studio-dev and matched locally byte-for-byte.

Canonical release coordinates:

- Chain `61997`
- RPC `https://studio-dev.genlayer.com/api`
- Contract `0xdA8781136eB4e59A5216e8891113222C42928a8C`
- Deployment transaction `0xfb84525500c58217ddf393a9bcacf2c6becf83ad824e7ad7276e9dfb2c8ebaf9`
- Source SHA-256 `c95c986fa8de44b9f541f58539cbd59787afd596acf774c7bccc6feef9a27595`
- Repository `https://github.com/GIFTEDLOV/agentpact`

See `docs/RELEASE_HANDOFF.md` for the final four-branch proof table and validation results.
