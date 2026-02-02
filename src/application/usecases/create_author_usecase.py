from dataclasses import dataclass

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


@dataclass(frozen=True, slots=True)
class CreateAuthorUsecase:
    uow: IUnitOfWork
    author_repo: IRepository

    async def __call__(self, author: AuthorDTO):
        uow = self.uow()
        
        async with uow():
            created_author = self.repo.create(author)

            if not created_author:
                raise
