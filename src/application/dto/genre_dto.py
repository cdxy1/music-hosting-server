from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.application.dto.base_dto import BaseDTO


@dataclass(frozen=True, slots=True)
class GenreDTO(BaseDTO):
    title: str
    id: Optional[UUID] = None
