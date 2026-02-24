import json
from typing import Callable

from src.infrastructure.cache.contract import ICache
from src.infrastructure.cache.utlis.serializer import serialize_to_json, deserialize_json_to_dto

class CacheWrapper:
    def __init__(self, cache: ICache):
        self.cache = cache
        
    async def get_or_create(self, key, fn: Callable):
        try:
            if cached_data := await self.cache.get(key):
                data = json.loads(cached_data)
                deserialized_data = deserialize_json_to_dto(data)
                return deserialized_data

            data = await fn()
            serialized_data = serialize_to_json(data)
            
            await self.cache.set(key, serialized_data)
            return data
        except Exception:
            import traceback
            traceback.print_exc()
    
    async def invalidate_cache(self, keys):
        for key in keys:
            await self.cache.delete(key)
        
