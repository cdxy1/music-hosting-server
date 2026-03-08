from typing import override

from src.application.dto.release_dto import ReleaseOutputDTO
from src.application.usecases.base import BaseUsecase
from src.domain.entities.release import Release


class GetAllReleasesUsecase(BaseUsecase):
    @override
    def __init__(self, repo, uow_factory, cache, file_storage):
        super().__init__(repo, uow_factory, cache)
        self.file_storage = file_storage
    
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            releases = await self.cache.get_or_create("releases:all", lambda: self.repo.get_all(session))
            
            releases_with_url = []
            for release in releases:
                image_url = self.file_storage.get_file_url(release.image_key) if release.image_key else None
                
                release_with_url = Release.to_dict_with_url(release, image_url)
                releases_with_url.append(release_with_url)
            
            return tuple(ReleaseOutputDTO(**release) for release in releases_with_url)
