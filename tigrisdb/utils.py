import base64
import json


def dict_to_str(doc: dict) -> str:
    return json.dumps(doc)


def str_to_bytes(doc_str: str) -> bytes:
    return doc_str.encode("utf-8")


def dict_to_bytes(doc: dict) -> bytes:
    return str_to_bytes(dict_to_str(doc))


def bytes_to_str(b: bytes) -> str:
    return b.decode("utf-8")


def str_to_dict(doc_str: str) -> dict:
    return json.loads(doc_str)


def bytes_to_dict(b: bytes) -> dict:
    return str_to_dict(bytes_to_str(b))


def b64_to_dict(b64_str: str) -> dict:
    return bytes_to_dict(base64.b64decode(b64_str))


def dict_to_b64(doc: dict) -> str:
    return bytes_to_str(base64.b64encode(dict_to_bytes(doc)))


def schema_to_bytes(schema: dict) -> bytes:
    return str_to_bytes(dict_to_str(schema))
