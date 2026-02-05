from src.application.dto.author_dto import AuthorDTO
from src.presetntation.http.schemas.author import CreateAuthorRequest, CreateAuthorResponse

def pydantic_to_dto(input: CreateAuthorRequest) -> AuthorDTO:
    ...

def dto_to_pydantic(output: AuthorDTO) -> CreateAuthorResponse:
    ...
