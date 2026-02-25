from uuid import UUID

from src.application.usecases.base import BaseUsecase


class DeleteAuthorUsecase(BaseUsecase):
    async def __call__(self, author_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            await self.repo.delete(session, author_id)
            
            await self.cache.invalidate_cache(["authors:all", f"authors:{author_id}"])
            return author_id
