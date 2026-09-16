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
    pass


def _install_genlayer_stub():
    gl = types.ModuleType("genlayer")
    gl.vm = types.SimpleNamespace(UserError=ValueError, Result=object, Return=object)
    gl.contract = types.SimpleNamespace(Contract=object)
    gl.Contract = object
    gl.storage = types.SimpleNamespace(TreeMap=_Generic, DynArray=_DynArray)
    gl.public = types.SimpleNamespace(write=lambda fn: fn, view=lambda fn: fn)
    gl.message_raw = {}
    gl.message = types.SimpleNamespace(sender_address="0x" + "0" * 40)
    gl.nondet = types.SimpleNamespace()
    gl.types = types.ModuleType("genlayer.types")
    gl.types.u8 = int
    gl.types.u64 = int
    gl.types.u256 = int
    gl.types.Address = _Address
    sys.modules.setdefault("genlayer", gl)
    sys.modules.setdefault("genlayer.types", gl.types)


_install_genlayer_stub()

