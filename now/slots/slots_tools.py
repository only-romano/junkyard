import pickle
from init_slots import init_slots


def create_today_file(slots):
    pass

def get_activity(slot):
    """Returns activity, rewrites state"""
    pass

def RESET_SLOTS(period):
    """Resets free slots to period start (all slots are available)"""
    pass

def load_slots():
    """Loads current available slots"""
    return {"day": 9}

def write_slots(period, slots):
    """Saves slots state after maden decisions"""
    pass


__ALL__ = ["create_today_file", "get_activity", "RESET_SLOTS", "load_slots", "write_slots"]
