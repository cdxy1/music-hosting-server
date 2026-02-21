from src.application.usecases.track.create_track_usecase import CreateTrackUsecase
from src.infrastructure.repository.release_repository_impl import ReleaseRepository
from src.infrastructure.repository.track_repository_impl import TrackRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_create_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    track_repo = TrackRepository()
    release_repo = ReleaseRepository()
    
    usecase = CreateTrackUsecase(track_repo=track_repo, release_repo=release_repo, uow_factory=uow)

    return usecase
