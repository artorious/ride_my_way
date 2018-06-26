""" Data representation for ride_my_way Web App

    Holds routines for users to interact with the API
"""


class Rides:
    """ Holds methods for rides

        Attributes:
            single_ride (dict) - Variable Holds data for a single ride
                {
                    rideId: int,
                    driver: str,
                    driver_tel: int,
                    departure_time: str,
                    travel_date: str,
                    departure_point: str,
                    destination: str,
                    seats_avail: int,
                    travel_route: str,
                    luggage_capacity: str,
                    detour_max_time: str,
                    vehicle_description: str,
                    driver_preferences: str
                }

            all_rides (dict) - Variable Holds all rides
                {ride_count: {single_ride}}
    """

    def __init__(self):
        self.all_rides = {}
        self.ride_counter = 0

    def fetch_all_rides(self):
        """ (Rides) -> dict

            Fetches all rides. Returns a dictionary
        """
        return self.all_rides
