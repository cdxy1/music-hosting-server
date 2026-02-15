from uuid import UUID

from src.application.dto.genre_dto import GenreDTO
from src.application.usecases.base import BaseUsecase


class GetGenreUsecase(BaseUsecase): 
    async def __call__(self, author_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            genre = await self.repo.get_by_id(session, author_id)
            
            return GenreDTO(title=genre.title, id=genre.id)
