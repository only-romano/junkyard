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
        self.day = 0
        self.justify = 40

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
        return "\n".join(["%s - %s" % (self.time(), slot_str(s)) for s in self]) \
            .replace("radiobroadcast", "Радиопередача - %s" % self._radio_broadcast())

    def time(self):
        time = self.now_time
        if time > self.zero_time:
            time -= self.zero_time
        hours = time // 60
        if hours > 23:
            hours -= 24
        minutes = time % 60
        return "%.2i:%.2i" % (hours, minutes)

    def create_todo_list(self):
        todo_list = []
        slot_index = 0
        for slot in self:
            todo_element = {}
            todo_element['time'] = self.time()
            print("\nВыбираем основное занятие на %s:" % self.time())
            todo_element.update(self.get_activity(slot, slot_index))
            todo_list.append(todo_element)
            slot_index += 1
        self.day += 1
        return todo_list

    def get_activity(self, slot, slot_index):
        while True:
            self.print_all(slot)
            activity, activity_index, available = self.get_option(slot, 'activities', slot_index)
            if not activity: continue
            video, video_index, available = self.get_option(slot, 'video', slot_index, available)
            if not video: continue
            audio, audio_index, a = self.get_option(slot, 'audio', slot_index, available)
            if not audio: continue
            else: break
        delete_option(slot_index, 'activities', activity_index)
        delete_option(slot_index, 'video', video_index)
        delete_option(slot_index, 'audio', audio_index)
        return {'activity': activity, 'video': video, 'audio': audio}

    def get_option(self, slot, type, index, available=True):
        if isinstance(slot[type], str):
            return slot[type], None, True
        if available is None:
            return None, None, None
        if available is True:
            to_choose = slot[type]
        else:
            to_choose = []
            to_choose_list = slot[type]
            for i in available:
                if isinstance(available[i], dict):
        print_options(to_choose)
        choosen_index = int(input("Номер опции: ")) - 1
        yes = input("Вы уверены? (любой символ для подтверждения, пустая строка для отмены): ")
        option = to_choose[choosen_index]
        if len(yes):
            self._choosen(option, type, index)
            avlb = None
            if 'available' in option:
                avlb = option['available']
            return (option['name'], choosen_index, avlb)

    def print_options(self, options):
        print("Введите номер желаемой опции:")
        index = 1
        for option in options:
            print("%i. %s" % (index, option['name']))

    def delete_option(self, slot_index, type, option_index=None):
        if option_index is None: return
        options = self._slots[slot_index][type]
        if isinstance(options, list):
            option = options[option_index]
            option["count"] -= 1
            if option['count'] == 0:
                del self._slots[slot_index][type][option_index]

    def _choosen(self, option, type, index):
        if option["last"]: return
        next_slot = self._next(index)
        if next_slot:
            for item in next_slot[type]:
                item["previous"] = item["name"] == option["name"]

    def j(self, string):
        return string.ljust(self.justify)

    def print_all(self, slot):
        j = self.j
        result = j("ACTIVITIES") + j("VIDEO") + "AUDIO" + "\n\n"
        if isinstance(slot['activities'], str):
            result += j(slot['activities']) + j(slot['video']) + slot['audio'] + '\n\n'
        else:
            for i in range(9):
                result += get_option_text(slot, 'activities', i)
                result += get_option_text(slot, 'video', i)
                result += get_option_text(slot, 'audio', i)
                result += "\n"
        print(result)
        input("Нажмите enter, чтобы продолжить")

    def get_option_text(self, slot, type, index):
        activity = ""
        if len(slot[type]) > index:
            activity = self.get_now_text(slot[type], index)
        return self.j(activity)

    def get_now_text(self, options, index):
        now = options[i]
        now_text = now['name']
        if now["previous"]:
            now_text += " (P)"
        return now_text

    def _next(self, index):
        index += 1
        if len(self._slots) > index:
            return self._slots[index]

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
        print(slots.time())
        for key in slot:
            print(key, " - ", slot[key], "\n")
    for slot in slots:
        print(slots.time())

    print("ACTIVITIES".ljust(33) + "VIDEO".ljust(33) + "AUDIO".ljust(33))
