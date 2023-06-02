from ...google.api import annotations_pb2 as _annotations_pb2
from ...openapiv3 import annotations_pb2 as _annotations_pb2_1
from ...server.v1 import observability_pb2 as _observability_pb2
from ...server.v1 import api_pb2 as _api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateByIdRequest(_message.Message):
    __slots__ = ["document", "id", "index", "project"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    document: bytes
    id: str
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., id: _Optional[str] = ..., document: _Optional[bytes] = ...) -> None: ...

class CreateByIdResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateDocumentRequest(_message.Message):
    __slots__ = ["documents", "index", "project"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CreateDocumentResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[DocStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[DocStatus, _Mapping]]] = ...) -> None: ...

class CreateOrReplaceDocumentRequest(_message.Message):
    __slots__ = ["documents", "index", "project"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CreateOrReplaceDocumentResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[DocStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[DocStatus, _Mapping]]] = ...) -> None: ...

class CreateOrUpdateIndexRequest(_message.Message):
    __slots__ = ["name", "only_create", "project", "schema"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLY_CREATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    only_create: bool
    project: str
    schema: bytes
    def __init__(self, project: _Optional[str] = ..., name: _Optional[str] = ..., schema: _Optional[bytes] = ..., only_create: bool = ...) -> None: ...

class CreateOrUpdateIndexResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteByQueryRequest(_message.Message):
    __slots__ = ["filter", "index", "project"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    filter: bytes
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., filter: _Optional[bytes] = ...) -> None: ...

class DeleteByQueryResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class DeleteDocumentRequest(_message.Message):
    __slots__ = ["ids", "index", "project"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteDocumentResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[DocStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[DocStatus, _Mapping]]] = ...) -> None: ...

class DeleteIndexRequest(_message.Message):
    __slots__ = ["name", "project"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    def __init__(self, project: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteIndexResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DocStatus(_message.Message):
    __slots__ = ["error", "id"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    error: _observability_pb2.Error
    id: str
    def __init__(self, id: _Optional[str] = ..., error: _Optional[_Union[_observability_pb2.Error, _Mapping]] = ...) -> None: ...

class GetDocumentRequest(_message.Message):
    __slots__ = ["ids", "index", "project"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDocumentResponse(_message.Message):
    __slots__ = ["documents"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[_api_pb2.SearchHit]
    def __init__(self, documents: _Optional[_Iterable[_Union[_api_pb2.SearchHit, _Mapping]]] = ...) -> None: ...

class GetIndexRequest(_message.Message):
    __slots__ = ["name", "project"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    def __init__(self, project: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetIndexResponse(_message.Message):
    __slots__ = ["index"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: IndexInfo
    def __init__(self, index: _Optional[_Union[IndexInfo, _Mapping]] = ...) -> None: ...

class IndexInfo(_message.Message):
    __slots__ = ["name", "schema"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema: bytes
    def __init__(self, name: _Optional[str] = ..., schema: _Optional[bytes] = ...) -> None: ...

class IndexSource(_message.Message):
    __slots__ = ["branch", "collection", "type"]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    branch: str
    collection: str
    type: str
    def __init__(self, type: _Optional[str] = ..., collection: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class ListIndexesRequest(_message.Message):
    __slots__ = ["filter", "project"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    filter: IndexSource
    project: str
    def __init__(self, project: _Optional[str] = ..., filter: _Optional[_Union[IndexSource, _Mapping]] = ...) -> None: ...

class ListIndexesResponse(_message.Message):
    __slots__ = ["indexes"]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[IndexInfo]
    def __init__(self, indexes: _Optional[_Iterable[_Union[IndexInfo, _Mapping]]] = ...) -> None: ...

class SearchIndexRequest(_message.Message):
    __slots__ = ["collation", "exclude_fields", "facet", "filter", "group_by", "include_fields", "index", "page", "page_size", "project", "q", "search_fields", "sort", "vector"]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FACET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    collation: _api_pb2.Collation
    exclude_fields: _containers.RepeatedScalarFieldContainer[str]
    facet: bytes
    filter: bytes
    group_by: bytes
    include_fields: _containers.RepeatedScalarFieldContainer[str]
    index: str
    page: int
    page_size: int
    project: str
    q: str
    search_fields: _containers.RepeatedScalarFieldContainer[str]
    sort: bytes
    vector: bytes
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., q: _Optional[str] = ..., search_fields: _Optional[_Iterable[str]] = ..., filter: _Optional[bytes] = ..., facet: _Optional[bytes] = ..., sort: _Optional[bytes] = ..., include_fields: _Optional[_Iterable[str]] = ..., exclude_fields: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ..., collation: _Optional[_Union[_api_pb2.Collation, _Mapping]] = ..., group_by: _Optional[bytes] = ..., vector: _Optional[bytes] = ...) -> None: ...

class SearchIndexResponse(_message.Message):
    __slots__ = ["facets", "group", "hits", "meta"]
    class FacetsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _api_pb2.SearchFacet
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_api_pb2.SearchFacet, _Mapping]] = ...) -> None: ...
    FACETS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    facets: _containers.MessageMap[str, _api_pb2.SearchFacet]
    group: _containers.RepeatedCompositeFieldContainer[_api_pb2.GroupedSearchHits]
    hits: _containers.RepeatedCompositeFieldContainer[_api_pb2.SearchHit]
    meta: _api_pb2.SearchMetadata
    def __init__(self, hits: _Optional[_Iterable[_Union[_api_pb2.SearchHit, _Mapping]]] = ..., facets: _Optional[_Mapping[str, _api_pb2.SearchFacet]] = ..., meta: _Optional[_Union[_api_pb2.SearchMetadata, _Mapping]] = ..., group: _Optional[_Iterable[_Union[_api_pb2.GroupedSearchHits, _Mapping]]] = ...) -> None: ...

class UpdateDocumentRequest(_message.Message):
    __slots__ = ["documents", "index", "project"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedScalarFieldContainer[bytes]
    index: str
    project: str
    def __init__(self, project: _Optional[str] = ..., index: _Optional[str] = ..., documents: _Optional[_Iterable[bytes]] = ...) -> None: ...

class UpdateDocumentResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[DocStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[DocStatus, _Mapping]]] = ...) -> None: ...
