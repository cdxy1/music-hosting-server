from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.genre_usecase import (
    get_all_genre_usecase,
    get_create_genre_usecase,
)
from src.presentation.http.mappers.genre_mapper import (
    dto_to_get_all_genres_pydantic,
    dto_to_pydantic,
    pydantic_to_dto,
)
from src.presentation.http.schemas.genre import CreateGenreRequest

router = APIRouter(prefix="/genres", tags=["genres"])

@router.post("/")
async def create_genre(genre: CreateGenreRequest, usecase = Depends(get_create_genre_usecase)):
    input_data = pydantic_to_dto(genre)
    genre_dto = await usecase(input_data)
    output_data = dto_to_pydantic(genre_dto)
    
    return output_data

@router.get("/")
async def get_genres(usecase = Depends(get_all_genre_usecase)):
    genres = await usecase()
    output_data = dto_to_get_all_genres_pydantic(genres)
    
    return output_data
