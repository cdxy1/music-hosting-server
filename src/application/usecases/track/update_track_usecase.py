from uuid import UUID

from src.application.dto.track_dto import UpdateTrackDTO
from src.application.usecases.base import BaseUsecase


class UpdateTrackUsecase(BaseUsecase):
    async def __call__(self, track_id: UUID, data_to_update: UpdateTrackDTO):
        uow = self.uow_factory()
        async with uow() as session:
            track = await self.repo.get_by_id(session, track_id)
            updated_track = track.update(**data_to_update.to_dict())
            await self.repo.update(session, updated_track)
            
            return updated_track.id
