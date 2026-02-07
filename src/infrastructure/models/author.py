from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models.base import BaseOrmModel


class AuthorModel(BaseOrmModel):
    __tablename__ = "author"

    author_id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    type: Mapped[str] = mapped_column(nullable=False)
