# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='file.proto',
    package='',
    serialized_pb=_b(
        '\n\nfile.proto\">\n\x04\x66ile\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x10\n\x08\x66ilename\x18\x02 \x02(\t\x12\x13\n\x0b\x66ilecontent\x18\x03 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FILE = _descriptor.Descriptor(
    name='file',
    full_name='file',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='file.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='filename', full_name='file.filename', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='filecontent', full_name='file.filecontent', index=2,
            number=3, type=12, cpp_type=9, label=2,
            has_default_value=False, default_value=_b(""),
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
    oneofs=[
    ],
    serialized_start=14,
    serialized_end=76,
)

DESCRIPTOR.message_types_by_name['file'] = _FILE

file = _reflection.GeneratedProtocolMessageType('file', (_message.Message,), dict(
    DESCRIPTOR=_FILE,
    __module__='file_pb2'
    # @@protoc_insertion_point(class_scope:file)
))
_sym_db.RegisterMessage(file)

# @@protoc_insertion_point(module_scope)