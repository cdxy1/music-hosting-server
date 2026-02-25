from uuid import UUID

from src.application.dto.genre_dto import UpdateGenreDTO
from src.application.usecases.base import BaseUsecase


class UpdateGenreUsecase(BaseUsecase):
    async def __call__(self, genre_id: UUID, data_to_update: UpdateGenreDTO):
        uow = self.uow_factory()
        async with uow() as session:
            genre = await self.repo.get_by_id(session, genre_id)
            updated_genre = genre.update(**data_to_update.to_dict())
            await self.repo.update(session, updated_genre)
            
            await self.cache.invalidate_cache(["genres:all", f"genres:{genre_id}"])
            return updated_genre.id
