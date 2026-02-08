from uuid import UUID

from pydantic import BaseModel

from src.domain.enums.author_type import AuthorType


class CreateAuthorBase(BaseModel):
   class Config:
       use_enum_values = True

class CreateAuthorRequest(CreateAuthorBase):
    name: str
    type: AuthorType
    
class CreateAuthorResponse(CreateAuthorBase):
    id: UUID
