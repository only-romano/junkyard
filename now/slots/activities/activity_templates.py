from functools import partial
from random import sample, randint

# PLACEHOLDERS
PLACEHOLDER = ["Activity", "Video", "Audio", 30]    # for unfilled slots
THEME = "тематика"                                  # current theme

# BASE ACTIVITY CLASS
class Activity:
    """
    Callable activity constructor
    usage
    activity = Activity(params)
    act1 = activity("Activity 1", *args, **kwargs)
    act2 = activity("Activity 2", *args, **kwargs)

    constructor returns list as:
    [name{str}, count{int}, last{bool} (, available{list}, sound_only{bool})]
    """
    # long is alias for "not last", short is alias for "last"
    def __init__(self, name=None, count=1, last=True, available=None, audio=False):
        self.name = name
        # count of unused activities
        self.count = count
        # last in line (if "True", next slot will not advice to continue)
        self.last = last
        # list of available video/audio
        self.available = available
        # if "True" - it is an audio, if "None" - it is audio-only basic activity
        self.audio = audio

    def __call__(self, *args, **kwargs):
        name, count, last, available = [None]*4
        # looking for unnamed args for a specific type
        for arg in args:
            if   isinstance(arg, str):
                name = arg
            elif isinstance(arg, bool):
                # fix-upped because isinstance(True, int) is True
                last = arg
            elif isinstance(arg, int):
                count = arg
            elif isinstance(arg, (list)):
                available = arg

        # order is - kwargs -> args -> default value, 'till first match
        name = 'name' in kwargs and kwargs['name'] or name or self.name
        count = 'count' in kwargs and kwargs['count'] or count or self.count

        if 'last' in kwargs:
            last = kwargs['last']
        elif 'long' in kwargs:
            last = not kwargs['long']
        elif 'short' in kwargs:
            last = kwargs['short']
        elif last == None:
            last = self.last

        result = [name, count, last]
        if not self.audio:
            # if not audio, adds availables param
            av_kwarg = 'available' in kwargs and kwargs['available']
            available = av_kwarg or available or self.available
            result.append(available)
            if self.audio == None:
                # flag for audio only basic activities
                # the "available" of this element consist of audio, not video
                result.append(True)

        return result


# Randomizer for available lists
class Randomize_and_pop_on_call:
    # created only to ease-up code a little
    def __init__(self, array):
        self.array = sample(array, len(array))

    def __call__(self):
        return self.array.pop() if len(self.array) else None

# alias
randomize = Randomize_and_pop_on_call


# random radio
random_broadcast = "Евгеника" if randint(1, 4) == 1 else "Маяк"


# BASE ACTIVITY INSTANCES
# basic
default = Activity(last=False)
default_last = Activity()
sound_only = Activity(audio=None)
edu = sport = hobby = default
act = default_last
# video
tv = anime = cartoon = default_last
# audio
audio = Activity(audio=True, last=False)

# ADDITIONAL TEMPLATES
def prs(*args, keyname="Программирование", **kwargs):
    if len(args) and isinstance(args[0], str):
        return default("%s (%s)" % (keyname, args[0]), *args[1:], **kwargs)
    return default(keyname, *args, **kwargs)

def author(*args, **kwargs):
    return default('АВТОР - "%s"' % args[0], *args[1:], **kwargs)

def game(*args, **kwargs):
    count = 1
    for arg in args:
        if isinstance(arg, int) and arg > 1:
            count = arg
            break
    only_game = count
    ambient = 0
    if 'available' in kwargs:
        length = len(kwargs['available'])
        only_game -= length
        ambient += length
        ambient = default(args[0]+" (с фоном)",*args[1:],**kwargs,count=ambient)
        del kwargs['available']
    if only_game > 0:
        only_game = default(*args, **kwargs, count=only_game, available=None)
        return (ambient, only_game) if ambient else only_game
    return ambient


# PARTIAL CALLS
# basic
project = partial(prs, keyname="Проект")
thought = partial(author, short=True)
math = partial(default, "Математика")
# video, video_* - with sound; vid_* - without sound
movie = partial(default, "ФИЛЬМ")
video_prs = partial(default, "Видео по программированию")
video_edu = partial(default, "Видео по предмету")
video_doc = partial(default, "Документальное видео")
video = partial(prs, keyname="Видео", short=True)
vid_theme = partial(video, THEME, short=False)
youtube = partial(prs, keyname="YouTube", short=True)
vid_letsplay = partial(youtube, "летсплей", short=False)
# audio
abook_novel = partial(audio, "АУДИОКНИГА - Роман")
abook_short = partial(audio, "АУДИОКНИГА - Рассказ")
podcast_prs = partial(audio, "Подкаст по программированию")
music_theme = partial(audio, "Музыка (%s)" % THEME)
music_fresh = partial(audio, "Музыка (свежий альбом)")
music_hits = partial(audio, "Музыка (хиты)")
music_radio = partial(audio, "Радио")


__all__ = [
    'abook_novel', 'abook_short', 'act', 'anime', 'author', 'cartoon',
    'default', 'edu', 'game', 'hobby', 'math', 'movie', 'music_fresh',
    'music_hits' 'music_radio', 'music_theme', 'PLACEHOLDER', 'podcast_prs',
    'project', 'prs', 'random_broadcast', 'Randomize_and_pop_on_call',
    'randomize', 'sound_only', 'sport', 'THEME', 'thought', 'tv',
    'vid_letsplay', 'vid_theme', 'video', 'video_doc', 'video_edu',
    'video_prs', 'youtube',
    ]

if __name__ == '__main__':
    print(sound_only("Hello", last=False))
    print(prs("Hello"))
    print(project(3, last=True))
    print(prs("Cat", 4, True, available=[1,2,3]))
    # randomizer check
    ar = Randomize_and_pop_on_call([1,2,3,4,5])
    print(ar(), ar(), ar(), ar(), ar(), ar())
