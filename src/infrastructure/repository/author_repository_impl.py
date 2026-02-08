from uuid import UUID

from sqlalchemy import select
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
        
    async def get_by_id(self, session: AsyncSession, author_id: UUID) -> Author:
        stmt = (select(AuthorModel)
                .where(AuthorModel.author_id == author_id))
        
        result = await session.execute(stmt)
        author_from_db = result.scalar()
        
        
        return Author(
            name=author_from_db.name,
            type=author_from_db.type,
            id=author_from_db.author_id,
        )
        
    async def get_all(self, session: AsyncSession):
        ...

    async def delete(self, session: AsyncSession):
        ...
        
    async def update(self, session: AsyncSession):
        ...
        
    async def exists(self, session: AsyncSession):
        ...
