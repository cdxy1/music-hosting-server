from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.author import Author
from src.domain.entities.genre import Genre
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
    
    async def get_by_id(self, session: AsyncSession, release_id: UUID):
        stmt = (select(ReleaseModel)
                .where(ReleaseModel.release_id == release_id))
        
        result = await session.execute(stmt)
        release_from_db = result.scalar()
        
        return Release(
            name=release_from_db.name,
            author=release_from_db.author,
            genre=release_from_db.genre,
            release_type=release_from_db.release_type,
            release_date=release_from_db.release_date,
            id=release_from_db.release_id
        )
        
    async def get_all(self, session: AsyncSession):
        stmt = select(ReleaseModel)
        
        result = await session.execute(stmt)
        releases_from_db = result.scalars().all()
        
        releases = []
        for release in releases_from_db:
            author = Author(name=release.author.name, type=release.author.type, id=release.author.author_id)
            genre = Genre(title=release.genre.title, id=release.genre.genre_id)
            
            releases.append(Release(name=release.name, author=author, genre=genre, release_type=release.release_type, release_date=release.release_date,id=release.release_id))
                
        return tuple(releases)
        
    async def delete(self, session: AsyncSession, release_id: UUID):
        stmt = (delete(ReleaseModel).
                where(ReleaseModel.release_id == release_id))
        
        await session.execute(stmt)
        
    async def update(self, session: AsyncSession):
        ...
