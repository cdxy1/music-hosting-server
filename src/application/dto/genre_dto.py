from dataclasses import dataclass, asdict
from typing import Optional
from uuid import UUID

@dataclass(frozen=True, slots=True)
class GenreDTO:
    title: str
    id: Optional[UUID] = None
    
    def to_dict(self):
        return asdict(self)
