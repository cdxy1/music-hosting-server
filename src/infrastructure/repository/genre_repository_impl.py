from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.genre import Genre
from src.infrastructure.models.genre import GenreModel


class GenreRepository(IRepository):
    def create(self, session: AsyncSession, genre: Genre):
        genre_orm_model = GenreModel(
            genre_id=genre.id,
            title=genre.title
        )
        
        session.add(genre_orm_model)
    
    async def get_by_id(self, session: AsyncSession, genre_id: UUID):
        stmt = (select(GenreModel)
                .where(GenreModel.genre_id == genre_id))
        
        result = await session.execute(stmt)
        genre_from_db = result.scalar()
        
        return Genre(
            title=genre_from_db.title,
            id=genre_from_db.genre_id,
        )
        
    async def get_all(self, session: AsyncSession):
        stmt = select(GenreModel)
        
        result = await session.execute(stmt)
        genres_from_db = result.scalars().all()
        
        genres = tuple(Genre(id=genre.genre_id, title=genre.title) for genre in genres_from_db)
                
        return genres
        
    async def delete(self, session: AsyncSession, genre_id: UUID):
        stmt = (delete(GenreModel).
                where(GenreModel.genre_id == genre_id))
        
        await session.execute(stmt)  
        
    async def update(self, session: AsyncSession):
        ...
