from base64 import b64encode
from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, File, UploadFile

from src.domain.enums.release_type import ReleaseType
from src.presentation.http.dependencies.release_usecases import (
    get_all_releases_usecase,
    get_create_release_usecase,
    get_delete_release_usecase,
    get_release_usecase,
)
from src.presentation.http.mappers.release_mapper import (
    many_dto_to_pydantic,
    pydantic_to_dto,
)
from src.presentation.http.schemas.release import CreateReleaseRequest

router = APIRouter(prefix="/releases", tags=["releases"])

@router.post("/")
async def create_release(
    name: str,
    author_id: UUID,
    genre_id: UUID,
    release_date: date,
    release_type: ReleaseType,
    file: UploadFile = File(...),
    usecase = Depends(get_create_release_usecase)):
    file_bytes = await file.read()
    encode_file = b64encode(file_bytes).decode("utf-8")
    
    release = CreateReleaseRequest(name=name, author_id=author_id, genre_id=genre_id, release_date=release_date, release_type=release_type)
    input_data = pydantic_to_dto(release, encode_file)
    
    response = await usecase(input_data)
    
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
