from datetime import date
from uuid import UUID

from pydantic import BaseModel

from src.domain.enums.release_type import ReleaseType


class CreateReleaseRequest(BaseModel):
    name: str
    author_id: UUID
    genre_id: UUID
    release_date: date
    release_type: ReleaseType
