import sys
import mock
try:
    import unittest2
except ImportError:
    if sys.version_info < (2, 7):
        raise
    import unittest as unittest2

# from restkit import Resource
from restkit.wrappers import Response
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.resource import BaruwaAPIClient
from BaruwaAPI.exceptions import BaruwaAPIError

API_URL = 'https://baruwa.example.com'
API_TOKEN = '6e2347bc-278e-42f6-a84b-fa1766140cbd'


class BaruwaAPIClientTestCase(unittest2.TestCase):

    def setUp(self):
        """Setup API"""
        self.mock_request = mock.MagicMock()
        self.mock_response = mock.Mock(spec=Response)
        self.api = BaruwaAPIClient(API_TOKEN, API_URL)

    def test_headers(self):
        headers = self.api._request_headers()
        self.assertIn('User-Agent', headers)
        self.assertIn('Content-Type', headers)
        self.assertIn('Authorization', headers)
        self.assertEqual(headers['Authorization'], "Bearer %s" % API_TOKEN)

    def test_request_ok(self):
        with open('tests/api/v1/users.json') as handle:
            data = handle.read()
        self.mock_response.status_int = 200
        self.mock_response.body_string.return_value = data
        self.mock_request.return_value = self.mock_response
        self.api.request = self.mock_request
        method = 'GET'
        kwargs = dict(path='/users', payload=None)
        response_dict = self.api._request(method, **kwargs)
        # print response_dict
        self.api.request.assert_called_once_with(
            method, headers=self.api._request_headers(), **kwargs)
        self.assertIn('meta', response_dict)
        self.assertEqual(response_dict['meta']['total'], 2)

    def test_request_error(self):
        error_code = 500
        error_message = "Internal Error Occured"
        self.mock_response.status_int = error_code
        self.mock_response.body_string.return_value = error_message
        self.mock_request.return_value = self.mock_response
        self.api.request = self.mock_request
        method = 'GET'
        kwargs = dict(path='/users', payload=None)
        with self.assertRaises(BaruwaAPIError) as cmo:
            self.api._request(method, **kwargs)
        self.api.request.assert_called_once_with(
            method, headers=self.api._request_headers(), **kwargs)
        self.assertEqual(cmo.exception.code, error_code)
        self.assertEqual(cmo.exception.message, error_message)

    def test_api_call(self):
        userid = 5
        user_dict = dict(userid=userid)
        path = ENDPOINTS['users']['get']['name'] % user_dict
        path = '/api/v1%s' % path
        kwargs = dict(path=path, payload=None)
        with open('tests/api/v1/users/%d.json' % userid) as handle:
            data = handle.read()
        self.mock_response.status_int = 200
        self.mock_response.body_string.return_value = data
        self.mock_request.return_value = self.mock_response
        self.api.request = self.mock_request
        response_dict = self.api.api_call(
            ENDPOINTS['users']['get'], user_dict)
        # print response_dict
        self.api.request.assert_called_once_with(
            ENDPOINTS['users']['get']['method'],
            headers=self.api._request_headers(),
            **kwargs)
        self.assertEqual(response_dict['username'], 'rowdyrough')


if __name__ == "__main__":
    unittest2.main()
