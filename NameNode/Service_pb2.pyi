from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Create(_message.Message):
    __slots__ = ("file_name", "num_partitions", "size")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    num_partitions: int
    size: int
    def __init__(self, file_name: _Optional[str] = ..., num_partitions: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("partitions", "status_code")
    class PartitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.ScalarMap[str, str]
    status_code: int
    def __init__(self, partitions: _Optional[_Mapping[str, str]] = ..., status_code: _Optional[int] = ...) -> None: ...
