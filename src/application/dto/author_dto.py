from uuid import UUID
from typing import Optional
from dataclasses import dataclass

from src.domain.enums.author_type import AuthorType
from src.application.dto.base_dto import BaseDTO


@dataclass(frozen=True, slots=True)
class AuthorDTO(BaseDTO):
    name: str
    type: AuthorType
    id: Optional[UUID] = None
