from abc import ABC, abstractmethod


class IUnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...
