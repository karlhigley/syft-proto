# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/types/torch/v1/parameter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.types.torch.v1 import tensor_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/types/torch/v1/parameter.proto',
  package='syft_proto.types.torch.v1',
  syntax='proto3',
  serialized_options=b'\n&org.openmined.syftproto.types.torch.v1',
  serialized_pb=b'\n)syft_proto/types/torch/v1/parameter.proto\x12\x19syft_proto.types.torch.v1\x1a!syft_proto/types/syft/v1/id.proto\x1a&syft_proto/types/torch/v1/tensor.proto\"\xda\x01\n\tParameter\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12>\n\x06tensor\x18\x02 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\x06tensor\x12#\n\rrequires_grad\x18\x03 \x01(\x08R\x0crequiresGrad\x12:\n\x04grad\x18\x04 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\x04gradB(\n&org.openmined.syftproto.types.torch.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2.DESCRIPTOR,])




_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='syft_proto.types.torch.v1.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.types.torch.v1.Parameter.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='syft_proto.types.torch.v1.Parameter.tensor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tensor', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requires_grad', full_name='syft_proto.types.torch.v1.Parameter.requires_grad', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='requiresGrad', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grad', full_name='syft_proto.types.torch.v1.Parameter.grad', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='grad', file=DESCRIPTOR),
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
  serialized_start=148,
  serialized_end=366,
)

_PARAMETER.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_PARAMETER.fields_by_name['tensor'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
_PARAMETER.fields_by_name['grad'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETER,
  '__module__' : 'syft_proto.types.torch.v1.parameter_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.types.torch.v1.Parameter)
  })
_sym_db.RegisterMessage(Parameter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
