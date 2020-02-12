import unittest
import json

from lichees_client.helpers import ResponseMetadata, ResponseEntity, Response
from lichees_client.utils.enums import RequestMethods


class TestResponseHelpers(unittest.TestCase):
    response: 'Response' = None
    metadata: 'ResponseMetadata' = None
    entity: 'ResponseEntity' = None

    url = 'https://lichees.org/account'
    content_type = 'application/json'
    timestamp = b'some timestamp'
    status = 200
    reason = 'SUCCESS'
    content = '{"key": "value"}'

    @classmethod
    def setUp(cls) -> None:
        cls.metadata = ResponseMetadata(method='GET', url=cls.url,
                                        content_type=cls.content_type, timestamp=cls.timestamp)

        cls.entity = ResponseEntity(status=cls.status, reason=cls.reason, content=cls.content)

        cls.response = Response(metadata=cls.metadata, entity=cls.entity)

    def test_01__metadata__check_all_parameters__all_parameters_are_set_correctly(self):
        self.assertEqual(self.metadata.method, RequestMethods.GET, msg='Metadata method was set incorrectly.')
        self.assertEqual(self.metadata.url, self.url, msg='Metadata url was set incorrectly.')
        self.assertEqual(self.metadata.content_type, self.content_type,
                         msg='Metadata content type was set incorrectly.')
        self.assertEqual(self.metadata.timestamp, self.timestamp, msg='Metadata timestamp was set incorrectly.')

    def test_02__entity__check_all_parameters__all_parameters_are_set_correctly(self):
        self.assertEqual(self.entity.status, self.status, msg='Entity status was set incorrectly')
        self.assertEqual(self.entity.reason, self.reason, msg='Entity reason was set incorrectly')
        self.assertEqual(self.entity.content, json.loads(self.content), msg='Entity content was set incorrectly')

    def test_03__response__check_all_parameters__all_parameters_are_set_correctly(self):
        self.assertIsInstance(self.response.entity, ResponseEntity,
                              msg='Entity of the response is not of type ResponseEntity')
        self.assertIsInstance(self.response.metadata, ResponseMetadata,
                              msg='Metadata of the response is not of type ResponseMetadata')

    def test_04__to_dict__check_if_all_to_dict_methods_worked_in_chain__all_objects_converted_to_dict(self):
        response_dict_representation = self.response.to_dict()
        self.assertIsInstance(response_dict_representation, dict, msg="Response.to_dict() not working properly.")
        self.assertIsInstance(response_dict_representation['entity'], dict,
                              msg="ResponseEntity.to_dict() not working properly.")
        self.assertIsInstance(response_dict_representation['metadata'], dict,
                              msg="ResponseMetadata.to_dict() not working properly.")
        self.assertIsInstance(self.response, Response,
                              msg="Response object was converted to dict! Deepcopy not working")

        print(response_dict_representation)

    def test_05__repr__inspect_representation_of_the_response(self):
        print(self.response)


if __name__ == '__main__':
    unittest.main()
