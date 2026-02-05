from uuid import UUID

from pydantic import BaseModel


class CreateAuthorRequest(BaseModel):
    name: str
    type: str
    
class CreateAuthorResponse(BaseModel):
    id: UUID
    name: str
    type: str
