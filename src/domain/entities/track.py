from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.value_objects.audio import Audio


@dataclass(frozen=True, slots=True)
class Track(BaseEntity):
    id: UUID
    title: str
    duration: int

    def __post_init__(self):
        self._ensure_id_is_uuid()
        self._ensure_title_is_not_blank()

    def _ensure_id_is_uuid(self):
        if not isinstance(self.id, UUID):
            raise ValueError("Track id must UUID")

    def _ensure_title_is_not_blank(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Track title must be non-empty")

    def _ensure_audio_is_audio(self):
        if not isinstance(self.audio, Audio):
            raise ValueError("Track audio must be Audio")
