from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models.base import BaseOrmModel


class AuthorModel(BaseOrmModel):
    __tablename__ = "author"

    author_id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(str, nullable=False)
    type: Mapped[str] = mapped_column(str, nullable=False)
