from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.models.base import BaseOrmModel


class GenreModel(BaseOrmModel):
    __tablename__ = "genre"

    genre_id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    release = relationship("ReleaseModel", back_populates="genre", uselist=True, lazy="selectin")
