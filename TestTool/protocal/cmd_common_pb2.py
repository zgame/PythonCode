# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd_common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd_common.proto',
  package='',
  serialized_pb='\n\x10\x63md_common.proto\"\xed\x01\n\x10\x63md_client_login\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\r\n\x05token\x18\x02 \x01(\x0c\x12\x0e\n\x06mac_id\x18\x03 \x01(\x0c\x12\x11\n\tgame_kind\x18\x04 \x01(\x05\x12\x11\n\tplat_kind\x18\x05 \x01(\x05\x12\x12\n\nclient_ver\x18\x06 \x01(\x05\x12\x11\n\tclient_ip\x18\x07 \x01(\x0c\x12\x13\n\x0b\x63lient_type\x18\x08 \x01(\x05\x12\x13\n\x0b\x64\x65vice_type\x18\t \x01(\x0c\x12\x10\n\x08\x64itch_id\x18\n \x01(\x05\x12\x0c\n\x04imei\x18\x0b \x01(\x0c\x12\x12\n\nis_android\x18\x0c \x01(\x05\"l\n\x14\x63md_client_login_rsp\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\terror_msg\x18\x02 \x01(\x0c\x12\x0f\n\x07game_id\x18\x03 \x01(\x05\x12\x11\n\tnick_name\x18\x04 \x01(\x0c\x12\x0c\n\x04\x63oin\x18\x05 \x01(\x01\".\n\x0f\x63md_client_kick\x12\x0b\n\x03msg\x18\x01 \x01(\x0c\x12\x0e\n\x06msg_id\x18\x02 \x01(\x05\"1\n\x0e\x63md_leave_game\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\x05\"2\n\x0e\x63md_leave_resp\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_str\x18\x02 \x01(\x0c\"=\n\x0c\x63md_coin_chg\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x63hange\x18\x02 \x01(\x01\x12\x0c\n\x04keep\x18\x03 \x01(\x01\"C\n\x10\x63md_roll_message\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0f\n\x07repeate\x18\x03 \x01(\x05\x42\x02H\x03')




_CMD_CLIENT_LOGIN = _descriptor.Descriptor(
  name='cmd_client_login',
  full_name='cmd_client_login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_client_login.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='cmd_client_login.token', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac_id', full_name='cmd_client_login.mac_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_kind', full_name='cmd_client_login.game_kind', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat_kind', full_name='cmd_client_login.plat_kind', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ver', full_name='cmd_client_login.client_ver', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='cmd_client_login.client_ip', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='cmd_client_login.client_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='cmd_client_login.device_type', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ditch_id', full_name='cmd_client_login.ditch_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imei', full_name='cmd_client_login.imei', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_android', full_name='cmd_client_login.is_android', index=11,
      number=12, type=5, cpp_type=1, label=1,
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
  serialized_start=21,
  serialized_end=258,
)


_CMD_CLIENT_LOGIN_RSP = _descriptor.Descriptor(
  name='cmd_client_login_rsp',
  full_name='cmd_client_login_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_client_login_rsp.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='cmd_client_login_rsp.error_msg', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='cmd_client_login_rsp.game_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nick_name', full_name='cmd_client_login_rsp.nick_name', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin', full_name='cmd_client_login_rsp.coin', index=4,
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
  serialized_start=260,
  serialized_end=368,
)


_CMD_CLIENT_KICK = _descriptor.Descriptor(
  name='cmd_client_kick',
  full_name='cmd_client_kick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='cmd_client_kick.msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='cmd_client_kick.msg_id', index=1,
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
  serialized_start=370,
  serialized_end=416,
)


_CMD_LEAVE_GAME = _descriptor.Descriptor(
  name='cmd_leave_game',
  full_name='cmd_leave_game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_leave_game.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='cmd_leave_game.reason', index=1,
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
  serialized_start=418,
  serialized_end=467,
)


_CMD_LEAVE_RESP = _descriptor.Descriptor(
  name='cmd_leave_resp',
  full_name='cmd_leave_resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_leave_resp.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_str', full_name='cmd_leave_resp.err_str', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=469,
  serialized_end=519,
)


_CMD_COIN_CHG = _descriptor.Descriptor(
  name='cmd_coin_chg',
  full_name='cmd_coin_chg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cmd_coin_chg.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change', full_name='cmd_coin_chg.change', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keep', full_name='cmd_coin_chg.keep', index=2,
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
  serialized_start=521,
  serialized_end=582,
)


_CMD_ROLL_MESSAGE = _descriptor.Descriptor(
  name='cmd_roll_message',
  full_name='cmd_roll_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='cmd_roll_message.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='cmd_roll_message.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeate', full_name='cmd_roll_message.repeate', index=2,
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
  serialized_start=584,
  serialized_end=651,
)

DESCRIPTOR.message_types_by_name['cmd_client_login'] = _CMD_CLIENT_LOGIN
DESCRIPTOR.message_types_by_name['cmd_client_login_rsp'] = _CMD_CLIENT_LOGIN_RSP
DESCRIPTOR.message_types_by_name['cmd_client_kick'] = _CMD_CLIENT_KICK
DESCRIPTOR.message_types_by_name['cmd_leave_game'] = _CMD_LEAVE_GAME
DESCRIPTOR.message_types_by_name['cmd_leave_resp'] = _CMD_LEAVE_RESP
DESCRIPTOR.message_types_by_name['cmd_coin_chg'] = _CMD_COIN_CHG
DESCRIPTOR.message_types_by_name['cmd_roll_message'] = _CMD_ROLL_MESSAGE

class cmd_client_login(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_CLIENT_LOGIN

  # @@protoc_insertion_point(class_scope:cmd_client_login)

class cmd_client_login_rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_CLIENT_LOGIN_RSP

  # @@protoc_insertion_point(class_scope:cmd_client_login_rsp)

class cmd_client_kick(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_CLIENT_KICK

  # @@protoc_insertion_point(class_scope:cmd_client_kick)

class cmd_leave_game(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_LEAVE_GAME

  # @@protoc_insertion_point(class_scope:cmd_leave_game)

class cmd_leave_resp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_LEAVE_RESP

  # @@protoc_insertion_point(class_scope:cmd_leave_resp)

class cmd_coin_chg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_COIN_CHG

  # @@protoc_insertion_point(class_scope:cmd_coin_chg)

class cmd_roll_message(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_ROLL_MESSAGE

  # @@protoc_insertion_point(class_scope:cmd_roll_message)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
