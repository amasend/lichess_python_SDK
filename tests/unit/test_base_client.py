import unittest
import asyncio

from lichees_client.clients.base_client import BaseClient
from tests.utils import async_test, get_token_from_config


class TestBaseClient(unittest.TestCase):
    event_loop = None

    client: 'BaseClient' = None
    token = get_token_from_config(section='amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.event_loop = asyncio.get_event_loop()

    @async_test
    async def test_01__initialization__init_of_BaseClient_class__all_arguments_stored(self):
        TestBaseClient.client = BaseClient(token=self.token, loop=self.event_loop)

        self.assertEqual(self.client._token, self.token, msg="Token incorrectly stored.")
        self.assertEqual(self.client.loop, self.event_loop, msg="Event loop incorrectly stored.")

    @async_test
    async def test_02__is_authorized__check_if_async_request_works__authorized(self):
        response = await self.client.is_authorized()

        self.assertTrue(response, msg="Not authorized.")

    @unittest.expectedFailure
    @async_test
    async def test_03__is_authorized__check_if_async_request_works__not_authorized(self):
        client = BaseClient(token="not_so_random_characters", loop=self.event_loop)
        response = await client.is_authorized()

        self.assertTrue(response, msg="Not authorized.")


if __name__ == '__main__':
    unittest.main()
