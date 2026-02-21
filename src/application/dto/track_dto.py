from dataclasses import dataclass
from uuid import UUID

from src.application.dto.base_dto import BaseDTO


@dataclass(frozen=True, slots=True)
class TrackInputDTO(BaseDTO):
    title: str
    release_id: UUID
