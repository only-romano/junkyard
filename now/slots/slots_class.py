"""
Slots class
"""
from random import randint

class Slots:
    def __init__(self, slots=False, start=375, end=1650):
        self._slots = []
        if slots:
            self.add(slots)
        self.start = start
        self.end = end
        self.zero_time = 1440
        self.now_time = start

    def __call__(self):
        return self._slots

    def __iter__(self):
        self.now_time = self.start
        for slot in self._slots:
            yield slot
            self.now_time += slot["length"]

    def __add__(self, value):
        self.add(value)
        return self

    def __str__(self):
        def slot_str(slot):
            slot_str = str(slot["activities"])
            if (slot["video"]):
                slot_str += "\t\t(VIDEO: %s)" % str(slot["video"])
            if (slot["audio"]):
                slot_str += "\t\t(AUDIO: %s)" % str(slot["audio"])
            return slot_str
        return "\n".join(["%s - %s" % (self.time(s), slot_str(s)) for s in self]) \
            .replace("radiobroadcast", "Радиопередача - %s" % self._radio_broadcast())

    def time(self, slot):
        time = self.now_time
        if time > self.zero_time:
            time -= self.zero_time
        hours = time // 60
        if hours > 23:
            hours -= 24
        minutes = time % 60
        return "%.2i:%.2i" % (hours, minutes)

    def add(self, slots):
        """
        Slots must be a list of slot_list - to create one - use interactive
        create_slot_list function from slot_tools.
        Or it can be single unpacked slot_list.
        """
        if len(slots) == 4 and isinstance(slots[3], int):
            # there is only one slot to add
            slots = [slots]
        for slot in slots:
            self._slots.append(self._create_slot_object(slot))

    def _radio_broadcast(self):
        return "Евгеника" if randint(1,4) == 1 else "Маяк"

    def _next(self, index):
        index += 1
        if len(self._slots) > index:
            return self._slots[index]

    def _choosen(self, option, type, index):
        if option["last"]: return
        next_slot = self._next(index)
        if next_slot:
            for item in next_slot[type]:
                item["previous"] = item["name"] == option["name"]

    def _create_slot_object(self, slot):
        slot_object = {
            "activities": self._create_options(slot[0]),
            "video": self._create_options(slot[1], "v"),
            "audio": self._create_options(slot[2], "a"),
            "length": slot[3]
            }
        return slot_object

    def _create_options(self, activities, flag=False):
        if not isinstance(activities, list):
            options = activities
        elif flag == "a":
            options = [self._option()(audio) for audio in activities]
        elif flag == "v":
            options = [self._create_video_option(video) for video in activities]
        else:
            options = [self._create_basic_option(basic) for basic in activities]
        return options

    def _option(function):
        def wrapper(activity):
            option = {
                "name": activity[0],
                "count":activity[1],
                "last": activity[2],
                "choosen": False,
                "previous": False,
                }
            if not isinstance(function, Slots):
                # fix for functionless calls
                option.update(function(activity[3:]))
            return option
        return wrapper

    @staticmethod
    @_option
    def _create_video_option(video):
        return {"available": video[0]}

    @staticmethod
    @_option
    def _create_basic_option(basic):
        return {"available": basic[0], "audio_only": len(basic) > 1}


__all__ = ['Slots']

if __name__ == '__main__':
    slots = Slots([[["activity 1", 2, False, [1,2,3], False], ["activity 2", 1, True, [2], True]],
        [["video 1", 2, False, [1,2,3]], ["video 2", 1, True, [2]]],
        [["audio 1", 2, False], ["audio 2", 1, True]], 1])

    slots += [[["slot 2 act", 2, True, [23, 15], False]], [["slot 2 video", 3, False, [0,1]]], [["slot 2 audio", 3,False]], 4]
    slots += [[["slot 3 act", 2, True, [23, 15], False]], None, "Only audio", 4]

    for slot in slots:
        print(slots.time(slot))
        for key in slot:
            print(key, " - ", slot[key], "\n")
    for slot in slots:
        print(slots.time(slot))
