from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from src.domain.entities.author import Author
from src.domain.entities.genre import Genre
from src.domain.entities.track import Track


@dataclass(slots=True, frozen=True)
class Release:
    name: str
    author: Author
    genre: Genre
    tracks: list[Track]
    release_data: datetime = field(default_factory=datetime.now)
    id: UUID = field(default_factory=uuid4) 
