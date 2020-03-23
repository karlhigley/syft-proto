# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/types/syft/v1/arg.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.execution.v1 import placeholder_pb2 as syft__proto_dot_execution_dot_v1_dot_placeholder__pb2
from syft_proto.generic.pointers.v1 import pointer_tensor_pb2 as syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2
from syft_proto.types.torch.v1 import tensor_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2
from syft_proto.types.syft.v1 import shape_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_shape__pb2
from syft_proto.types.torch.v1 import parameter_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/types/syft/v1/arg.proto',
  package='syft_proto.types.syft.v1',
  syntax='proto3',
  serialized_options=b'\n%org.openmined.syftproto.types.syft.v1',
  serialized_pb=b'\n\"syft_proto/types/syft/v1/arg.proto\x12\x18syft_proto.types.syft.v1\x1a)syft_proto/execution/v1/placeholder.proto\x1a\x33syft_proto/generic/pointers/v1/pointer_tensor.proto\x1a&syft_proto/types/torch/v1/tensor.proto\x1a$syft_proto/types/syft/v1/shape.proto\x1a)syft_proto/types/torch/v1/parameter.proto\"\x8d\x04\n\x03\x41rg\x12\x1b\n\x08\x61rg_bool\x18\x01 \x01(\x08H\x00R\x07\x61rgBool\x12\x19\n\x07\x61rg_int\x18\x02 \x01(\x05H\x00R\x06\x61rgInt\x12\x1d\n\targ_float\x18\x03 \x01(\x02H\x00R\x08\x61rgFloat\x12\x1f\n\narg_string\x18\x04 \x01(\tH\x00R\targString\x12>\n\targ_shape\x18\x05 \x01(\x0b\x32\x1f.syft_proto.types.syft.v1.ShapeH\x00R\x08\x61rgShape\x12G\n\narg_tensor\x18\x06 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorH\x00R\targTensor\x12N\n\x0f\x61rg_torch_param\x18\x07 \x01(\x0b\x32$.syft_proto.types.torch.v1.ParameterH\x00R\rargTorchParam\x12]\n\x12\x61rg_pointer_tensor\x18\x08 \x01(\x0b\x32-.syft_proto.generic.pointers.v1.PointerTensorH\x00R\x10\x61rgPointerTensor\x12O\n\x0f\x61rg_placeholder\x18\t \x01(\x0b\x32$.syft_proto.execution.v1.PlaceholderH\x00R\x0e\x61rgPlaceholderB\x05\n\x03\x61rgB\'\n%org.openmined.syftproto.types.syft.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_execution_dot_v1_dot_placeholder__pb2.DESCRIPTOR,syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2.DESCRIPTOR,syft__proto_dot_types_dot_syft_dot_v1_dot_shape__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2.DESCRIPTOR,])




_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='syft_proto.types.syft.v1.Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg_bool', full_name='syft_proto.types.syft.v1.Arg.arg_bool', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argBool', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_int', full_name='syft_proto.types.syft.v1.Arg.arg_int', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argInt', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_float', full_name='syft_proto.types.syft.v1.Arg.arg_float', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argFloat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_string', full_name='syft_proto.types.syft.v1.Arg.arg_string', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argString', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_shape', full_name='syft_proto.types.syft.v1.Arg.arg_shape', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argShape', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_tensor', full_name='syft_proto.types.syft.v1.Arg.arg_tensor', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argTensor', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_torch_param', full_name='syft_proto.types.syft.v1.Arg.arg_torch_param', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argTorchParam', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_pointer_tensor', full_name='syft_proto.types.syft.v1.Arg.arg_pointer_tensor', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argPointerTensor', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg_placeholder', full_name='syft_proto.types.syft.v1.Arg.arg_placeholder', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='argPlaceholder', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='arg', full_name='syft_proto.types.syft.v1.Arg.arg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=282,
  serialized_end=807,
)

_ARG.fields_by_name['arg_shape'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_shape__pb2._SHAPE
_ARG.fields_by_name['arg_tensor'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
_ARG.fields_by_name['arg_torch_param'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2._PARAMETER
_ARG.fields_by_name['arg_pointer_tensor'].message_type = syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2._POINTERTENSOR
_ARG.fields_by_name['arg_placeholder'].message_type = syft__proto_dot_execution_dot_v1_dot_placeholder__pb2._PLACEHOLDER
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_bool'])
_ARG.fields_by_name['arg_bool'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_int'])
_ARG.fields_by_name['arg_int'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_float'])
_ARG.fields_by_name['arg_float'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_string'])
_ARG.fields_by_name['arg_string'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_shape'])
_ARG.fields_by_name['arg_shape'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_tensor'])
_ARG.fields_by_name['arg_tensor'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_torch_param'])
_ARG.fields_by_name['arg_torch_param'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_pointer_tensor'])
_ARG.fields_by_name['arg_pointer_tensor'].containing_oneof = _ARG.oneofs_by_name['arg']
_ARG.oneofs_by_name['arg'].fields.append(
  _ARG.fields_by_name['arg_placeholder'])
_ARG.fields_by_name['arg_placeholder'].containing_oneof = _ARG.oneofs_by_name['arg']
DESCRIPTOR.message_types_by_name['Arg'] = _ARG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), {
  'DESCRIPTOR' : _ARG,
  '__module__' : 'syft_proto.types.syft.v1.arg_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.types.syft.v1.Arg)
  })
_sym_db.RegisterMessage(Arg)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
