# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/plat_eight_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/plat_eight_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/platform/responses/plat_eight_response.proto\x12(pogoprotos.networking.platform.responses\"$\n\x11PlatEightResponse\x12\x0f\n\x07message\x18\x02 \x01(\tb\x06proto3')
)




_PLATEIGHTRESPONSE = _descriptor.Descriptor(
  name='PlatEightResponse',
  full_name='pogoprotos.networking.platform.responses.PlatEightResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pogoprotos.networking.platform.responses.PlatEightResponse.message', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['PlatEightResponse'] = _PLATEIGHTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatEightResponse = _reflection.GeneratedProtocolMessageType('PlatEightResponse', (_message.Message,), dict(
  DESCRIPTOR = _PLATEIGHTRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.plat_eight_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.PlatEightResponse)
  ))
_sym_db.RegisterMessage(PlatEightResponse)


# @@protoc_insertion_point(module_scope)
