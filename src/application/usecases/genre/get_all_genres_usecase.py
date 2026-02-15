from typing import Callable

from src.application.dto.genre_dto import GenreDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork


class GetAllGenreUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            genres = await self.repo.get_all(session)
            
            return tuple(GenreDTO(title=genre.title, id=genre.id) for genre in genres)
