from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class IRepository(ABC):
    @abstractmethod
    def get_by_id(self) -> T: ...

    @abstractmethod
    def get_all(self) -> list[T]: ...

    @abstractmethod
    def create(self) -> bool: ...

    @abstractmethod
    def update(self) -> bool: ...

    @abstractmethod
    def delete(abs) -> bool: ...

    @abstractmethod
    def exists(self) -> bool: ...
