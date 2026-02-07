from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.author import Author
from src.infrastructure.models.author import AuthorModel


class AuthorRepository(IRepository):  
    def create(self, session: AsyncSession, author: Author):
        author_orm_model = AuthorModel(
            author_id=author.id,
            name=author.name,
            type=author.type,
        )
        
        session.add(author_orm_model)
