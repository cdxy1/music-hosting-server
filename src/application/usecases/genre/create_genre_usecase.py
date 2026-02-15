from src.application.dto.genre_dto import GenreDTO
from src.application.usecases.base import BaseUsecase
from src.domain.entities.genre import Genre


class CreateGenreUsecase(BaseUsecase):
    async def __call__(self, genre_dto: GenreDTO):
        uow = self.uow_factory()
        async with uow() as session:
            genre = Genre(title=genre_dto.title)
            self.repo.create(session, genre)
            
            return GenreDTO(title=genre.title, id=genre.id)
