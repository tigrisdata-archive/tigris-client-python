from ...google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ...openapiv3 import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppKey(_message.Message):
    __slots__ = ["created_at", "created_by", "description", "id", "name", "project", "secret", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    created_by: str
    description: str
    id: str
    name: str
    project: str
    secret: str
    updated_at: int
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., secret: _Optional[str] = ..., created_at: _Optional[int] = ..., created_by: _Optional[str] = ..., updated_at: _Optional[int] = ..., updated_by: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class BeginTransactionRequest(_message.Message):
    __slots__ = ["branch", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    options: TransactionOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., options: _Optional[_Union[TransactionOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class BeginTransactionResponse(_message.Message):
    __slots__ = ["tx_ctx"]
    TX_CTX_FIELD_NUMBER: _ClassVar[int]
    tx_ctx: TransactionCtx
    def __init__(self, tx_ctx: _Optional[_Union[TransactionCtx, _Mapping]] = ...) -> None: ...

class BranchInfo(_message.Message):
    __slots__ = ["branch", "metadata"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    branch: str
    metadata: BranchMetadata
    def __init__(self, branch: _Optional[str] = ..., metadata: _Optional[_Union[BranchMetadata, _Mapping]] = ...) -> None: ...

class BranchMetadata(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class BuildCollectionIndexRequest(_message.Message):
    __slots__ = ["branch", "collection", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class BuildCollectionIndexResponse(_message.Message):
    __slots__ = ["indexes"]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[CollectionIndex]
    def __init__(self, indexes: _Optional[_Iterable[_Union[CollectionIndex, _Mapping]]] = ...) -> None: ...

class Collation(_message.Message):
    __slots__ = ["case"]
    CASE_FIELD_NUMBER: _ClassVar[int]
    case: str
    def __init__(self, case: _Optional[str] = ...) -> None: ...

class CollectionDescription(_message.Message):
    __slots__ = ["collection", "indexes", "metadata", "schema", "size"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    collection: str
    indexes: _containers.RepeatedCompositeFieldContainer[CollectionIndex]
    metadata: CollectionMetadata
    schema: bytes
    size: int
    def __init__(self, collection: _Optional[str] = ..., metadata: _Optional[_Union[CollectionMetadata, _Mapping]] = ..., schema: _Optional[bytes] = ..., size: _Optional[int] = ..., indexes: _Optional[_Iterable[_Union[CollectionIndex, _Mapping]]] = ...) -> None: ...

class CollectionIndex(_message.Message):
    __slots__ = ["fields", "name", "state"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    name: str
    state: str
    def __init__(self, name: _Optional[str] = ..., state: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ["collection", "metadata"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    collection: str
    metadata: CollectionMetadata
    def __init__(self, collection: _Optional[str] = ..., metadata: _Optional[_Union[CollectionMetadata, _Mapping]] = ...) -> None: ...

class CollectionMetadata(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CollectionOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CommitTransactionRequest(_message.Message):
    __slots__ = ["branch", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    project: str
    def __init__(self, project: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class CommitTransactionResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class CountRequest(_message.Message):
    __slots__ = ["branch", "collection", "filter", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    filter: bytes
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., filter: _Optional[bytes] = ..., branch: _Optional[str] = ...) -> None: ...

class CountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CreateAppKeyRequest(_message.Message):
    __slots__ = ["description", "name", "project"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    project: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class CreateAppKeyResponse(_message.Message):
    __slots__ = ["created_app_key"]
    CREATED_APP_KEY_FIELD_NUMBER: _ClassVar[int]
    created_app_key: AppKey
    def __init__(self, created_app_key: _Optional[_Union[AppKey, _Mapping]] = ...) -> None: ...

class CreateBranchRequest(_message.Message):
    __slots__ = ["branch", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    project: str
    def __init__(self, project: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class CreateBranchResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class CreateOrUpdateCollectionRequest(_message.Message):
    __slots__ = ["branch", "collection", "only_create", "options", "project", "schema"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    ONLY_CREATE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    only_create: bool
    options: CollectionOptions
    project: str
    schema: bytes
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., schema: _Optional[bytes] = ..., only_create: bool = ..., options: _Optional[_Union[CollectionOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class CreateOrUpdateCollectionResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DatabaseMetadata(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DatabaseOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAppKeyRequest(_message.Message):
    __slots__ = ["id", "project"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    id: str
    project: str
    def __init__(self, id: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class DeleteAppKeyResponse(_message.Message):
    __slots__ = ["deleted"]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class DeleteBranchRequest(_message.Message):
    __slots__ = ["branch", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    project: str
    def __init__(self, project: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class DeleteBranchResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["branch", "collection", "filter", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    filter: bytes
    options: DeleteRequestOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., filter: _Optional[bytes] = ..., options: _Optional[_Union[DeleteRequestOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class DeleteRequestOptions(_message.Message):
    __slots__ = ["collation", "limit", "write_options"]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    WRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    collation: Collation
    limit: int
    write_options: WriteOptions
    def __init__(self, write_options: _Optional[_Union[WriteOptions, _Mapping]] = ..., collation: _Optional[_Union[Collation, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ["deleted_count", "metadata", "status"]
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    deleted_count: int
    metadata: ResponseMetadata
    status: str
    def __init__(self, metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., status: _Optional[str] = ..., deleted_count: _Optional[int] = ...) -> None: ...

class DescribeCollectionRequest(_message.Message):
    __slots__ = ["branch", "collection", "options", "project", "schema_format"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    options: CollectionOptions
    project: str
    schema_format: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., schema_format: _Optional[str] = ..., options: _Optional[_Union[CollectionOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class DescribeCollectionResponse(_message.Message):
    __slots__ = ["collection", "indexes", "metadata", "schema", "size"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    collection: str
    indexes: _containers.RepeatedCompositeFieldContainer[CollectionIndex]
    metadata: CollectionMetadata
    schema: bytes
    size: int
    def __init__(self, collection: _Optional[str] = ..., metadata: _Optional[_Union[CollectionMetadata, _Mapping]] = ..., schema: _Optional[bytes] = ..., size: _Optional[int] = ..., indexes: _Optional[_Iterable[_Union[CollectionIndex, _Mapping]]] = ...) -> None: ...

class DescribeDatabaseRequest(_message.Message):
    __slots__ = ["branch", "project", "schema_format"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    project: str
    schema_format: str
    def __init__(self, project: _Optional[str] = ..., schema_format: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class DescribeDatabaseResponse(_message.Message):
    __slots__ = ["branches", "collections", "metadata", "size"]
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedScalarFieldContainer[str]
    collections: _containers.RepeatedCompositeFieldContainer[CollectionDescription]
    metadata: DatabaseMetadata
    size: int
    def __init__(self, metadata: _Optional[_Union[DatabaseMetadata, _Mapping]] = ..., collections: _Optional[_Iterable[_Union[CollectionDescription, _Mapping]]] = ..., size: _Optional[int] = ..., branches: _Optional[_Iterable[str]] = ...) -> None: ...

class DropCollectionRequest(_message.Message):
    __slots__ = ["branch", "collection", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    options: CollectionOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., options: _Optional[_Union[CollectionOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class DropCollectionResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class ExplainResponse(_message.Message):
    __slots__ = ["collection", "field", "filter", "key_range", "read_type", "sorting"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGE_FIELD_NUMBER: _ClassVar[int]
    READ_TYPE_FIELD_NUMBER: _ClassVar[int]
    SORTING_FIELD_NUMBER: _ClassVar[int]
    collection: str
    field: str
    filter: str
    key_range: _containers.RepeatedScalarFieldContainer[str]
    read_type: str
    sorting: str
    def __init__(self, collection: _Optional[str] = ..., read_type: _Optional[str] = ..., filter: _Optional[str] = ..., sorting: _Optional[str] = ..., key_range: _Optional[_Iterable[str]] = ..., field: _Optional[str] = ...) -> None: ...

class FacetCount(_message.Message):
    __slots__ = ["count", "value"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    count: int
    value: str
    def __init__(self, count: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class FacetStats(_message.Message):
    __slots__ = ["avg", "count", "max", "min", "sum"]
    AVG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    avg: float
    count: int
    max: float
    min: float
    sum: float
    def __init__(self, avg: _Optional[float] = ..., max: _Optional[float] = ..., min: _Optional[float] = ..., sum: _Optional[float] = ..., count: _Optional[int] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GroupedSearchHits(_message.Message):
    __slots__ = ["group_keys", "hits"]
    GROUP_KEYS_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    group_keys: _containers.RepeatedScalarFieldContainer[str]
    hits: _containers.RepeatedCompositeFieldContainer[SearchHit]
    def __init__(self, group_keys: _Optional[_Iterable[str]] = ..., hits: _Optional[_Iterable[_Union[SearchHit, _Mapping]]] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ["autogenerated", "branch", "collection", "create_collection", "documents", "options", "primary_key", "project"]
    AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    autogenerated: _containers.RepeatedScalarFieldContainer[str]
    branch: str
    collection: str
    create_collection: bool
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    options: ImportRequestOptions
    primary_key: _containers.RepeatedScalarFieldContainer[str]
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ..., options: _Optional[_Union[ImportRequestOptions, _Mapping]] = ..., branch: _Optional[str] = ..., create_collection: bool = ..., primary_key: _Optional[_Iterable[str]] = ..., autogenerated: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportRequestOptions(_message.Message):
    __slots__ = ["write_options"]
    WRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    write_options: WriteOptions
    def __init__(self, write_options: _Optional[_Union[WriteOptions, _Mapping]] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ["keys", "metadata", "status"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    metadata: ResponseMetadata
    status: str
    def __init__(self, metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., status: _Optional[str] = ..., keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class InsertRequest(_message.Message):
    __slots__ = ["branch", "collection", "documents", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    options: InsertRequestOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ..., options: _Optional[_Union[InsertRequestOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class InsertRequestOptions(_message.Message):
    __slots__ = ["write_options"]
    WRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    write_options: WriteOptions
    def __init__(self, write_options: _Optional[_Union[WriteOptions, _Mapping]] = ...) -> None: ...

class InsertResponse(_message.Message):
    __slots__ = ["keys", "metadata", "status"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    metadata: ResponseMetadata
    status: str
    def __init__(self, metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., status: _Optional[str] = ..., keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ListAppKeysRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class ListAppKeysResponse(_message.Message):
    __slots__ = ["app_keys"]
    APP_KEYS_FIELD_NUMBER: _ClassVar[int]
    app_keys: _containers.RepeatedCompositeFieldContainer[AppKey]
    def __init__(self, app_keys: _Optional[_Iterable[_Union[AppKey, _Mapping]]] = ...) -> None: ...

class ListBranchesRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class ListBranchesResponse(_message.Message):
    __slots__ = ["branches"]
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedCompositeFieldContainer[BranchInfo]
    def __init__(self, branches: _Optional[_Iterable[_Union[BranchInfo, _Mapping]]] = ...) -> None: ...

class ListCollectionsRequest(_message.Message):
    __slots__ = ["branch", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    options: CollectionOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., options: _Optional[_Union[CollectionOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class ListCollectionsResponse(_message.Message):
    __slots__ = ["collections"]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[CollectionInfo]
    def __init__(self, collections: _Optional[_Iterable[_Union[CollectionInfo, _Mapping]]] = ...) -> None: ...

class ListProjectsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListProjectsResponse(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[ProjectInfo]
    def __init__(self, projects: _Optional[_Iterable[_Union[ProjectInfo, _Mapping]]] = ...) -> None: ...

class Match(_message.Message):
    __slots__ = ["fields", "score", "vector_distance"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    VECTOR_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[MatchField]
    score: str
    vector_distance: float
    def __init__(self, fields: _Optional[_Iterable[_Union[MatchField, _Mapping]]] = ..., score: _Optional[str] = ..., vector_distance: _Optional[float] = ...) -> None: ...

class MatchField(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ["current", "size"]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    current: int
    size: int
    def __init__(self, current: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ProjectDescription(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProjectInfo(_message.Message):
    __slots__ = ["metadata", "project"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    metadata: ProjectMetadata
    project: str
    def __init__(self, project: _Optional[str] = ..., metadata: _Optional[_Union[ProjectMetadata, _Mapping]] = ...) -> None: ...

class ProjectMetadata(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ["branch", "collection", "fields", "filter", "options", "project", "sort"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    fields: bytes
    filter: bytes
    options: ReadRequestOptions
    project: str
    sort: bytes
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., filter: _Optional[bytes] = ..., fields: _Optional[bytes] = ..., options: _Optional[_Union[ReadRequestOptions, _Mapping]] = ..., sort: _Optional[bytes] = ..., branch: _Optional[str] = ...) -> None: ...

class ReadRequestOptions(_message.Message):
    __slots__ = ["collation", "limit", "offset", "skip"]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    collation: Collation
    limit: int
    offset: bytes
    skip: int
    def __init__(self, limit: _Optional[int] = ..., skip: _Optional[int] = ..., offset: _Optional[bytes] = ..., collation: _Optional[_Union[Collation, _Mapping]] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ["data", "metadata", "resume_token"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    metadata: ResponseMetadata
    resume_token: bytes
    def __init__(self, data: _Optional[bytes] = ..., resume_token: _Optional[bytes] = ..., metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ...) -> None: ...

class ReplaceRequest(_message.Message):
    __slots__ = ["branch", "collection", "documents", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    options: ReplaceRequestOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ..., options: _Optional[_Union[ReplaceRequestOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class ReplaceRequestOptions(_message.Message):
    __slots__ = ["write_options"]
    WRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    write_options: WriteOptions
    def __init__(self, write_options: _Optional[_Union[WriteOptions, _Mapping]] = ...) -> None: ...

class ReplaceResponse(_message.Message):
    __slots__ = ["keys", "metadata", "status"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    metadata: ResponseMetadata
    status: str
    def __init__(self, metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., status: _Optional[str] = ..., keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ResponseMetadata(_message.Message):
    __slots__ = ["created_at", "deleted_at", "updated_at"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RollbackTransactionRequest(_message.Message):
    __slots__ = ["branch", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    project: str
    def __init__(self, project: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class RollbackTransactionResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class RotateAppKeyRequest(_message.Message):
    __slots__ = ["id", "project"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    id: str
    project: str
    def __init__(self, id: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class RotateAppKeyResponse(_message.Message):
    __slots__ = ["app_key"]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    app_key: AppKey
    def __init__(self, app_key: _Optional[_Union[AppKey, _Mapping]] = ...) -> None: ...

class SearchFacet(_message.Message):
    __slots__ = ["counts", "stats"]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    counts: _containers.RepeatedCompositeFieldContainer[FacetCount]
    stats: FacetStats
    def __init__(self, counts: _Optional[_Iterable[_Union[FacetCount, _Mapping]]] = ..., stats: _Optional[_Union[FacetStats, _Mapping]] = ...) -> None: ...

class SearchHit(_message.Message):
    __slots__ = ["data", "metadata"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    metadata: SearchHitMeta
    def __init__(self, data: _Optional[bytes] = ..., metadata: _Optional[_Union[SearchHitMeta, _Mapping]] = ...) -> None: ...

class SearchHitMeta(_message.Message):
    __slots__ = ["created_at", "match", "updated_at"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    match: Match
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., match: _Optional[_Union[Match, _Mapping]] = ...) -> None: ...

class SearchMetadata(_message.Message):
    __slots__ = ["found", "matched_fields", "page", "total_pages"]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    found: int
    matched_fields: _containers.RepeatedScalarFieldContainer[str]
    page: Page
    total_pages: int
    def __init__(self, found: _Optional[int] = ..., total_pages: _Optional[int] = ..., page: _Optional[_Union[Page, _Mapping]] = ..., matched_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ["branch", "collation", "collection", "exclude_fields", "facet", "filter", "group_by", "include_fields", "page", "page_size", "project", "q", "search_fields", "sort", "vector"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FACET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collation: Collation
    collection: str
    exclude_fields: _containers.RepeatedScalarFieldContainer[str]
    facet: bytes
    filter: bytes
    group_by: bytes
    include_fields: _containers.RepeatedScalarFieldContainer[str]
    page: int
    page_size: int
    project: str
    q: str
    search_fields: _containers.RepeatedScalarFieldContainer[str]
    sort: bytes
    vector: bytes
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., q: _Optional[str] = ..., search_fields: _Optional[_Iterable[str]] = ..., filter: _Optional[bytes] = ..., facet: _Optional[bytes] = ..., sort: _Optional[bytes] = ..., include_fields: _Optional[_Iterable[str]] = ..., exclude_fields: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ..., collation: _Optional[_Union[Collation, _Mapping]] = ..., branch: _Optional[str] = ..., group_by: _Optional[bytes] = ..., vector: _Optional[bytes] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ["facets", "group", "hits", "meta"]
    class FacetsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SearchFacet
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SearchFacet, _Mapping]] = ...) -> None: ...
    FACETS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    facets: _containers.MessageMap[str, SearchFacet]
    group: _containers.RepeatedCompositeFieldContainer[GroupedSearchHits]
    hits: _containers.RepeatedCompositeFieldContainer[SearchHit]
    meta: SearchMetadata
    def __init__(self, hits: _Optional[_Iterable[_Union[SearchHit, _Mapping]]] = ..., facets: _Optional[_Mapping[str, SearchFacet]] = ..., meta: _Optional[_Union[SearchMetadata, _Mapping]] = ..., group: _Optional[_Iterable[_Union[GroupedSearchHits, _Mapping]]] = ...) -> None: ...

class TransactionCtx(_message.Message):
    __slots__ = ["id", "origin"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    origin: str
    def __init__(self, id: _Optional[str] = ..., origin: _Optional[str] = ...) -> None: ...

class TransactionOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAppKeyRequest(_message.Message):
    __slots__ = ["description", "id", "name", "project"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    project: str
    def __init__(self, id: _Optional[str] = ..., project: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateAppKeyResponse(_message.Message):
    __slots__ = ["updated_app_key"]
    UPDATED_APP_KEY_FIELD_NUMBER: _ClassVar[int]
    updated_app_key: AppKey
    def __init__(self, updated_app_key: _Optional[_Union[AppKey, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["branch", "collection", "fields", "filter", "options", "project"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    fields: bytes
    filter: bytes
    options: UpdateRequestOptions
    project: str
    def __init__(self, project: _Optional[str] = ..., collection: _Optional[str] = ..., fields: _Optional[bytes] = ..., filter: _Optional[bytes] = ..., options: _Optional[_Union[UpdateRequestOptions, _Mapping]] = ..., branch: _Optional[str] = ...) -> None: ...

class UpdateRequestOptions(_message.Message):
    __slots__ = ["collation", "limit", "write_options"]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    WRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    collation: Collation
    limit: int
    write_options: WriteOptions
    def __init__(self, write_options: _Optional[_Union[WriteOptions, _Mapping]] = ..., collation: _Optional[_Union[Collation, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["metadata", "modified_count", "status"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: ResponseMetadata
    modified_count: int
    status: str
    def __init__(self, metadata: _Optional[_Union[ResponseMetadata, _Mapping]] = ..., modified_count: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class WriteOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
