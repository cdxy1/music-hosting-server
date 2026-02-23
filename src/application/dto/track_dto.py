from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.application.dto.base_dto import BaseDTO


@dataclass(frozen=True, slots=True)
class TrackInputDTO(BaseDTO):
    title: str
    audio_data: str
    release_id: UUID
    
@dataclass(frozen=True, slots=True)
class TrackOutputDTO(BaseDTO):
    id: UUID
    title: str
    duration: Optional[int] = None
    audio_key: Optional[str] = None
    image_key: Optional[str] = None
    

@dataclass(frozen=True, slots=True)
class UpdateTrackDTO(BaseDTO):
    title: Optional[str] = None
    duration: Optional[int] = None
    audio_key: Optional[str] = None
    image_key: Optional[str] = None    
