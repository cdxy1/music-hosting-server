from abc import ABC
from typing import Any, Callable


class ICacheWrapper(ABC):
    async def get_or_create(self, key, fn: Callable) -> Any:
        ...
    
    async def invalidate_cache(self, keys):
        ...
