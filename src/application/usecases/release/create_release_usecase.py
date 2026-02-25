from typing import Callable, override

from src.application.dto.release_dto import ReleaseInputDTO, ReleaseOutputDTO
from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork
from src.application.usecases.base import BaseUsecase
from src.domain.entities.author import Author
from src.domain.entities.genre import Genre
from src.domain.entities.release import Release
from src.application.cache.contract import ICacheWrapper



class CreateReleaseUsecase(BaseUsecase):
    @override
    def __init__(self, release_repo: IRepository, author_repo: IRepository, genre_repo: IRepository, uow_factory: Callable[[], IUnitOfWork], cache: ICacheWrapper):
        self.release_repo = release_repo
        self.author_repo = author_repo
        self.genre_repo = genre_repo
        self.uow_factory = uow_factory
        self.cache = cache
    
    async def __call__(self, release_dto: ReleaseInputDTO):
        uow = self.uow_factory()
        async with uow() as session:
            author_dto = await self.author_repo.get_by_id(session, release_dto.author_id)
            genre_dto = await self.genre_repo.get_by_id(session, release_dto.genre_id)
            
            author = Author(id=author_dto.id, name=author_dto.name, type=author_dto.type)
            genre = Genre(id=genre_dto.id, title=genre_dto.title)
            
            release = Release(name=release_dto.name, author=author, genre=genre, release_type=release_dto.release_type, release_date=release_dto.release_date)
            self.release_repo.create(session, release)
            
            await self.cache.invalidate_cache(["releases:all"])
            return ReleaseOutputDTO(**release.to_dict())
