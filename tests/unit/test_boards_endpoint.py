import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestBoardsEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__stream_incoming_events__fetching_information_about_incoming_game__response_object_returned_with_success(self):
        async for response in self.client.boards.stream_incoming_events():
            print(response)

            self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
            self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__create_a_seek__seeking_the_game__response_object_returned_with_success(self):
        response = await self.client.boards.create_a_seek(time=15, increment=15, rated=True)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
