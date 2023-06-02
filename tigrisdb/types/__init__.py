import abc
import os
from dataclasses import dataclass
from typing import Dict, Optional, Type

Document: Type[dict] = Dict


@dataclass
class ClientConfig:
    project_name: str = ""
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    branch: str = ""
    server_url: str = ""

    def __post_init__(self):
        self.server_url = self.server_url or os.getenv(
            "TIGRIS_URI", "api.preview.tigrisdata.cloud"
        )
        self.project_name = self.project_name or os.getenv("TIGRIS_PROJECT")
        self.client_id = self.client_id or os.getenv("TIGRIS_CLIENT_ID")
        self.client_secret = self.client_secret or os.getenv("TIGRIS_CLIENT_SECRET")
        self.branch = self.branch or os.getenv("TIGRIS_DB_BRANCH", "")

    def validate(self, with_creds=False):
        if not self.project_name:
            raise ValueError("Failed to resolve `TIGRIS_PROJECT` environment variable")
        if with_creds and not self.client_id:
            raise ValueError(
                "Failed to resolve `TIGRIS_CLIENT_ID` environment variable"
            )
        if with_creds and not self.client_secret:
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
