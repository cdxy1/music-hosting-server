from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from src.domain.entities.author import Author
from src.domain.entities.genre import Genre
# from src.domain.entities.track import Track
from src.domain.enums.release_type import ReleaseType


@dataclass(slots=True, frozen=True)
class Release:
    name: str
    author: Author
    genre: Genre
    # tracks: list[Track]
    release_type: ReleaseType
    release_date: date
    id: UUID = field(default_factory=uuid4) 
