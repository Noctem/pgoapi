# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/add_fort_modifier_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.responses import fort_details_response_pb2 as pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/add_fort_modifier_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n@pogoprotos/networking/responses/add_fort_modifier_response.proto\x12\x1fpogoprotos.networking.responses\x1a;pogoprotos/networking/responses/fort_details_response.proto\"\xc2\x02\n\x17\x41\x64\x64\x46ortModifierResponse\x12O\n\x06result\x18\x01 \x01(\x0e\x32?.pogoprotos.networking.responses.AddFortModifierResponse.Result\x12J\n\x0c\x66ort_details\x18\x02 \x01(\x0b\x32\x34.pogoprotos.networking.responses.FortDetailsResponse\"\x89\x01\n\x06Result\x12\x11\n\rNO_RESULT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1d\n\x19\x46ORT_ALREADY_HAS_MODIFIER\x10\x02\x12\x10\n\x0cTOO_FAR_AWAY\x10\x03\x12\x18\n\x14NO_ITEM_IN_INVENTORY\x10\x04\x12\x14\n\x10POI_INACCESSIBLE\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2.DESCRIPTOR,])



_ADDFORTMODIFIERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.AddFortModifierResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_RESULT_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORT_ALREADY_HAS_MODIFIER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_FAR_AWAY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ITEM_IN_INVENTORY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_INACCESSIBLE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=348,
  serialized_end=485,
)
_sym_db.RegisterEnumDescriptor(_ADDFORTMODIFIERRESPONSE_RESULT)


_ADDFORTMODIFIERRESPONSE = _descriptor.Descriptor(
  name='AddFortModifierResponse',
  full_name='pogoprotos.networking.responses.AddFortModifierResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.AddFortModifierResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_details', full_name='pogoprotos.networking.responses.AddFortModifierResponse.fort_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADDFORTMODIFIERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=485,
)

_ADDFORTMODIFIERRESPONSE.fields_by_name['result'].enum_type = _ADDFORTMODIFIERRESPONSE_RESULT
_ADDFORTMODIFIERRESPONSE.fields_by_name['fort_details'].message_type = pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2._FORTDETAILSRESPONSE
_ADDFORTMODIFIERRESPONSE_RESULT.containing_type = _ADDFORTMODIFIERRESPONSE
DESCRIPTOR.message_types_by_name['AddFortModifierResponse'] = _ADDFORTMODIFIERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddFortModifierResponse = _reflection.GeneratedProtocolMessageType('AddFortModifierResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDFORTMODIFIERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.add_fort_modifier_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.AddFortModifierResponse)
  ))
_sym_db.RegisterMessage(AddFortModifierResponse)


# @@protoc_insertion_point(module_scope)
