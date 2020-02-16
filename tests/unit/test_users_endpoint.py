import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes, VariantTypes
from tests.utils import get_token_from_config, async_test


class TestAccountEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__get_real_time_users_status__fetching_several_users_status__response_object_returned_with_success(self):
        response = await self.client.users.get_real_time_users_status(users_ids=['amasend', 'lovlas'])
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__get_all_top_10__fetching_profile_info__response_object_returned_with_success(self):
        response = await self.client.users.get_all_top_10()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_03__get_one_leaderboard__fetching_leaderboard__response_object_returned_with_success(self):
        response = await self.client.users.get_one_leaderboard(limit=135, variant=VariantTypes.BLITZ)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

        self.assertEqual(135, len(response.entity.content.get('users', [])),
                         msg="The number of users fetched does not match the requested one.")

    @async_test
    async def test_04__get_user_public_data__fetching_user_data__response_object_returned_with_success(self):
        response = await self.client.users.get_user_public_data(username='amasend')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_05__get_rating_history_of_a_user__fetching_user_rating_histpry__response_object_returned_with_success(self):
        response = await self.client.users.get_rating_history_of_a_user(username='amasend')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_06__get_user_activity__fetching_user_activity__response_object_returned_with_success(self):
        response = await self.client.users.get_user_activity(username='amasend')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_07__get_your_puzzle_activity__fetching_user_puzzles_activity__response_object_returned_with_success(self):
        response = await self.client.users.get_your_puzzle_activity()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

        response_2 = await self.client.users.get_your_puzzle_activity(limit=2)
        self.assertEqual(2, len(response_2.entity.content), msg="The number of entries is incorrect.")

    @async_test
    async def test_08__get_users_by_id__fetching_users__response_object_returned_with_success(self):
        response = await self.client.users.get_users_by_id(users_ids=['amasend', 'lovlas'])
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_09__get_members_of_a_team__fetching_team_members__response_object_returned_with_success(self):
        response = await self.client.users.get_members_of_a_team(team_id='team')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_10__get_live_streamers__fetching_live_streamers__response_object_returned_with_success(self):
        response = await self.client.users.get_live_streamers()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")
