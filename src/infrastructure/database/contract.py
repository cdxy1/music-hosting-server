from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def _create_engine(self): ...

    @abstractmethod
    def _create_session(self): ...

    @abstractmethod
    def get_session(self): ...
