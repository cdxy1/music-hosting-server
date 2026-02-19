from uuid import UUID

# from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.release import Release
from src.infrastructure.models.release import ReleaseModel


class ReleaseRepository(IRepository):
    def create(self, session: AsyncSession, release: Release):
        release_orm_model = ReleaseModel(
            release_id=release.id,
            name=release.name,
            release_date=release.release_date,
            release_type=release.release_type,
            author_fk=release.author.id,
            genre_fk=release.genre.id
        )
        
        session.add(release_orm_model)
    
    async def get_by_id(self, session: AsyncSession, genre_id: UUID):
        ...
        
    async def get_all(self, session: AsyncSession):
        ...
        
    async def delete(self, session: AsyncSession, genre_id: UUID):
        ...
        
    async def update(self, session: AsyncSession):
        ...
