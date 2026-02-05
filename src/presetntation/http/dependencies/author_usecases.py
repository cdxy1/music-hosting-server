from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.infrastructure.unit_of_work.unit_of_work_factory import uow_factory

def get_create_author_usecase():
    repository = AuthorRepository()
    usecase = CreateAuthorUsecase(repository, uow_factory)
    
    return usecase
