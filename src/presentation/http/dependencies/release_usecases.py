from src.application.usecases.release.create_release_usecase import CreateReleaseUsecase
from src.application.usecases.release.delete_release_usecase import DeleteReleaseUsecase
from src.application.usecases.release.get_all_releases_usecase import (
    GetAllReleasesUsecase,
)
from src.application.usecases.release.get_release_usecase import GetReleaseUsecase
from src.infrastructure.background_tasks.dispatcher import TasksDispatcher
from src.infrastructure.cache.cache import CacheWrapper
from src.infrastructure.config.s3 import S3Config
from src.infrastructure.database.redis.database import AsyncRedisCache
from src.infrastructure.database.s3.adapter import S3Adapter
from src.infrastructure.database.s3.database import S3Storage
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
    cache = CacheWrapper(AsyncRedisCache())
    task_dispatcher = TasksDispatcher()
    
    usecase = CreateReleaseUsecase(release_repo=release_repo, author_repo=author_repo, genre_repo=genre_repo, uow_factory=uow, cache=cache, dispatcher=task_dispatcher)

    return usecase

def get_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = ReleaseRepository()
    cache = CacheWrapper(AsyncRedisCache())
    s3 = S3Storage(S3Config())
    file_storage = S3Adapter(s3)
    
    usecase = GetReleaseUsecase(repo, uow, cache, file_storage)
    
    return usecase

def get_all_releases_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = ReleaseRepository()
    cache = CacheWrapper(AsyncRedisCache())
    s3 = S3Storage(S3Config())
    file_storage = S3Adapter(s3)
    
    usecase = GetAllReleasesUsecase(repo, uow, cache, file_storage)
    
    return usecase

def get_delete_release_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repo = ReleaseRepository()
    cache = CacheWrapper(AsyncRedisCache())
    
    usecase = DeleteReleaseUsecase(repo, uow, cache)
    
    return usecase
