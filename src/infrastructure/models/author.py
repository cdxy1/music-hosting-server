from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models.base import BaseOrmModel


class AuthorModel(BaseOrmModel):
    __tablename__ = "author"

    author_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default_factory=uuid4)
    name: Mapped[str] = mapped_column(str, nullable=False)
    type: Mapped[str] = mapped_column(str, nullable=False)
