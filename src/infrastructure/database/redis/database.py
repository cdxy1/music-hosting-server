from typing import Optional

from redis import ConnectionError
from redis import asyncio as aioredis

from src.infrastructure.config.contract import IDatabaseConfig


class RedisCache:
    _instance = None
    _connection = None
    _config = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config: IDatabaseConfig = None):
        if not self._instance and not config:
            raise
        
        if config:
            self._config = config
        
    async def connect(self):
        self._connection = await aioredis.from_url(self._config.database_uri, decode_responses=True)

    async def close(self):
        if self._connection:
            await self._connection.close()

    async def set(self, key: str, value: str, seconds_to_expire=None):
        try:
            ttl = seconds_to_expire if seconds_to_expire else self._config.ttl_seconds
            
            await self._connection.setex(key, ttl, value)
        except ConnectionError:
            raise

    async def get(self, key) -> Optional[str]:
        try:
            return await self._connection.get(key)
        except ConnectionError:
            raise

    async def delete(self, key):
        try:
            await self._connection.delete(key)
        except ConnectionError:
            raise
