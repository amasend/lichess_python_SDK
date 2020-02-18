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


class VariantTypes(str, Enum):
    """Game variant types"""
    ULTRA_BULLET = "ultraBullet"
    BULLET = "bullet"
    BLITZ = "blitz"
    RAPID = "rapid"
    CLASSICAL = "classical"
    CHESS960="chess960"
    CRAZYHOUSE = "crazyhouse"
    ANTICHESS = "antichess"
    ATOMIC = "atomic"
    HORDE = "horde"
    KING_OF_THE_HILL = "kingOfTheHill"
    RACING_KINGS = "racingKings"
    THRESS_CHECK = "threeCheck"
