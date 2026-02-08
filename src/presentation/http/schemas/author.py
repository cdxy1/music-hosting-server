from uuid import UUID

from pydantic import BaseModel

from src.domain.enums.author_type import AuthorType


class AuthorBase(BaseModel):
   class Config:
       use_enum_values = True

class CreateAuthorRequest(AuthorBase):
    name: str
    type: AuthorType
    
class CreateAuthorResponse(AuthorBase):
    id: UUID


class GetAuthorResponse(AuthorBase):
    id: UUID
    name: str
    type: AuthorType
