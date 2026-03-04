from uuid import UUID
from typing import override

from src.application.dto.track_dto import TrackOutputDTO
from src.application.usecases.base import BaseUsecase


class GetTrackUsecase(BaseUsecase): 
    @override
    def __init__(self, repo, uow_factory, cache, file_storage):
        super().__init__(repo, uow_factory, cache)
        self.file_storage = file_storage
    
    async def __call__(self, track_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            track = await self.cache.get_or_create(f"tracks:{track_id}", lambda: self.repo.get_by_id(session, track_id))
            track_url = self.file_storage.get_file_url(track.audio_key) if track.audio_key else None
            track_with_url = track.to_dict_with_url(track_url)
            
            return TrackOutputDTO(**track_with_url)
