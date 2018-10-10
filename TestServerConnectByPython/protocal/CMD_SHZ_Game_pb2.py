# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CMD_SHZ_Game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CMD_SHZ_Game.proto',
  package='CMD_SHZ',
  serialized_pb='\n\x12\x43MD_SHZ_Game.proto\x12\x07\x43MD_SHZ\"\x1a\n\x0b\x43MD_S_ERROR\x12\x0b\n\x03\x65rr\x18\x01 \x01(\x05\"<\n\x13\x43MD_C_MainGameStart\x12\x11\n\tbet_score\x18\x01 \x01(\x03\x12\x12\n\nline_count\x18\x02 \x01(\r\"2\n\x0btagLineInfo\x12\x0f\n\x07line_id\x18\x01 \x01(\x05\x12\x12\n\nicon_index\x18\x02 \x03(\x05\"\xdc\x01\n\x14\x43MD_S_MainGameResult\x12\x11\n\tbet_score\x18\x01 \x01(\x03\x12\x12\n\nline_count\x18\x02 \x01(\r\x12\x11\n\twin_score\x18\x03 \x01(\x03\x12\x13\n\x0bresult_type\x18\x04 \x01(\x05\x12\x18\n\x10\x62onus_game_count\x18\x05 \x01(\r\x12\x13\n\x0bresult_icon\x18\x06 \x03(\x05\x12)\n\x0bresult_line\x18\x07 \x03(\x0b\x32\x14.CMD_SHZ.tagLineInfo\x12\x1b\n\x13personal_prize_pool\x18\x08 \x01(\x03\":\n\x13\x43MD_C_DiceGameStart\x12\x11\n\tbet_score\x18\x01 \x01(\x03\x12\x10\n\x08\x62\x65t_type\x18\x02 \x01(\r\"b\n\x14\x43MD_S_DiceGameResult\x12\x11\n\tbet_score\x18\x01 \x01(\x03\x12\x10\n\x08\x62\x65t_type\x18\x02 \x01(\x05\x12\x12\n\ndice_point\x18\x03 \x01(\x05\x12\x11\n\twin_score\x18\x04 \x01(\x03\"\x15\n\x13\x43MD_C_MaryGameStart\"i\n\x11tagMaryGameResult\x12\x11\n\twin_score\x18\x01 \x01(\x03\x12\x17\n\x0f\x63urr_game_count\x18\x02 \x01(\r\x12\x13\n\x0b\x63\x65nter_icon\x18\x03 \x03(\x05\x12\x13\n\x0bresult_icon\x18\x04 \x01(\x05\"G\n\x14\x43MD_S_MaryGameResult\x12/\n\x0bmary_result\x18\x01 \x03(\x0b\x32\x1a.CMD_SHZ.tagMaryGameResult\"\'\n\x10\x43MD_C_SwitchGame\x12\x13\n\x0bswitch_game\x18\x01 \x01(\x05\"\x8e\x02\n\x15\x43MD_S_UpdateGameScene\x12\x11\n\tcurr_game\x18\x01 \x01(\x05\x12\x12\n\nuser_score\x18\x02 \x01(\x03\x12\x14\n\x0c\x62\x65t_per_line\x18\x03 \x01(\x03\x12\x12\n\nline_count\x18\x04 \x01(\x05\x12\x16\n\x0emain_win_score\x18\x05 \x01(\x03\x12\x10\n\x08\x62\x65t_list\x18\x06 \x03(\r\x12\x10\n\x08\x62\x65t_dice\x18\x07 \x01(\x03\x12\x16\n\x0e\x64ice_win_score\x18\x08 \x01(\x03\x12\x10\n\x08\x62\x65t_mary\x18\t \x01(\x03\x12\x1b\n\x13personal_prize_pool\x18\n \x01(\x03\x12!\n\x19personal_prize_pool_limit\x18\x0b \x01(\x03\x42\x02H\x03')




_CMD_S_ERROR = _descriptor.Descriptor(
  name='CMD_S_ERROR',
  full_name='CMD_SHZ.CMD_S_ERROR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='CMD_SHZ.CMD_S_ERROR.err', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=31,
  serialized_end=57,
)


