from uuid import UUID

from src.application.dto.genre_dto import GenreDTO
from src.application.usecases.base import BaseUsecase


class GetGenreUsecase(BaseUsecase): 
    async def __call__(self, genre_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            genre = await self.cache.get_or_create(f"genres:{genre_id}", lambda: self.repo.get_by_id(session, genre_id))
            
            return GenreDTO(title=genre.title, id=genre.id)
