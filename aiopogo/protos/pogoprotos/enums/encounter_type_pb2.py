# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/encounter_type.proto

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
  name='pogoprotos/enums/encounter_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n%pogoprotos/enums/encounter_type.proto\x12\x10pogoprotos.enums*7\n\rEncounterType\x12\x0f\n\x0bSPAWN_POINT\x10\x00\x12\x0b\n\x07INCENSE\x10\x01\x12\x08\n\x04\x44ISK\x10\x02\x62\x06proto3')
)

_ENCOUNTERTYPE = _descriptor.EnumDescriptor(
  name='EncounterType',
  full_name='pogoprotos.enums.EncounterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAWN_POINT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=59,
  serialized_end=114,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERTYPE)

EncounterType = enum_type_wrapper.EnumTypeWrapper(_ENCOUNTERTYPE)
SPAWN_POINT = 0
INCENSE = 1
DISK = 2


DESCRIPTOR.enum_types_by_name['EncounterType'] = _ENCOUNTERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
