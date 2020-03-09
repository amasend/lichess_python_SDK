import logging
from logging.handlers import RotatingFileHandler
from typing import Any


logger = logging.getLogger('lichess_client')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('lichess_python_client.log', maxBytes=10240, backupCount=3)
handler.setFormatter(logging.Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s", datefmt='%Y-%m-%dT%H:%M:%S'))
logger.addHandler(handler)


class BaseError(Exception):
    def __init__(self, value: Any, reason: str) -> None:
        super().__init__(value, reason)
        logger.debug(f"Error in: {value} Reason: {reason}")


class ToManyIDs(BaseError):
    def __init__(self, value: Any, reason: str) -> None:
        super().__init__(value, reason)


class LimitError(BaseError):
    def __init__(self, value: Any, reason: str) -> None:
        super().__init__(value, reason)


class RatingRangeError(BaseError):
    def __init__(self, value: Any, reason: str) -> None:
        super().__init__(value, reason)
