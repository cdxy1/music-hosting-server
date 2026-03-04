from abc import ABC, abstractmethod

class IFileStorage(ABC):
    @abstractmethod
    def get_file_url(self, key: str) -> str:
        pass
