# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd_monitor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmd_monitor.proto',
  package='',
  serialized_pb='\n\x11\x63md_monitor.proto\"\x18\n\x16\x63md_monitor_client_reg\"T\n\x16\x63md_monitor_server_reg\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x13\n\x0bserver_name\x18\x02 \x01(\x0c\x12\x12\n\nstart_time\x18\x03 \x01(\x05\"L\n\x0etagmonitoritem\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x13\n\x0bserver_name\x18\x02 \x01(\x0c\x12\x12\n\nstart_time\x18\x03 \x01(\x05\"6\n\x14\x63md_monitor_item_lst\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.tagmonitoritem\"5\n\x14\x63md_monitor_new_item\x12\x1d\n\x04item\x18\x01 \x01(\x0b\x32\x0f.tagmonitoritem\")\n\x14\x63md_monitor_del_item\x12\x11\n\tserver_id\x18\x01 \x01(\x05\"{\n\x16\x63md_monitor_item_state\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x03\x12\x0b\n\x03\x63pu\x18\x03 \x01(\x05\x12\x0f\n\x07io_read\x18\x04 \x01(\x03\x12\x10\n\x08io_write\x18\x05 \x01(\x03\x12\x0e\n\x06online\x18\x06 \x01(\x05\"[\n\x0f\x63md_monitor_log\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x11\n\tlog_level\x18\x02 \x01(\x05\x12\x10\n\x08log_time\x18\x03 \x01(\x03\x12\x10\n\x08log_text\x18\x04 \x01(\x0c\"D\n\x0f\x63md_monitor_cmd\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x11\n\tclient_id\x18\x02 \x01(\x05\x12\x0b\n\x03\x63md\x18\x03 \x01(\x0c\"L\n\x14\x63md_monitor_cmd_resp\x12\x11\n\tserver_id\x18\x01 \x01(\x05\x12\x11\n\tclient_id\x18\x02 \x01(\x05\x12\x0e\n\x06result\x18\x03 \x01(\x0c\x42\x02H\x03')




_CMD_MONITOR_CLIENT_REG = _descriptor.Descriptor(
  name='cmd_monitor_client_reg',
  full_name='cmd_monitor_client_reg',
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
  serialized_start=21,
  serialized_end=45,
)


_CMD_MONITOR_SERVER_REG = _descriptor.Descriptor(
  name='cmd_monitor_server_reg',
  full_name='cmd_monitor_server_reg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_server_reg.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='cmd_monitor_server_reg.server_name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cmd_monitor_server_reg.start_time', index=2,
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
  serialized_start=47,
  serialized_end=131,
)


_TAGMONITORITEM = _descriptor.Descriptor(
  name='tagmonitoritem',
  full_name='tagmonitoritem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='tagmonitoritem.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='tagmonitoritem.server_name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tagmonitoritem.start_time', index=2,
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
  serialized_start=133,
  serialized_end=209,
)


_CMD_MONITOR_ITEM_LST = _descriptor.Descriptor(
  name='cmd_monitor_item_lst',
  full_name='cmd_monitor_item_lst',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='cmd_monitor_item_lst.items', index=0,
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
  serialized_start=211,
  serialized_end=265,
)


_CMD_MONITOR_NEW_ITEM = _descriptor.Descriptor(
  name='cmd_monitor_new_item',
  full_name='cmd_monitor_new_item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='cmd_monitor_new_item.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=267,
  serialized_end=320,
)


_CMD_MONITOR_DEL_ITEM = _descriptor.Descriptor(
  name='cmd_monitor_del_item',
  full_name='cmd_monitor_del_item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_del_item.server_id', index=0,
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
  serialized_start=322,
  serialized_end=363,
)


_CMD_MONITOR_ITEM_STATE = _descriptor.Descriptor(
  name='cmd_monitor_item_state',
  full_name='cmd_monitor_item_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_item_state.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='cmd_monitor_item_state.memory', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='cmd_monitor_item_state.cpu', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='io_read', full_name='cmd_monitor_item_state.io_read', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='io_write', full_name='cmd_monitor_item_state.io_write', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online', full_name='cmd_monitor_item_state.online', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=365,
  serialized_end=488,
)


