import abc
import os
from dataclasses import dataclass
from typing import Dict, Optional, Type

Document: Type[dict] = Dict


@dataclass
class ClientConfig:
    project: str = ""
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    branch: str = ""
    server_url: str = ""

    def __post_init__(self):
        self.server_url = self.server_url or os.getenv(
            "TIGRIS_URI", "api.preview.tigrisdata.cloud"
        )
        self.project = self.project or os.getenv("TIGRIS_PROJECT")
        self.client_id = self.client_id or os.getenv("TIGRIS_CLIENT_ID")
        self.client_secret = self.client_secret or os.getenv("TIGRIS_CLIENT_SECRET")
        self.branch = self.branch or os.getenv("TIGRIS_DB_BRANCH", "")

    def merge(self, **kwargs):
        self.project = kwargs.get("project", self.project)
        self.server_url = kwargs.get("server_url", self.server_url)
        self.client_id = kwargs.get("client_id", self.client_id)
        self.client_secret = kwargs.get("client_secret", self.client_secret)
        self.branch = kwargs.get("branch", self.branch)

    def is_local_dev(self) -> bool:
        return any(
            map(
                lambda k: k in self.server_url,
                ["localhost", "127.0.0.1", "tigrisdb-local-server:", "[::1]"],
            )
        )

    def validate(self):
        is_remote = not self.is_local_dev()
        if not self.project:
            raise ValueError("Failed to resolve `TIGRIS_PROJECT` environment variable")
        if is_remote and not self.client_id:
            raise ValueError(
                "Failed to resolve `TIGRIS_CLIENT_ID` environment variable"
            )
        if is_remote and not self.client_secret:
            raise ValueError(
                "Failed to resolve `TIGRIS_CLIENT_SECRET` environment variable"
            )


class Serializable(abc.ABC):
    @abc.abstractmethod
    def query(self) -> Dict:
        raise NotImplementedError()


class BaseOperator(abc.ABC):
    @property
    @abc.abstractmethod
    def operator(self):
        raise NotImplementedError()
