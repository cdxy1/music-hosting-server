from fastapi import APIRouter, Depends

from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.presetntation.http.dependencies.author_usecases import (
    get_create_author_usecase,
)
from src.presetntation.http.mappers.author_mapper import (
    dto_to_pydantic,
    pydantic_to_dto,
)
from src.presetntation.http.schemas.author import (
    CreateAuthorRequest,
    CreateAuthorResponse,
)

router = APIRouter(prefix="/authors", tags=["authors"])

@router.post("/")
async def create_author(author: CreateAuthorRequest, usecase: CreateAuthorUsecase = Depends(get_create_author_usecase)) -> CreateAuthorResponse:
    input_data = pydantic_to_dto(author)
    author_dto = await usecase(input_data)
    response = dto_to_pydantic(author_dto)
    
    return response
    
@router.get("/")
async def get_authors():
    ...

@router.get("/{author_id}")
async def get_author():
    ...
