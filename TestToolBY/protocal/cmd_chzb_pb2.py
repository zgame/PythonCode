# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd_chzb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd_chzb.proto',
  package='',
  serialized_pb='\n\x0e\x63md_chzb.proto\"\x86\x01\n\x10\x63md_game_sitdown\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08table_id\x18\x02 \x01(\x05\x12\x10\n\x08\x63hair_id\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\x05\x12\x0f\n\x07seconds\x18\x05 \x01(\x05\x12\r\n\x05times\x18\x06 \x01(\x05\x12\x0e\n\x06param1\x18\x07 \x01(\x05\"S\n\x0f\x63md_table_state\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\x12\x0f\n\x07seconds\x18\x03 \x01(\x05\x12\x0e\n\x06param1\x18\x04 \x01(\x05\"J\n\x0ftagChipItemInfo\x12\x10\n\x08\x63hip_idx\x18\x01 \x01(\x05\x12\x11\n\tchip_coin\x18\x02 \x01(\x01\x12\x12\n\nchip_award\x18\x03 \x01(\x01\"5\n\rcmd_chip_info\x12$\n\nchip_items\x18\x01 \x03(\x0b\x32\x10.tagChipItemInfo\"E\n\rcmd_user_chip\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x63hip_idx\x18\x02 \x01(\x05\x12\x11\n\tchip_coin\x18\x03 \x01(\x01\"K\n\x12\x63md_user_chip_resp\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12\x10\n\x08\x63hip_idx\x18\x02 \x01(\x05\x12\x11\n\tchip_coin\x18\x03 \x01(\x01\"I\n\x10\x63md_user_chip_ex\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12$\n\nchip_items\x18\x02 \x03(\x0b\x32\x10.tagChipItemInfo\"O\n\x15\x63md_user_chip_resp_ex\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12$\n\nchip_items\x18\x02 \x03(\x0b\x32\x10.tagChipItemInfo\"C\n\x0e\x63md_table_draw\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x10\n\x08\x61ward_id\x18\x02 \x01(\x05\x12\r\n\x05times\x18\x03 \x01(\x05\"F\n\rcmd_user_trad\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12$\n\nchip_items\x18\x02 \x03(\x0b\x32\x10.tagChipItemInfoB\x02H\x03')




_CMD_GAME_SITDOWN = _descriptor.Descriptor(
  name='cmd_game_sitdown',
  full_name='cmd_game_sitdown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_game_sitdown.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='cmd_game_sitdown.table_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chair_id', full_name='cmd_game_sitdown.chair_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='cmd_game_sitdown.state', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='cmd_game_sitdown.seconds', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='cmd_game_sitdown.times', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='cmd_game_sitdown.param1', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=19,
  serialized_end=153,
)


_CMD_TABLE_STATE = _descriptor.Descriptor(
  name='cmd_table_state',
  full_name='cmd_table_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='cmd_table_state.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='cmd_table_state.state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='cmd_table_state.seconds', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='cmd_table_state.param1', index=3,
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
  serialized_start=155,
  serialized_end=238,
)


_TAGCHIPITEMINFO = _descriptor.Descriptor(
  name='tagChipItemInfo',
  full_name='tagChipItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chip_idx', full_name='tagChipItemInfo.chip_idx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_coin', full_name='tagChipItemInfo.chip_coin', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_award', full_name='tagChipItemInfo.chip_award', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=240,
  serialized_end=314,
)


_CMD_CHIP_INFO = _descriptor.Descriptor(
  name='cmd_chip_info',
  full_name='cmd_chip_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chip_items', full_name='cmd_chip_info.chip_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=316,
  serialized_end=369,
)


_CMD_USER_CHIP = _descriptor.Descriptor(
  name='cmd_user_chip',
  full_name='cmd_user_chip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_chip.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_idx', full_name='cmd_user_chip.chip_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_coin', full_name='cmd_user_chip.chip_coin', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=371,
  serialized_end=440,
)


