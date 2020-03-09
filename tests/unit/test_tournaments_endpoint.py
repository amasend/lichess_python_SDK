import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestTournamentsEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__get_current__fetching_current_tournament_info__response_object_returned_with_success(self):
        response = await self.client.tournaments.get_current()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__create__posting_a_tournament__response_object_returned_with_success(self):
        response = await self.client.tournaments.create(clock_time=1, clock_increment=1, minutes=60)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_03__export_games__download_tournament_games_info__response_object_returned_with_success(self):
        response = await self.client.tournaments.export_games(tournament_id='q7zvsdUF')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_04__get_results__download_tournament_results__response_object_returned_with_success(self):
        response = await self.client.tournaments.get_results(tournament_id='q7zvsdUF')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_05__get_tournaments_created_by_a_user__download_details__response_object_returned_with_success(self):
        response = await self.client.tournaments.get_tournaments_created_by_a_user(tournament_id='q7zvsdUF')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
