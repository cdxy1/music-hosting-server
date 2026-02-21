from src.application.dto.track_dto import TrackOutputDTO
from src.application.usecases.base import BaseUsecase


class GetAllTracksUsecase(BaseUsecase):
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            tracks = await self.repo.get_all(session)
            
            return tuple(TrackOutputDTO(**track.to_dict()) for track in tracks)
