from src.application.dto.genre_dto import GenreDTO, UpdateGenreDTO
from src.presentation.http.schemas.genre import (
    CreateGenreRequest,
    CreateGenreResponse,
    GetGenreResponse,
    UpdateGenreRequest,
)


def pydantic_to_dto(input: CreateGenreRequest) -> GenreDTO:
    return GenreDTO(**input.model_dump())

def update_pydantic_to_dto(input: UpdateGenreRequest):
    return UpdateGenreDTO(**input.model_dump())

def dto_to_pydantic(output: GenreDTO):
    return CreateGenreResponse(**output.to_dict())

def dto_to_get_all_genres_pydantic(output: tuple[GenreDTO]) -> tuple[GetGenreResponse]:
    return tuple(GetGenreResponse(**dto.to_dict()) for dto in output)

def dto_to_get_genre_pydantic(output: GenreDTO) -> GetGenreResponse:
    return GetGenreResponse(**output.to_dict())
