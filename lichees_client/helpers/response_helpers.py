import json
from copy import deepcopy
from lichees_client.utils.enums import RequestMethods


class BaseHelper:
    def to_dict(self) -> dict:
        _dict: dict = deepcopy(vars(self))
        for key, val in _dict.items():
            if hasattr(val, 'to_dict'):
                _dict[key] = val.to_dict()
        return _dict

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        return str(self.to_dict())


class ResponseMetadata(BaseHelper):
    def __init__(self, method: str,  url: str, content_type: str, timestamp: bytes) -> None:
        self.method = RequestMethods[method]
        self.url = url
        self.content_type = content_type
        self.timestamp = timestamp


class ResponseEntity(BaseHelper):
    def __init__(self, status: int, reason: str, content: str) -> None:
        self.status = status
        self.reason = reason
        self.content = json.loads(content)


class Response(BaseHelper):
    def __init__(self, metadata: 'ResponseMetadata', entity: 'ResponseEntity') -> None:
        self.metadata = metadata
        self.entity = entity
