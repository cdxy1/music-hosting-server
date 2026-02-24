from src.application.usecases.genre.create_genre_usecase import CreateGenreUsecase
from src.application.usecases.genre.delete_genre_usecase import DeleteGenreUsecase
from src.application.usecases.genre.get_all_genres_usecase import GetAllGenreUsecase
from src.application.usecases.genre.get_genre_usecase import GetGenreUsecase
from src.application.usecases.genre.update_genre_usecase import UpdateGenreUsecase
from src.infrastructure.repository.genre_repository_impl import GenreRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)
from src.infrastructure.cache.cache import CacheWrapper
from src.infrastructure.database.redis.database import RedisCache


def get_create_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    cache = CacheWrapper(RedisCache())
    usecase = CreateGenreUsecase(repository, uow, cache)

    return usecase

def get_all_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    cache = CacheWrapper(RedisCache())
    usecase = GetAllGenreUsecase(repository, uow, cache)

    return usecase

def get_genre_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    cache = CacheWrapper(RedisCache())
    usecase = GetGenreUsecase(repository, uow, cache)

    return usecase

def get_delete_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    cache = CacheWrapper(RedisCache())
    usecase = DeleteGenreUsecase(repository, uow, cache)

    return usecase

def get_update_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = GenreRepository()
    cache = CacheWrapper(RedisCache())
    usecase = UpdateGenreUsecase(repository, uow, cache)

    return usecase   
