import inspect
import configparser
import os
from asyncio import coroutine, get_event_loop


def async_test(f):
    """Async wrapper for unit tests. Wraps tests functions to be handled by asyncio event loop"""
    def wrapper(*args, **kwargs):
        if inspect.iscoroutinefunction(f):
            future = f(*args, **kwargs)
        else:
            coroutine_ = coroutine(f)
            future = coroutine_(*args, **kwargs)
        get_event_loop().run_until_complete(future)
    return wrapper


def get_token_from_config(section: str) -> str:
    """Read token from configuration file or environment."""
    try:
        config = configparser.ConfigParser()
        config.read('credentials.ini')
        return config.get(section, 'token')

    except:
        return os.environ[section]
