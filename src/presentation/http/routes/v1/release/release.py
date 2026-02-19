from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.release_usecases import (
    get_create_release_usecase,
)
from src.presentation.http.mappers.release_mapper import pydantic_to_dto
from src.presentation.http.schemas.release import CreateReleaseRequest

router = APIRouter(prefix="/releases", tags=["releases"])

@router.post("/")
async def create_release(release: CreateReleaseRequest, usecase = Depends(get_create_release_usecase)):
    input_data = pydantic_to_dto(release)
    release = await usecase(input_data)
    
    return release
