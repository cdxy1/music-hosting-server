from src.application.usecases.track.update_track_usecase import UpdateTrackUsecase
from src.infrastructure.repository.track_repository_impl import TrackRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_update_track_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = TrackRepository()
    usecase = UpdateTrackUsecase(repository, uow)
    
    return usecase
