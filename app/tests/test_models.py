""" Test cases for models.py """

from app.models import Rides
import unittest


class TestRidesCases(unittest.TestCase):
    """ Test cases for Rides class """

    def setUp(self):
        """ Intatiate sample data """
        self.sample_rides = Rides()

    def test_rides_class_constucts_an_empty_dict(self):
        """
            Test model returns a dict to hold all_rides
        """
        self.assertDictEqual(
            {}, self.sample_rides.all_rides,
            msg='Class does not initalze an empty dictionary'
        )

    def test_rides_class_returns_valid_data(self):
        """
            Test model returns a dict of the right form with
            all required data
        """
        self.assertIsInstance(self.sample_rides.all_rides, dict)
