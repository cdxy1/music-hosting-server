from typing import Callable

from src.infrastructure.cache.contract import ICache
from src.infrastructure.cache.utlis.serializer import (
    deserialize_json_to_dto,
    serialize_to_json,
)


class CacheWrapper:
    def __init__(self, cache: ICache):
        self.cache = cache
        
    async def get_or_create(self, key, fn: Callable):
        if cached_data := await self.cache.get(key):
            deserialized_data = deserialize_json_to_dto(cached_data)
            return deserialized_data

        data = await fn()
        serialized_data = serialize_to_json(data)
        
        await self.cache.set(key, serialized_data)
        return data

    
    async def invalidate_cache(self, keys):
        for key in keys:
            await self.cache.delete(key)
        
