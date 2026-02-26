import json
from collections import namedtuple
from datetime import date
from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.infrastructure.models.base import BaseOrmModel

UNSERIALIZABLE_TYPES = (date, dict, UUID, BaseOrmModel, BaseEntity)

def serialize_to_json(data):
    serialized_data = json.dumps(_convert_object_to_serializable(data))
    return serialized_data

def deserialize_json_to_dto(data):
    if not data:
        raise
    
    loaded_data = json.loads(data)
    dto = _create_dto(loaded_data[0].keys())
 
    for obj in loaded_data:
        for k, v in obj.items():
            obj[k] = _sanitize_deserialized_obj(v)

            if _is_json(v):
                obj[k] = deserialize_json_to_dto(v)
    
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
    elif isinstance(data, dict):
        list_data = [{k: v if not isinstance(v, UNSERIALIZABLE_TYPES) else serialize_to_json(v) for k,v in data.items()}]
    else:
        list_data = [{k: v if not isinstance(v, UNSERIALIZABLE_TYPES) else serialize_to_json(v) for k,v in data.to_dict().items()}]

    return list_data    

def _convert_uuid_to_str(id):
    return str(id)

def _convert_date_to_str(obj_date):
    return str(obj_date)

def _is_json(data: str):
    if not data:
        return False
    
    if not data.startswith(("[", "{")):
        return False

    try:
        json.loads(data)
    except ValueError:
        return False
    return True

def _create_dto(keys):
    obj = namedtuple("DTO", keys)

    class DTO(obj):
        slots = ()
        
        def to_dict(self):
            temp = self._asdict()
            
            for k, v in temp.items():
                if isinstance(v, tuple):
                    temp[k] = v._asdict()
            return temp
            
    return DTO

def _sanitize_deserialized_obj(data: str):
    if not data:
        return data
    
    data_copy = data.strip()

    if '"' in data_copy:
        sanitized_data = data_copy.replace('"', "")
        
        if casted_data := _cast_to_type(sanitized_data):
            return casted_data
        
        return sanitized_data
    return data

def _cast_to_type(data):
    if obj := _cast_to_uuid(data):
        return obj

def _cast_to_uuid(data):
    try:
        obj = UUID(data)
        return obj
    except ValueError:
        return None
