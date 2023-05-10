import os
from typing import Optional

import grpc

from api.generated.server.v1 import api_pb2_grpc as tigris_grpc
from tigris.config import TigrisClientConfig
from tigris.database import Database
from tigris.errors import TigrisException


class TigrisClient(object):
    __LOCAL_SERVER = 'localhost:8081'

    __tigris_stub: tigris_grpc.TigrisStub
    __config: TigrisClientConfig

    def __init__(self, config: Optional[TigrisClientConfig]):

        os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

        if not config:
            config = TigrisClientConfig()
        self.__config = config
        if not config.server_url:
            config.server_url = TigrisClient.__LOCAL_SERVER
        if config.server_url.startswith('https://'):
            config.server_url.replace('https://', '')

        is_local_dev = filter(lambda k: k in config.server_url,
                              ['localhost', '127.0.0.1', 'tigris-local-server:', '[::1]'])

        if is_local_dev:
            channel = grpc.insecure_channel(config.server_url)
        else:
            raise NotImplementedError('Secure channels will be supported in upcoming versions')

        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except:
            raise TigrisException(f'Connection timed out: {config.server_url}')

        self.__tigris_stub = tigris_grpc.TigrisStub(channel)

    def get_db(self):
        return Database(self.__tigris_stub, self.__config)
