from src.application.dto.author_dto import AuthorDTO
from src.application.usecases.base import BaseUsecase


class GetAllAuthorUsecase(BaseUsecase):  
    async def __call__(self):
        uow = self.uow_factory()
        async with uow() as session:
            authors = await self.repo.get_all(session)
            
            return tuple(AuthorDTO(name=author.name, type=author.type, id=author.id) for author in authors)
