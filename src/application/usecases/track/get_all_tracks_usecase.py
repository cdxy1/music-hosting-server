from typing import override

from src.application.dto.track_dto import TrackOutputDTO
from src.application.usecases.base import BaseUsecase


class GetAllTracksUsecase(BaseUsecase):
    @override
    def __init__(self, repo, uow_factory, cache, file_storage):
        super().__init__(repo, uow_factory, cache)
        self.file_storage = file_storage    
    
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            tracks = await self.cache.get_or_create("tracks:all", lambda: self.repo.get_all(session))
            
            tracks_with_url = []
            for track in tracks:
                track_url = self.file_storage.get_file_url(track.audio_key) if track.audio_key else None
                
                track_with_url = track.to_dict_with_url(track_url)
                tracks_with_url.append(track_with_url)
            
            return tuple(TrackOutputDTO(**track) for track in tracks_with_url)
