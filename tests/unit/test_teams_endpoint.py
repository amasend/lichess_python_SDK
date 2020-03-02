import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestTeamsEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    @unittest.expectedFailure
    async def test_01__get_members_of_a_team__fetching_team_members__not_implemented_raises(self):
        response = await self.client.teams.get_members_of_a_team()

    @async_test
    async def test_02__join_a_team__joining_to_a_team__response_object_returned_with_success(self):
        response = await self.client.teams.join_a_team(team_id='some_team')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_03__leave_a_team__leaving_a_team__response_object_returned_with_success(self):
        response = await self.client.teams.leave_a_team(team_id='some_team')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_04__kick_a_user_from_your_team__kicking_user_from_team__response_object_returned_with_success(self):
        response = await self.client.teams.kick_a_user_from_your_team(team_id='some_team', user_id='amasend')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
