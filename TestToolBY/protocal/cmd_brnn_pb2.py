# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd_brnn.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd_brnn.proto',
  package='',
  serialized_pb='\n\x0e\x63md_brnn.proto\"!\n\x0etagChipHistory\x12\x0f\n\x07history\x18\x01 \x03(\x05\"\xc2\x01\n\x10\x63md_game_sitdown\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08table_id\x18\x02 \x01(\x05\x12\x10\n\x08\x63hair_id\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\x05\x12\x0f\n\x07seconds\x18\x05 \x01(\x01\x12\r\n\x05times\x18\x06 \x01(\x05\x12\x13\n\x0bserver_time\x18\x07 \x01(\x03\x12\x0e\n\x06param1\x18\x08 \x01(\x05\x12%\n\x0c\x63hip_history\x18\t \x03(\x0b\x32\x0f.tagChipHistory\"L\n\x1d\x63md_sync_player_onlinet_count\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x19\n\x11user_online_count\x18\x02 \x01(\x05\"h\n\x0f\x63md_table_state\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\x12\x0f\n\x07seconds\x18\x03 \x01(\x01\x12\x0e\n\x06param1\x18\x04 \x01(\x05\x12\x13\n\x0bserver_time\x18\x05 \x01(\x03\"J\n\x0ftagChipItemInfo\x12\x10\n\x08\x63hip_idx\x18\x01 \x01(\x05\x12\x11\n\tchip_coin\x18\x02 \x01(\x01\x12\x12\n\nchip_award\x18\x03 \x01(\x01\"^\n\x12tagUserChipHistory\x12\x10\n\x08\x63hip_idx\x18\x01 \x01(\x05\x12\x11\n\tchip_coin\x18\x02 \x01(\x01\x12\x12\n\nchip_award\x18\x03 \x01(\x01\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\"G\n\rcmd_chip_info\x12$\n\nchip_items\x18\x01 \x03(\x0b\x32\x10.tagChipItemInfo\x12\x10\n\x08my_chips\x18\x02 \x03(\x01\"E\n\rcmd_user_chip\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x63hip_idx\x18\x02 \x01(\x05\x12\x11\n\tchip_coin\x18\x03 \x01(\x01\"\\\n\x12\x63md_user_chip_resp\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12\x10\n\x08\x63hip_idx\x18\x02 \x01(\x05\x12\x11\n\tchip_coin\x18\x03 \x01(\x01\x12\x0f\n\x07user_id\x18\x04 \x01(\x05\"I\n\x10\x63md_user_chip_ex\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12$\n\nchip_items\x18\x02 \x03(\x0b\x32\x10.tagChipItemInfo\"`\n\x15\x63md_user_chip_resp_ex\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12$\n\nchip_items\x18\x02 \x03(\x0b\x32\x10.tagChipItemInfo\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\"u\n\x0f\x63md_s_card_data\x12\x11\n\tcard_data\x18\x01 \x03(\r\x12\r\n\x05mutil\x18\x02 \x01(\r\x12\x12\n\nplayer_win\x18\x03 \x01(\x08\x12\x11\n\tcard_type\x18\x04 \x01(\r\x12\x19\n\x11\x61rea_total_result\x18\x05 \x01(\x01\"\x8a\x01\n\x0e\x63md_table_draw\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x15\n\rarea_my_chips\x18\x02 \x01(\x01\x12\r\n\x05score\x18\x03 \x03(\x01\x12(\n\x0esend_card_data\x18\x04 \x03(\x0b\x32\x10.cmd_s_card_data\x12\x16\n\x0e\x61rea_all_chips\x18\x05 \x01(\x01\"q\n\rcmd_user_trad\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x15\n\rarea_my_chips\x18\x03 \x01(\x01\x12\x14\n\x0cresult_score\x18\x04 \x01(\x01\x12\x10\n\x08now_coin\x18\x05 \x01(\x01\x42\x02H\x03')




_TAGCHIPHISTORY = _descriptor.Descriptor(
  name='tagChipHistory',
  full_name='tagChipHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='history', full_name='tagChipHistory.history', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=18,
  serialized_end=51,
)


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
      number=5, type=1, cpp_type=5, label=1,
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
      name='server_time', full_name='cmd_game_sitdown.server_time', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='cmd_game_sitdown.param1', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_history', full_name='cmd_game_sitdown.chip_history', index=8,
      number=9, type=11, cpp_type=10, label=3,
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
  serialized_start=54,
  serialized_end=248,
)


