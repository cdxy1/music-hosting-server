from dataclasses import dataclass
from datetime import date
from typing import Optional
from uuid import UUID

from src.application.dto.author_dto import AuthorDTO
from src.application.dto.base_dto import BaseDTO
from src.application.dto.genre_dto import GenreDTO
from src.domain.enums.release_type import ReleaseType


@dataclass(frozen=True, slots=True)
class ReleaseOutputDTO(BaseDTO):
    name: str
    author: AuthorDTO
    genre: GenreDTO
    release_date: date
    release_type: ReleaseType
    image_url: str
    id: Optional[UUID] = None

@dataclass(frozen=True, slots=True)
class ReleaseInputDTO(BaseDTO):
    name: str
    author_id: UUID
    genre_id: UUID
    release_date: date
    release_type: ReleaseType
    image_data: str

