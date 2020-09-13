"""
Slots class
"""
from random import randint
from copy import deepcopy
from textwrap import wrap

class Slots:
    def __init__(self, slots=False, start=375, end=1650):
        self.language = "RU"
        self._slots = []
        if slots:
            self.add(slots)
        self.start = start
        self.end = end
        self.zero_time = 1440
        self.now_time = start
        self.day = 0
        self.justify = 40
        self._str_flag = 0
        # all-time values
        self.days_at_all = 0
        self.smoke = [0, 0]
        self.diet_day = 0
        self.diet_done = 0
        self.diet = []
        self.weight = []
        self.muscle = []
        self.water = []
        self.fat = []
        self.good_things = []
        self.new_things = []

    def __call__(self):
        return self._slots

    def __iter__(self):
        if self._str_flag == 1:
            self.now_time = self.start
            for slot in self._slots:
                yield slot
                self.now_time += slot['length']
        else:
            self.now_time = self.start
            index = 0
            for slot in self._slots:
                activity = self._get_activity(slot, index)
                self._slots[index] = activity['slot']
                yield activity['result']
                self.now_time += slot["length"]
                index += 1

    def __add__(self, value):
        self.add(value)
        return self

    def __str__(self):
        self._str_flag = 1
        def slot_str(slot):
            slot_str = str(slot["activities"])
            if (slot["video"]):
                slot_str += "\t\t(VIDEO: %s)" % str(slot["video"])
            if (slot["audio"]):
                slot_str += "\t\t(AUDIO: %s)" % str(slot["audio"])
            return slot_str
        string = "\n".join(["%s - %s" % (self.time(), slot_str(s)) for s in self]) \
            .replace("radiobroadcast", "Радиопередача - %s" % self._radio_broadcast())
        self._str_flag = 0
        return string

    def _get_activity(self, slot, index):
        if isinstance(slot['activities'], str):
            result = {
                'time': self.time(),
                'basic': slot['activities'],
                'video': slot['video'],
                'audio': slot['audio'],
                }
        else:
            self._show_all_activities(slot)
            self._show_basic_activities(slot)
            choice_basic = self._choice(len(slot['activities']))
            if choice_basic == 17: return self._get_activity(slot, index)
            choosen_basic = slot['activities'][choice_basic]
            available = choosen_basic['available']
            choosen_video = None
            choosen_audio = None
            if available is not None and isinstance(available, list) and len(available):
                if choosen_basic['audio_only']:
                    audio = [slot['audio'][x] for x in available]
                    self._show_audio_activities(audio)
                    choice_audio = self._choice(len(audio))
                    if choice_audio == 17: return self._get_activity(slot, index)
                    choosen_audio = audio[choice_audio]
                    index_audio = available[choice_audio]
                    choosen_basic['count'] -= 1
                    choosen_audio['count'] -= 1
                    del choosen_basic['available'][choice_audio]
                    result = {
                        'time': self.time(),
                        'basic': choosen_basic['name'],
                        'video': None,
                        'audio': choosen_audio['name'],
                        }
                    self._choosen(choosen_basic, 'activities', index)
                    self._choosen(choosen_audio, 'audio', index)
                    if choosen_basic['count'] == 0:
                        del slot['activities'][choice_basic]
                    else:
                        slot['activities'][choice_basic] = choosen_basic
                    slot['audio'][index_audio] = choosen_audio if choosen_audio['count'] > 0 else None

                else:
                    video = [slot['video'][x] if isinstance(x, int) \
                        else self._copy_and_update(slot['video'], x)
                            for x in available]
                    self._show_video_activities(slot, video)
                    choice_video = self._choice(len(video))
                    if choice_video == 17: return self._get_activity(slot, index)
                    video_index = available[choice_video]
                    choosen_video = video[choice_video]
                    available = choosen_video['available']
                    if available is not None and isinstance(available, list) and len(available):
                        if 'dict' in choosen_video:
                            choosen_audio = slot['audio'][choosen_video['value']]
                            choosen_audio['count'] -= 1
                            choosen_video['count'] -= 1
                            choosen_basic['count'] -= 1
                            del choosen_basic['available'][choice_video]
                            choosen_video['available'].remove({
                                choosen_video['value']: choosen_video['key']
                                })
                            result = {
                                'time': self.time(),
                                'basic': choosen_basic['name'],
                                'video': choosen_video['name'],
                                'audio': choosen_audio['name'],
                                }
                            self._choosen(choosen_basic, 'activities', index)
                            self._choosen(choosen_video, 'video', index)
                            self._choosen(choosen_audio, 'audio', index)
                            if choosen_basic['count'] == 0:
                                del slot['activities'][choice_basic]
                            else:
                                slot['activities'][choice_basic] = choosen_basic
                            slot['audio'][choosen_video['value']] = choosen_audio if choosen_audio['count'] > 0 else None
                            del choosen_video['dict']
                            del choosen_video['key']
                            del choosen_video['value']
                            if isinstance(video_index, dict):
                                video_index = list(video_index.keys())[0]
                            slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
                        else:
                            audio = [slot['audio'][x] for x in available if isinstance(x, int)]
                            self._show_audio_activities(audio)
                            choice_audio = self._choice(len(audio))
                            if choice_audio == 17: return self._get_activity(slot, index)
                            choosen_audio = audio[choice_audio]
                            index_audio = self._get_true_index_audio(available, choice_audio)
                            choosen_basic['count'] -= 1
                            choosen_video['count'] -= 1
                            choosen_audio['count'] -= 1
                            del choosen_basic['available'][choice_video]
                            choosen_video['available'].remove(index_audio)
                            result = {
                                'time': self.time(),
                                'basic': choosen_basic['name'],
                                'video': choosen_video['name'],
                                'audio': choosen_audio['name'],
                                }
                            self._choosen(choosen_basic, 'activities', index)
                            self._choosen(choosen_video, 'video', index)
                            self._choosen(choosen_audio, 'audio', index)
                            if choosen_basic['count'] == 0:
                                del slot['activities'][choice_basic]
                            else:
                                slot['activities'][choice_basic] = choosen_basic
                            slot['audio'][index_audio] = choosen_audio if choosen_audio['count'] > 0 else None
                            slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
                    else:
                        choosen_video['count'] -= 1
                        choosen_basic['count'] -= 1
                        del choosen_basic['available'][choice_video]
                        result = {
                            'time': self.time(),
                            'basic': choosen_basic['name'],
                            'video': choosen_video['name'],
                            'audio': None,
                            }
                        self._choosen(choosen_basic, 'activities', index)
                        self._choosen(choosen_video, 'video', index)
                        if choosen_basic['count'] == 0:
                            del slot['activities'][choice_basic]
                        else:
                            slot['activities'][choice_basic] = choosen_basic
                        slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
            else:
                choosen_basic['count'] -= 1
                result = {
                    'time': self.time(),
                    'basic': choosen_basic['name'],
                    'video': None,
                    'audio': None,
                        }
                self._choosen(choosen_basic, 'activities', index)
                if choosen_basic['count'] == 0:
                    del slot['activities'][choice_basic]
                else:
                    slot['activities'][choice_basic] = choosen_basic
        return {
            'slot': slot,
            'result': result
            }

    def _copy_and_update(self, options, dict_map):
        key = list(dict_map.keys())[0]
        value = list(dict_map.values())[0]
        option_copy = deepcopy(options[key])
        option_copy.update({"dict": dict_map, "key": key, "value": value})
        return option_copy

    def _get_true_index_audio(self, available, choice_audio):
        for i in range(len(available)):
            if isinstance(available[i], int):
                choice_audio -= 1
                if choice_audio == -1:
                    return available[i]

    def _show_all_activities(self, slot):
        j = self._justify
        print("\n", '-'*80)
        print("\nВРЕМЯ - %s" % self.time(), "\n")
        print("Для этого слота доступно:\n")
        result = j("ACTIVITIES", 43) + j("VIDEO", 43) + "AUDIO" + "\n"
        for i in range(8):
                temp, flag = self._get_option_line(slot, i)
                if flag:
                    result += temp + "\n"
        print(result)

    def _show_basic_activities(self, slot):
        basic = slot['activities']
        if len(basic) > 1:
            print("Выберите базовое занятие:")
            for i in range(len(basic)):
                option = basic[i]
                if option == None:
                    continue
                availables = self._get_availables(slot, option)
                print("%i. %s%s" % (i+1,
                    self._justify(self._get_option_text(basic, i)),
                        (("audio: " if option['audio_only'] else "video: ") +
                            ("\n"+50*" ").join(availables)) if availables else ""))

    def _show_video_activities(self, slot, video):
        print("\nВыберите видео:")
        for i in range(len(video)):
            option = video[i]
            if option == None: continue
            availables = self._get_availables(slot, option) \
                if 'dict' not in option else \
                    { self._get_option_text(slot['audio'], list(option['dict'].values())[0]) }
            print("%i. %s%s" % (i+1,
                self._justify(self._get_option_text(video, i)),
                    ("audio: " + ";  ".join(availables)) if availables else ""))

    def _show_audio_activities(self, audio):
        print("\nВыберите аудио:")
        for i in range(len(audio)):
            option = audio[i]
            if option == None: continue
            print("%i. %s" % (i+1, self._get_option_text(audio, i)))

    def _get_availables(self, slot, option):
        if option['available'] == None:
            return None
        elif 'audio_only' in option and not option['audio_only']:
            return {self._get_option_text(slot['video'], x) if isinstance(x, int) \
                else self._get_option_text(slot['video'], list(x.keys())[0]) + " + " + \
                    self._get_option_text(slot['audio'], list(x.values())[0]) \
                        if isinstance(x, dict) else "---" \
                            for x in option['available'] \
                                } or None
        else:
            return {self._get_option_text(slot['audio'], x) \
                        for x in option['available'] \
                            if isinstance(x, int) \
                                } or None

    def _justify(self, string, value=None):
        return string.ljust(value or self.justify)

    def _get_option_line(self, slot, index):
        line = ""
        temp, flag = self._get_option_tab(slot, index, 'activities')
        line += temp
        temp, flag = self._get_option_tab(slot, index, 'video', flag)
        line += temp
        temp, flag = self._get_option_tab(slot, index, 'audio', flag)
        line += temp
        return line, flag

    def _get_option_tab(self, slot, index, type, flag=False):
        tab = ""
        if len(slot[type]) > index:
            tab = self._get_option_text(slot[type], index)
        if tab or flag:
            flag = True
        return self._justify(tab, 43), flag

    def _get_option_text(self, options, index):
        now = options[index]
        if now == None:
            return "---"
        now_text = now['name']
        if now["previous"]:
            now_text += " (P)"
        return now_text

    def _choice(self, max):
        if max > 1:
            try:
                choice = int(input("Выберите номер: "))
                if choice == 17:
                    print("Возврат -->")
                    return 17
                elif choice > max:
                    raise Exception
            except Exception:
                choice = 1
            print("Текущий выбор - %i." % choice)
        else:
            choice = 1
        return choice-1

    def time(self):
        time = self.now_time
        if time > self.zero_time:
            time -= self.zero_time
        hours = time // 60
        if hours > 23:
            hours -= 24
        minutes = time % 60
        return "%.2i:%.2i" % (hours, minutes)

    def delete_option(self, slot_index, type, option_index=None):
        if option_index is None: return
        options = self._slots[slot_index][type]
        if isinstance(options, list):
            self._slots[slot_index][type][option_index]["count"] -= 1
            if self._slots[slot_index][type][option_index]["count"] == 0:
                self._slots[slot_index][type][option_index] = None

    def _choosen(self, option, type, index):
        if option["last"]: return
        next_slot = self._next(index)
        if next_slot and isinstance(next_slot[type], list):
            for item in next_slot[type]:
                if item is None: continue
                item["previous"] = item["name"] == option["name"]

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
    slots = Slots([[["activity 1", 2, False, [0,1]], ["activity 2", 1, True, [1], True]],
        [["video 1", 2, False, [0,1]], ["video 2", 1, True, [1]]],
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

    slots.create_todo_list()