_CMD_USER_CHIP_RESP = _descriptor.Descriptor(
  name='cmd_user_chip_resp',
  full_name='cmd_user_chip_resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='cmd_user_chip_resp.err_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_idx', full_name='cmd_user_chip_resp.chip_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_coin', full_name='cmd_user_chip_resp.chip_coin', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=442,
  serialized_end=517,
)


_CMD_USER_CHIP_EX = _descriptor.Descriptor(
  name='cmd_user_chip_ex',
  full_name='cmd_user_chip_ex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_chip_ex.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_items', full_name='cmd_user_chip_ex.chip_items', index=1,
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
  serialized_start=519,
  serialized_end=592,
)


_CMD_USER_CHIP_RESP_EX = _descriptor.Descriptor(
  name='cmd_user_chip_resp_ex',
  full_name='cmd_user_chip_resp_ex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='cmd_user_chip_resp_ex.err_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_items', full_name='cmd_user_chip_resp_ex.chip_items', index=1,
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
  serialized_start=594,
  serialized_end=673,
)


_CMD_TABLE_DRAW = _descriptor.Descriptor(
  name='cmd_table_draw',
  full_name='cmd_table_draw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='cmd_table_draw.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='award_id', full_name='cmd_table_draw.award_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='cmd_table_draw.times', index=2,
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
  serialized_start=675,
  serialized_end=742,
)


_CMD_USER_TRAD = _descriptor.Descriptor(
  name='cmd_user_trad',
  full_name='cmd_user_trad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_trad.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_items', full_name='cmd_user_trad.chip_items', index=1,
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
  serialized_start=744,
  serialized_end=814,
)

_CMD_CHIP_INFO.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_USER_CHIP_EX.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_USER_CHIP_RESP_EX.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_USER_TRAD.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
DESCRIPTOR.message_types_by_name['cmd_game_sitdown'] = _CMD_GAME_SITDOWN
DESCRIPTOR.message_types_by_name['cmd_table_state'] = _CMD_TABLE_STATE
DESCRIPTOR.message_types_by_name['tagChipItemInfo'] = _TAGCHIPITEMINFO
DESCRIPTOR.message_types_by_name['cmd_chip_info'] = _CMD_CHIP_INFO
DESCRIPTOR.message_types_by_name['cmd_user_chip'] = _CMD_USER_CHIP
DESCRIPTOR.message_types_by_name['cmd_user_chip_resp'] = _CMD_USER_CHIP_RESP
DESCRIPTOR.message_types_by_name['cmd_user_chip_ex'] = _CMD_USER_CHIP_EX
DESCRIPTOR.message_types_by_name['cmd_user_chip_resp_ex'] = _CMD_USER_CHIP_RESP_EX
DESCRIPTOR.message_types_by_name['cmd_table_draw'] = _CMD_TABLE_DRAW
DESCRIPTOR.message_types_by_name['cmd_user_trad'] = _CMD_USER_TRAD

class cmd_game_sitdown(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_GAME_SITDOWN

  # @@protoc_insertion_point(class_scope:cmd_game_sitdown)

class cmd_table_state(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_TABLE_STATE

  # @@protoc_insertion_point(class_scope:cmd_table_state)

class tagChipItemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGCHIPITEMINFO

  # @@protoc_insertion_point(class_scope:tagChipItemInfo)

class cmd_chip_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_CHIP_INFO

  # @@protoc_insertion_point(class_scope:cmd_chip_info)

class cmd_user_chip(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_USER_CHIP

  # @@protoc_insertion_point(class_scope:cmd_user_chip)

class cmd_user_chip_resp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_USER_CHIP_RESP

  # @@protoc_insertion_point(class_scope:cmd_user_chip_resp)

class cmd_user_chip_ex(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_USER_CHIP_EX

  # @@protoc_insertion_point(class_scope:cmd_user_chip_ex)

class cmd_user_chip_resp_ex(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_USER_CHIP_RESP_EX

  # @@protoc_insertion_point(class_scope:cmd_user_chip_resp_ex)

class cmd_table_draw(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_TABLE_DRAW

  # @@protoc_insertion_point(class_scope:cmd_table_draw)

class cmd_user_trad(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_USER_TRAD

  # @@protoc_insertion_point(class_scope:cmd_user_trad)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)