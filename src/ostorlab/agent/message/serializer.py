"""Serializer handles matching of selector to the proper protobuf message definition."""
import importlib
import os
import pathlib
import re
from typing import Dict, Optional, List, Any

from google.protobuf import json_format

from ostorlab import exceptions

PROTO_CLASS_NAME = 'Message'

MESSAGE_PROTO = '.proto'
MESSAGE_CODE_PATH = pathlib.Path(__file__).parent / 'proto'


class SerializationError(exceptions.OstorlabError):
    """Base serialization Error."""


class TooManyMatchingPackageNamesError(SerializationError):
    """There are over 2 matching package names."""


class NoMatchingPackageNameError(SerializationError):
    """There are no matching package name."""


def _find_package_name(selector: str) -> Optional[str]:
    """Finds matching package name to selector."""
    files = _list_message_proto_files()
    pattern = re.compile(_selector_to_package_regex(selector))
    matching = [pattern.match(f) for f in files]
    filtered_matching = [m.group(0) for m in matching if m is not None]
    if len(filtered_matching) > 1:
        raise TooManyMatchingPackageNamesError()
    elif len(filtered_matching) == 0:
        raise NoMatchingPackageNameError()
    else:
        # Remove the path to the current package.
        matching_package = re.sub(r'^.*/ostorlab/', 'ostorlab/', filtered_matching[0])
        # Replace / with .
        matching_package = matching_package.replace('/', '.')
        # Point to the compiled protobufs.
        return re.sub(r'\.proto$', '_pb2', re.sub(r'^\.code\.', '', matching_package))


def _list_message_proto_files() -> List[str]:
    """List all the proto files."""
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(MESSAGE_CODE_PATH):
        for file in f:
            if MESSAGE_PROTO in file:
                files.append(os.path.join(r, file))
        del d
    return files


def _selector_to_package_regex(subject):
    """Maps selector to package matching regular expression."""
    splitted = subject.split('.')
    return '.*/message/proto/' + '/'.join([f'(_[_a-zA-Z0-9]+|{s})' for s in splitted]) + r'.[_a-zA-Z0-9]+\.proto'


def serialize(selector: str, message: Dict[str, Any]):
    """Serializes a Request message using the proper format defined using the seelctor value.
    If the subject is a.b.c. The corresponding proto is located at message/a/b/c/xxx.proto.

    Args:
        selector: Message selector, must specify the version in use.
        message: Dict representation of the message to serialize.

    Returns:
        Proto serialized message.
    """
    try:
        return _serialize(selector, PROTO_CLASS_NAME, message)
    except json_format.Error as e:
        raise SerializationError('Error serializing message') from e


def _serialize(selector: str, class_name: str, message: Dict[str, Any]):
    """Serializes message using the selector and defined class name."""
    package_name = _find_package_name(selector)
    class_object = getattr(importlib.import_module(package_name), class_name)
    proto_message = class_object()
    json_format.ParseDict(message, proto_message)
    return proto_message


def deserialize(selector: str, serialized: bytes):
    """Deserializes a Request message using the proper format defined using the selector value.

    Args:
        selector: Message selector, must specify the version in use.
        serialized: Raw message to deserialize.

    Returns:
        Dict
    """
    return _deserialize(selector, PROTO_CLASS_NAME, serialized)


def _deserialize(selector: str, class_name: str, serialized: bytes):
    """Deserializes message using the selector and defined class name."""
    package_name = _find_package_name(selector)
    class_object = getattr(importlib.import_module(package_name), class_name)
    proto_message = class_object()
    proto_message.ParseFromString(serialized)
    return proto_message