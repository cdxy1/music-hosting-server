# from typing import Any, Self
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager


class IUnitOfWork(ABC):
    @abstractmethod
    @asynccontextmanager
    async def __call__(self): ...
