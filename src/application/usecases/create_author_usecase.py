from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


class CreateAuthorUsecase:
    
    def __init__(self, repo: IRepository, uow: IUnitOfWork):
        self.repo = repo
        self.uow = uow     

    async def __call__(self, author: AuthorDTO):        
        async with self.uow() as session:
            created_author = self.repo().create(session, author)
