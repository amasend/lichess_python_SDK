from enum import Enum


class RequestMethods(Enum):
    """HTTP REST methods types"""
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class StatusTypes(str, Enum):
    """API response statuses"""
    SUCCESS = 'success'
    ERROR = 'error'
