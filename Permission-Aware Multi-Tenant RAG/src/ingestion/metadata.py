from dataclasses import dataclass
from typing import List


@dataclass
class DocumentMetadata:
    tenant_id: str
    document_type: str
    allowed_roles: List[str]
    source: str