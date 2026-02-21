from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.domain.enums.release_type import ReleaseType
from src.presentation.http.schemas.author import GetAuthorResponse
from src.presentation.http.schemas.genre import GetGenreResponse


class ReleaseBase(BaseModel):
    class Config:
        use_enum_values = True

class CreateReleaseRequest(ReleaseBase):
    name: str
    author_id: UUID
    genre_id: UUID
    release_date: date
    release_type: ReleaseType

class CreateReleaseResponse(ReleaseBase):
    id: UUID

class GetReleaseResponse(ReleaseBase):
    name: str
    author: GetAuthorResponse
    genre: GetGenreResponse
    release_date: date
    release_type: ReleaseType
    id: Optional[UUID] = None
