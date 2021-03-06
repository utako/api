# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/adapter/model/v1beta1/quota.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/adapter/model/v1beta1/quota.proto',
  package='istio.mixer.adapter.model.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n\'mixer/adapter/model/v1beta1/quota.proto\x12!istio.mixer.adapter.model.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\"\x81\x02\n\x0cQuotaRequest\x12Q\n\x06quotas\x18\x01 \x03(\x0b\x32;.istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotasEntryB\x04\xc8\xde\x1f\x00\x1a\x32\n\x0bQuotaParams\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\x12\x13\n\x0b\x62\x65st_effort\x18\x02 \x01(\x08\x1aj\n\x0bQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotaParams:\x02\x38\x01\"\xcf\x02\n\x0bQuotaResult\x12P\n\x06quotas\x18\x01 \x03(\x0b\x32:.istio.mixer.adapter.model.v1beta1.QuotaResult.QuotasEntryB\x04\xc8\xde\x1f\x00\x1a\x87\x01\n\x06Result\x12;\n\x0evalid_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x16\n\x0egranted_amount\x18\x03 \x01(\x03\x12(\n\x06status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xc8\xde\x1f\x00\x1a\x64\n\x0bQuotasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32\x35.istio.mixer.adapter.model.v1beta1.QuotaResult.Result:\x02\x38\x01\x42\x36Z(istio.io/api/mixer/adapter/model/v1beta1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_QUOTAREQUEST_QUOTAPARAMS = _descriptor.Descriptor(
  name='QuotaParams',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotaParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotaParams.amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_effort', full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotaParams.best_effort', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=257,
  serialized_end=307,
)

_QUOTAREQUEST_QUOTASENTRY = _descriptor.Descriptor(
  name='QuotasEntry',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=415,
)

_QUOTAREQUEST = _descriptor.Descriptor(
  name='QuotaRequest',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quotas', full_name='istio.mixer.adapter.model.v1beta1.QuotaRequest.quotas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUOTAREQUEST_QUOTAPARAMS, _QUOTAREQUEST_QUOTASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=415,
)


_QUOTARESULT_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid_duration', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.Result.valid_duration', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granted_amount', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.Result.granted_amount', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.Result.status', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=516,
  serialized_end=651,
)

_QUOTARESULT_QUOTASENTRY = _descriptor.Descriptor(
  name='QuotasEntry',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.QuotasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.QuotasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.QuotasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=753,
)

_QUOTARESULT = _descriptor.Descriptor(
  name='QuotaResult',
  full_name='istio.mixer.adapter.model.v1beta1.QuotaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quotas', full_name='istio.mixer.adapter.model.v1beta1.QuotaResult.quotas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUOTARESULT_RESULT, _QUOTARESULT_QUOTASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=753,
)

_QUOTAREQUEST_QUOTAPARAMS.containing_type = _QUOTAREQUEST
_QUOTAREQUEST_QUOTASENTRY.fields_by_name['value'].message_type = _QUOTAREQUEST_QUOTAPARAMS
_QUOTAREQUEST_QUOTASENTRY.containing_type = _QUOTAREQUEST
_QUOTAREQUEST.fields_by_name['quotas'].message_type = _QUOTAREQUEST_QUOTASENTRY
_QUOTARESULT_RESULT.fields_by_name['valid_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_QUOTARESULT_RESULT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_QUOTARESULT_RESULT.containing_type = _QUOTARESULT
_QUOTARESULT_QUOTASENTRY.fields_by_name['value'].message_type = _QUOTARESULT_RESULT
_QUOTARESULT_QUOTASENTRY.containing_type = _QUOTARESULT
_QUOTARESULT.fields_by_name['quotas'].message_type = _QUOTARESULT_QUOTASENTRY
DESCRIPTOR.message_types_by_name['QuotaRequest'] = _QUOTAREQUEST
DESCRIPTOR.message_types_by_name['QuotaResult'] = _QUOTARESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuotaRequest = _reflection.GeneratedProtocolMessageType('QuotaRequest', (_message.Message,), dict(

  QuotaParams = _reflection.GeneratedProtocolMessageType('QuotaParams', (_message.Message,), dict(
    DESCRIPTOR = _QUOTAREQUEST_QUOTAPARAMS,
    __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotaParams)
    ))
  ,

  QuotasEntry = _reflection.GeneratedProtocolMessageType('QuotasEntry', (_message.Message,), dict(
    DESCRIPTOR = _QUOTAREQUEST_QUOTASENTRY,
    __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaRequest.QuotasEntry)
    ))
  ,
  DESCRIPTOR = _QUOTAREQUEST,
  __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaRequest)
  ))
_sym_db.RegisterMessage(QuotaRequest)
_sym_db.RegisterMessage(QuotaRequest.QuotaParams)
_sym_db.RegisterMessage(QuotaRequest.QuotasEntry)

QuotaResult = _reflection.GeneratedProtocolMessageType('QuotaResult', (_message.Message,), dict(

  Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
    DESCRIPTOR = _QUOTARESULT_RESULT,
    __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaResult.Result)
    ))
  ,

  QuotasEntry = _reflection.GeneratedProtocolMessageType('QuotasEntry', (_message.Message,), dict(
    DESCRIPTOR = _QUOTARESULT_QUOTASENTRY,
    __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaResult.QuotasEntry)
    ))
  ,
  DESCRIPTOR = _QUOTARESULT,
  __module__ = 'mixer.adapter.model.v1beta1.quota_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.QuotaResult)
  ))
_sym_db.RegisterMessage(QuotaResult)
_sym_db.RegisterMessage(QuotaResult.Result)
_sym_db.RegisterMessage(QuotaResult.QuotasEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z(istio.io/api/mixer/adapter/model/v1beta1\310\341\036\000\250\342\036\000\360\341\036\000'))
_QUOTAREQUEST_QUOTASENTRY.has_options = True
_QUOTAREQUEST_QUOTASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_QUOTAREQUEST.fields_by_name['quotas'].has_options = True
_QUOTAREQUEST.fields_by_name['quotas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_QUOTARESULT_RESULT.fields_by_name['valid_duration'].has_options = True
_QUOTARESULT_RESULT.fields_by_name['valid_duration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\230\337\037\001'))
_QUOTARESULT_RESULT.fields_by_name['status'].has_options = True
_QUOTARESULT_RESULT.fields_by_name['status']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_QUOTARESULT_QUOTASENTRY.has_options = True
_QUOTARESULT_QUOTASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_QUOTARESULT.fields_by_name['quotas'].has_options = True
_QUOTARESULT.fields_by_name['quotas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
# @@protoc_insertion_point(module_scope)
