# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scan_stop.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='scan_stop.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b('\n\x0fscan_stop.proto\"\x1c\n\tscan_stop\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05')
)

_SCAN_STOP = _descriptor.Descriptor(
    name='scan_stop',
    full_name='scan_stop',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='scan_stop.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=19,
    serialized_end=47,
)

DESCRIPTOR.message_types_by_name['scan_stop'] = _SCAN_STOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

scan_stop = _reflection.GeneratedProtocolMessageType('scan_stop', (_message.Message,), dict(
    DESCRIPTOR=_SCAN_STOP,
    __module__='scan_stop_pb2'
    # @@protoc_insertion_point(class_scope:scan_stop)
))
_sym_db.RegisterMessage(scan_stop)

# @@protoc_insertion_point(module_scope)