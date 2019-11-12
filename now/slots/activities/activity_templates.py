from functools import partial

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
                # available consist of audio, not video
                result.append(True)

        return result


# BASE ACTIVITY INSTANCES
# basic
default = Activity(last=False)
default_last = Activity()
sound_only = Activity(audio=None)
edu = sport = hobby = game = default
act = default_last
# video
movie = default
video = tv = anime = cartoon = default_last
# audio
audio = Activity(audio=True, last=False)

# ADDITIONAL TEMPLATES
def prs(*args, keyname="Программирование", **kwargs):
    if len(args) and isinstance(args[0], str):
        return default("%s (%s)" % (keyname, args[0]), *args[1:], **kwargs)
    return default(keyname, *args, **kwargs)

def author(*args, **kwargs):
    return default('АВТОР - "%s"' % args[0], *args[1:], **kwargs)

# PARTIAL CALLS
# basic
project = partial(prs, keyname="Проект")
thought = partial(author, short=True)
math = partial(default, "Математика")
# video, video_* - with sound; vid_* - without sound
video_prs = partial(default, "Видео по программированию")
video_edu = partial(default, "Видео по предмету")
video_doc = partial(default, "Документальное видео")
vid_theme = partial(default, "YouTube (%s)" % THEME)
vid_letsplay = partial(default, "YouTube (летсплей)")
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
    'project', 'prs', 'sport', 'THEME', 'thought', 'tv', 'vid_letsplay',
    'vid_theme', 'video', 'video_doc', 'video_edu', 'video_prs',
    ]

if __name__ == '__main__':
    print(sound_only("Hello", last=False))
    print(prs("Hello"))
    print(project(3, last=True))
    print(prs("Cat", 4, True, available=[1,2,3]))
