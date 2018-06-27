""" Data representation for ride_my_way Web App

    Holds routines for users to interact with the API
"""


class Rides:
    """ Holds methods for rides

        Attributes:
            all_rides (dict) - Class variable Holds all rides
                {ride_count: {single_ride}}
    """
    global all_rides = {}

    def __init__(self):
        pass

    def fetch_all_rides(self):
        """ (Rides) -> dict

            Fetches all rides. Returns a dictionary
        """
        return all_rides
