from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.genre import Genre
from src.infrastructure.models.genre import GenreModel

class GenreRepository(IRepository):
    def create(self, session: AsyncSession, genre: Genre):
        ...
    
    async def get_by_id(self, session: AsyncSession, genre_id: UUID):
        ...
        
    async def get_all(self, session: AsyncSession):
        ...
        
    async def delete(self, session: AsyncSession, genre_id: UUID):
        ...
        
    async def update(self, session: AsyncSession):
        ...
        
    async def exists(self, session: AsyncSession):
        ...
