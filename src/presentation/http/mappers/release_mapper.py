from src.application.dto.release_dto import ReleaseInputDTO
from src.presentation.http.schemas.release import CreateReleaseRequest


def pydantic_to_dto(input: CreateReleaseRequest):
    return ReleaseInputDTO(**input.model_dump())
