from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.models.base import BaseOrmModel


class ReleaseModel(BaseOrmModel):
    __tablename__ = "release"
    
    release_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[UUID] = mapped_column(ForeignKey(
        "author.author_id"
        ))
    genre: Mapped[UUID] = mapped_column(ForeignKey(
        "genre.genre_id"
    ))
    realease_data: Mapped[datetime]
    
