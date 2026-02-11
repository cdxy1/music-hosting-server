from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.presentation.http.dependencies.author_usecases import (
    get_all_authors_usecase,
    get_author_usecase,
    get_create_author_usecase,
    get_delete_author_usecase,
)
from src.presentation.http.mappers.author_mapper import (
    dto_to_create_author_pydantic,
    dto_to_delete_author_pydantic,
    dto_to_get_all_author_pydantic,
    dto_to_get_author_pydantic,
    pydantic_to_dto,
)
from src.presentation.http.schemas.author import (
    CreateAuthorRequest,
    CreateAuthorResponse,
)

router = APIRouter(prefix="/authors", tags=["authors"])

@router.post("/")
async def create_author(author: CreateAuthorRequest, usecase: CreateAuthorUsecase = Depends(get_create_author_usecase)) -> CreateAuthorResponse:
    input_data = pydantic_to_dto(author)
    author_dto = await usecase(input_data)
    response = dto_to_create_author_pydantic(author_dto)
    
    return response
    
@router.get("/")
async def get_authors(usecase: CreateAuthorUsecase = Depends(get_all_authors_usecase)):
    authors_dto = await usecase()
    response = dto_to_get_all_author_pydantic(authors_dto)
    
    return response

@router.get("/{author_id}")
async def get_author(author_id: UUID, usecase: CreateAuthorUsecase = Depends(get_author_usecase)):
    author_dto = await usecase(author_id)
    response = dto_to_get_author_pydantic(author_dto)
    
    return response

@router.delete("/{author_id}")
async def delete_author(author_id: UUID, usecase = Depends(get_delete_author_usecase)):
    author_uuid = await usecase(author_id)
    response = dto_to_delete_author_pydantic(author_uuid)
    
    return response
