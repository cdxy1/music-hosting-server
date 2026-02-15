from pydantic import BaseModel


class GenreBase(BaseModel):
    class Config:
        use_enum_values = True

class CreateGenreRequest(GenreBase):
    title: str
