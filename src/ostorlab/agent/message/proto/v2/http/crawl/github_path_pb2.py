# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github_path.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='github_path.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x11github_path.proto\"G\n\x0bgithub_path\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0b\n\x03org\x18\x02 \x02(\t\x12\x0c\n\x04repo\x18\x03 \x02(\t\x12\x0c\n\x04path\x18\x04 \x02(\t')
)

_GITHUB_PATH = _descriptor.Descriptor(
    name='github_path',
    full_name='github_path',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='github_path.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='org', full_name='github_path.org', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='repo', full_name='github_path.repo', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='path', full_name='github_path.path', index=3,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    serialized_start=21,
    serialized_end=92,
)

DESCRIPTOR.message_types_by_name['github_path'] = _GITHUB_PATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

github_path = _reflection.GeneratedProtocolMessageType('github_path', (_message.Message,), dict(
    DESCRIPTOR=_GITHUB_PATH,
    __module__='github_path_pb2'
    # @@protoc_insertion_point(class_scope:github_path)
))
_sym_db.RegisterMessage(github_path)

# @@protoc_insertion_point(module_scope)