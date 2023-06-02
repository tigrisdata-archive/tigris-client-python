from ...google.api import annotations_pb2 as _annotations_pb2
from ...openapiv3 import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ABORTED: Code
ALL: TigrisOperation
ALREADY_EXISTS: Code
AVG: MetricQuerySpaceAggregation
BAD_GATEWAY: Code
CANCELLED: Code
CONFLICT: Code
CONTENT_TOO_LARGE: Code
COUNT: MetricQueryFunction
DATA_LOSS: Code
DEADLINE_EXCEEDED: Code
DESCRIPTOR: _descriptor.FileDescriptor
FAILED_PRECONDITION: Code
INTERNAL: Code
INVALID_ARGUMENT: Code
MAX: MetricQuerySpaceAggregation
METADATA: TigrisOperation
METHOD_NOT_ALLOWED: Code
MIN: MetricQuerySpaceAggregation
NONE: MetricQueryFunction
NOT_FOUND: Code
OK: Code
OUT_OF_RANGE: Code
PERMISSION_DENIED: Code
RATE: MetricQueryFunction
READ: TigrisOperation
RESOURCE_EXHAUSTED: Code
ROLLUP_AGGREGATOR_AVG: RollupAggregator
ROLLUP_AGGREGATOR_COUNT: RollupAggregator
ROLLUP_AGGREGATOR_MAX: RollupAggregator
ROLLUP_AGGREGATOR_MIN: RollupAggregator
ROLLUP_AGGREGATOR_SUM: RollupAggregator
SUM: MetricQuerySpaceAggregation
UNAUTHENTICATED: Code
UNAVAILABLE: Code
UNIMPLEMENTED: Code
UNKNOWN: Code
WRITE: TigrisOperation

class AdditionalFunction(_message.Message):
    __slots__ = ["rollup"]
    ROLLUP_FIELD_NUMBER: _ClassVar[int]
    rollup: RollupFunction
    def __init__(self, rollup: _Optional[_Union[RollupFunction, _Mapping]] = ...) -> None: ...

class DataPoint(_message.Message):
    __slots__ = ["timestamp", "value"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    value: float
    def __init__(self, timestamp: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: Code
    message: str
    def __init__(self, code: _Optional[_Union[Code, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ErrorDetails(_message.Message):
    __slots__ = ["code", "message", "retry"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    retry: RetryInfo
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., retry: _Optional[_Union[RetryInfo, _Mapping]] = ...) -> None: ...

class GetInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ["error", "server_version"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: Error
    server_version: str
    def __init__(self, server_version: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class MetricSeries(_message.Message):
    __slots__ = ["dataPoints", "metric", "scope", "to"]
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    dataPoints: _containers.RepeatedCompositeFieldContainer[DataPoint]
    metric: str
    scope: str
    to: int
    def __init__(self, to: _Optional[int] = ..., metric: _Optional[str] = ..., scope: _Optional[str] = ..., dataPoints: _Optional[_Iterable[_Union[DataPoint, _Mapping]]] = ..., **kwargs) -> None: ...

class QueryTimeSeriesMetricsRequest(_message.Message):
    __slots__ = ["additionalFunctions", "branch", "collection", "db", "function", "metric_name", "quantile", "space_aggregated_by", "space_aggregation", "tigris_operation", "to"]
    ADDITIONALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DB_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    SPACE_AGGREGATED_BY_FIELD_NUMBER: _ClassVar[int]
    SPACE_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    TIGRIS_OPERATION_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    additionalFunctions: _containers.RepeatedCompositeFieldContainer[AdditionalFunction]
    branch: str
    collection: str
    db: str
    function: MetricQueryFunction
    metric_name: str
    quantile: float
    space_aggregated_by: _containers.RepeatedScalarFieldContainer[str]
    space_aggregation: MetricQuerySpaceAggregation
    tigris_operation: TigrisOperation
    to: int
    def __init__(self, db: _Optional[str] = ..., branch: _Optional[str] = ..., collection: _Optional[str] = ..., to: _Optional[int] = ..., metric_name: _Optional[str] = ..., tigris_operation: _Optional[_Union[TigrisOperation, str]] = ..., space_aggregation: _Optional[_Union[MetricQuerySpaceAggregation, str]] = ..., space_aggregated_by: _Optional[_Iterable[str]] = ..., function: _Optional[_Union[MetricQueryFunction, str]] = ..., quantile: _Optional[float] = ..., additionalFunctions: _Optional[_Iterable[_Union[AdditionalFunction, _Mapping]]] = ..., **kwargs) -> None: ...

class QueryTimeSeriesMetricsResponse(_message.Message):
    __slots__ = ["query", "series", "to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    query: str
    series: _containers.RepeatedCompositeFieldContainer[MetricSeries]
    to: int
    def __init__(self, to: _Optional[int] = ..., query: _Optional[str] = ..., series: _Optional[_Iterable[_Union[MetricSeries, _Mapping]]] = ..., **kwargs) -> None: ...

class QuotaLimitsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QuotaLimitsResponse(_message.Message):
    __slots__ = ["ReadUnits", "StorageSize", "WriteUnits"]
    READUNITS_FIELD_NUMBER: _ClassVar[int]
    ReadUnits: int
    STORAGESIZE_FIELD_NUMBER: _ClassVar[int]
    StorageSize: int
    WRITEUNITS_FIELD_NUMBER: _ClassVar[int]
    WriteUnits: int
    def __init__(self, ReadUnits: _Optional[int] = ..., WriteUnits: _Optional[int] = ..., StorageSize: _Optional[int] = ...) -> None: ...

class QuotaUsageRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QuotaUsageResponse(_message.Message):
    __slots__ = ["ReadUnits", "ReadUnitsThrottled", "StorageSize", "StorageSizeThrottled", "WriteUnits", "WriteUnitsThrottled"]
    READUNITSTHROTTLED_FIELD_NUMBER: _ClassVar[int]
    READUNITS_FIELD_NUMBER: _ClassVar[int]
    ReadUnits: int
    ReadUnitsThrottled: int
    STORAGESIZETHROTTLED_FIELD_NUMBER: _ClassVar[int]
    STORAGESIZE_FIELD_NUMBER: _ClassVar[int]
    StorageSize: int
    StorageSizeThrottled: int
    WRITEUNITSTHROTTLED_FIELD_NUMBER: _ClassVar[int]
    WRITEUNITS_FIELD_NUMBER: _ClassVar[int]
    WriteUnits: int
    WriteUnitsThrottled: int
    def __init__(self, ReadUnits: _Optional[int] = ..., WriteUnits: _Optional[int] = ..., StorageSize: _Optional[int] = ..., ReadUnitsThrottled: _Optional[int] = ..., WriteUnitsThrottled: _Optional[int] = ..., StorageSizeThrottled: _Optional[int] = ...) -> None: ...

class RetryInfo(_message.Message):
    __slots__ = ["delay"]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    delay: int
    def __init__(self, delay: _Optional[int] = ...) -> None: ...

class RollupFunction(_message.Message):
    __slots__ = ["aggregator", "interval"]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    aggregator: RollupAggregator
    interval: int
    def __init__(self, aggregator: _Optional[_Union[RollupAggregator, str]] = ..., interval: _Optional[int] = ...) -> None: ...

class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TigrisOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MetricQueryFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RollupAggregator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MetricQuerySpaceAggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
