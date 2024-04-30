from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogRootFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_ROOT_FORMAT_UNKNOWN: _ClassVar[LogRootFormat]
    LOG_ROOT_FORMAT_V1: _ClassVar[LogRootFormat]

class HashStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_HASH_STRATEGY: _ClassVar[HashStrategy]
    RFC6962_SHA256: _ClassVar[HashStrategy]
    TEST_MAP_HASHER: _ClassVar[HashStrategy]
    OBJECT_RFC6962_SHA256: _ClassVar[HashStrategy]
    CONIKS_SHA512_256: _ClassVar[HashStrategy]
    CONIKS_SHA256: _ClassVar[HashStrategy]

class TreeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TREE_STATE: _ClassVar[TreeState]
    ACTIVE: _ClassVar[TreeState]
    FROZEN: _ClassVar[TreeState]
    DEPRECATED_SOFT_DELETED: _ClassVar[TreeState]
    DEPRECATED_HARD_DELETED: _ClassVar[TreeState]
    DRAINING: _ClassVar[TreeState]

class TreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TREE_TYPE: _ClassVar[TreeType]
    LOG: _ClassVar[TreeType]
    PREORDERED_LOG: _ClassVar[TreeType]
LOG_ROOT_FORMAT_UNKNOWN: LogRootFormat
LOG_ROOT_FORMAT_V1: LogRootFormat
UNKNOWN_HASH_STRATEGY: HashStrategy
RFC6962_SHA256: HashStrategy
TEST_MAP_HASHER: HashStrategy
OBJECT_RFC6962_SHA256: HashStrategy
CONIKS_SHA512_256: HashStrategy
CONIKS_SHA256: HashStrategy
UNKNOWN_TREE_STATE: TreeState
ACTIVE: TreeState
FROZEN: TreeState
DEPRECATED_SOFT_DELETED: TreeState
DEPRECATED_HARD_DELETED: TreeState
DRAINING: TreeState
UNKNOWN_TREE_TYPE: TreeType
LOG: TreeType
PREORDERED_LOG: TreeType

class Tree(_message.Message):
    __slots__ = ("tree_id", "tree_state", "tree_type", "display_name", "description", "storage_settings", "max_root_duration", "create_time", "update_time", "deleted", "delete_time")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_STATE_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_ROOT_DURATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    tree_state: TreeState
    tree_type: TreeType
    display_name: str
    description: str
    storage_settings: _any_pb2.Any
    max_root_duration: _duration_pb2.Duration
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    deleted: bool
    delete_time: _timestamp_pb2.Timestamp
    def __init__(self, tree_id: _Optional[int] = ..., tree_state: _Optional[_Union[TreeState, str]] = ..., tree_type: _Optional[_Union[TreeType, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., storage_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., max_root_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SignedLogRoot(_message.Message):
    __slots__ = ("log_root",)
    LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    log_root: bytes
    def __init__(self, log_root: _Optional[bytes] = ...) -> None: ...

class Proof(_message.Message):
    __slots__ = ("leaf_index", "hashes")
    LEAF_INDEX_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    leaf_index: int
    hashes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, leaf_index: _Optional[int] = ..., hashes: _Optional[_Iterable[bytes]] = ...) -> None: ...
