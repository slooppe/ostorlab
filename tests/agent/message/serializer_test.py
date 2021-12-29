"""Tests for serializer module."""
import pytest

from ostorlab.agent.message import serializer


def testSerializeRequest_withFileFingerprint_returnsCorrectProtobufMessage():
    """Test message proper seralization from a dict object to a protobuf based on the selector."""
    serialized = serializer.serialize('v3.fingerprint.file', {
        'path': '/etc/hosts',
    })

    assert serialized.path == '/etc/hosts'


def testSerializeRequest_withIncorrectDict_throwsError():
    """Test message serialization error if passed fields are not present in the message definition."""
    with pytest.raises(serializer.SerializationError):
        serializer.serialize('v3.fingerprint.file', {
            'path': '/etc/hosts',
            'random': 'error'
        })


def testSerializeRequest_withMissingSelector_throwsError():
    """Test message serialization error if passed fields are not present in the message definition."""
    with pytest.raises(serializer.SerializationError):
        serializer.serialize('v3.random.foo.bar', {
            'path': '/etc/hosts',
            'random': 'error'
        })


def testDeserializeRequest_withFileFingerprint_returnsCorrectObjects():
    """Test message proper deserialization based on the selector."""
    serialized = serializer.serialize('v3.fingerprint.file', {
        'path': '/etc/hosts',
    })

    deserialized_object = serializer.deserialize('v3.fingerprint.file', serialized.SerializeToString())

    assert deserialized_object.path == '/etc/hosts'


def testDeserializeRequest_withIncorrectSelector_throwsError():
    """Test message deserialization error with incorrect selector."""
    with pytest.raises(AttributeError):
        serialized = serializer.serialize('v3.fingerprint.file', {
            'path': '/etc/hosts',
        })

        serializer.deserialize('v3.capture.logs', serialized.SerializeToString())
