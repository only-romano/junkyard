"""
Init new slots instance, fill it up with activities.
Module used to create default chain of activities for every start period.
Activities modifications is allowed.
"""
# Deprecated
#from custom_slot import create_custom_slots
from slots_class import Slots
from activities.phases import PHASES_LIST


def get_slots(phase):
    if phase > 2: phase = 2
    slots = Slots() # initialize Slots class instance
    slots.add(PHASES_LIST[phase])

    return slots


# interactive slots creation tool
# Deprecated
#slots = create_custom_slots(slots)

__all__ = ['slots']

if __name__ == '__main__':
    from random import choice
    slots = get_slots(5)
    for slot in slots:
        print(slot)
        activity = slot['activities']
        if isinstance(activity, list):
            activity = choice(activity)['name']
        print(slots.time(), activity)
