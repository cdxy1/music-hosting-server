from src.application.dto.genre_dto import GenreDTO
from src.presentation.http.schemas.genre import (
    CreateGenreRequest,
    CreateGenreResponse,
    GetGenresResponse,
)


def pydantic_to_dto(input: CreateGenreRequest) -> GenreDTO:
    return GenreDTO(**input.model_dump())

def dto_to_pydantic(output: GenreDTO):
    return CreateGenreResponse(**output.to_dict())

def dto_to_get_all_genres_pydantic(output: tuple[GenreDTO]) -> tuple[CreateGenreResponse]:
    return tuple(GetGenresResponse(**dto.to_dict()) for dto in output)
