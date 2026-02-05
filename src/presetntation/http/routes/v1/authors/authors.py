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

@router.get("/")
async def get_authors(author: CreateAuthorRequest, usecase: CreateAuthorUsecase = Depends(get_create_author_usecase)) -> CreateAuthorResponse:
    usecase()

@router.post("/")
async def create_author():
    ...

@router.get("/{author_id}")
async def get_author():
    ...
