from src.application.usecases.author.create_author_usecase import CreateAuthorUsecase
from src.application.usecases.author.delete_author_usecase import DeleteAuthorUsecase
from src.application.usecases.author.get_all_authors import GetAllAuthorUsecase
from src.application.usecases.author.get_author_usecase import GetAuthorUsecase
from src.application.usecases.author.update_author_usecase import UpdateAuthorUsecase
from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)
from src.infrastructure.cache.cache import CacheWrapper
from src.infrastructure.database.redis.database import RedisCache


def get_create_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    cache = CacheWrapper(RedisCache())
    usecase = CreateAuthorUsecase(repository, uow, cache)
    
    return usecase

def get_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    cache = CacheWrapper(RedisCache())
    usecase = GetAuthorUsecase(repository, uow, cache)
    
    return usecase

def get_all_authors_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    cache = CacheWrapper(RedisCache())
    usecase = GetAllAuthorUsecase(repository, uow, cache)
    
    return usecase

def get_delete_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    cache = CacheWrapper(RedisCache())    
    usecase = DeleteAuthorUsecase(repository, uow, cache)
    
    return usecase

def get_update_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    cache = cache = CacheWrapper(RedisCache())
    usecase = UpdateAuthorUsecase(repository, uow, cache)
    
    return usecase
