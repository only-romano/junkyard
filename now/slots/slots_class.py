"""
Slots class
"""
class Slots:
    def __init__(self, slots=False, start=15, end=1290):
        self._slots = []
        if slots:
            self.add(slots)
        self.start = start
        self.end = end

    def __iter__(self):
        for slot in self._slots:
            yield slot

    def __add__(self, value):
        self.add(value)
        return self

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
                "attn": activity[1],
                "count":activity[2],
                "last": activity[3],
                }
            if not isinstance(function, Slots):
                # fix for functionless calls
                option.update(function(activity[4:]))
            return option
        return wrapper

    @staticmethod
    @_option
    def _create_video_option(video):
        return {"available_audio": video[0]}

    @staticmethod
    @_option
    def _create_basic_option(basic):
        return {"available": basic[0], "audio_only": basic[1]}


if __name__ == '__main__':
    slots = Slots([[["activity 1", 5, 2, False, [1,2,3], False], ["activity 2", 1, 1, True, [2], True]],
        [["video 1", 2, 2, False, [1,2,3]], ["video 2", 1, 1, True, [2]]],
        [["audio 1", 2, 2, False], ["audio 2", 1, 1, True]], 1])

    slots += [[["slot 2 act", 1 , 2, True, [23, 15], False]], [["slot 2 video", 2, 3, False, [0,1]]], [["slot 2 audio", 2,3,False]], 4]
    slots += [[["slot 3 act", 1 , 2, True, [23, 15], False]], None, "Only audio", 4]

    for slot in slots:
        for key in slot:
            print(key, " - ", slot[key], "\n")
