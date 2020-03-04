import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestResponseEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('connector_123')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__stream_incoming_events__fetching_information_about_incoming_game__response_object_returned_with_success(self):
        response = await self.client.bots.stream_incoming_events()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
