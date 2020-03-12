import unittest

from lichess_client import APIClient
from lichess_client.helpers import Response
from lichess_client.utils.enums import StatusTypes
from tests.utils import get_token_from_config, async_test


class TestStudiesEndpoint(unittest.TestCase):
    client = None
    token = get_token_from_config('amasend')
    study_id = "KMMrJvE1"
    chapter_id = "King in the Center"

    @classmethod
    def setUp(cls) -> None:
        cls.client = APIClient(token=cls.token)

    @unittest.SkipTest
    @async_test
    async def test_01__export_chapter__downloading_one_study_chapter__response_object_returned_with_success(self):
        response = await self.client.studies.export_chapter(study_id=self.study_id, chapter_id=self.chapter_id)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")

    @async_test
    async def test_02__export_all_chapters__downloading_a_study__response_object_returned_with_success(self):
        response = await self.client.studies.export_all_chapters(study_id=self.study_id)
        print(response)

        self.assertIsInstance(response, Response, msg="Response in not of type \"Response\"")
        self.assertEqual(response.entity.status, StatusTypes.SUCCESS, msg="Request was unsuccessful.")


if __name__ == '__main__':
    unittest.main()
