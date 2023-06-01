from dataclasses import InitVar, dataclass
from typing import Dict, List, TypedDict

from tigrisdb.types.search import IndexedDoc, dataclass_default_proto_field


class Document(TypedDict, total=False):
    id: str
    text: str
    embeddings: List[float]
    metadata: Dict


@dataclass
class DocWithScore:
    doc: Document = None
    score: float = 0.0
    _h: InitVar[IndexedDoc] = dataclass_default_proto_field

    def __post_init__(self, _h: IndexedDoc):
        if _h and _h.doc:
            self.doc = _h.doc
        if _h and _h.meta:
            self.score = _h.meta.text_match.vector_distance
