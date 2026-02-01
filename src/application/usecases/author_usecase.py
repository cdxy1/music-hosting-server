from dataclasses import dataclass

from src.application.dto.author_dto import AuthorDTO
from src.application.repository.contract import IRepository


@dataclass(frozen=True, slots=True)
class AuthorUsecase:
    repo: IRepository

    def create(self, author: AuthorDTO):
        created_author = self.repo.create(author)

        if not created_author:
            raise

    def update(self): ...

    def delete(self): ...

    def get(self): ...

    def get_all(self): ...
