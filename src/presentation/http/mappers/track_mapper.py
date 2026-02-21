from src.application.dto.track_dto import TrackInputDTO
from src.presentation.http.schemas.track import CreateTrackRequest


def pydantic_to_dto(input: CreateTrackRequest):
    return TrackInputDTO(**input.model_dump())
