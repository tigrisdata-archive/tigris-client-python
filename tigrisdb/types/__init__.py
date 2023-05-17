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


# todo: shorten import paths


class Serializable(abc.ABC):
    @abc.abstractmethod
    def as_obj(self) -> Dict:
        raise NotImplementedError()
