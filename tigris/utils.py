import json

from tigris.types import Document


def doc_to_str(doc: Document) -> str:
    return json.dumps(doc)


def str_to_bytes(doc_str: str) -> bytes:
    return doc_str.encode()


def doc_to_bytes(doc: Document) -> bytes:
    return str_to_bytes(doc_to_str(doc))


def bytes_to_str(b: bytes) -> str:
    return b.decode()


def str_to_doc(doc_str: str) -> Document:
    return json.loads(doc_str)


def bytes_to_doc(b: bytes) -> Document:
    return str_to_doc(bytes_to_str(b))
