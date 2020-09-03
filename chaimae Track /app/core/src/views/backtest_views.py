import pandas as pd 
import json 
from flask import request
from core.src.Utils.dtoo import TrackerDto
from flask_restplus import Resource,fields
from core.src.database.tracker_service import (save_new_tracker,
                                               get_all_trackers,
                                               get_one_tracker,
                                               delete_one_tracker,
                                               update_tracker)
import numpy as np
ns_trakers = TrackerDto.ns_trakers
_tracker = TrackerDto._tracker
@ns_trakers.route("/trackers")
class TrackersView(Resource):
    @ns_trakers.response(200, "Tracker successfully created")
    @ns_trakers.marshal_with(_tracker, as_list=True)
    def  get(self):
        """List of all trackers"""
        try:
            trackers=get_all_trackers()
            return trackers,200
        except Exception as e:
            print(str(e))
    @ns_trakers.expect(_tracker, validate=True)
    def post(self):
        """Create a new tracker"""
        try:
            data = request.json
            assert np.allclose(
                sum(data["weights"].values()), 1.0), "weights sum must be 1.0"
            assert set(data["weights"].keys()) == set(data["ubound_weights"].keys()) == set(
                data["lbound_weights"].keys()) == set(data["tickers"]), "one or more tickers are missing"
            new_data = {**data,
            "tracker_id": data["name"] + data["direction"]}
            save_new_tracker(**new_data)
            return "Tracker has been created successfully.",200
        except :
            pass
@ns_trakers.route("/trackers/<string:tracker_id>")
class TrackerDetailView(Resource):
    @ns_trakers.marshal_with(_tracker)
    def get(self, tracker_id: str):
        """ Get a tracker given its identifier"""
        try:
            tracker = get_one_tracker(tracker_id)
            print(tracker)
            return tracker, 200
        except Exception as e:
            print(str(e))
            pass

    @ns_trakers.expect(_tracker, validate=True)
    def put(self, tracker_id: str):
        """ Edit a tracker by its identifier """
        try:
            data = request.json
            assert np.allclose(
                sum(data["weights"].values()), 1.0), "weights sum must be 1.0"

            assert set(data["weights"].keys()) == set(data["ubound_weights"].keys()) == set(
                data["lbound_weights"].keys()) == set(data["tickers"]), "one or more tickers are missing"
            new_data = {**data,
                        "tracker_id": data["name"] + data["direction"]}
            update_tracker(tracker_id, new_data)
            return "Tracker updated successfully ", 200
        except:
            pass

    def delete(self, tracker_id: str):
        """ Delete a tracker by its identifier """
        try:
            delete_one_tracker(tracker_id)
        except:
            pass     