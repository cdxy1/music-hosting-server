from uuid import UUID

from pydantic import BaseModel


class GenreBase(BaseModel):
    class Config:
        use_enum_values = True

class CreateTrackRequest(GenreBase):
    title: str
    release_id: UUID
