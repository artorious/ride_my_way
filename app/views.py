""" Routes for rid_my_way app """

from flask import request
from flask import jsonify
from app.models import Rides
from app import app

SAMPLE_RIDES = Rides()


@app.route('/api/v1/rides', methods=['GET'])
def rides():
    """ Fetches all rides """
    return jsonify(SAMPLE_RIDES.all_rides)

