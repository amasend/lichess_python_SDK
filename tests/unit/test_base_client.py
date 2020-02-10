import unittest
import asyncio
import pprint

from lichees_client.clients import BaseClient
from tests.utils import async_test


class TestBaseClient(unittest.TestCase):
    event_loop = None

    client: 'BaseClient' = None
    token = '...'

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
        pprint.pprint(response)

        self.assertNotIn('error', response, msg="Not authorized.")


if __name__ == '__main__':
    unittest.main()
