from src.application.usecases.create_author_usecase import CreateAuthorUsecase
from src.infrastructure.config.postgres import PostgresConfig
from src.infrastructure.database.postgres import PostgresDatabase
from src.infrastructure.repository.author_repository_impl import AuthorRepository
from src.infrastructure.unit_of_work.unit_of_work_factory import uow_factory


def get_create_author_usecase():
    database_config = PostgresConfig()
    database = PostgresDatabase(database_config)
    uow = uow_factory(database)
    
    repository = AuthorRepository()
    usecase = CreateAuthorUsecase(repository, uow)
    
    return usecase
