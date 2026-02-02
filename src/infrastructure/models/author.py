from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models.base import BaseOrmModel


class AuthorModel(BaseOrmModel):
    __tablename__ = "author"

    author_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
