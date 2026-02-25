from src.application.dto.author_dto import AuthorDTO
from src.application.usecases.base import BaseUsecase
from src.domain.entities.author import Author


class CreateAuthorUsecase(BaseUsecase):
    async def __call__(self, author_dto: AuthorDTO):
        uow = self.uow_factory()
        async with uow() as session:
            author = Author(name=author_dto.name, type=author_dto.type)
            self.repo.create(session, author)
            
            await self.cache.invalidate_cache(["authors:all"])
            return AuthorDTO(author.name, author.type, author.id)
