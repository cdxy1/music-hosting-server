from uuid import UUID
from dataclasses import dataclass

@dataclass(frozen=True)
class Genre:
    id: UUID
    title: str
