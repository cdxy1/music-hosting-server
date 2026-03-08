from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

from src.domain.entities.base import BaseEntity


@dataclass(frozen=True, slots=True)
class Track(BaseEntity):
    title: str
    duration: Optional[int] = None
    audio_key: Optional[str] = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self._ensure_id_is_uuid()
        self._ensure_title_is_not_blank()

    def _ensure_id_is_uuid(self):
        if not isinstance(self.id, UUID):
            raise ValueError("Track id must UUID")

    def _ensure_title_is_not_blank(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Track title must be non-empty")

    def update(self, title: Optional[str] = None, duration: Optional[int] = None, audio_key: Optional[str] = None) -> Track:
        return Track(id=self.id, 
                     title=title if title else self.title, duration=duration if duration else self.duration, 
                     audio_key=audio_key if audio_key else self.audio_key,
                     )

    @staticmethod
    def to_dict_with_url(obj, audio_url: str) -> dict:
        if isinstance(obj, Track):
            return {
                "id": obj.id,
                "title": obj.title,
                "duration": obj.duration,
                "audio_url": audio_url
            }
        else:
            new_obj = obj.to_dict()
            new_obj.pop("audio_key")
            new_obj["audio_url"] = audio_url
            
            return new_obj
