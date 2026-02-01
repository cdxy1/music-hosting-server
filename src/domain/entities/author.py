from uuid import UUID
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Author:
    id: UUID
    name: str
    type: str
    
