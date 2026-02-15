from typing import Callable
from uuid import UUID

from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


class DeleteAuthorUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self, author_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            await self.repo.delete(session, author_id)
            
            return author_id
