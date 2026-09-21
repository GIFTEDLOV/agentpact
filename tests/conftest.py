"""Small GenVM import shim for direct tests of pure contract helpers."""

import sys
import types


class _Generic(dict):
    @classmethod
    def __class_getitem__(cls, _item):
        return cls


class _DynArray(list):
    @classmethod
    def __class_getitem__(cls, _item):
        return cls


class _Address(str):
    def __new__(cls, value):
        text = str(value)
        if (
            len(text) != 42
            or text[:2].lower() != "0x"
            or any(character not in "0123456789abcdefABCDEF" for character in text[2:])
        ):
            raise ValueError("invalid address")
        return str.__new__(cls, "0x" + text[2:].lower())


class _Return:
    def __init__(self, calldata):
        self.calldata = calldata


class _Response:
    def __init__(self, status=200, body=b""):
        self.status = status
        self.body = body


def _direct_run_nondet(leader_fn, validator_fn, /, **_kwargs):
    calldata = leader_fn()
    if not validator_fn(_Return(calldata)):
        raise ValueError("direct validator rejected leader result")
    return calldata


def _install_genlayer_stub():
    gl = types.ModuleType("genlayer")
    gl.vm = types.SimpleNamespace(
        UserError=ValueError,
        Result=object,
        Return=_Return,
        run_nondet=_direct_run_nondet,
    )
    gl.contract = types.SimpleNamespace(Contract=object)
    gl.Contract = object
    gl.storage = types.SimpleNamespace(TreeMap=_Generic, DynArray=_DynArray)
    gl.public = types.SimpleNamespace(write=lambda fn: fn, view=lambda fn: fn)
    gl.message_raw = {}
    gl.message = types.SimpleNamespace(
        sender_address="0x" + "0" * 40,
        datetime="2026-01-01T00:00:00+00:00",
    )
    gl.nondet = types.SimpleNamespace(
        web=types.SimpleNamespace(get=lambda _url: _Response()),
        exec_prompt=lambda _prompt, response_format="json": {
            "criterion_results": ["PASS"]
        },
    )
    gl.types = types.ModuleType("genlayer.types")
    gl.types.u8 = int
    gl.types.u64 = int
    gl.types.u256 = int
    gl.types.Address = _Address
    sys.modules.setdefault("genlayer", gl)
    sys.modules.setdefault("genlayer.types", gl.types)


_install_genlayer_stub()
