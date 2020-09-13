try:
    # introduction set of slots
    from introduction import INTRODUCTION
    # default set of slots
    from wake_up import WAKE_UP
    from morning import MORNING
    from day_early import EARLY_DAY
    from midday import MIDDAY
    from day_late import LATEDAY
    from evening import EVENING
    from night_early import NIGHT
    from night_late import LATE_NIGHT

except ImportError:
    # introduction set of slots
    from activities.introduction import INTRODUCTION
    # default set of slots
    from activities.wake_up import WAKE_UP
    from activities.morning import MORNING
    from activities.day_early import EARLY_DAY
    from activities.midday import MIDDAY
    from activities.day_late import LATEDAY
    from activities.evening import EVENING
    from activities.night_early import NIGHT
    from activities.night_late import LATE_NIGHT

DEFAULT = WAKE_UP + MORNING + EARLY_DAY + MIDDAY + LATEDAY + EVENING + NIGHT + LATE_NIGHT


PHASES_LIST = [
    INTRODUCTION,   # first 15 days
    DEFAULT,        # 16 - 30 days
    DEFAULT,        # 31 - 45 days
    DEFAULT,        # 46 - 60 days
    DEFAULT,        # 61 - 75 days
    DEFAULT,        # 76 - 90 days
    DEFAULT,        # 91 - 105 days
    DEFAULT,        # 106 - 120 days
    DEFAULT,        # 121 - 135 days
]

__all__ = ['PHASES_LIST']
