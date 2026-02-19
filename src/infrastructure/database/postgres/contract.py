from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class IDatabase(ABC):
    @abstractmethod
    def _create_engine(self): ...

    @abstractmethod
    def create_session(self) -> AsyncSession: ...
