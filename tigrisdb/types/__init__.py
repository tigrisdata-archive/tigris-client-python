import abc
from dataclasses import dataclass
from typing import Dict, Optional, Type


@dataclass
class ClientConfig:
    project_name: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    branch: str = ""
    server_url: str = "localhost:8081"


Document: Type[dict] = Dict
RFC3339_format = "%Y-%m-%dT%H:%M:%S%z"


# todo: shorten import paths


class BaseOperator(abc.ABC):
    @abc.abstractmethod
    def query(self) -> Dict:
        raise NotImplementedError()