_CMD_MONITOR_LOG = _descriptor.Descriptor(
  name='cmd_monitor_log',
  full_name='cmd_monitor_log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_log.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='cmd_monitor_log.log_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_time', full_name='cmd_monitor_log.log_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_text', full_name='cmd_monitor_log.log_text', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=490,
  serialized_end=581,
)


_CMD_MONITOR_CMD = _descriptor.Descriptor(
  name='cmd_monitor_cmd',
  full_name='cmd_monitor_cmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_cmd.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='cmd_monitor_cmd.client_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='cmd_monitor_cmd.cmd', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=583,
  serialized_end=651,
)


_CMD_MONITOR_CMD_RESP = _descriptor.Descriptor(
  name='cmd_monitor_cmd_resp',
  full_name='cmd_monitor_cmd_resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='cmd_monitor_cmd_resp.server_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='cmd_monitor_cmd_resp.client_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='cmd_monitor_cmd_resp.result', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=653,
  serialized_end=729,
)

_CMD_MONITOR_ITEM_LST.fields_by_name['items'].message_type = _TAGMONITORITEM
_CMD_MONITOR_NEW_ITEM.fields_by_name['item'].message_type = _TAGMONITORITEM
DESCRIPTOR.message_types_by_name['cmd_monitor_client_reg'] = _CMD_MONITOR_CLIENT_REG
DESCRIPTOR.message_types_by_name['cmd_monitor_server_reg'] = _CMD_MONITOR_SERVER_REG
DESCRIPTOR.message_types_by_name['tagmonitoritem'] = _TAGMONITORITEM
DESCRIPTOR.message_types_by_name['cmd_monitor_item_lst'] = _CMD_MONITOR_ITEM_LST
DESCRIPTOR.message_types_by_name['cmd_monitor_new_item'] = _CMD_MONITOR_NEW_ITEM
DESCRIPTOR.message_types_by_name['cmd_monitor_del_item'] = _CMD_MONITOR_DEL_ITEM
DESCRIPTOR.message_types_by_name['cmd_monitor_item_state'] = _CMD_MONITOR_ITEM_STATE
DESCRIPTOR.message_types_by_name['cmd_monitor_log'] = _CMD_MONITOR_LOG
DESCRIPTOR.message_types_by_name['cmd_monitor_cmd'] = _CMD_MONITOR_CMD
DESCRIPTOR.message_types_by_name['cmd_monitor_cmd_resp'] = _CMD_MONITOR_CMD_RESP

class cmd_monitor_client_reg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_CLIENT_REG

  # @@protoc_insertion_point(class_scope:cmd_monitor_client_reg)

class cmd_monitor_server_reg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_SERVER_REG

  # @@protoc_insertion_point(class_scope:cmd_monitor_server_reg)

class tagmonitoritem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGMONITORITEM

  # @@protoc_insertion_point(class_scope:tagmonitoritem)

class cmd_monitor_item_lst(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_ITEM_LST

  # @@protoc_insertion_point(class_scope:cmd_monitor_item_lst)

class cmd_monitor_new_item(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_NEW_ITEM

  # @@protoc_insertion_point(class_scope:cmd_monitor_new_item)

class cmd_monitor_del_item(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_DEL_ITEM

  # @@protoc_insertion_point(class_scope:cmd_monitor_del_item)

class cmd_monitor_item_state(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_ITEM_STATE

  # @@protoc_insertion_point(class_scope:cmd_monitor_item_state)

class cmd_monitor_log(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_LOG

  # @@protoc_insertion_point(class_scope:cmd_monitor_log)

class cmd_monitor_cmd(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_CMD

  # @@protoc_insertion_point(class_scope:cmd_monitor_cmd)

class cmd_monitor_cmd_resp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CMD_MONITOR_CMD_RESP

  # @@protoc_insertion_point(class_scope:cmd_monitor_cmd_resp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