_CMD_C_MAINGAMESTART = _descriptor.Descriptor(
  name='CMD_C_MainGameStart',
  full_name='CMD_SHZ.CMD_C_MainGameStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='CMD_SHZ.CMD_C_MainGameStart.bet_score', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='CMD_SHZ.CMD_C_MainGameStart.line_count', index=1,
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
  serialized_start=59,
  serialized_end=119,
)


_TAGLINEINFO = _descriptor.Descriptor(
  name='tagLineInfo',
  full_name='CMD_SHZ.tagLineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_id', full_name='CMD_SHZ.tagLineInfo.line_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon_index', full_name='CMD_SHZ.tagLineInfo.icon_index', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=121,
  serialized_end=171,
)


_CMD_S_MAINGAMERESULT = _descriptor.Descriptor(
  name='CMD_S_MainGameResult',
  full_name='CMD_SHZ.CMD_S_MainGameResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='CMD_SHZ.CMD_S_MainGameResult.bet_score', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='CMD_SHZ.CMD_S_MainGameResult.line_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_score', full_name='CMD_SHZ.CMD_S_MainGameResult.win_score', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_type', full_name='CMD_SHZ.CMD_S_MainGameResult.result_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bonus_game_count', full_name='CMD_SHZ.CMD_S_MainGameResult.bonus_game_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_icon', full_name='CMD_SHZ.CMD_S_MainGameResult.result_icon', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_line', full_name='CMD_SHZ.CMD_S_MainGameResult.result_line', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='personal_prize_pool', full_name='CMD_SHZ.CMD_S_MainGameResult.personal_prize_pool', index=7,
      number=8, type=3, cpp_type=2, label=1,
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
  serialized_start=174,
  serialized_end=394,
)


_CMD_C_DICEGAMESTART = _descriptor.Descriptor(
  name='CMD_C_DiceGameStart',
  full_name='CMD_SHZ.CMD_C_DiceGameStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='CMD_SHZ.CMD_C_DiceGameStart.bet_score', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_type', full_name='CMD_SHZ.CMD_C_DiceGameStart.bet_type', index=1,
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
  serialized_start=396,
  serialized_end=454,
)


_CMD_S_DICEGAMERESULT = _descriptor.Descriptor(
  name='CMD_S_DiceGameResult',
  full_name='CMD_SHZ.CMD_S_DiceGameResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bet_score', full_name='CMD_SHZ.CMD_S_DiceGameResult.bet_score', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_type', full_name='CMD_SHZ.CMD_S_DiceGameResult.bet_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dice_point', full_name='CMD_SHZ.CMD_S_DiceGameResult.dice_point', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_score', full_name='CMD_SHZ.CMD_S_DiceGameResult.win_score', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=456,
  serialized_end=554,
)


_CMD_C_MARYGAMESTART = _descriptor.Descriptor(
  name='CMD_C_MaryGameStart',
  full_name='CMD_SHZ.CMD_C_MaryGameStart',
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
  serialized_start=556,
  serialized_end=577,
)


_TAGMARYGAMERESULT = _descriptor.Descriptor(
  name='tagMaryGameResult',
  full_name='CMD_SHZ.tagMaryGameResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='win_score', full_name='CMD_SHZ.tagMaryGameResult.win_score', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curr_game_count', full_name='CMD_SHZ.tagMaryGameResult.curr_game_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center_icon', full_name='CMD_SHZ.tagMaryGameResult.center_icon', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_icon', full_name='CMD_SHZ.tagMaryGameResult.result_icon', index=3,
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
  serialized_start=579,
  serialized_end=684,
)


_CMD_S_MARYGAMERESULT = _descriptor.Descriptor(
  name='CMD_S_MaryGameResult',
  full_name='CMD_SHZ.CMD_S_MaryGameResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mary_result', full_name='CMD_SHZ.CMD_S_MaryGameResult.mary_result', index=0,
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
  serialized_start=686,
  serialized_end=757,
)


_CMD_C_SWITCHGAME = _descriptor.Descriptor(
  name='CMD_C_SwitchGame',
  full_name='CMD_SHZ.CMD_C_SwitchGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch_game', full_name='CMD_SHZ.CMD_C_SwitchGame.switch_game', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=759,
  serialized_end=798,
)


