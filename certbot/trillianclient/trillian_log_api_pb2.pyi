from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
import trillian_pb2 as _trillian_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChargeTo(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user: _Optional[_Iterable[str]] = ...) -> None: ...

class QueueLeafRequest(_message.Message):
    __slots__ = ("log_id", "leaf", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    leaf: LogLeaf
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., leaf: _Optional[_Union[LogLeaf, _Mapping]] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class QueueLeafResponse(_message.Message):
    __slots__ = ("queued_leaf",)
    QUEUED_LEAF_FIELD_NUMBER: _ClassVar[int]
    queued_leaf: QueuedLogLeaf
    def __init__(self, queued_leaf: _Optional[_Union[QueuedLogLeaf, _Mapping]] = ...) -> None: ...

class GetInclusionProofRequest(_message.Message):
    __slots__ = ("log_id", "leaf_index", "tree_size", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_INDEX_FIELD_NUMBER: _ClassVar[int]
    TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    leaf_index: int
    tree_size: int
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., leaf_index: _Optional[int] = ..., tree_size: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class GetInclusionProofResponse(_message.Message):
    __slots__ = ("proof", "signed_log_root")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    proof: _trillian_pb2.Proof
    signed_log_root: _trillian_pb2.SignedLogRoot
    def __init__(self, proof: _Optional[_Union[_trillian_pb2.Proof, _Mapping]] = ..., signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class GetInclusionProofByHashRequest(_message.Message):
    __slots__ = ("log_id", "leaf_hash", "tree_size", "order_by_sequence", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_HASH_FIELD_NUMBER: _ClassVar[int]
    TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    leaf_hash: bytes
    tree_size: int
    order_by_sequence: bool
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., leaf_hash: _Optional[bytes] = ..., tree_size: _Optional[int] = ..., order_by_sequence: bool = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class GetInclusionProofByHashResponse(_message.Message):
    __slots__ = ("proof", "signed_log_root")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    proof: _containers.RepeatedCompositeFieldContainer[_trillian_pb2.Proof]
    signed_log_root: _trillian_pb2.SignedLogRoot
    def __init__(self, proof: _Optional[_Iterable[_Union[_trillian_pb2.Proof, _Mapping]]] = ..., signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class GetConsistencyProofRequest(_message.Message):
    __slots__ = ("log_id", "first_tree_size", "second_tree_size", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SECOND_TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    first_tree_size: int
    second_tree_size: int
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., first_tree_size: _Optional[int] = ..., second_tree_size: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class GetConsistencyProofResponse(_message.Message):
    __slots__ = ("proof", "signed_log_root")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    proof: _trillian_pb2.Proof
    signed_log_root: _trillian_pb2.SignedLogRoot
    def __init__(self, proof: _Optional[_Union[_trillian_pb2.Proof, _Mapping]] = ..., signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class GetLatestSignedLogRootRequest(_message.Message):
    __slots__ = ("log_id", "charge_to", "first_tree_size")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    FIRST_TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    charge_to: ChargeTo
    first_tree_size: int
    def __init__(self, log_id: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ..., first_tree_size: _Optional[int] = ...) -> None: ...

class GetLatestSignedLogRootResponse(_message.Message):
    __slots__ = ("signed_log_root", "proof")
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    signed_log_root: _trillian_pb2.SignedLogRoot
    proof: _trillian_pb2.Proof
    def __init__(self, signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ..., proof: _Optional[_Union[_trillian_pb2.Proof, _Mapping]] = ...) -> None: ...

class GetEntryAndProofRequest(_message.Message):
    __slots__ = ("log_id", "leaf_index", "tree_size", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_INDEX_FIELD_NUMBER: _ClassVar[int]
    TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    leaf_index: int
    tree_size: int
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., leaf_index: _Optional[int] = ..., tree_size: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class GetEntryAndProofResponse(_message.Message):
    __slots__ = ("proof", "leaf", "signed_log_root")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    LEAF_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    proof: _trillian_pb2.Proof
    leaf: LogLeaf
    signed_log_root: _trillian_pb2.SignedLogRoot
    def __init__(self, proof: _Optional[_Union[_trillian_pb2.Proof, _Mapping]] = ..., leaf: _Optional[_Union[LogLeaf, _Mapping]] = ..., signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class InitLogRequest(_message.Message):
    __slots__ = ("log_id", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class InitLogResponse(_message.Message):
    __slots__ = ("created",)
    CREATED_FIELD_NUMBER: _ClassVar[int]
    created: _trillian_pb2.SignedLogRoot
    def __init__(self, created: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class AddSequencedLeavesRequest(_message.Message):
    __slots__ = ("log_id", "leaves", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    LEAVES_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    leaves: _containers.RepeatedCompositeFieldContainer[LogLeaf]
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., leaves: _Optional[_Iterable[_Union[LogLeaf, _Mapping]]] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class AddSequencedLeavesResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[QueuedLogLeaf]
    def __init__(self, results: _Optional[_Iterable[_Union[QueuedLogLeaf, _Mapping]]] = ...) -> None: ...

class GetLeavesByRangeRequest(_message.Message):
    __slots__ = ("log_id", "start_index", "count", "charge_to")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CHARGE_TO_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    start_index: int
    count: int
    charge_to: ChargeTo
    def __init__(self, log_id: _Optional[int] = ..., start_index: _Optional[int] = ..., count: _Optional[int] = ..., charge_to: _Optional[_Union[ChargeTo, _Mapping]] = ...) -> None: ...

class GetLeavesByRangeResponse(_message.Message):
    __slots__ = ("leaves", "signed_log_root")
    LEAVES_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LOG_ROOT_FIELD_NUMBER: _ClassVar[int]
    leaves: _containers.RepeatedCompositeFieldContainer[LogLeaf]
    signed_log_root: _trillian_pb2.SignedLogRoot
    def __init__(self, leaves: _Optional[_Iterable[_Union[LogLeaf, _Mapping]]] = ..., signed_log_root: _Optional[_Union[_trillian_pb2.SignedLogRoot, _Mapping]] = ...) -> None: ...

class QueuedLogLeaf(_message.Message):
    __slots__ = ("leaf", "status")
    LEAF_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    leaf: LogLeaf
    status: _status_pb2.Status
    def __init__(self, leaf: _Optional[_Union[LogLeaf, _Mapping]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class LogLeaf(_message.Message):
    __slots__ = ("merkle_leaf_hash", "leaf_value", "extra_data", "leaf_index", "leaf_identity_hash", "queue_timestamp", "integrate_timestamp")
    MERKLE_LEAF_HASH_FIELD_NUMBER: _ClassVar[int]
    LEAF_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    LEAF_INDEX_FIELD_NUMBER: _ClassVar[int]
    LEAF_IDENTITY_HASH_FIELD_NUMBER: _ClassVar[int]
    QUEUE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INTEGRATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    merkle_leaf_hash: bytes
    leaf_value: bytes
    extra_data: bytes
    leaf_index: int
    leaf_identity_hash: bytes
    queue_timestamp: _timestamp_pb2.Timestamp
    integrate_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, merkle_leaf_hash: _Optional[bytes] = ..., leaf_value: _Optional[bytes] = ..., extra_data: _Optional[bytes] = ..., leaf_index: _Optional[int] = ..., leaf_identity_hash: _Optional[bytes] = ..., queue_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., integrate_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
