from src.application.dto.author_dto import AuthorDTO
from src.presentation.http.schemas.author import (
    CreateAuthorRequest,
    CreateAuthorResponse,
)


def pydantic_to_dto(input: CreateAuthorRequest) -> AuthorDTO:
    return AuthorDTO(**input.model_dump())

def dto_to_pydantic(output: AuthorDTO) -> CreateAuthorResponse:
    return CreateAuthorResponse(id=output.id)
