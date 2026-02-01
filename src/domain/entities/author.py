from dataclasses import dataclass
from uuid import UUID

from src.domain.enums.author_type import AuthorType


@dataclass(frozen=True, slots=True)
class Author:
    id: UUID
    name: str
    type: AuthorType
    
    def __post_init__(self):
        self._ensure_id_is_uuid()
        self._ensure_name_is_str()
        
    def _ensure_id_is_uuid(self):
        if not isinstance(self.id, UUID):
            raise ValueError("Author id must be UUID")
        
    def _ensure_name_is_str(self):
        if not isinstance(self.name, str):
            raise ValueError("Author name must be string")
        
        if not self.name.strip():
            raise ValueError("Author name must be non-empty")
        
    def _ensure_author_type(self):
        ...
    
