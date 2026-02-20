from uuid import UUID

from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.release_usecases import (
    get_create_release_usecase,
    get_all_releases_usecase,
    get_release_usecase
)
from src.presentation.http.mappers.release_mapper import pydantic_to_dto, dto_to_pydantic, many_dto_to_pydantic
from src.presentation.http.schemas.release import CreateReleaseRequest

router = APIRouter(prefix="/releases", tags=["releases"])

@router.post("/")
async def create_release(release: CreateReleaseRequest, usecase = Depends(get_create_release_usecase)):
    input_data = pydantic_to_dto(release)
    release = await usecase(input_data)
    output_data = dto_to_pydantic(release)
    
    return output_data

@router.get("/")
async def get_all_releases(usecase = Depends(get_all_releases_usecase)):
    releases = await usecase()
    output_data = many_dto_to_pydantic(releases)
    
    return output_data

@router.get("/{release_id}")
async def get_release(release_id: UUID, usecase = Depends(get_release_usecase)):
    release = await usecase(release_id)
    return release

