from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.application.usecases.get_author_usecase import GetAuthorUsecase
from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)


def get_create_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    usecase = CreateAuthorUsecase(repository, uow)
    
    return usecase

def get_author_usecase():
    uow = UnitOfWorkSingletonFactory().create_uow_instance
    repository = AuthorRepository()
    usecase = GetAuthorUsecase(repository, uow)
    
    return usecase
