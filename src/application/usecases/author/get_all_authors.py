from typing import Callable

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


class GetAllAuthorUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            authors = await self.repo.get_all(session)
            
            return tuple(AuthorDTO(name=author.name, type=author.type, id=author.id) for author in authors)
