import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestChallengesEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__create_a_challenge__sent_challenge_invitation__response_object_returned_with_success(self):
        response = await self.client.challenges.create(username='some_user')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__accept_a_challenge__accepting_a_challenge__response_object_returned_with_success(self):
        response = await self.client.challenges.accept(username='some_user')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_03__decline_a_challenge__declining_a_challenge__response_object_returned_with_success(self):
        response = await self.client.challenges.decline(username='some_user')
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
