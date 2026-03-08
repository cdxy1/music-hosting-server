from typing import Callable, override

from src.application.cache.contract import ICacheWrapper
from src.application.dispatcher.contract import IDispatcher
from src.application.dto.track_dto import TrackInputDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork
from src.application.usecases.base import BaseUsecase
from src.domain.entities.track import Track


class CreateTrackUsecase(BaseUsecase):
    @override
    def __init__(self, track_repo: IRepository, release_repo: IRepository, dispatcher: IDispatcher, uow_factory: Callable[[], IUnitOfWork], cache: ICacheWrapper):
        self.track_repo = track_repo
        self.release_repo = release_repo
        self.dispatcher = dispatcher
        self.uow_factory = uow_factory
        self.cache = cache
    
    async def __call__(self, track_dto: TrackInputDTO):
        uow = self.uow_factory()
        async with uow() as session:
            release = await self.release_repo.get_by_id(session, track_dto.release_id)
            track = Track(title=track_dto.title)

            self.track_repo.create(session, track, release)
            self.dispatcher.dispatch_upload_file("tracks", track.id, track_dto.audio_data)
            
            await self.cache.invalidate_cache(["tracks:all"])
            return track.id
