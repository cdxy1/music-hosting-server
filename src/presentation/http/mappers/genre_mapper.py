from src.application.dto.genre_dto import GenreDTO
from src.presentation.http.schemas.genre import CreateGenreRequest


def pydantic_to_dto(input: CreateGenreRequest) -> GenreDTO:
    return GenreDTO(**input.model_dump())
