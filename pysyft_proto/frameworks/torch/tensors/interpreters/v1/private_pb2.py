# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pysyft_proto/frameworks/torch/tensors/interpreters/v1/private.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pysyft_proto.generic.v1 import tensor_pb2 as pysyft__proto_dot_generic_dot_v1_dot_tensor__pb2
from pysyft_proto.types.syft.v1 import id_pb2 as pysyft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pysyft_proto/frameworks/torch/tensors/interpreters/v1/private.proto',
  package='pysyft_proto.frameworks.torch.tensors.interpreters.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCpysyft_proto/frameworks/torch/tensors/interpreters/v1/private.proto\x12\x35pysyft_proto.frameworks.torch.tensors.interpreters.v1\x1a$pysyft_proto/generic/v1/tensor.proto\x1a#pysyft_proto/types/syft/v1/id.proto\"\xd1\x01\n\rPrivateTensor\x12.\n\x02id\x18\x01 \x01(\x0b\x32\x1e.pysyft_proto.types.syft.v1.IdR\x02id\x12#\n\rallowed_users\x18\x02 \x03(\tR\x0c\x61llowedUsers\x12\x35\n\x05\x63hain\x18\x03 \x01(\x0b\x32\x1f.pysyft_proto.generic.v1.TensorR\x05\x63hain\x12\x12\n\x04tags\x18\x07 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scriptionb\x06proto3')
  ,
  dependencies=[pysyft__proto_dot_generic_dot_v1_dot_tensor__pb2.DESCRIPTOR,pysyft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,])




_PRIVATETENSOR = _descriptor.Descriptor(
  name='PrivateTensor',
  full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowed_users', full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor.allowed_users', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='allowedUsers', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain', full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor.chain', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chain', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor.tags', index=3,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor.description', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=411,
)

_PRIVATETENSOR.fields_by_name['id'].message_type = pysyft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_PRIVATETENSOR.fields_by_name['chain'].message_type = pysyft__proto_dot_generic_dot_v1_dot_tensor__pb2._TENSOR
DESCRIPTOR.message_types_by_name['PrivateTensor'] = _PRIVATETENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrivateTensor = _reflection.GeneratedProtocolMessageType('PrivateTensor', (_message.Message,), {
  'DESCRIPTOR' : _PRIVATETENSOR,
  '__module__' : 'pysyft_proto.frameworks.torch.tensors.interpreters.v1.private_pb2'
  # @@protoc_insertion_point(class_scope:pysyft_proto.frameworks.torch.tensors.interpreters.v1.PrivateTensor)
  })
_sym_db.RegisterMessage(PrivateTensor)


# @@protoc_insertion_point(module_scope)