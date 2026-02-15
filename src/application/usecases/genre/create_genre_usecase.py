from typing import Callable

from src.application.dto.genre_dto import GenreDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork
from src.domain.entities.genre import Genre


class CreateGenreUsecase:
    
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork]):
        self.repo = repo
        self.uow_factory = uow_factory     

    async def __call__(self, genre_dto: GenreDTO):
        uow = self.uow_factory()
        async with uow() as session:
            genre = Genre(title=genre_dto.title)
            self.repo.create(session, genre)
            
            return GenreDTO(title=genre.title, id=genre.id)
