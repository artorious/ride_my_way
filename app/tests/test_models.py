""" Test cases for models.py """

from app.models import Rides
import unittest


class TestRidesCases(unittest.TestCase):
    """ Test cases for Rides class """
    def setUp(self):
        """ Intatiate sample data """
        self.sample_rides = Rides()
        # Sample Rides data
        self.good_rides_sample_data = {
            "rideId": 1,
            "driver": "Partick Njiru",
            "driver_tel": +254770771164,
            "departure_time": "8:00 AM",
            "travel_date": "08-08-2018",
            "departure_point": "Westlands Post Office",
            "destination": "Ukunda, Kwale",
            "seats_avail": 3,
            "travel_route": "Nairobi-Mombasa Highway",
            "luggage_capacity": "1 medium suitcase per person",
            "detour_max_time": "30 minutes off-route",
            "vehicle_description": "Brown Vauxhaul van",
            "driver_preferences": "No smoking, No pets, No loud music"
        }

    def test_rides_class_inits_and_constucts_a_dict(self):
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
        self.assertIsInstance(dict, self.sample_rides)
