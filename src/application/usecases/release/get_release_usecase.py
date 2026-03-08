from typing import override
from uuid import UUID

from src.application.dto.release_dto import ReleaseOutputDTO
from src.application.usecases.base import BaseUsecase
from src.domain.entities.release import Release


class GetReleaseUsecase(BaseUsecase): 
    @override
    def __init__(self, repo, uow_factory, cache, file_storage):
        super().__init__(repo, uow_factory, cache)
        self.file_storage = file_storage    

    async def __call__(self, release_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            release = await self.cache.get_or_create(f"releases:{release_id}", lambda: self.repo.get_by_id(session, release_id))
            image_url = self.file_storage.get_file_url(release.image_key) if release.image_key else None
            
            release_with_url = Release.to_dict_with_url(release,image_url)
            
            return ReleaseOutputDTO(**release_with_url)
