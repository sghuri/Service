from core.src.Models.trackers import Trackers
import pandas as pd
import json
def save_new_tracker(**kwargs) -> Trackers:
    tck =  Trackers(**kwargs)
    tck.save()
    return tck
def get_all_trackers():
    trackers = Trackers.objects.all().to_json()
    return  json.loads(trackers)
def update_tracker(tracker_id, kwargs) -> Trackers:
    tck = Trackers.objects.get(tracker_id = tracker_id).update(**kwargs)
    return tck 
        
def delete_one_tracker(tracker_id : str) -> bool:
    tck = Trackers.objects.get(tracker_id = tracker_id)
    tck.delete()
    return True
def get_one_tracker(tracker_id:str) -> Trackers:
    tck = Trackers.objects.get(tracker_id = tracker_id).to_json()
    return json.loads(tck)