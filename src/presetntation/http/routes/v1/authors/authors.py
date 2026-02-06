from fastapi import APIRouter, Depends

from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.presetntation.http.dependencies.author_usecases import (
    get_create_author_usecase,
)
from src.presetntation.http.schemas.author import (
    CreateAuthorRequest,
    CreateAuthorResponse,
)

router = APIRouter(prefix="/authors", tags=["authors"])

@router.post("/")
async def create_author(author: CreateAuthorRequest, usecase: CreateAuthorUsecase = Depends(get_create_author_usecase)) -> CreateAuthorResponse:
    from src.application.dto.author_dto import AuthorDTO
    await usecase(AuthorDTO(name=author.name, type=author.type))
    
@router.get("/")
async def get_authors():
    ...

@router.get("/{author_id}")
async def get_author():
    ...
