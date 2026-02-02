from abc import ABC, abstractmethod


class IDatabaseConfig(ABC):
    @property
    @abstractmethod
    def database_uri(self) -> str:
        ...
