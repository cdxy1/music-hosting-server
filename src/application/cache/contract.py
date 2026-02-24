from abc import ABC
from typing import Callable

class ICacheWrapper(ABC):
    async def get_or_create(self, key, fn: Callable):
        ...
    
    async def invalidate_cache(self, keys):
        ...
