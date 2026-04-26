from dataclasses import dataclass, field
from datetime import date
from typing import Any, Optional, Union
from uuid import UUID, uuid4

from src.domain.entities.author import Author
from src.domain.entities.base import BaseEntity
from src.domain.entities.genre import Genre

from src.domain.enums.release_type import ReleaseType


@dataclass(slots=True, frozen=True)
class Release(BaseEntity):
    name: str
    author: Author
    genre: Genre
    release_type: ReleaseType
    release_date: date
    image_key: Optional[str] = None
    id: UUID = field(default_factory=uuid4) 
    
    @staticmethod
    def to_dict_with_url(obj: Union[Release|Any], image_url: str) -> dict:
        if isinstance(obj, Release):
            return {
                "id": obj.id,
                "name": obj.name,
                "author": obj.author,
                "genre": obj.genre,
                "release_type": obj.release_type,
                "release_date": obj.release_date,
                "image_url": image_url
            }
        else:
            new_obj = obj.to_dict()
            new_obj.pop("image_key")
            new_obj["image_url"] = image_url
            
            return new_obj
