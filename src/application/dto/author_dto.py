from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.application.dto.base_dto import BaseDTO
from src.domain.enums.author_type import AuthorType


@dataclass(frozen=True, slots=True)
class AuthorDTO(BaseDTO):
    name: str
    type: AuthorType
    id: Optional[UUID] = None
    
@dataclass(frozen=True, slots=True)
class UpdateAuthorDTO(BaseDTO):
    name: Optional[str] = None
    type : Optional[AuthorType] = None
