from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)
from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.infrastructure.repository.genre_repository_impl import GenreRepository
from src.infrastructure.repository.release_repository_impl import ReleaseRepository
from src.application.usecases.release.create_release_usecase import CreateReleaseUsecase

def get_create_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    author_repo = AuthorRepository()
    genre_repo = GenreRepository()
    release_repo = ReleaseRepository()
    
    usecase = CreateReleaseUsecase(release_repo=release_repo, author_repo=author_repo, genre_repo=genre_repo, uow_factory=uow)

    return usecase
