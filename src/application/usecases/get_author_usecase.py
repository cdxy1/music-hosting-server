from typing import Callable
from uuid import UUID

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


class GetAuthorUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self, author_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            author = await self.repo.get_by_id(session, author_id)
            
            return AuthorDTO(author.name, author.type, author.id)
