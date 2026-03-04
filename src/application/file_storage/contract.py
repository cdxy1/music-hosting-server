from abc import ABC, abstractmethod

class IFileStorage(ABC):
    @abstractmethod
    async def get_url(self, key: str) -> str:
        pass
