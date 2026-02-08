from dataclasses import asdict, dataclass
from typing import Optional
from uuid import UUID

from src.domain.enums.author_type import AuthorType


@dataclass(frozen=True, slots=True)
class AuthorDTO:
    name: str
    type: AuthorType
    id: Optional[UUID] = None
    
    def to_dict(self):
        return asdict(self)
