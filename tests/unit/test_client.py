import unittest
import asyncio

from lichess_client import APIClient
from tests.utils import async_test, get_token_from_config


class TestClient(unittest.TestCase):
    client: 'APIClient' = None
    token = get_token_from_config(section='amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token, loop=asyncio.get_event_loop())


if __name__ == '__main__':
    unittest.main()
