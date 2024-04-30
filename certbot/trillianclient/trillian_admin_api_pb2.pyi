import trillian_pb2 as _trillian_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTreesRequest(_message.Message):
    __slots__ = ("show_deleted",)
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    show_deleted: bool
    def __init__(self, show_deleted: bool = ...) -> None: ...

class ListTreesResponse(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _containers.RepeatedCompositeFieldContainer[_trillian_pb2.Tree]
    def __init__(self, tree: _Optional[_Iterable[_Union[_trillian_pb2.Tree, _Mapping]]] = ...) -> None: ...

class GetTreeRequest(_message.Message):
    __slots__ = ("tree_id",)
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    def __init__(self, tree_id: _Optional[int] = ...) -> None: ...

class CreateTreeRequest(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _trillian_pb2.Tree
    def __init__(self, tree: _Optional[_Union[_trillian_pb2.Tree, _Mapping]] = ...) -> None: ...

class UpdateTreeRequest(_message.Message):
    __slots__ = ("tree", "update_mask")
    TREE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tree: _trillian_pb2.Tree
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tree: _Optional[_Union[_trillian_pb2.Tree, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteTreeRequest(_message.Message):
    __slots__ = ("tree_id",)
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    def __init__(self, tree_id: _Optional[int] = ...) -> None: ...

class UndeleteTreeRequest(_message.Message):
    __slots__ = ("tree_id",)
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    def __init__(self, tree_id: _Optional[int] = ...) -> None: ...