_CMD_S_UPDATEGAMESCENE = _descriptor.Descriptor(
  name='CMD_S_UpdateGameScene',
  full_name='CMD_SHZ.CMD_S_UpdateGameScene',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='curr_game', full_name='CMD_SHZ.CMD_S_UpdateGameScene.curr_game', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_score', full_name='CMD_SHZ.CMD_S_UpdateGameScene.user_score', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_per_line', full_name='CMD_SHZ.CMD_S_UpdateGameScene.bet_per_line', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_count', full_name='CMD_SHZ.CMD_S_UpdateGameScene.line_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='main_win_score', full_name='CMD_SHZ.CMD_S_UpdateGameScene.main_win_score', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_list', full_name='CMD_SHZ.CMD_S_UpdateGameScene.bet_list', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_dice', full_name='CMD_SHZ.CMD_S_UpdateGameScene.bet_dice', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dice_win_score', full_name='CMD_SHZ.CMD_S_UpdateGameScene.dice_win_score', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bet_mary', full_name='CMD_SHZ.CMD_S_UpdateGameScene.bet_mary', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='personal_prize_pool', full_name='CMD_SHZ.CMD_S_UpdateGameScene.personal_prize_pool', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='personal_prize_pool_limit', full_name='CMD_SHZ.CMD_S_UpdateGameScene.personal_prize_pool_limit', index=10,
      number=11, type=3, cpp_type=2, label=1,
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
  serialized_start=801,
  serialized_end=1071,
)

_CMD_S_MAINGAMERESULT.fields_by_name['result_line'].message_type = _TAGLINEINFO
_CMD_S_MARYGAMERESULT.fields_by_name['mary_result'].message_type = _TAGMARYGAMERESULT
DESCRIPTOR.message_types_by_name['CMD_S_ERROR'] = _CMD_S_ERROR
DESCRIPTOR.message_types_by_name['CMD_C_MainGameStart'] = _CMD_C_MAINGAMESTART
DESCRIPTOR.message_types_by_name['tagLineInfo'] = _TAGLINEINFO
DESCRIPTOR.message_types_by_name['CMD_S_MainGameResult'] = _CMD_S_MAINGAMERESULT
DESCRIPTOR.message_types_by_name['CMD_C_DiceGameStart'] = _CMD_C_DICEGAMESTART
DESCRIPTOR.message_types_by_name['CMD_S_DiceGameResult'] = _CMD_S_DICEGAMERESULT
DESCRIPTOR.message_types_by_name['CMD_C_MaryGameStart'] = _CMD_C_MARYGAMESTART
DESCRIPTOR.message_types_by_name['tagMaryGameResult'] = _TAGMARYGAMERESULT
DESCRIPTOR.message_types_by_name['CMD_S_MaryGameResult'] = _CMD_S_MARYGAMERESULT
DESCRIPTOR.message_types_by_name['CMD_C_SwitchGame'] = _CMD_C_SWITCHGAME
DESCRIPTOR.message_types_by_name['CMD_S_UpdateGameScene'] = _CMD_S_UPDATEGAMESCENE

class CMD_S_ERROR(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_ERROR

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_S_ERROR)

class CMD_C_MainGameStart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_MAINGAMESTART

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_C_MainGameStart)

class tagLineInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGLINEINFO

  # @@protoc_insertion_point(class_scope:CMD_SHZ.tagLineInfo)

class CMD_S_MainGameResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_MAINGAMERESULT

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_S_MainGameResult)

class CMD_C_DiceGameStart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_DICEGAMESTART

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_C_DiceGameStart)

class CMD_S_DiceGameResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_DICEGAMERESULT

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_S_DiceGameResult)

class CMD_C_MaryGameStart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_MARYGAMESTART

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_C_MaryGameStart)

class tagMaryGameResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGMARYGAMERESULT

  # @@protoc_insertion_point(class_scope:CMD_SHZ.tagMaryGameResult)

class CMD_S_MaryGameResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_MARYGAMERESULT

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_S_MaryGameResult)

class CMD_C_SwitchGame(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_C_SWITCHGAME

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_C_SwitchGame)

class CMD_S_UpdateGameScene(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_S_UPDATEGAMESCENE

  # @@protoc_insertion_point(class_scope:CMD_SHZ.CMD_S_UpdateGameScene)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)