from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdditionalPropertiesItem(_message.Message):
    __slots__ = ["boolean", "schema_or_reference"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    schema_or_reference: SchemaOrReference
    def __init__(self, schema_or_reference: _Optional[_Union[SchemaOrReference, _Mapping]] = ..., boolean: bool = ...) -> None: ...

class Any(_message.Message):
    __slots__ = ["value", "yaml"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    YAML_FIELD_NUMBER: _ClassVar[int]
    value: _any_pb2.Any
    yaml: str
    def __init__(self, value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., yaml: _Optional[str] = ...) -> None: ...

class AnyOrExpression(_message.Message):
    __slots__ = ["any", "expression"]
    ANY_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    any: Any
    expression: Expression
    def __init__(self, any: _Optional[_Union[Any, _Mapping]] = ..., expression: _Optional[_Union[Expression, _Mapping]] = ...) -> None: ...

class Callback(_message.Message):
    __slots__ = ["path", "specification_extension"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedCompositeFieldContainer[NamedPathItem]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, path: _Optional[_Iterable[_Union[NamedPathItem, _Mapping]]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class CallbackOrReference(_message.Message):
    __slots__ = ["callback", "reference"]
    CALLBACK_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    callback: Callback
    reference: Reference
    def __init__(self, callback: _Optional[_Union[Callback, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class CallbacksOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedCallbackOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedCallbackOrReference, _Mapping]]] = ...) -> None: ...

class Components(_message.Message):
    __slots__ = ["callbacks", "examples", "headers", "links", "parameters", "request_bodies", "responses", "schemas", "security_schemes", "specification_extension"]
    CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODIES_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    callbacks: CallbacksOrReferences
    examples: ExamplesOrReferences
    headers: HeadersOrReferences
    links: LinksOrReferences
    parameters: ParametersOrReferences
    request_bodies: RequestBodiesOrReferences
    responses: ResponsesOrReferences
    schemas: SchemasOrReferences
    security_schemes: SecuritySchemesOrReferences
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, schemas: _Optional[_Union[SchemasOrReferences, _Mapping]] = ..., responses: _Optional[_Union[ResponsesOrReferences, _Mapping]] = ..., parameters: _Optional[_Union[ParametersOrReferences, _Mapping]] = ..., examples: _Optional[_Union[ExamplesOrReferences, _Mapping]] = ..., request_bodies: _Optional[_Union[RequestBodiesOrReferences, _Mapping]] = ..., headers: _Optional[_Union[HeadersOrReferences, _Mapping]] = ..., security_schemes: _Optional[_Union[SecuritySchemesOrReferences, _Mapping]] = ..., links: _Optional[_Union[LinksOrReferences, _Mapping]] = ..., callbacks: _Optional[_Union[CallbacksOrReferences, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ["email", "name", "specification_extension", "url"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    url: str
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., email: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class DefaultType(_message.Message):
    __slots__ = ["boolean", "number", "string"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    number: float
    string: str
    def __init__(self, number: _Optional[float] = ..., boolean: bool = ..., string: _Optional[str] = ...) -> None: ...

class Discriminator(_message.Message):
    __slots__ = ["mapping", "property_name", "specification_extension"]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    mapping: Strings
    property_name: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, property_name: _Optional[str] = ..., mapping: _Optional[_Union[Strings, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ["components", "external_docs", "info", "openapi", "paths", "security", "servers", "specification_extension", "tags"]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DOCS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    OPENAPI_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    components: Components
    external_docs: ExternalDocs
    info: Info
    openapi: str
    paths: Paths
    security: _containers.RepeatedCompositeFieldContainer[SecurityRequirement]
    servers: _containers.RepeatedCompositeFieldContainer[Server]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, openapi: _Optional[str] = ..., info: _Optional[_Union[Info, _Mapping]] = ..., servers: _Optional[_Iterable[_Union[Server, _Mapping]]] = ..., paths: _Optional[_Union[Paths, _Mapping]] = ..., components: _Optional[_Union[Components, _Mapping]] = ..., security: _Optional[_Iterable[_Union[SecurityRequirement, _Mapping]]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., external_docs: _Optional[_Union[ExternalDocs, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Encoding(_message.Message):
    __slots__ = ["allow_reserved", "content_type", "explode", "headers", "specification_extension", "style"]
    ALLOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    allow_reserved: bool
    content_type: str
    explode: bool
    headers: HeadersOrReferences
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    style: str
    def __init__(self, content_type: _Optional[str] = ..., headers: _Optional[_Union[HeadersOrReferences, _Mapping]] = ..., style: _Optional[str] = ..., explode: bool = ..., allow_reserved: bool = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Encodings(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedEncoding]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedEncoding, _Mapping]]] = ...) -> None: ...

class Example(_message.Message):
    __slots__ = ["description", "external_value", "specification_extension", "summary", "value"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    description: str
    external_value: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    summary: str
    value: Any
    def __init__(self, summary: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[_Union[Any, _Mapping]] = ..., external_value: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ExampleOrReference(_message.Message):
    __slots__ = ["example", "reference"]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    example: Example
    reference: Reference
    def __init__(self, example: _Optional[_Union[Example, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class ExamplesOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedExampleOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedExampleOrReference, _Mapping]]] = ...) -> None: ...

class Expression(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ExternalDocs(_message.Message):
    __slots__ = ["description", "specification_extension", "url"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    description: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    url: str
    def __init__(self, description: _Optional[str] = ..., url: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["allow_empty_value", "allow_reserved", "content", "deprecated", "description", "example", "examples", "explode", "required", "schema", "specification_extension", "style"]
    ALLOW_EMPTY_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    allow_empty_value: bool
    allow_reserved: bool
    content: MediaTypes
    deprecated: bool
    description: str
    example: Any
    examples: ExamplesOrReferences
    explode: bool
    required: bool
    schema: SchemaOrReference
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    style: str
    def __init__(self, description: _Optional[str] = ..., required: bool = ..., deprecated: bool = ..., allow_empty_value: bool = ..., style: _Optional[str] = ..., explode: bool = ..., allow_reserved: bool = ..., schema: _Optional[_Union[SchemaOrReference, _Mapping]] = ..., example: _Optional[_Union[Any, _Mapping]] = ..., examples: _Optional[_Union[ExamplesOrReferences, _Mapping]] = ..., content: _Optional[_Union[MediaTypes, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class HeaderOrReference(_message.Message):
    __slots__ = ["header", "reference"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    header: Header
    reference: Reference
    def __init__(self, header: _Optional[_Union[Header, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class HeadersOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedHeaderOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedHeaderOrReference, _Mapping]]] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["contact", "description", "license", "specification_extension", "summary", "terms_of_service", "title", "version"]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TERMS_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    contact: Contact
    description: str
    license: License
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    summary: str
    terms_of_service: str
    title: str
    version: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., terms_of_service: _Optional[str] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ..., license: _Optional[_Union[License, _Mapping]] = ..., version: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ..., summary: _Optional[str] = ...) -> None: ...

class ItemsItem(_message.Message):
    __slots__ = ["schema_or_reference"]
    SCHEMA_OR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    schema_or_reference: _containers.RepeatedCompositeFieldContainer[SchemaOrReference]
    def __init__(self, schema_or_reference: _Optional[_Iterable[_Union[SchemaOrReference, _Mapping]]] = ...) -> None: ...

class License(_message.Message):
    __slots__ = ["name", "specification_extension", "url"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    url: str
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ["description", "operation_id", "operation_ref", "parameters", "request_body", "server", "specification_extension"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_REF_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    description: str
    operation_id: str
    operation_ref: str
    parameters: AnyOrExpression
    request_body: AnyOrExpression
    server: Server
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, operation_ref: _Optional[str] = ..., operation_id: _Optional[str] = ..., parameters: _Optional[_Union[AnyOrExpression, _Mapping]] = ..., request_body: _Optional[_Union[AnyOrExpression, _Mapping]] = ..., description: _Optional[str] = ..., server: _Optional[_Union[Server, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class LinkOrReference(_message.Message):
    __slots__ = ["link", "reference"]
    LINK_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    link: Link
    reference: Reference
    def __init__(self, link: _Optional[_Union[Link, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class LinksOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedLinkOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedLinkOrReference, _Mapping]]] = ...) -> None: ...

class MediaType(_message.Message):
    __slots__ = ["encoding", "example", "examples", "schema", "specification_extension"]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    encoding: Encodings
    example: Any
    examples: ExamplesOrReferences
    schema: SchemaOrReference
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, schema: _Optional[_Union[SchemaOrReference, _Mapping]] = ..., example: _Optional[_Union[Any, _Mapping]] = ..., examples: _Optional[_Union[ExamplesOrReferences, _Mapping]] = ..., encoding: _Optional[_Union[Encodings, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class MediaTypes(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedMediaType]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedMediaType, _Mapping]]] = ...) -> None: ...

class NamedAny(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: Any
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[Any, _Mapping]] = ...) -> None: ...

class NamedCallbackOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: CallbackOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[CallbackOrReference, _Mapping]] = ...) -> None: ...

class NamedEncoding(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: Encoding
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[Encoding, _Mapping]] = ...) -> None: ...

class NamedExampleOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: ExampleOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[ExampleOrReference, _Mapping]] = ...) -> None: ...

class NamedHeaderOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: HeaderOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[HeaderOrReference, _Mapping]] = ...) -> None: ...

class NamedLinkOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: LinkOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[LinkOrReference, _Mapping]] = ...) -> None: ...

class NamedMediaType(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: MediaType
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[MediaType, _Mapping]] = ...) -> None: ...

class NamedParameterOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: ParameterOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[ParameterOrReference, _Mapping]] = ...) -> None: ...

class NamedPathItem(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: PathItem
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[PathItem, _Mapping]] = ...) -> None: ...

class NamedRequestBodyOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: RequestBodyOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[RequestBodyOrReference, _Mapping]] = ...) -> None: ...

class NamedResponseOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: ResponseOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[ResponseOrReference, _Mapping]] = ...) -> None: ...

class NamedSchemaOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: SchemaOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[SchemaOrReference, _Mapping]] = ...) -> None: ...

class NamedSecuritySchemeOrReference(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: SecuritySchemeOrReference
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[SecuritySchemeOrReference, _Mapping]] = ...) -> None: ...

class NamedServerVariable(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: ServerVariable
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[ServerVariable, _Mapping]] = ...) -> None: ...

class NamedString(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class NamedStringArray(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: StringArray
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[StringArray, _Mapping]] = ...) -> None: ...

class OauthFlow(_message.Message):
    __slots__ = ["authorization_url", "refresh_url", "scopes", "specification_extension", "token_url"]
    AUTHORIZATION_URL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    authorization_url: str
    refresh_url: str
    scopes: Strings
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    token_url: str
    def __init__(self, authorization_url: _Optional[str] = ..., token_url: _Optional[str] = ..., refresh_url: _Optional[str] = ..., scopes: _Optional[_Union[Strings, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class OauthFlows(_message.Message):
    __slots__ = ["authorization_code", "client_credentials", "implicit", "password", "specification_extension"]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    IMPLICIT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    authorization_code: OauthFlow
    client_credentials: OauthFlow
    implicit: OauthFlow
    password: OauthFlow
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, implicit: _Optional[_Union[OauthFlow, _Mapping]] = ..., password: _Optional[_Union[OauthFlow, _Mapping]] = ..., client_credentials: _Optional[_Union[OauthFlow, _Mapping]] = ..., authorization_code: _Optional[_Union[OauthFlow, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Operation(_message.Message):
    __slots__ = ["callbacks", "deprecated", "description", "external_docs", "operation_id", "parameters", "request_body", "responses", "security", "servers", "specification_extension", "summary", "tags"]
    CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DOCS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    callbacks: CallbacksOrReferences
    deprecated: bool
    description: str
    external_docs: ExternalDocs
    operation_id: str
    parameters: _containers.RepeatedCompositeFieldContainer[ParameterOrReference]
    request_body: RequestBodyOrReference
    responses: Responses
    security: _containers.RepeatedCompositeFieldContainer[SecurityRequirement]
    servers: _containers.RepeatedCompositeFieldContainer[Server]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    summary: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags: _Optional[_Iterable[str]] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ..., external_docs: _Optional[_Union[ExternalDocs, _Mapping]] = ..., operation_id: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[ParameterOrReference, _Mapping]]] = ..., request_body: _Optional[_Union[RequestBodyOrReference, _Mapping]] = ..., responses: _Optional[_Union[Responses, _Mapping]] = ..., callbacks: _Optional[_Union[CallbacksOrReferences, _Mapping]] = ..., deprecated: bool = ..., security: _Optional[_Iterable[_Union[SecurityRequirement, _Mapping]]] = ..., servers: _Optional[_Iterable[_Union[Server, _Mapping]]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ["allow_empty_value", "allow_reserved", "content", "deprecated", "description", "example", "examples", "explode", "name", "required", "schema", "specification_extension", "style"]
    ALLOW_EMPTY_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    allow_empty_value: bool
    allow_reserved: bool
    content: MediaTypes
    deprecated: bool
    description: str
    example: Any
    examples: ExamplesOrReferences
    explode: bool
    name: str
    required: bool
    schema: SchemaOrReference
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    style: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., deprecated: bool = ..., allow_empty_value: bool = ..., style: _Optional[str] = ..., explode: bool = ..., allow_reserved: bool = ..., schema: _Optional[_Union[SchemaOrReference, _Mapping]] = ..., example: _Optional[_Union[Any, _Mapping]] = ..., examples: _Optional[_Union[ExamplesOrReferences, _Mapping]] = ..., content: _Optional[_Union[MediaTypes, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ..., **kwargs) -> None: ...

class ParameterOrReference(_message.Message):
    __slots__ = ["parameter", "reference"]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    parameter: Parameter
    reference: Reference
    def __init__(self, parameter: _Optional[_Union[Parameter, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class ParametersOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedParameterOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedParameterOrReference, _Mapping]]] = ...) -> None: ...

class PathItem(_message.Message):
    __slots__ = ["_ref", "delete", "description", "get", "head", "options", "parameters", "patch", "post", "put", "servers", "specification_extension", "summary", "trace"]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    PUT_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TRACE_FIELD_NUMBER: _ClassVar[int]
    _REF_FIELD_NUMBER: _ClassVar[int]
    _ref: str
    delete: Operation
    description: str
    get: Operation
    head: Operation
    options: Operation
    parameters: _containers.RepeatedCompositeFieldContainer[ParameterOrReference]
    patch: Operation
    post: Operation
    put: Operation
    servers: _containers.RepeatedCompositeFieldContainer[Server]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    summary: str
    trace: Operation
    def __init__(self, _ref: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ..., get: _Optional[_Union[Operation, _Mapping]] = ..., put: _Optional[_Union[Operation, _Mapping]] = ..., post: _Optional[_Union[Operation, _Mapping]] = ..., delete: _Optional[_Union[Operation, _Mapping]] = ..., options: _Optional[_Union[Operation, _Mapping]] = ..., head: _Optional[_Union[Operation, _Mapping]] = ..., patch: _Optional[_Union[Operation, _Mapping]] = ..., trace: _Optional[_Union[Operation, _Mapping]] = ..., servers: _Optional[_Iterable[_Union[Server, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[ParameterOrReference, _Mapping]]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Paths(_message.Message):
    __slots__ = ["path", "specification_extension"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedCompositeFieldContainer[NamedPathItem]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, path: _Optional[_Iterable[_Union[NamedPathItem, _Mapping]]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Properties(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedSchemaOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedSchemaOrReference, _Mapping]]] = ...) -> None: ...

class Reference(_message.Message):
    __slots__ = ["_ref", "description", "summary"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    _REF_FIELD_NUMBER: _ClassVar[int]
    _ref: str
    description: str
    summary: str
    def __init__(self, _ref: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class RequestBodiesOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedRequestBodyOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedRequestBodyOrReference, _Mapping]]] = ...) -> None: ...

class RequestBody(_message.Message):
    __slots__ = ["content", "description", "required", "specification_extension"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    content: MediaTypes
    description: str
    required: bool
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, description: _Optional[str] = ..., content: _Optional[_Union[MediaTypes, _Mapping]] = ..., required: bool = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class RequestBodyOrReference(_message.Message):
    __slots__ = ["reference", "request_body"]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    reference: Reference
    request_body: RequestBody
    def __init__(self, request_body: _Optional[_Union[RequestBody, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["content", "description", "headers", "links", "specification_extension"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    content: MediaTypes
    description: str
    headers: HeadersOrReferences
    links: LinksOrReferences
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, description: _Optional[str] = ..., headers: _Optional[_Union[HeadersOrReferences, _Mapping]] = ..., content: _Optional[_Union[MediaTypes, _Mapping]] = ..., links: _Optional[_Union[LinksOrReferences, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ResponseOrReference(_message.Message):
    __slots__ = ["reference", "response"]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    reference: Reference
    response: Response
    def __init__(self, response: _Optional[_Union[Response, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class Responses(_message.Message):
    __slots__ = ["default", "response_or_reference", "specification_extension"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_OR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    default: ResponseOrReference
    response_or_reference: _containers.RepeatedCompositeFieldContainer[NamedResponseOrReference]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, default: _Optional[_Union[ResponseOrReference, _Mapping]] = ..., response_or_reference: _Optional[_Iterable[_Union[NamedResponseOrReference, _Mapping]]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ResponsesOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedResponseOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedResponseOrReference, _Mapping]]] = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ["additional_properties", "all_of", "any_of", "default", "deprecated", "description", "discriminator", "enum", "example", "exclusive_maximum", "exclusive_minimum", "external_docs", "format", "items", "max_items", "max_length", "max_properties", "maximum", "min_items", "min_length", "min_properties", "minimum", "multiple_of", "nullable", "one_of", "pattern", "properties", "read_only", "required", "specification_extension", "title", "type", "unique_items", "write_only", "xml"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ALL_OF_FIELD_NUMBER: _ClassVar[int]
    ANY_OF_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DOCS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MIN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_OF_FIELD_NUMBER: _ClassVar[int]
    NOT_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    ONE_OF_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    WRITE_ONLY_FIELD_NUMBER: _ClassVar[int]
    XML_FIELD_NUMBER: _ClassVar[int]
    additional_properties: AdditionalPropertiesItem
    all_of: _containers.RepeatedCompositeFieldContainer[SchemaOrReference]
    any_of: _containers.RepeatedCompositeFieldContainer[SchemaOrReference]
    default: DefaultType
    deprecated: bool
    description: str
    discriminator: Discriminator
    enum: _containers.RepeatedCompositeFieldContainer[Any]
    example: Any
    exclusive_maximum: bool
    exclusive_minimum: bool
    external_docs: ExternalDocs
    format: str
    items: ItemsItem
    max_items: int
    max_length: int
    max_properties: int
    maximum: float
    min_items: int
    min_length: int
    min_properties: int
    minimum: float
    multiple_of: float
    nullable: bool
    one_of: _containers.RepeatedCompositeFieldContainer[SchemaOrReference]
    pattern: str
    properties: Properties
    read_only: bool
    required: _containers.RepeatedScalarFieldContainer[str]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    title: str
    type: str
    unique_items: bool
    write_only: bool
    xml: Xml
    def __init__(self, nullable: bool = ..., discriminator: _Optional[_Union[Discriminator, _Mapping]] = ..., read_only: bool = ..., write_only: bool = ..., xml: _Optional[_Union[Xml, _Mapping]] = ..., external_docs: _Optional[_Union[ExternalDocs, _Mapping]] = ..., example: _Optional[_Union[Any, _Mapping]] = ..., deprecated: bool = ..., title: _Optional[str] = ..., multiple_of: _Optional[float] = ..., maximum: _Optional[float] = ..., exclusive_maximum: bool = ..., minimum: _Optional[float] = ..., exclusive_minimum: bool = ..., max_length: _Optional[int] = ..., min_length: _Optional[int] = ..., pattern: _Optional[str] = ..., max_items: _Optional[int] = ..., min_items: _Optional[int] = ..., unique_items: bool = ..., max_properties: _Optional[int] = ..., min_properties: _Optional[int] = ..., required: _Optional[_Iterable[str]] = ..., enum: _Optional[_Iterable[_Union[Any, _Mapping]]] = ..., type: _Optional[str] = ..., all_of: _Optional[_Iterable[_Union[SchemaOrReference, _Mapping]]] = ..., one_of: _Optional[_Iterable[_Union[SchemaOrReference, _Mapping]]] = ..., any_of: _Optional[_Iterable[_Union[SchemaOrReference, _Mapping]]] = ..., items: _Optional[_Union[ItemsItem, _Mapping]] = ..., properties: _Optional[_Union[Properties, _Mapping]] = ..., additional_properties: _Optional[_Union[AdditionalPropertiesItem, _Mapping]] = ..., default: _Optional[_Union[DefaultType, _Mapping]] = ..., description: _Optional[str] = ..., format: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ..., **kwargs) -> None: ...

class SchemaOrReference(_message.Message):
    __slots__ = ["reference", "schema"]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    reference: Reference
    schema: Schema
    def __init__(self, schema: _Optional[_Union[Schema, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class SchemasOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedSchemaOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedSchemaOrReference, _Mapping]]] = ...) -> None: ...

class SecurityRequirement(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedStringArray]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedStringArray, _Mapping]]] = ...) -> None: ...

class SecurityScheme(_message.Message):
    __slots__ = ["bearer_format", "description", "flows", "name", "open_id_connect_url", "scheme", "specification_extension", "type"]
    BEARER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FLOWS_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_CONNECT_URL_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    bearer_format: str
    description: str
    flows: OauthFlows
    name: str
    open_id_connect_url: str
    scheme: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    type: str
    def __init__(self, type: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ..., scheme: _Optional[str] = ..., bearer_format: _Optional[str] = ..., flows: _Optional[_Union[OauthFlows, _Mapping]] = ..., open_id_connect_url: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ..., **kwargs) -> None: ...

class SecuritySchemeOrReference(_message.Message):
    __slots__ = ["reference", "security_scheme"]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SCHEME_FIELD_NUMBER: _ClassVar[int]
    reference: Reference
    security_scheme: SecurityScheme
    def __init__(self, security_scheme: _Optional[_Union[SecurityScheme, _Mapping]] = ..., reference: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...

class SecuritySchemesOrReferences(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedSecuritySchemeOrReference]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedSecuritySchemeOrReference, _Mapping]]] = ...) -> None: ...

class Server(_message.Message):
    __slots__ = ["description", "specification_extension", "url", "variables"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    description: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    url: str
    variables: ServerVariables
    def __init__(self, url: _Optional[str] = ..., description: _Optional[str] = ..., variables: _Optional[_Union[ServerVariables, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ServerVariable(_message.Message):
    __slots__ = ["default", "description", "enum", "specification_extension"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    default: str
    description: str
    enum: _containers.RepeatedScalarFieldContainer[str]
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, enum: _Optional[_Iterable[str]] = ..., default: _Optional[str] = ..., description: _Optional[str] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class ServerVariables(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedServerVariable]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedServerVariable, _Mapping]]] = ...) -> None: ...

class SpecificationExtension(_message.Message):
    __slots__ = ["boolean", "number", "string"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    number: float
    string: str
    def __init__(self, number: _Optional[float] = ..., boolean: bool = ..., string: _Optional[str] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class Strings(_message.Message):
    __slots__ = ["additional_properties"]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    additional_properties: _containers.RepeatedCompositeFieldContainer[NamedString]
    def __init__(self, additional_properties: _Optional[_Iterable[_Union[NamedString, _Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ["description", "external_docs", "name", "specification_extension"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DOCS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    description: str
    external_docs: ExternalDocs
    name: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., external_docs: _Optional[_Union[ExternalDocs, _Mapping]] = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...

class Xml(_message.Message):
    __slots__ = ["attribute", "name", "namespace", "prefix", "specification_extension", "wrapped"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATION_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    WRAPPED_FIELD_NUMBER: _ClassVar[int]
    attribute: bool
    name: str
    namespace: str
    prefix: str
    specification_extension: _containers.RepeatedCompositeFieldContainer[NamedAny]
    wrapped: bool
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., prefix: _Optional[str] = ..., attribute: bool = ..., wrapped: bool = ..., specification_extension: _Optional[_Iterable[_Union[NamedAny, _Mapping]]] = ...) -> None: ...
