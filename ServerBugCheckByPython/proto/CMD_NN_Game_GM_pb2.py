# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CMD_NN_Game_GM.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CMD_NN_Game_GM.proto',
  package='CMD_NN',
  syntax='proto2',
  serialized_pb=_b('\n\x14\x43MD_NN_Game_GM.proto\x12\x06\x43MD_NN\"m\n\x11\x43MD_S_GM_GameInfo\x12\x13\n\x0b\x62\x61nker_name\x18\x01 \x01(\x0c\x12\x13\n\x0btotal_board\x18\x02 \x01(\r\x12\x15\n\rcurrent_store\x18\x03 \x01(\x04\x12\x17\n\x0fstore_down_line\x18\x04 \x01(\x04\"J\n\x14\x43MD_C_Screen_Control\x12\x0f\n\x07sys_win\x18\x01 \x01(\x08\x12\x0e\n\x06\x63\x62type\x18\x02 \x01(\r\x12\x11\n\tmax_score\x18\x03 \x01(\x03\"Y\n\x11\x43MD_C_UserControl\x12\x10\n\x08user_win\x18\x01 \x01(\x08\x12\x0f\n\x07game_id\x18\x02 \x01(\r\x12\x0e\n\x06\x63\x62type\x18\x03 \x01(\x05\x12\x11\n\tmax_score\x18\x04 \x01(\x03\"%\n\x11\x43MD_C_AreaControl\x12\x10\n\x08\x61rea_win\x18\x01 \x03(\x08\"+\n\x11\x43MD_C_Card_Config\x12\x16\n\x0e\x63\x62SendCardData\x18\x01 \x03(\r\"<\n\x13\x43MD_GM_S_SysMessage\x12\x10\n\x08sys_type\x18\x01 \x01(\r\x12\x13\n\x0bsys_message\x18\x02 \x01(\x0c\x42\x02H\x03')
)




_CMD_S_GM_GAMEINFO = _descriptor.Descriptor(
  name='CMD_S_GM_GameInfo',
  full_name='CMD_NN.CMD_S_GM_GameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='banker_name', full_name='CMD_NN.CMD_S_GM_GameInfo.banker_name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_board', full_name='CMD_NN.CMD_S_GM_GameInfo.total_board', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_store', full_name='CMD_NN.CMD_S_GM_GameInfo.current_store', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_down_line', full_name='CMD_NN.CMD_S_GM_GameInfo.store_down_line', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=141,
)


_CMD_C_SCREEN_CONTROL = _descriptor.Descriptor(
  name='CMD_C_Screen_Control',
  full_name='CMD_NN.CMD_C_Screen_Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sys_win', full_name='CMD_NN.CMD_C_Screen_Control.sys_win', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cbtype', full_name='CMD_NN.CMD_C_Screen_Control.cbtype', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='CMD_NN.CMD_C_Screen_Control.max_score', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=217,
)


_CMD_C_USERCONTROL = _descriptor.Descriptor(
  name='CMD_C_UserControl',
  full_name='CMD_NN.CMD_C_UserControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_win', full_name='CMD_NN.CMD_C_UserControl.user_win', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='CMD_NN.CMD_C_UserControl.game_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cbtype', full_name='CMD_NN.CMD_C_UserControl.cbtype', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='CMD_NN.CMD_C_UserControl.max_score', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=308,
)


_CMD_C_AREACONTROL = _descriptor.Descriptor(
  name='CMD_C_AreaControl',
  full_name='CMD_NN.CMD_C_AreaControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_win', full_name='CMD_NN.CMD_C_AreaControl.area_win', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=347,
)


_CMD_C_CARD_CONFIG = _descriptor.Descriptor(
  name='CMD_C_Card_Config',
  full_name='CMD_NN.CMD_C_Card_Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cbSendCardData', full_name='CMD_NN.CMD_C_Card_Config.cbSendCardData', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=392,
)


_CMD_GM_S_SYSMESSAGE = _descriptor.Descriptor(
  name='CMD_GM_S_SysMessage',
  full_name='CMD_NN.CMD_GM_S_SysMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sys_type', full_name='CMD_NN.CMD_GM_S_SysMessage.sys_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_message', full_name='CMD_NN.CMD_GM_S_SysMessage.sys_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=454,
)

DESCRIPTOR.message_types_by_name['CMD_S_GM_GameInfo'] = _CMD_S_GM_GAMEINFO
DESCRIPTOR.message_types_by_name['CMD_C_Screen_Control'] = _CMD_C_SCREEN_CONTROL
DESCRIPTOR.message_types_by_name['CMD_C_UserControl'] = _CMD_C_USERCONTROL
DESCRIPTOR.message_types_by_name['CMD_C_AreaControl'] = _CMD_C_AREACONTROL
DESCRIPTOR.message_types_by_name['CMD_C_Card_Config'] = _CMD_C_CARD_CONFIG
DESCRIPTOR.message_types_by_name['CMD_GM_S_SysMessage'] = _CMD_GM_S_SYSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CMD_S_GM_GameInfo = _reflection.GeneratedProtocolMessageType('CMD_S_GM_GameInfo', (_message.Message,), dict(
  DESCRIPTOR = _CMD_S_GM_GAMEINFO,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_S_GM_GameInfo)
  ))
_sym_db.RegisterMessage(CMD_S_GM_GameInfo)

CMD_C_Screen_Control = _reflection.GeneratedProtocolMessageType('CMD_C_Screen_Control', (_message.Message,), dict(
  DESCRIPTOR = _CMD_C_SCREEN_CONTROL,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_C_Screen_Control)
  ))
_sym_db.RegisterMessage(CMD_C_Screen_Control)

CMD_C_UserControl = _reflection.GeneratedProtocolMessageType('CMD_C_UserControl', (_message.Message,), dict(
  DESCRIPTOR = _CMD_C_USERCONTROL,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_C_UserControl)
  ))
_sym_db.RegisterMessage(CMD_C_UserControl)

CMD_C_AreaControl = _reflection.GeneratedProtocolMessageType('CMD_C_AreaControl', (_message.Message,), dict(
  DESCRIPTOR = _CMD_C_AREACONTROL,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_C_AreaControl)
  ))
_sym_db.RegisterMessage(CMD_C_AreaControl)

CMD_C_Card_Config = _reflection.GeneratedProtocolMessageType('CMD_C_Card_Config', (_message.Message,), dict(
  DESCRIPTOR = _CMD_C_CARD_CONFIG,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_C_Card_Config)
  ))
_sym_db.RegisterMessage(CMD_C_Card_Config)

CMD_GM_S_SysMessage = _reflection.GeneratedProtocolMessageType('CMD_GM_S_SysMessage', (_message.Message,), dict(
  DESCRIPTOR = _CMD_GM_S_SYSMESSAGE,
  __module__ = 'CMD_NN_Game_GM_pb2'
  # @@protoc_insertion_point(class_scope:CMD_NN.CMD_GM_S_SysMessage)
  ))
_sym_db.RegisterMessage(CMD_GM_S_SysMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)