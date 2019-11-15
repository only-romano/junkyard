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
        self.justify = 30
        self._str_flag = 0

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
            choosen_basic = slot['activities'][choice_basic]
            choosen_basic['choosen'] = "yes" # set choosen property to "yes"
            choosen_basic['count'] -= 1
            available = choosen_basic['available']
            choosen_video = None
            choosen_audio = None
            if available is not None and isinstance(available, list) and len(available):
                if choosen_basic['audio_only']:
                    audio = [slot['audio'][x] for x in available]
                    self._show_audio_activities(audio)
                    choice_audio = self._choice(len(audio))
                    choosen_audio = audio[choice_audio]
                    choosen_audio['choosen'] = "yes"
                    index_audio = available[choice_audio]
                    del choosen_basic['available'][choice_audio]
                    choosen_audio['count'] -= 1
                    result = {
                        'time': self.time(),
                        'basic': choosen_basic['name'],
                        'video': None,
                        'audio': choosen_audio['name'],
                        }
                    self._choosen(choosen_basic, 'activities', index)
                    self._choosen(choosen_audio, 'audio', index)
                    choosen_basic['choosen'] = False
                    choosen_audio['choosen'] = False
                    if choosen_basic['count'] == 0:
                        del slot['activities'][choice_basic]
                    else:
                        slot['activities'][choice_basic] = choosen_basic
                    slot['audio'][index_audio] = choosen_audio if choosen_audio['count'] > 0 else None

                else:
                    video = [slot['video'][x] if isinstance(x, int) \
                        else slot['video'][list(x.keys())[0]].update({"dict": x})
                            or slot['video'][list(x.keys())[0]] \
                                for x in available]
                    self._show_video_activities(slot, video)
                    choice_video = self._choice(len(video))
                    video_index = available[choice_video]
                    del choosen_basic['available'][choice_video]
                    choosen_video = video[choice_video]
                    choosen_video['choosen'] = "yes"
                    choosen_video['count'] -= 1
                    available = choosen_video['available']
                    if available is not None and isinstance(available, list) and len(available):
                        if 'dict' in choosen_video:
                            choosen_audio = slot['audio'][list(choosen_video['dict'].values())[0]]
                            choosen_audio['choosen'] = 'yes'
                            choosen_audio['count'] -= 1
                            choosen_video['available'].remove({
                                list(choosen_video['dict'].values())[0]: list(choosen_video['dict'].keys())[0]
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
                            choosen_basic['choosen'] = False
                            choosen_video['choosen'] = False
                            choosen_audio['choosen'] = False
                            if choosen_basic['count'] == 0:
                                del slot['activities'][choice_basic]
                            else:
                                slot['activities'][choice_basic] = choosen_basic
                            slot['audio'][list(choosen_video['dict'].values())[0]] = choosen_audio if choosen_audio['count'] > 0 else None
                            del choosen_video['dict']
                            if isinstance(video_index, dict):
                                video_index = list(video_index.keys())[0]
                            slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
                        else:
                            audio = [slot['audio'][x] for x in available if isinstance(x, int)]
                            self._show_audio_activities(audio)
                            choice_audio = self._choice(len(audio))
                            choosen_audio = audio[choice_audio]
                            choosen_audio['choosen'] = "yes"
                            index_audio = available[choice_audio]
                            choosen_video['available'].remove(index_audio)
                            choosen_audio['count'] -= 1
                            result = {
                                'time': self.time(),
                                'basic': choosen_basic['name'],
                                'video': choosen_video['name'],
                                'audio': choosen_audio['name'],
                                }
                            self._choosen(choosen_basic, 'activities', index)
                            self._choosen(choosen_video, 'video', index)
                            self._choosen(choosen_audio, 'audio', index)
                            choosen_basic['choosen'] = False
                            choosen_video['choosen'] = False
                            choosen_audio['choosen'] = False
                            if choosen_basic['count'] == 0:
                                del slot['activities'][choice_basic]
                            else:
                                slot['activities'][choice_basic] = choosen_basic
                            slot['audio'][index_audio] = choosen_audio if choosen_audio['count'] > 0 else None
                            slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
                    else:
                        result = {
                            'time': self.time(),
                            'basic': choosen_basic['name'],
                            'video': choosen_video['name'],
                            'audio': None,
                            }
                        self._choosen(choosen_basic, 'activities', index)
                        self._choosen(choosen_video, 'video', index)
                        choosen_basic['choosen'] = False
                        choosen_video['choosen'] = False
                        if choosen_basic['count'] == 0:
                            del slot['activities'][choice_basic]
                        else:
                            slot['activities'][choice_basic] = choosen_basic
                        slot['video'][video_index] = choosen_video if choosen_video['count'] > 0 else None
            else:
                result = {
                    'time': self.time(),
                    'basic': choosen_basic['name'],
                    'video': None,
                    'audio': None,
                        }
        return {
            'slot': slot,
            'result': result
            }

    def _show_all_activities(self, slot):
        j = self._justify
        print("\n", '-'*80)
        print("\nВРЕМЯ - %s" % self.time(), "\n")
        print("Для этого слота доступно:")
        result = j("ACTIVITIES") + j("VIDEO") + "AUDIO" + "\n"
        for i in range(8):
                temp, flag = self._get_option_line(slot, i)
                if flag:
                    result += temp + "\n"
        print(result)

    def _show_basic_activities(self, slot):
        basic = slot['activities']
        if len(basic) > 1:
            print("Выберете базовое занятие:")
            for i in range(len(basic)):
                option = basic[i]
                if option == None:
                    continue
                print("%i. %s (%s: %s)" % (i+1,
                    self._get_option_text(basic, i),
                        "audio" if option['audio_only'] else "video",
                            self._get_availables(slot, option)))

    def _show_video_activities(self, slot, video):
        print("\nВыберете видео:")
        for i in range(len(video)):
            option = video[i]
            if option == None: continue
            print("%i. %s (%s: %s)" % (i+1,
                self._get_option_text(video, i),
                    "audio",
                        self._get_availables(slot, option) if 'dict' not in option \
                            else slot['audio'][list(option['dict'].values())[0]]['name']))

    def _show_audio_activities(self, audio):
        print("\nВыберете аудио:")
        for i in range(len(audio)):
            option = audio[i]
            if option == None: continue
            print("%i. %s" % (i+1, self._get_option_text(audio, i)))

    def _get_availables(self, slot, option):
        if option['available'] == None: return "---"
        if 'audio_only' in option and not option['audio_only']:
            return ", ".join([slot['video'][x]['name'] if isinstance(x, int) \
                else slot['video'][list(x.keys())[0]]['name'] + "+" + \
                    slot['audio'][x[list(x.keys())[0]]]['name'] \
                        for x in option['available']]) or "---"
        else:
            return ", ".join([slot['audio'][x]['name'] if isinstance(x, int) \
                else slot['audio'][list(x.keys())[0]]['name'] \
                    for x in option['available']]) or "---"

    def _justify(self, string):
        return string.ljust(self.justify)

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
        return self._justify(tab), flag

    def _get_option_text(self, options, index):
        now = options[index]
        if now == None:
            return "---"
        now_text = now['name']
        if now["previous"]:
            now_text += " (P)"
        return now_text

    def _choice(self, max):
        yes = True
        if max > 1:
            while yes:
                try:
                    choice = int(input("Выберете номер: "))
                    if choice > max:
                        raise Exception
                except Exception:
                    choice = 1
                print("Текущий выбор - %i." % choice)
                yes = ""
        else:
            return 0
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
            activity, activity_index, available, a = self.get_option(slot, 'activities', slot_index)
            if not activity: continue
            video, video_index, available, v_ind = self.get_option(slot, 'video', slot_index, available)
            if not video: continue
            audio, audio_index, a, a_ind = self.get_option(slot, 'audio', slot_index, available)
            if not audio: continue
            else: break
        self.update_availables(slot_index, activity_index, video_index, audio_index, v_ind, a_ind)
        return {'activity': activity, 'video': video, 'audio': audio}

    def update_availables(self, slot_index, act_index, v_index, a_index, act_ind, v_ind, a_ind):
        if act_index:
            del self._slots[slot_index]['activities'][act_index]['available'][v_ind]
            self.delete_option(slot_index, 'activities', act_index)
        if v_index:
            del self._slots[slot_index]['activities'][v_index]['available'][a_ind]
            self.delete_option(slot_index, 'video', v_index)
        self.delete_option(slot_index, 'audio', a_index)

    def get_option(self, slot, type, index, available=True):
        if isinstance(slot[type], str):
            return slot[type], None, True, None
        if available is None or slot[type] is None: return True, None, None, None
        if available is True:
            to_choose = slot[type]
        else:
            to_choose = []
            to_choose_list = slot[type]
            item_index = 0
            for item in available:
                if item == 'sound':
                    if type == 'video': return True, None, available, None
                    else: continue
                if isinstance(item, dict):
                    if type == 'video':
                        for key in item:
                            opt_to_choose = to_choose_list[key]
                            opt_to_choose['dict'] = item
                            opt_to_choose['name'] += " (+ %s)" % slot['audio'][key]['name']
                            break
                    else: continue
                else:
                    opt_to_choose = to_choose_list[i]
                opt_to_choose['index'] = item_index
                to_choose.append(opt_to_choose)
                item_index += 1
        self.print_options(to_choose)
        if len(to_choose) > 1:
            choosen_index = int(input("Номер опции: ")) - 1
            yes = input("Отменить? (любой символ для отмены, пустая строка для продолжения): ")
        else:
            choosen_index, yes = 0, ""
        option = to_choose[choosen_index]
        is_dict = 'dict' in option
        if not len(yes):
            self._choosen(option, type, index)
            avlb = None
            if is_dict:
                if type == 'video':
                    avlb = [option['dict']]
            elif 'available' in option:
                avlb = option['available']
                if type == 'activities' and option['audio_only']:
                    avlb.append('sound')
            return (option['name'], choosen_index, avlb, option['index'])
        else:
            return False, None, None

    def print_options(self, options):
        print("Введите номер желаемой опции:")
        index = 1
        for option in options:
            print("%i. %s" % (index, option['name']))
            index+=1

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
