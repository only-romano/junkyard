"""
Midday activites (until second dinner [included, 13:00 - 15:30])

 Now it consist of:
 - SLEEP slot
 - micro-activity slot
 - dinner slot
 - 3 standard slots
 - second dinner slot
"""
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of module (18th at all) - current - SLEEP slot
slot_18 = ["СОН", None, None, 15]


# 2-nd slot of module (19th at all) - current - micro-activity slot
# randomizer
a19 = AT.randomize([1,2,2,2,3,3,3,3,3])     # audio, 19th slot, randomized
v19 = AT.randomize([0,3,3,3,3,5])           # video, 19th slot, randomized
v19d = AT.randomize([2,4])                  # clips / dance videos
# slot
slot_19 = [
    [   # basic activities
        AT.sport("РАЗМИНКА", 5, available=[v19(),v19(),v19(),v19(),v19d()]),
        AT.sound_only("Готовка", available=[0,a19()]),
        AT.act("Танцы", available=[1,2,4,4,v19d()]),
        AT.act("Ощущение Своего Тела"),
        AT.game(AT.GAME_RELAX, 2, available=[v19(),v19()], short=True),
    ],[ # video activities
        AT.cartoon('По другую сторону изгороди'),
        AT.video("Хореография"),
        AT.video("Клипы", 2),
        AT.vid_theme(4, available=[a19(),a19(),a19(),a19()]),
        AT.youtube("Танцы", 3, available=[a19(),a19(),a19()]),
        AT.vid_letsplay(available=[a19()]),
    ],[ # audio activities
        AT.abook_short(),
        AT.music_theme(),
        AT.music_hits(3, last=True),
        AT.music_radio(5, last=True),
    ], 15] # length


# 3-rd slot of module (20th at all) - current - DINNER slot
slot_20 = ["Обед", None, "radiobroadcast", 15]


# 4-th slot of module (21th at all) - current - standard slot
# randomizer
a21 = AT.randomize([1,2,3])         # audio, 21th slot, randomized
v21 = AT.randomize([1,5,6])         # anime / youtube / letsplay
v21d = AT.randomize([3,3,4])        # educational videos / music
# slot
slot_21 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v21()]),
        AT.project("My Little Life", 2, available=[0, v21()]),
        AT.edu("История", available=[v21d()]),
        AT.edu("Биология", available=[v21d()]),
        AT.edu("Химия", available=[v21d()]),
        AT.thought("О Музыке"),
        AT.game(AT.GAME_COMPLEX, 3, available=[{4:0},0,v21()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime('Код ГИАС R2'),
        AT.video_prs(),
        AT.video_edu(2),
        AT.vid_theme(3, available=[{0:4},{0:4},a21()]),
        AT.youtube("Медицина", available=[a21()]),
        AT.vid_letsplay(available=[a21()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 5-th slot of module (22th at all) - current - standard slot
# randomizer
a22 = AT.randomize([1,2,3])         # audio, 22th slot, randomized
v22 = AT.randomize([1,5,6])         # anime / youtube / letsplay
v22d = AT.randomize([3,3,4])        # educational videos / music
# slot
slot_22 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v22()]),
        AT.project("My Little Life", 2, available=[0, v22()]),
        AT.edu("История", available=[v22d()]),
        AT.edu("Биология", available=[v22d()], last=True),
        AT.edu("Химия", available=[v22d()], last=True),
        AT.thought("Об Актёрстве"),
        AT.game(AT.GAME_COMPLEX, 3, available=[{4:0},0,v22()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime('Код ГИАС R2'),
        AT.video_prs(),
        AT.video_edu(2),
        AT.vid_theme(3, available=[{0:4},{0:4},a22()]),
        AT.youtube("Природа", available=[a22()]),
        AT.vid_letsplay(available=[a22()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (23th at all) - current - standard slot
# randomizer
a23 = AT.randomize([1,2,3])         # audio, 23th slot, randomized
v23 = AT.randomize([1,5,6])         # anime / youtube / letsplay
v23d = AT.randomize([3,3,4])        # educational videos / music
# slot
slot_23 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v23()]),
        AT.project("My Little Life", 2, available=[0, v23()]),
        AT.edu("История", available=[v23d()], last=True),
        AT.edu("Социология", available=[v23d()], last=True),
        AT.edu("Обществознание", available=[v23d()], last=True),
        AT.thought("О Путешествиях"),
        AT.game(AT.GAME_COMPLEX, 3, available=[{4:0},0,v23()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime('Код ГИАС R2'),
        AT.video_prs(),
        AT.video_edu(2, last=True),
        AT.vid_theme(3, available=[{0:4},{0:4},a23()]),
        AT.youtube("Путешествия", available=[a23()]),
        AT.vid_letsplay(available=[a23()]),
    ],[ # audio activities
        AT.abook_short(2, last=True),
        AT.music_theme(),
        AT.music_fresh(last=True),
        AT.music_hits(),
    ], 30] # length


# 7-th slot of module (24th at all) - current - second DINNER slot
slot_24 = ["Полдник", None, "radiobroadcast", 15]


# exported variable
MIDDAY = [slot_18, slot_19, slot_20, slot_21, slot_22, slot_23, slot_24]


__all__ = ["MIDDAY"]

if __name__ == '__main__':
    print(MIDDAY)
