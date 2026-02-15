from src.presentation.http.schemas.genre import CreateGenreRequest
from src.application.dto.genre_dto import GenreDTO


def pydantic_to_dto(input: CreateGenreRequest) -> GenreDTO:
    return GenreDTO(**input.model_dump())
