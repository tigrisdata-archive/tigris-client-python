from ...google.api import annotations_pb2 as _annotations_pb2
from ...openapiv3 import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CLIENT_CREDENTIALS: GrantType
DESCRIPTOR: _descriptor.FileDescriptor
REFRESH_TOKEN: GrantType

class CreateInvitationsRequest(_message.Message):
    __slots__ = ["invitations"]
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    invitations: _containers.RepeatedCompositeFieldContainer[InvitationInfo]
    def __init__(self, invitations: _Optional[_Iterable[_Union[InvitationInfo, _Mapping]]] = ...) -> None: ...

class CreateInvitationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteInvitationsRequest(_message.Message):
    __slots__ = ["email", "status"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    email: str
    status: str
    def __init__(self, email: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteInvitationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAccessTokenRequest(_message.Message):
    __slots__ = ["client_id", "client_secret", "grant_type", "refresh_token"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    grant_type: GrantType
    refresh_token: str
    def __init__(self, grant_type: _Optional[_Union[GrantType, str]] = ..., refresh_token: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class GetAccessTokenResponse(_message.Message):
    __slots__ = ["access_token", "expires_in", "refresh_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    refresh_token: str
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class Invitation(_message.Message):
    __slots__ = ["created_by", "created_by_name", "email", "expiration_time", "role", "status", "tigris_namespace", "tigris_namespace_name"]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIGRIS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIGRIS_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    created_by: str
    created_by_name: str
    email: str
    expiration_time: int
    role: str
    status: str
    tigris_namespace: str
    tigris_namespace_name: str
    def __init__(self, email: _Optional[str] = ..., role: _Optional[str] = ..., status: _Optional[str] = ..., tigris_namespace: _Optional[str] = ..., tigris_namespace_name: _Optional[str] = ..., created_by: _Optional[str] = ..., created_by_name: _Optional[str] = ..., expiration_time: _Optional[int] = ...) -> None: ...

class InvitationInfo(_message.Message):
    __slots__ = ["email", "invitation_sent_by_name", "role"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    INVITATION_SENT_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    invitation_sent_by_name: str
    role: str
    def __init__(self, email: _Optional[str] = ..., role: _Optional[str] = ..., invitation_sent_by_name: _Optional[str] = ...) -> None: ...

class ListInvitationsRequest(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ListInvitationsResponse(_message.Message):
    __slots__ = ["invitations"]
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    invitations: _containers.RepeatedCompositeFieldContainer[Invitation]
    def __init__(self, invitations: _Optional[_Iterable[_Union[Invitation, _Mapping]]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["created_at", "email", "name", "picture", "role"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    email: str
    name: str
    picture: str
    role: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[int] = ..., picture: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class VerifyInvitationRequest(_message.Message):
    __slots__ = ["code", "email"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    code: str
    email: str
    def __init__(self, email: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class VerifyInvitationResponse(_message.Message):
    __slots__ = ["role", "tigris_namespace", "tigris_namespace_name"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TIGRIS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TIGRIS_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    role: str
    tigris_namespace: str
    tigris_namespace_name: str
    def __init__(self, tigris_namespace: _Optional[str] = ..., tigris_namespace_name: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
