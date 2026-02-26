from datetime import date
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.models.base import BaseOrmModel


class ReleaseModel(BaseOrmModel):
    __tablename__ = "release"
    
    release_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    author_fk: Mapped[UUID] = mapped_column(ForeignKey("author.author_id"))
    genre_fk: Mapped[UUID] = mapped_column(ForeignKey("genre.genre_id"))
    release_date: Mapped[date] = mapped_column( nullable=False)
    release_type: Mapped[str] = mapped_column(nullable=False)
    # image_key: Mapped[str] = mapped_column(unique=True, nullable=True)
    
    author = relationship("AuthorModel", back_populates="release", uselist=False, lazy="selectin")
    genre = relationship("GenreModel", back_populates="release", uselist=False, lazy="selectin")
    tracks = relationship("TrackModel", back_populates="release", uselist=True, lazy="selectin")
    
