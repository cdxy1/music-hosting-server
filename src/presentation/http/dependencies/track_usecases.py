from src.application.usecases.track.create_track_usecase import CreateTrackUsecase
from src.application.usecases.track.delete_track_usecase import DeleteTrackUsecase
from src.application.usecases.track.get_all_tracks_usecase import GetAllTracksUsecase
from src.application.usecases.track.get_track_usecase import GetTrackUsecase
from src.infrastructure.repository.release_repository_impl import ReleaseRepository
from src.infrastructure.repository.track_repository_impl import TrackRepository
from src.infrastructure.background_tasks.dispatcher import TasksDispatcher
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_create_track_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    track_repo = TrackRepository()
    release_repo = ReleaseRepository()
    task_dispatcher = TasksDispatcher()
    
    usecase = CreateTrackUsecase(track_repo=track_repo, release_repo=release_repo, dispatcher=task_dispatcher,uow_factory=uow)

    return usecase

def get_all_tracks_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = TrackRepository()
    
    usecase = GetAllTracksUsecase(repo, uow)

    return usecase    

def get_track_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = TrackRepository()
    
    usecase = GetTrackUsecase(repo, uow)

    return usecase    

def get_delete_track_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = TrackRepository()
    
    usecase = DeleteTrackUsecase(repo, uow)

    return usecase    
