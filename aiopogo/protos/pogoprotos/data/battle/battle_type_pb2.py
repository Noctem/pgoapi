# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_type.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/data/battle/battle_type.proto\x12\x16pogoprotos.data.battle*U\n\nBattleType\x12\x15\n\x11\x42\x41TTLE_TYPE_UNSET\x10\x00\x12\x16\n\x12\x42\x41TTLE_TYPE_NORMAL\x10\x01\x12\x18\n\x14\x42\x41TTLE_TYPE_TRAINING\x10\x02\x62\x06proto3')
)

_BATTLETYPE = _descriptor.EnumDescriptor(
  name='BattleType',
  full_name='pogoprotos.data.battle.BattleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATTLE_TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLE_TYPE_NORMAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLE_TYPE_TRAINING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=68,
  serialized_end=153,
)
_sym_db.RegisterEnumDescriptor(_BATTLETYPE)

BattleType = enum_type_wrapper.EnumTypeWrapper(_BATTLETYPE)
BATTLE_TYPE_UNSET = 0
BATTLE_TYPE_NORMAL = 1
BATTLE_TYPE_TRAINING = 2


DESCRIPTOR.enum_types_by_name['BattleType'] = _BATTLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
