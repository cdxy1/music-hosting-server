from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class TrackUsecase:
    def __init__(self):
        pass
    
    def create(self):
        ...
        
    def get(self):
        ...
    
    def get_all(self):
        ...
        
    def delete(self):
        ...
