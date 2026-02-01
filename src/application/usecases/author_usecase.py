from dataclasses import dataclass

@dataclass(frozen=True)
class AuthorUsecase:
    def __init__(self):
        ...
        
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