_CMD_SYNC_PLAYER_ONLINET_COUNT = _descriptor.Descriptor(
  name='cmd_sync_player_onlinet_count',
  full_name='cmd_sync_player_onlinet_count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='cmd_sync_player_onlinet_count.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_online_count', full_name='cmd_sync_player_onlinet_count.user_online_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=250,
  serialized_end=326,
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
      number=3, type=1, cpp_type=5, label=1,
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
    _descriptor.FieldDescriptor(
      name='server_time', full_name='cmd_table_state.server_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=328,
  serialized_end=432,
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
  serialized_start=434,
  serialized_end=508,
)


_TAGUSERCHIPHISTORY = _descriptor.Descriptor(
  name='tagUserChipHistory',
  full_name='tagUserChipHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chip_idx', full_name='tagUserChipHistory.chip_idx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_coin', full_name='tagUserChipHistory.chip_coin', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_award', full_name='tagUserChipHistory.chip_award', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tagUserChipHistory.user_id', index=3,
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
  serialized_start=510,
  serialized_end=604,
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
    _descriptor.FieldDescriptor(
      name='my_chips', full_name='cmd_chip_info.my_chips', index=1,
      number=2, type=1, cpp_type=5, label=3,
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
  serialized_start=606,
  serialized_end=677,
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
  serialized_start=679,
  serialized_end=748,
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
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_chip_resp.user_id', index=3,
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
  serialized_start=750,
  serialized_end=842,
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
  serialized_start=844,
  serialized_end=917,
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
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_chip_resp_ex.user_id', index=2,
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
  serialized_start=919,
  serialized_end=1015,
)


_CMD_S_CARD_DATA = _descriptor.Descriptor(
  name='cmd_s_card_data',
  full_name='cmd_s_card_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_data', full_name='cmd_s_card_data.card_data', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mutil', full_name='cmd_s_card_data.mutil', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_win', full_name='cmd_s_card_data.player_win', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_type', full_name='cmd_s_card_data.card_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_total_result', full_name='cmd_s_card_data.area_total_result', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=1017,
  serialized_end=1134,
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
      name='area_my_chips', full_name='cmd_table_draw.area_my_chips', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='cmd_table_draw.score', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_card_data', full_name='cmd_table_draw.send_card_data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_all_chips', full_name='cmd_table_draw.area_all_chips', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=1137,
  serialized_end=1275,
)


_CMD_USER_TRAD = _descriptor.Descriptor(
  name='cmd_user_trad',
  full_name='cmd_user_trad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='cmd_user_trad.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_user_trad.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_my_chips', full_name='cmd_user_trad.area_my_chips', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_score', full_name='cmd_user_trad.result_score', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_coin', full_name='cmd_user_trad.now_coin', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=1277,
  serialized_end=1390,
)

_CMD_GAME_SITDOWN.fields_by_name['chip_history'].message_type = _TAGCHIPHISTORY
_CMD_CHIP_INFO.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_USER_CHIP_EX.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_USER_CHIP_RESP_EX.fields_by_name['chip_items'].message_type = _TAGCHIPITEMINFO
_CMD_TABLE_DRAW.fields_by_name['send_card_data'].message_type = _CMD_S_CARD_DATA
DESCRIPTOR.message_types_by_name['tagChipHistory'] = _TAGCHIPHISTORY
DESCRIPTOR.message_types_by_name['cmd_game_sitdown'] = _CMD_GAME_SITDOWN
DESCRIPTOR.message_types_by_name['cmd_sync_player_onlinet_count'] = _CMD_SYNC_PLAYER_ONLINET_COUNT
DESCRIPTOR.message_types_by_name['cmd_table_state'] = _CMD_TABLE_STATE
DESCRIPTOR.message_types_by_name['tagChipItemInfo'] = _TAGCHIPITEMINFO
DESCRIPTOR.message_types_by_name['tagUserChipHistory'] = _TAGUSERCHIPHISTORY
DESCRIPTOR.message_types_by_name['cmd_chip_info'] = _CMD_CHIP_INFO
DESCRIPTOR.message_types_by_name['cmd_user_chip'] = _CMD_USER_CHIP
DESCRIPTOR.message_types_by_name['cmd_user_chip_resp'] = _CMD_USER_CHIP_RESP
DESCRIPTOR.message_types_by_name['cmd_user_chip_ex'] = _CMD_USER_CHIP_EX
DESCRIPTOR.message_types_by_name['cmd_user_chip_resp_ex'] = _CMD_USER_CHIP_RESP_EX
DESCRIPTOR.message_types_by_name['cmd_s_card_data'] = _CMD_S_CARD_DATA
DESCRIPTOR.message_types_by_name['cmd_table_draw'] = _CMD_TABLE_DRAW
DESCRIPTOR.message_types_by_name['cmd_user_trad'] = _CMD_USER_TRAD

class tagChipHistory(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGCHIPHISTORY

  # @@protoc_insertion_point(class_scope:tagChipHistory)

class cmd_game_sitdown(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_GAME_SITDOWN

  # @@protoc_insertion_point(class_scope:cmd_game_sitdown)

class cmd_sync_player_onlinet_count(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_SYNC_PLAYER_ONLINET_COUNT

  # @@protoc_insertion_point(class_scope:cmd_sync_player_onlinet_count)

class cmd_table_state(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_TABLE_STATE

  # @@protoc_insertion_point(class_scope:cmd_table_state)

class tagChipItemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGCHIPITEMINFO

  # @@protoc_insertion_point(class_scope:tagChipItemInfo)

class tagUserChipHistory(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGUSERCHIPHISTORY

  # @@protoc_insertion_point(class_scope:tagUserChipHistory)

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

class cmd_s_card_data(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_CARD_DATA

  # @@protoc_insertion_point(class_scope:cmd_s_card_data)

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
