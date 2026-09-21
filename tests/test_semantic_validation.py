import json
import subprocess
import sys
from pathlib import Path


CONTRACT = Path(__file__).parents[1] / "contracts" / "agent_pact.py"
EXPECTED_METHODS = {
    "adjudicate",
    "contract_info",
    "create_commitment",
    "expire_unsubmitted",
    "get_commitment",
    "get_commitment_count",
    "get_commitment_ids",
    "get_status",
    "get_verdict",
    "open_dispute",
    "submit_delivery",
}


def _semantic_snapshot():
    script = r"""
import json
import sys
from pathlib import Path

from genvm_linter.validate.sdk_loader import (
    find_contract_class,
    load_contract_module,
    load_sdk,
)
path = Path(sys.argv[1])
get_schema, _upgrade_notes = load_sdk(path)
module = load_contract_module(path)
selected = find_contract_class(module)
schema = get_schema(selected)
print(json.dumps({
    "selected_is_agentpact": selected is module.AgentPact,
    "agent_init_in_dict": "__init__" in module.AgentPact.__dict__,
    "contract_base_alias_present": hasattr(module, "ContractBase"),
    "direct_sdk_base": (
        module.AgentPact.__bases__ == (module.gl.contract.Contract,)
        and module.AgentPact.__bases__[0].__module__ == "genlayer.contract"
        and module.AgentPact.__bases__[0].__name__ == "Contract"
    ),
    "ok": True,
    "errors": [],
    "schema": schema,
}))
"""
    completed = subprocess.run(
        [sys.executable, "-X", "utf8", "-c", script, str(CONTRACT)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    return json.loads(completed.stdout)


def test_current_sdk_semantic_discovery_targets_agentpact():
    snapshot = _semantic_snapshot()
    assert snapshot["selected_is_agentpact"] is True
    assert snapshot["agent_init_in_dict"] is True
    assert snapshot["contract_base_alias_present"] is False
    assert snapshot["direct_sdk_base"] is True
    assert snapshot["ok"] is True, snapshot["errors"]

    schema = snapshot["schema"]
    assert schema["ctor"]["params"] == []
    assert schema["ctor"]["kwparams"] == {}
    assert set(schema["methods"]) == EXPECTED_METHODS
    assert len(schema["methods"]) == 11
