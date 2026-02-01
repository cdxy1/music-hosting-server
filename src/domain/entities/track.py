from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.audio import Audio
from src.domain.entities.author import Author
from src.domain.entities.genre import Genre


@dataclass(frozen=True)
class Track:
    id: UUID
    title: str
    genre: Genre
    audio: Audio
    author: Author
    
    def __post_init__(self):
        self._ensure_id_is_uuid()
        self._ensure_title_is_not_blank()
        self._validate_genre_is_genre()
        self._ensure_audio_is_audio()
        self._ensure_author_is_author()
    
    def _ensure_id_is_uuid(self):
        if not isinstance(self.id, UUID):
            raise ValueError("Track id must UUID")
        
    def _ensure_title_is_not_blank(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Track title must be non-empty")
        
    def _validate_genre_is_genre(self):
        if not isinstance(self.genre, Genre):
            raise ValueError("Track genre must be Genre")
        
    def _ensure_audio_is_audio(self):
        if not isinstance(self.audio, Audio):
            raise ValueError("Track audio must be Audio")
    
    def _ensure_author_is_author(self):
        if not isinstance(self.author, Author):
            raise ValueError("Track author must be Author")
