import unittest
import time

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestAccountEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('connector_123')

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @async_test
    async def test_01__get_my_profile__fetching_profile_info__response_object_returned_with_success(self):
        response = await self.client.account.get_my_profile()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__get_my_email_address__fetching_email__response_object_returned_with_success(self):
        response = await self.client.account.get_my_email_address()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_03__get_my_preferences__fetching_preferences__response_object_returned_with_success(self):
        response = await self.client.account.get_my_preferences()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_04__get_my_kid_mode_status__fetching_kid_status__response_object_returned_with_success(self):
        response = await self.client.account.get_my_kid_mode_status()
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_05__set_my_kid_mode_status__setting_kid_status__response_object_returned_with_success(self):
        response_1 = await self.client.account.set_my_kid_mode_status(turned_on=True)
        time.sleep(2)
        response_2 = await self.client.account.get_my_kid_mode_status()
        print(f"Setting kid mode: {response_1}")
        print(f"Kid mode set to: {response_2.entity.content['kid']}")

        self.assertIsInstance(response_1, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response_1.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")
        self.assertTrue(response_2.entity.content['kid'], msg="Kid mode status was not set correctly.")

        await self.client.account.set_my_kid_mode_status(turned_on=False)
        time.sleep(2)
        response_3 = await self.client.account.get_my_kid_mode_status()
        print(f"Kid mode set to: {response_3.entity.content['kid']}")


if __name__ == '__main__':
    unittest.main()
