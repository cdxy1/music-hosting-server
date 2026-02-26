from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TrackBase(BaseModel):
    class Config:
        use_enum_values = True

class CreateTrackRequest(TrackBase):
    title: str
    release_id: UUID
    
class GetTrackResponse(TrackBase):
    id: UUID
    title: str
    duration: Optional[int] = None
    audio_key: Optional[str] = None
