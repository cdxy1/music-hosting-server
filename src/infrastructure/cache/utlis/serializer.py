import json
from uuid import UUID
from collections import namedtuple

def serialize_to_json(data):
    if isinstance(data, (tuple, list, set)):
        serialized_data = json.dumps([{k: v if not isinstance(v, UUID) else str(v) for k,v in obj.to_dict().items()} for obj in data])
    else:
        serialized_data = json.dumps([{k: v if not isinstance(v, UUID) else str(v) for k,v in data.to_dict().items()}])
        
    return serialized_data

def deserialize_json_to_dto(data):
    if not data:
        raise
    
    dto = namedtuple("DTO", data[0].keys())
    
    if len(data) > 1:
        return [dto(**obj) for obj in data]
    elif len(data) == 1:
        return dto(**data[0])

        
