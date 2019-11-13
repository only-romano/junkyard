"""
Init new slots instance, fill it up with activities.
Module used to create default chain of activities for every start period.
Activities modifications is allowed.
"""
from slots_class import Slots
from custom_slot import create_custom_slots
from activities.wake_up import WAKE_UP
from activities.morning import MORNING
from activities.day_early import EARLY_DAY
from activities.midday import MIDDAY
#from activities.day_late import LATEDAY
#from activities.evening import EVENING
#from activities.night_early import NIGHT
#from activities.night_late import LATE_NIGHT

slots = Slots() # initialize Slots class instance

# Wake up activities (until 7:00)
slots.add(WAKE_UP)
# Morning activities (until morning training min-finish time [07:00 - 10:00])
slots.add(MORNING)
# Early daytime activities (until midday siesta [not included, 10:00 - 13:00])
slots.add(EARLY_DAY)
# Midday activites (until second dinner [included, 13:00 - 15:30])
slots.add(MIDDAY)
# Late daytime activities (until evening siesta [not included, 15:30 - 19:00])
#slots.add(LATE_DAY)
# Evening activities (until night siesta [included, 19:00 - 22:00])
#slots.add(EVENING)
# Night activities (until possible sleep start [not included, 22:00 - 00:30])
#slots.add(NIGHT)
# Late night activities (until required sleep [not included, 00:30 - 03:30])
#slots.add(LATE_NIGHT)

# interactive slots creation tool
slots = create_custom_slots(slots)

__all__ = ['slots']

if __name__ == '__main__':
    print(slots)
