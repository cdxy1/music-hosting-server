from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class IRepository(ABC):
    @abstractmethod
    async def get_by_id(self) -> T: ...

    @abstractmethod
    async def get_all(self) -> list[T]: ...

    @abstractmethod
    async def create(self) -> bool: ...

    @abstractmethod
    async def update(self) -> bool: ...

    @abstractmethod
    async def delete(self) -> bool: ...

    @abstractmethod
    async def exists(self) -> bool: ...
