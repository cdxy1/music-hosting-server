from src.application.usecases.release.create_release_usecase import CreateReleaseUsecase
from src.application.usecases.release.get_release_usecase import GetReleaseUsecase
from src.application.usecases.release.get_all_releases_usecase import GetAllReleasesUsecase
from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.infrastructure.repository.genre_repository_impl import GenreRepository
from src.infrastructure.repository.release_repository_impl import ReleaseRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_create_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    author_repo = AuthorRepository()
    genre_repo = GenreRepository()
    release_repo = ReleaseRepository()
    
    usecase = CreateReleaseUsecase(release_repo=release_repo, author_repo=author_repo, genre_repo=genre_repo, uow_factory=uow)

    return usecase

def get_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = ReleaseRepository()
    
    usecase = GetReleaseUsecase(repo, uow)
    
    return usecase

def get_all_releases_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = ReleaseRepository()
    
    usecase = GetAllReleasesUsecase(repo, uow)
    
    return usecase
