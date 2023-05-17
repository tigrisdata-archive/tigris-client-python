import base64
import json


def obj_to_str(doc: object) -> str:
    return json.dumps(doc)


def str_to_bytes(doc_str: str) -> bytes:
    return doc_str.encode("utf-8")


def marshal(doc: object) -> bytes:
    return str_to_bytes(obj_to_str(doc))


def bytes_to_str(b: bytes) -> str:
    return b.decode("utf-8")


def str_to_obj(doc_str: str) -> object:
    return json.loads(doc_str)


def unmarshal(b: bytes) -> object:
    return str_to_obj(bytes_to_str(b))


def b64_to_object(b64_str: str) -> object:
    return unmarshal(base64.b64decode(b64_str))


def obj_to_b64(doc: object) -> str:
    return bytes_to_str(base64.b64encode(marshal(doc)))


def schema_to_bytes(schema: dict) -> bytes:
    return marshal(schema)
