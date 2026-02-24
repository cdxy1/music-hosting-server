from abc import ABC

class ICache(ABC):
    async def set(self, key: str, value: str, seconds_to_expire=None):
        ...

    async def get(self, key):
        ...

    async def delete(self, key):
        ...
