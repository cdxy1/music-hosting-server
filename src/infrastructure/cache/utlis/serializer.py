import json
from uuid import UUID
from collections import namedtuple
from datetime import date

from src.infrastructure.models.base import BaseOrmModel

UNSERIALIZABLE_TYPES = (UUID, BaseOrmModel, date)

def serialize_to_json(data):
    serialized_data = json.dumps(_convert_object_to_serializable(data))
    return serialized_data

def deserialize_json_to_dto(data):
    if not data:
        raise
    
    dto = namedtuple("DTO", data[0].keys())
    
    if len(data) > 1:
        return [dto(**obj) for obj in data]
    elif len(data) == 1:
        return dto(**data[0])
    
def _convert_object_to_serializable(data):
    if isinstance(data, UUID):
        return _convert_uuid_to_str(data)
    if isinstance(data, date):
        return _convert_date_to_str(data)
    
    if isinstance(data, (tuple, list, set)):
        list_data = [{k: v if not isinstance(v, UNSERIALIZABLE_TYPES) else serialize_to_json(v) for k,v in obj.to_dict().items()} for obj in data]
    else:
        list_data = [{k: v if not isinstance(v, UNSERIALIZABLE_TYPES) else serialize_to_json(v) for k,v in data.to_dict().items()}]
        
    return list_data    

def _convert_uuid_to_str(id):
    return str(id)

def _convert_date_to_str(obj_date):
    return str(obj_date)
