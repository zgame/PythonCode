# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd_dfmj.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd_dfmj.proto',
  package='',
  serialized_pb='\n\x0e\x63md_dfmj.proto\"<\n\x13\x63md_c_maingamestart\x12\x11\n\tbet_score\x18\x01 \x01(\x01\x12\x12\n\nline_count\x18\x02 \x01(\r\"D\n\x0btaglineinfo\x12\x0f\n\x07line_id\x18\x01 \x01(\x05\x12\x12\n\nicon_index\x18\x02 \x03(\x05\x12\x10\n\x08multiple\x18\x03 \x01(\x05\"\xcb\x01\n\x14\x63md_s_maingameresult\x12\x11\n\tbet_score\x18\x01 \x01(\x01\x12\x12\n\nline_count\x18\x02 \x01(\r\x12\x11\n\twin_score\x18\x03 \x01(\x01\x12\x13\n\x0bresult_type\x18\x04 \x01(\x05\x12\x18\n\x10\x62onus_game_count\x18\x05 \x01(\r\x12\x13\n\x0bresult_icon\x18\x06 \x03(\x05\x12!\n\x0bresult_line\x18\x07 \x03(\x0b\x32\x0c.taglineinfo\x12\x12\n\nerror_code\x18\x08 \x01(\x05\"\x15\n\x13\x63md_c_marygamestart\"j\n\x12tag_marygameresult\x12\x11\n\twin_score\x18\x01 \x01(\x01\x12\x17\n\x0f\x63urr_game_count\x18\x02 \x01(\r\x12\x13\n\x0b\x63\x65nter_icon\x18\x03 \x03(\x05\x12\x13\n\x0bresult_icon\x18\x04 \x01(\x05\"T\n\x14\x63md_s_marygameresult\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12(\n\x0bmary_result\x18\x02 \x03(\x0b\x32\x13.tag_marygameresultB\x02H\x03')




_CMD_C_MAINGAMESTART = _descriptor.Descriptor(
  name='cmd_c_maingamestart',
  full_name='cmd_c_maingamestart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='cmd_c_maingamestart.bet_score', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='cmd_c_maingamestart.line_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=18,
  serialized_end=78,
)


_TAGLINEINFO = _descriptor.Descriptor(
  name='taglineinfo',
  full_name='taglineinfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_id', full_name='taglineinfo.line_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon_index', full_name='taglineinfo.icon_index', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='taglineinfo.multiple', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=80,
  serialized_end=148,
)


_CMD_S_MAINGAMERESULT = _descriptor.Descriptor(
  name='cmd_s_maingameresult',
  full_name='cmd_s_maingameresult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='cmd_s_maingameresult.bet_score', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='cmd_s_maingameresult.line_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_score', full_name='cmd_s_maingameresult.win_score', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_type', full_name='cmd_s_maingameresult.result_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bonus_game_count', full_name='cmd_s_maingameresult.bonus_game_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_icon', full_name='cmd_s_maingameresult.result_icon', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_line', full_name='cmd_s_maingameresult.result_line', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='cmd_s_maingameresult.error_code', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=151,
  serialized_end=354,
)


_CMD_C_MARYGAMESTART = _descriptor.Descriptor(
  name='cmd_c_marygamestart',
  full_name='cmd_c_marygamestart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=356,
  serialized_end=377,
)


_TAG_MARYGAMERESULT = _descriptor.Descriptor(
  name='tag_marygameresult',
  full_name='tag_marygameresult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='win_score', full_name='tag_marygameresult.win_score', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curr_game_count', full_name='tag_marygameresult.curr_game_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center_icon', full_name='tag_marygameresult.center_icon', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_icon', full_name='tag_marygameresult.result_icon', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=379,
  serialized_end=485,
)


_CMD_S_MARYGAMERESULT = _descriptor.Descriptor(
  name='cmd_s_marygameresult',
  full_name='cmd_s_marygameresult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='cmd_s_marygameresult.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mary_result', full_name='cmd_s_marygameresult.mary_result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=487,
  serialized_end=571,
)

_CMD_S_MAINGAMERESULT.fields_by_name['result_line'].message_type = _TAGLINEINFO
_CMD_S_MARYGAMERESULT.fields_by_name['mary_result'].message_type = _TAG_MARYGAMERESULT
DESCRIPTOR.message_types_by_name['cmd_c_maingamestart'] = _CMD_C_MAINGAMESTART
DESCRIPTOR.message_types_by_name['taglineinfo'] = _TAGLINEINFO
DESCRIPTOR.message_types_by_name['cmd_s_maingameresult'] = _CMD_S_MAINGAMERESULT
DESCRIPTOR.message_types_by_name['cmd_c_marygamestart'] = _CMD_C_MARYGAMESTART
DESCRIPTOR.message_types_by_name['tag_marygameresult'] = _TAG_MARYGAMERESULT
DESCRIPTOR.message_types_by_name['cmd_s_marygameresult'] = _CMD_S_MARYGAMERESULT

class cmd_c_maingamestart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_MAINGAMESTART

  # @@protoc_insertion_point(class_scope:cmd_c_maingamestart)

class taglineinfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGLINEINFO

  # @@protoc_insertion_point(class_scope:taglineinfo)

class cmd_s_maingameresult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_MAINGAMERESULT

  # @@protoc_insertion_point(class_scope:cmd_s_maingameresult)

class cmd_c_marygamestart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_MARYGAMESTART

  # @@protoc_insertion_point(class_scope:cmd_c_marygamestart)

class tag_marygameresult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAG_MARYGAMERESULT

  # @@protoc_insertion_point(class_scope:tag_marygameresult)

class cmd_s_marygameresult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_MARYGAMERESULT

  # @@protoc_insertion_point(class_scope:cmd_s_marygameresult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
