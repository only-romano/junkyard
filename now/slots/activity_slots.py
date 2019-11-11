"""
1. create empty SLot object (must have add, remove methods)
2. fill in with activities, videos, audios, time
"""
from init_slots import init_slots

class Slots:
    def __init__(self, slots=False, start=15, end=1290):
        self._slots = slots and self.add(slots) or []
        self.length = self._length(self)
        self.start = start
        self.end = end

    def _length(self):
        return len(self._slots)

    def add(self, slots_list):
        if len(slots_list) == 4 and isinstance(slots_list[3], int):
            # there is only one slot to add
            slots_list = [slots_list]
        for one_slot in slots_list:
            self._slots.append(self._create_slot(self, one_slot))


    def _create_slot(self, params):
        slot = {}
        slot["activities"] = self._create_list_of_options(self, params[0])
        slot["video"] = self._create_list_of_options(self, params[1], "video")
        slot["audio"] = self._create_list_of_options(self, params[2], "audio")
        slot["length"] = params[3]
        return slot

    def _create_list_of_options(self, data, flag=False):
        list_of_options = []
        for option in data:
            list_of_options.append(self._create_option(option))
        return list_of_options

    def _create_option(self, option, flag):
        option_to_write =
    return {
        "name": name,
        "available_video": video,
        "available_audio": audio,
        "max_length": length,
        "COUNT": count,
    }

Slots = init_slots() # must initialize slots class

Slots.add(slot_01)

slot_01 = None
slot_02 = None
slot_03 = None
slot_04 = None
slot_05 = None
slot_06 = None
slot_07 = None
slot_08 = None
slot_09 = None
slot_10 = None
slot_11 = None
slot_12 = None
slot_13 = None
slot_14 = None
slot_15 = None
slot_16 = None
slot_17 = None
slot_18 = None
slot_19 = None
slot_20 = None
slot_21 = None
slot_22 = None
slot_23 = None
slot_24 = None
slot_25 = None
slot_26 = None
slot_27 = None
slot_28 = None
slot_29 = None
slot_30 = None
slot_31 = None
slot_32 = None
slot_33 = None
slot_34 = None
