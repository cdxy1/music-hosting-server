from src.application.dto.genre_dto import GenreDTO
from src.application.usecases.base import BaseUsecase


class GetAllGenreUsecase(BaseUsecase):
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            genres = await self.repo.get_all(session)
            
            return tuple(GenreDTO(title=genre.title, id=genre.id) for genre in genres)
