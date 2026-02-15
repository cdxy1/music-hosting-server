from src.application.usecases.genre.create_genre_usecase import CreateGenreUsecase
from src.application.usecases.genre.get_all_genres_usecase import GetAllGenreUsecase
from src.application.usecases.genre.get_genre_usecase import GetGenreUsecase
from src.infrastructure.repository.genre_repository_impl import GenreRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_create_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    usecase = CreateGenreUsecase(repository, uow)

    return usecase

def get_all_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    usecase = GetAllGenreUsecase(repository, uow)

    return usecase

def get_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    usecase = GetGenreUsecase(repository, uow)

    return usecase
  
