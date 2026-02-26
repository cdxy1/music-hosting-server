from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.models.base import BaseOrmModel


class TrackModel(BaseOrmModel):
    __tablename__ = "track"

    track_id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    duration: Mapped[int] = mapped_column(nullable=True)
    audio_key: Mapped[str] = mapped_column(unique=True, nullable=True)
    release_fk: Mapped[UUID] = mapped_column(ForeignKey("release.release_id"))
    
    release = relationship("ReleaseModel", back_populates="tracks", uselist=False, lazy="selectin")
