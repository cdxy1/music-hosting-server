from uuid import UUID

from src.application.dto.author_dto import UpdateAuthorDTO
from src.application.usecases.base import BaseUsecase


class UpdateAuthorUsecase(BaseUsecase):
    async def __call__(self, author_id: UUID, data_to_update: UpdateAuthorDTO):
        uow = self.uow_factory()
        async with uow() as session:
            author = await self.repo.get_by_id(session, author_id)
            updated_author = author.update(**data_to_update.to_dict())
            await self.repo.update(session, updated_author)
            
            return updated_author.id
