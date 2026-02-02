from sqlalchemy.ext.asyncio import AsyncSession

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.infrastructure.models.author import AuthorModel


class AuthorRepository(IRepository):  
    def create(self, session: AsyncSession, author: AuthorDTO):
        author = AuthorModel(
            name=author.name,
            type=author.type,
        )
        session.add(author)
