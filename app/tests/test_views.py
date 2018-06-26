""" Test cases for views.py """
from app import app
import unittest
import json


class TestRoutesCases(unittest.TestCase):
    """ Test cases for routes in views.py """
    def setUp(self):
        """ Instantiate test client """
        pass

    def test_non_error_path_response_code(self):
        """
            Test that a valid path returns all ride offers in JSON and
            HTTP response code of 200(OK)
        """
        pass

    def test_malformed_path_response_code(self):
        """
            Test path with error (malformed syntax) returns an appropriate
            error message in JSON and HTTP response code of 400 (BAD REQUEST)
            """
        pass
