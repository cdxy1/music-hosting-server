from uuid import UUID

from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.release_usecases import (
    get_all_releases_usecase,
    get_create_release_usecase,
    get_delete_release_usecase,
    get_release_usecase,
)
from src.presentation.http.mappers.release_mapper import (
    dto_to_pydantic,
    many_dto_to_pydantic,
    pydantic_to_dto,
)
from src.presentation.http.schemas.release import CreateReleaseRequest

router = APIRouter(prefix="/releases", tags=["releases"])

@router.post("/")
async def create_release(release: CreateReleaseRequest, usecase = Depends(get_create_release_usecase)):
    input_data = pydantic_to_dto(release)
    release = await usecase(input_data)
    response = dto_to_pydantic(release)
    
    return response

@router.get("/")
async def get_all_releases(usecase = Depends(get_all_releases_usecase)):
    releases = await usecase()
    response = many_dto_to_pydantic(releases)
    
    return response

@router.get("/{release_id}")
async def get_release(release_id: UUID, usecase = Depends(get_release_usecase)):
    response = await usecase(release_id)
    return response

@router.delete("/{release_id}")
async def delete_release(release_id: UUID, usecase = Depends(get_delete_release_usecase)):
    response = await usecase(release_id)

    return response
