from uuid import UUID

from pydantic import BaseModel


class GenreBase(BaseModel):
    class Config:
        use_enum_values = True

class CreateGenreRequest(GenreBase):
    title: str

class CreateGenreResponse(GenreBase):
    id: UUID

class GetGenresResponse(GenreBase):
    id: UUID
    title: str
