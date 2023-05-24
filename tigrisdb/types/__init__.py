import abc
from dataclasses import dataclass
from typing import Dict, Optional, Type

Document: Type[dict] = Dict


@dataclass
class ClientConfig:
    project_name: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    branch: str = ""
    server_url: str = "localhost:8081"


class Serializable(abc.ABC):
    @abc.abstractmethod
    def query(self) -> Dict:
        raise NotImplementedError()


class BaseOperator(abc.ABC):
    @property
    @abc.abstractmethod
    def operator(self):
        raise NotImplementedError()
