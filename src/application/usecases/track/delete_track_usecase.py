from uuid import UUID

from src.application.usecases.base import BaseUsecase


class DeleteTrackUsecase(BaseUsecase):
    async def __call__(self, track_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            await self.repo.delete(session, track_id)
            await self.cache.invalidate_cache(["tracks:all", f"tracks:{track_id}"])
            
            return track_id
