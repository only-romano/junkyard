from functools import partial
try:
    from activity_class import Activity
    from activity_placeholders import THEME
except ImportError:
    from activities.activity_class import Activity
    from activities.activity_placeholders import THEME

# BASE ACTIVITY INSTANCES
default = Activity(last=False)
default_last = Activity()
sound_only = Activity(audio=None)
# basic
edu = sport = hobby = default
act = default_last
# video
tv = anime = cartoon = default_last
# audio
audio = Activity(audio=True, last=False)

# ADDITIONAL TEMPLATES
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

def prs(*args, keyname="Программирование", **kwargs):
    if len(args) and isinstance(args[0], str):
        return default("%s (%s)" % (keyname, args[0]), *args[1:], **kwargs)
    return default(keyname, *args, **kwargs)


# PARTIAL CALLS
# basic
math = partial(default, "Математика")
project = partial(prs, keyname="Проект")
sleep = partial(default, "СОН")
thought = partial(author, short=True)
# video, video_* - with sound; vid_* - without sound
movie = partial(default, "ФИЛЬМ")
video = partial(prs, keyname="Видео", short=True)
vid_theme = partial(video, THEME, short=False)
video_doc = partial(default, "Документальное видео")
video_edu = partial(default, "Видео по предмету")
video_prs = partial(default, "Видео по программированию")
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


# exported all variables
"""
__all__ = [
    'abook_novel', 'abook_short', 'act', 'anime', 'author', 'cartoon',
    'default', 'edu', 'game', 'hobby', 'math', 'movie', 'music_fresh',
    'music_hits' 'music_radio', 'music_theme', 'PLACEHOLDER', 'podcast_prs',
    'project', 'prs', 'random_broadcast', 'Randomize_and_pop_on_call',
    'randomize', 'sound_only', 'sport', 'THEME', 'thought', 'tv',
    'vid_letsplay', 'vid_theme', 'video', 'video_doc', 'video_edu',
    'video_prs', 'youtube',
    ]
"""

if __name__ == '__main__':
    print(sound_only("Hello", last=False))
    print(prs("Hello"))
    print(project(3, last=True))
    print(prs("Cat", 4, True, available=[1,2,3]))
