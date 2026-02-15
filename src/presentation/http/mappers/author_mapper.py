from uuid import UUID

from src.application.dto.author_dto import AuthorDTO
from src.presentation.http.schemas.author import (
    CreateAuthorRequest,
    CreateAuthorResponse,
    DeleteAuthorResponse,
    GetAuthorResponse,
)


def pydantic_to_dto(input: CreateAuthorRequest) -> AuthorDTO:
    return AuthorDTO(**input.model_dump())

def dto_to_create_author_pydantic(output: AuthorDTO) -> CreateAuthorResponse:
    return CreateAuthorResponse(**output.to_dict())

def dto_to_get_author_pydantic(output: AuthorDTO) -> CreateAuthorResponse:
    return GetAuthorResponse(**output.to_dict())

def dto_to_get_all_authors_pydantic(output: tuple[AuthorDTO]) -> tuple[CreateAuthorResponse]:
    return tuple(GetAuthorResponse(**dto.to_dict()) for dto in output)

def dto_to_delete_author_pydantic(output: UUID) -> DeleteAuthorResponse:
    return DeleteAuthorResponse(id=output)
