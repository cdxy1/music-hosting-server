from uuid import UUID

from src.application.dto.track_dto import TrackOutputDTO
from src.application.usecases.base import BaseUsecase


class GetTrackUsecase(BaseUsecase): 
    async def __call__(self, track_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            track = await self.cache.get_or_create(f"tracks:{track_id}", lambda: self.repo.get_by_id(session, track_id))
            
            return TrackOutputDTO(**track.to_dict())
