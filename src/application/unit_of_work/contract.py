# from typing import Any, Self
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager


class IUnitOfWork(ABC):
    # @abstractmethod
    # async def __aenter__(self) -> Self: ...

    # @abstractmethod
    # async def __aexit__(
    #     self,
    #     exc_type: type[BaseException] | None,
    #     exc_val: BaseException | None,
    #     exc_tb: Any,
    # ): ...

    # @abstractmethod
    # async def commit(self): ...

    # @abstractmethod
    # async def rollback(self): ...
    
    @abstractmethod
    @asynccontextmanager
    async def __call__(self):
        ...
