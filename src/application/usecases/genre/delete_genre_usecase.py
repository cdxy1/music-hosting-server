from uuid import UUID

from src.application.usecases.base import BaseUsecase


class DeleteGenreUsecase(BaseUsecase):
    async def __call__(self, genre_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            await self.repo.delete(session, genre_id)
            
            await self.cache.invalidate_cache(["genres:all", f"genres:{genre_id}"])
            return genre_id
