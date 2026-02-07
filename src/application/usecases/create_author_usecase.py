from typing import Callable

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork
from src.domain.entities.author import Author


class CreateAuthorUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self, author_dto: AuthorDTO):
        uow = self.uow_factory()
        async with uow() as session:
            author = Author(name=author_dto.name, type=author_dto.type)
            self.repo.create(session, author)
            
            return AuthorDTO(author.name, author.type, author.id)
