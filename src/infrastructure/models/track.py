from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.models.base import BaseOrmModel


class TrackModel(BaseOrmModel):
    __tablename__ = "track"

    track_id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    duration: Mapped[int]
    audio_key: Mapped[str] = Mapped(unique=True)
    image_key: Mapped[str] = Mapped(unique=True)
    release_fk: Mapped[UUID] = mapped_column(ForeignKey("release.release_id"))
    
    release = relationship("ReleaseModel", back_populates="tracks", uselist=False, lazy="selectin")
