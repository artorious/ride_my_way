""" Test cases for views.py """
import unittest
from app import app


class TestRoutesCases(unittest.TestCase):
    """ Test cases for routes in views.py """
    def setUp(self):
        """ Instantiate test client """
        self.app = app.test_client()

    def test_non_error_path_response_code(self):
        """ Test that a valid path returns all ride offers in JSON and
            HTTP response code of 200(OK)
        """
        test_response = self.app.get(
            'api/v1/rides',
            headers={'content-type': 'applcation/json'}
            )
        self.assertEqual(test_response.status_code, 200, msg='Expected 200')

    def test_malformed_path_response_code(self):
        """
            Test path with error (malformed syntax) returns an appropriate
            error message in JSON and HTTP response code of 404 (NOT FOUND)
        """

        test_response = self.app.get(
            'api/v1/ridess',
            headers={'content-type': 'applcation/json'}
            )
        self.assertEqual(
            test_response.status_code,
            404,
            msg='ERROR:RESOURCE NOT FOUND'
            )
