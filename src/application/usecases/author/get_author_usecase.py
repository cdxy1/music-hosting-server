from uuid import UUID

from src.application.dto.author_dto import AuthorDTO
from src.application.usecases.base import BaseUsecase


class GetAuthorUsecase(BaseUsecase):
    async def __call__(self, author_id: UUID):
        uow = self.uow_factory()
        async with uow() as session:
            author = await self.repo.get_by_id(session, author_id)
            
            return AuthorDTO(author.name, author.type, author.id)
