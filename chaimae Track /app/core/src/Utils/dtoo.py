from flask_restplus import (Namespace, fields, Api)
from core import api
import pandas as pd
class formattedDateTime(fields.DateTime):
    def format(self, value):
        if isinstance(value, dict):
            return pd.Timestamp(int(value["$date"]), unit="ms").isoformat()
        else:
            return value

class TrackerDto:
    ns_trakers = api.namespace("tracker1", description="Trackers related operations")
    _tracker=ns_trakers.model("tracker1", 
                        dict(
                        tracker_id = fields.String(),
                        creation_date = formattedDateTime(),
                        name = fields.String(required = True),
                        asset_class = fields.String(),
                        theme = fields.String(),
                        direction = fields.String(required = True),
                        portal_name = fields.String(),
                        tickers = fields.List(fields.String(required = True)),
                        weights = fields.Raw(required = True),
                        lbound_weights = fields.Raw(required = True),
                        ubound_weights = fields.Raw(required = True),
                        volatility_target = fields.Float(required = True, min = 0.0),
                        volatility_max = fields.Float(required = True, min = 0.0),
                        volatility_tolerance = fields.Float(required = True, min = 0.0),
                        volatility_duration = fields.Integer(required = True,  min = 0),
                        notional = fields.Float(required = True, min = 0.0),
                        calibration_volume_threshold = fields.Float(required = True, min = 0.0),
                        retails_units = fields.Raw(),
                        leverage = fields.Float(required = True),
                        min_risky = fields.Float(required = True),
                        gonogo_return = fields.Float(required = True),
                        gonogo_weight = fields.Float(required = True),
                        max_uncalibrate = fields.Integer(required = True),
                        factsheet_link = fields.String(),
                        performances = fields.Raw(),
                        benchmark= fields.String())
    )
