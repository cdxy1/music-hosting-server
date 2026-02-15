from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.genre_usecase import get_create_genre_usecase
from src.presentation.http.schemas.genre import CreateGenreRequest
from src.presentation.http.mappers.genre_mapper import pydantic_to_dto

router = APIRouter(prefix="/genres", tags=["genres"])

@router.post("/")
async def create_genr(genre: CreateGenreRequest, usecase = Depends(get_create_genre_usecase)):
    input_data = pydantic_to_dto(genre)
    genre_dto = await usecase(input_data)

    return genre
