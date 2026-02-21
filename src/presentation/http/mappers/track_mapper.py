from src.application.dto.track_dto import TrackInputDTO, TrackOutputDTO
from src.presentation.http.schemas.track import CreateTrackRequest, GetTrackResponse


def pydantic_to_dto(input: CreateTrackRequest):
    return TrackInputDTO(**input.model_dump())

def dto_to_pydantic(output: TrackOutputDTO):
    return GetTrackResponse(**output.to_dict())

def many_dto_to_pydantic(output: tuple[TrackOutputDTO]):
    return tuple(GetTrackResponse(**dto.to_dict()) for dto in output)
