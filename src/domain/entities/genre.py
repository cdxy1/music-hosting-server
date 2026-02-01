from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class Genre:
    id: UUID
    title: str
