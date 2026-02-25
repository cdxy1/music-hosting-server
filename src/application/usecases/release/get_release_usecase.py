from uuid import UUID

from src.application.dto.release_dto import ReleaseOutputDTO
from src.application.usecases.base import BaseUsecase


class GetReleaseUsecase(BaseUsecase): 
    async def __call__(self, release_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            release = await self.cache.get_or_create(f"releases:{release_id}", lambda: self.repo.get_by_id(session, release_id))
            
            return ReleaseOutputDTO(**release.to_dict())
