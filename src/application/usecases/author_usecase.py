from dataclasses import dataclass

from src.application.repository.contract import IRepository


@dataclass(frozen=True, slots=True)
class AuthorUsecase:
    repo: IRepository
        
    def create(self):
        ...
        
    def update(self):
        ...
        
    def delete(self):
        ...
        
    def get(self):
        ...
        
    def get_all(self):
        ...
