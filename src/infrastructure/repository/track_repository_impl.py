from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository.contract import IRepository
from src.domain.entities.release import Release
from src.domain.entities.track import Track
from src.infrastructure.models.track import TrackModel


class TrackRepository(IRepository):
    def create(self, session: AsyncSession, track: Track, release: Release):
        track_orm_model = TrackModel(
            track_id = track.id,
            title=track.title,
            duration=track.duration,
            release_fk=release.id
        )
        
        session.add(track_orm_model)
    
    async def get_by_id(self, session: AsyncSession, track_id: UUID):
        stmt = (select(TrackModel)
                .where(TrackModel.track_id == track_id))
        
        result = await session.execute(stmt)
        track_from_db = result.scalar()
        
        return Track(
            id=track_from_db.track_id,
            title=track_from_db.title,
            duration=track_from_db.duration,
            audio_key=track_from_db.audio_key
        )
        
    async def get_all(self, session: AsyncSession):
        stmt = select(TrackModel)
        
        result = await session.execute(stmt)
        track_from_db = result.scalars().all()
        
        tracks = tuple(Track(id=track.track_id, title=track.title, duration=track.duration, audio_key=track.audio_key, image_key=track.image_key) for track in track_from_db)
                
        return tuple(tracks)
        
    async def delete(self, session: AsyncSession, track_id: UUID):
        stmt = (delete(TrackModel).
                where(TrackModel.track_id == track_id))
        
        await session.execute(stmt)
        
    async def update(self, session: AsyncSession, track: Track):
        data_to_update = {k: v if not isinstance(v, UUID) else str(v) 
                          for k, v in track.to_dict().items() 
                          if k != "id" and v}
        
        stmt = (update(TrackModel).
                where(TrackModel.track_id == track.id).
                values(**data_to_update))
        
        await session.execute(stmt)
