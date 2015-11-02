# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BleProxyMsg.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BleProxyMsg.proto',
  package='',
  serialized_pb='\n\x11\x42leProxyMsg.proto\"#\n\x07\x43ontrol\x12\x18\n\x03\x63md\x18\x01 \x02(\x0e\x32\x0b.ControlCmd\"9\n\nScanResult\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\t\x12\x0c\n\x04rssi\x18\x03 \x02(\x05\"\x1a\n\x07\x43onnect\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\" \n\rBleDisconnect\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\"4\n\rConnectResult\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x13\n\x0b\x65rrorString\x18\x02 \x01(\t\"\x19\n\tProxyData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"\xec\x01\n\x0b\x42leProxyMsg\x12\x19\n\x03\x63md\x18\x01 \x02(\x0e\x32\x0c.ProxyMsgCmd\x12\x19\n\x07\x63ontrol\x18\x02 \x01(\x0b\x32\x08.Control\x12\x1f\n\nscanResult\x18\x03 \x01(\x0b\x32\x0b.ScanResult\x12\x19\n\x07\x63onnect\x18\x04 \x01(\x0b\x32\x08.Connect\x12%\n\rbleDisconnect\x18\x05 \x01(\x0b\x32\x0e.BleDisconnect\x12%\n\rconnectResult\x18\x06 \x01(\x0b\x32\x0e.ConnectResult\x12\x1d\n\tproxyData\x18\x07 \x01(\x0b\x32\n.ProxyData*p\n\x0bProxyMsgCmd\x12\x0b\n\x07\x43ONTROL\x10\x01\x12\x0f\n\x0bSCAN_RESULT\x10\x02\x12\x0b\n\x07\x43ONNECT\x10\x03\x12\x12\n\x0e\x42LE_DISCONNECT\x10\x04\x12\x12\n\x0e\x43ONNECT_RESULT\x10\x05\x12\x0e\n\nPROXY_DATA\x10\x06*F\n\nControlCmd\x12\x0b\n\x07TURN_ON\x10\x00\x12\x0c\n\x08TURN_OFF\x10\x01\x12\x0e\n\nSTART_SCAN\x10\x02\x12\r\n\tSTOP_SCAN\x10\x03')

_PROXYMSGCMD = _descriptor.EnumDescriptor(
  name='ProxyMsgCmd',
  full_name='ProxyMsgCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCAN_RESULT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DISCONNECT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT_RESULT', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_DATA', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=499,
  serialized_end=611,
)

ProxyMsgCmd = enum_type_wrapper.EnumTypeWrapper(_PROXYMSGCMD)
_CONTROLCMD = _descriptor.EnumDescriptor(
  name='ControlCmd',
  full_name='ControlCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TURN_ON', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURN_OFF', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_SCAN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_SCAN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=613,
  serialized_end=683,
)

ControlCmd = enum_type_wrapper.EnumTypeWrapper(_CONTROLCMD)
CONTROL = 1
SCAN_RESULT = 2
CONNECT = 3
BLE_DISCONNECT = 4
CONNECT_RESULT = 5
PROXY_DATA = 6
TURN_ON = 0
TURN_OFF = 1
START_SCAN = 2
STOP_SCAN = 3



_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='Control.cmd', index=0,
      number=1, type=14, cpp_type=8, label=2,
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
  serialized_end=56,
)


_SCANRESULT = _descriptor.Descriptor(
  name='ScanResult',
  full_name='ScanResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ScanResult.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='ScanResult.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='ScanResult.rssi', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=58,
  serialized_end=115,
)


_CONNECT = _descriptor.Descriptor(
  name='Connect',
  full_name='Connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='Connect.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=117,
  serialized_end=143,
)


_BLEDISCONNECT = _descriptor.Descriptor(
  name='BleDisconnect',
  full_name='BleDisconnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='BleDisconnect.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=145,
  serialized_end=177,
)


_CONNECTRESULT = _descriptor.Descriptor(
  name='ConnectResult',
  full_name='ConnectResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ConnectResult.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorString', full_name='ConnectResult.errorString', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=179,
  serialized_end=231,
)


_PROXYDATA = _descriptor.Descriptor(
  name='ProxyData',
  full_name='ProxyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ProxyData.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=233,
  serialized_end=258,
)


_BLEPROXYMSG = _descriptor.Descriptor(
  name='BleProxyMsg',
  full_name='BleProxyMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='BleProxyMsg.cmd', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control', full_name='BleProxyMsg.control', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scanResult', full_name='BleProxyMsg.scanResult', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connect', full_name='BleProxyMsg.connect', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bleDisconnect', full_name='BleProxyMsg.bleDisconnect', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connectResult', full_name='BleProxyMsg.connectResult', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxyData', full_name='BleProxyMsg.proxyData', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=261,
  serialized_end=497,
)

_CONTROL.fields_by_name['cmd'].enum_type = _CONTROLCMD
_BLEPROXYMSG.fields_by_name['cmd'].enum_type = _PROXYMSGCMD
_BLEPROXYMSG.fields_by_name['control'].message_type = _CONTROL
_BLEPROXYMSG.fields_by_name['scanResult'].message_type = _SCANRESULT
_BLEPROXYMSG.fields_by_name['connect'].message_type = _CONNECT
_BLEPROXYMSG.fields_by_name['bleDisconnect'].message_type = _BLEDISCONNECT
_BLEPROXYMSG.fields_by_name['connectResult'].message_type = _CONNECTRESULT
_BLEPROXYMSG.fields_by_name['proxyData'].message_type = _PROXYDATA
DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
DESCRIPTOR.message_types_by_name['ScanResult'] = _SCANRESULT
DESCRIPTOR.message_types_by_name['Connect'] = _CONNECT
DESCRIPTOR.message_types_by_name['BleDisconnect'] = _BLEDISCONNECT
DESCRIPTOR.message_types_by_name['ConnectResult'] = _CONNECTRESULT
DESCRIPTOR.message_types_by_name['ProxyData'] = _PROXYDATA
DESCRIPTOR.message_types_by_name['BleProxyMsg'] = _BLEPROXYMSG

class Control(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTROL

  # @@protoc_insertion_point(class_scope:Control)

class ScanResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCANRESULT

  # @@protoc_insertion_point(class_scope:ScanResult)

class Connect(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONNECT

  # @@protoc_insertion_point(class_scope:Connect)

class BleDisconnect(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLEDISCONNECT

  # @@protoc_insertion_point(class_scope:BleDisconnect)

class ConnectResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONNECTRESULT

  # @@protoc_insertion_point(class_scope:ConnectResult)

class ProxyData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROXYDATA

  # @@protoc_insertion_point(class_scope:ProxyData)

class BleProxyMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLEPROXYMSG

  # @@protoc_insertion_point(class_scope:BleProxyMsg)


# @@protoc_insertion_point(module_scope)