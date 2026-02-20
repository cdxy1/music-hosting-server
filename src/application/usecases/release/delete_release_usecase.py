from uuid import UUID

from src.application.usecases.base import BaseUsecase


class DeleteReleaseUsecase(BaseUsecase):
    async def __call__(self, release_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            await self.repo.delete(session, release_id)
            
            return release_id
