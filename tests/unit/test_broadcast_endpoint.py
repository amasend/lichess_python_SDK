import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestBroadcastEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')
    broadcast_id = None
    games = None

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__create__broadcast_creation__response_object_returned_with_success(self):
        response = await self.client.broadcast.create(name="Test broadcast", description="This is desc.")
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")
        TestBroadcastEndpoint.broadcast_id = response.entity.content['broadcast']['id']

    @async_test
    async def test_02__get__get_info_about_created_broadcast__response_object_returned_with_success(self):
        response = await self.client.broadcast.get(broadcast_id=self.broadcast_id)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @unittest.SkipTest
    @async_test
    async def test_03__update__updating_broadcast__response_object_returned_with_success(self):
        response = await self.client.broadcast.update(broadcast_id=self.broadcast_id, name="Updated broadcast",
                                                      description="Ohh a new description!")
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_04__push_pgn__pushing_games_info__response_object_returned_with_success(self):
        response = await self.client.broadcast.push_pgn(broadcast_id=self.broadcast_id, games=self.games)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
