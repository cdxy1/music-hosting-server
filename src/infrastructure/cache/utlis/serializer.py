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
    
    loaded_data = json.loads(data)
    dto = namedtuple("DTO", loaded_data[0].keys())
    dto.to_dict = lambda: dto._asdict()
    
    for k, v in loaded_data[0].items():
        if _is_json(v):
            loaded_data[0][k] = deserialize_json_to_dto(v)
    
    if len(loaded_data) > 1:        
        deserialized_data = [dto(**obj) for obj in loaded_data]
    elif len(loaded_data) == 1:
        deserialized_data = dto(**loaded_data[0])
   
    return deserialized_data
    
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

def _is_json(data: str):
    if not data.startswith(("[", "{")):
        return False

    try:
        json.loads(data)
    except ValueError:
        return False
    return True

def _create_dto(keys):
    
