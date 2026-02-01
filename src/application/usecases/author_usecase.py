from dataclasses import dataclass

from src.application.repository.contract import IRepository

@dataclass(frozen=True)
class AuthorUsecase:
    def __init__(self, repo: IRepository):
        self.repo = repo
        
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
