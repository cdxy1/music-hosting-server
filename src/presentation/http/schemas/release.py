from datetime import date
from uuid import UUID
from typing import Optional

from pydantic import BaseModel

from src.domain.enums.release_type import ReleaseType
from src.presentation.http.schemas.author import GetAuthorResponse
from src.presentation.http.schemas.genre import GetGenreResponse


class CreateReleaseRequest(BaseModel):
    name: str
    author_id: UUID
    genre_id: UUID
    release_date: date
    release_type: ReleaseType

class CreateReleaseResponse(BaseModel):
    id: UUID

class GetReleaseResponse(BaseModel):
    name: str
    author: GetAuthorResponse
    genre: GetGenreResponse
    release_date: date
    release_type: ReleaseType
    id: Optional[UUID] = None
