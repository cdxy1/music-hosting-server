from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.domain.entities.base import BaseEntity


@dataclass(frozen=True, slots=True)
class Genre(BaseEntity):
    title: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self._ensure_id_is_uuid()
        self._ensure_title_is_str()
    
    def _ensure_id_is_uuid(self):
        if not isinstance(self.id, UUID):
            raise ValueError("Genre id must be UUID")
        
    def _ensure_title_is_str(self):
        if not isinstance(self.title, str):
            raise ValueError("Genre title must be string")

        if not self.title.strip():
            raise ValueError("Genre title must be non-empty")
