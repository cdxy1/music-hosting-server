from sqlalchemy.ext.asyncio import AsyncSession

from src.application.dto.author_dto import AuthorDTO
from src.infrastructure.models.author import AuthorModel
from src.application.repository.contract import IRepository


class AuthorRepository(IRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
        
    def create(self, author: AuthorDTO):
        author = AuthorModel(
            name=AuthorDTO.name,
            type=AuthorDTO.type,
        )
        self._session.add(author)
