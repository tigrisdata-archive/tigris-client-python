from dataclasses import dataclass
from typing import Optional


@dataclass
class TigrisClientConfig:
    project_name: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    branch: str = ''
    server_url: str = 'localhost:8081'
