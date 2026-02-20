from src.application.dto.release_dto import ReleaseOutputDTO
from src.application.usecases.base import BaseUsecase


class GetAllReleasesUsecase(BaseUsecase):
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            releases = await self.repo.get_all(session)
            
            return tuple(ReleaseOutputDTO(**release.to_dict()) for release in releases)
