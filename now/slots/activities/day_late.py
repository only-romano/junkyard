"""
Late daytime activities (until evening siesta [not included, 15:30 - 19:00])

 Now it consist of:
 - 3 standard slots
 - constant Evening Training 1h slot
 - 2 standard slots
"""
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of module (25th at all) - current - standard slot
# randomizer
a25 = AT.randomize([2,3,3,3])         # audio, 25th slot, randomized
v25 = AT.randomize([3,4,4,5])         # video, 25th slot, randomized
# slot
slot_25 = [
    [   # basic activities
        AT.prs(6, available=[{3:0},0,0,0,1,1]),
        AT.project("My Little Life", 2, available=[0, v25()], last=True),
        AT.math(available=[v25()]),
        AT.edu("Физика", available=[v25()]),
        AT.hobby("Создание Музыки", available=[2]),
        AT.author("Рассказ"),
        AT.game(AT.GAME_COMPLEX, 3, available=[{3:1},0,v25()], last=True),
    ],[ # video activities
        AT.movie(5),
        AT.video_prs(2),
        AT.video("Создание музыки"),
        AT.vid_theme(3, available=[{0:3},{1:3},a25()]),
        AT.youtube("Война", 2, available=[a25(),a25()]),
        AT.vid_letsplay(available=[a25()]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_theme(),
        AT.music_hits(3),
    ], 30] # length


# 2-nd slot of module (26th at all) - current - standard slot
# randomizer
a26 = AT.randomize([2,3,4])         # audio, 26th slot, randomized
v26 = AT.randomize([0,4,5])         # video, 26th slot, randomized
v26e = AT.randomize([2,4])          # educational video / music
# slot
slot_26 = [
    [   # basic activities
        AT.sport("ВЕЧЕРНЯЯ ТРЕНИРОВКА", available=[{3:0}]),
        AT.prs(6, available=[{3:0},0,0,0,1,1]),
        AT.math(available=[v26e()]),
        AT.edu("Физика", available=[v26e()]),
        AT.hobby("Создание Музыки", available=[v26()], last=True),
        AT.author("Рассказ"),
        AT.game(AT.GAME_BRAIN, 4, available=[{3:1},0,v26(),v26()], short=True),
    ],[ # video activities
        AT.movie(5),
        AT.video_prs(2, last=True),
        AT.video_edu(),
        AT.vid_theme(4, available=[{0:3},{0:3},{1:3},a26()]),
        AT.youtube("Стимпанк", available=[a26()]),
        AT.vid_letsplay(available=[a26()]),
    ],[ # audio activities
        AT.abook_novel(2),
        AT.abook_short(),
        AT.music_theme(last=True),
        AT.music_hits(),
        AT.music_radio(),
    ], 30] # length


# 3-rd slot of module (27th at all) - current - standard slot
# randomizer
a27 = AT.randomize([2,3])           # audio, 27th slot, randomized
v27 = AT.randomize([0,5,6])         # video, 27th slot, randomized
v27e = AT.randomize([0,1,4])        # movie / educational video / music
# slot
slot_27 = [
    [   # basic activities
        AT.sport("ВЕЧЕРНЯЯ ТРЕНИРОВКА", 6, available=[2,2,2,2,2,2]),
        AT.prs(1, available=[v27()], last=True),
        AT.math(available=[v27e()], last=True),
        AT.edu("Физика", available=[v27e()], last=True),
        AT.edu("Экономика", available=[v27e()], last=True),
        AT.author("Рассказ", last=True),
        AT.game(AT.GAME_BRAIN, 4, available=[0,3,v27(),v27()], short=True),
    ],[ # video activities
        AT.movie(3, last=True),
        AT.video_edu(last=True),
        AT.vid_theme(6, available=[0,0,0,0,0,0]),
        AT.youtube("Море", available=[1]),
        AT.youtube("Дружба", available=[a27()]),
        AT.youtube("Еда", available=[0]),
        AT.vid_letsplay(available=[a27()], last=True),
    ],[ # audio activities
        AT.abook_novel(7),
        AT.abook_short(last=True),
        AT.music_hits(last=True),
        AT.music_radio(last=True),
    ], 30] # length


# 4-th slot of module (28th at all) - current - evening training slot
slot_28 = ["ВЕЧЕРНЯЯ ТРЕНИРОВКА", "Видео (%s)" % AT.THEME, "АУДИОКНИГА - Роман", 60]


# 5-st slot of module (29th at all) - current - standard slot
# randomizer
a29 = AT.randomize([1,1,2,3])           # audio, 29th slot, randomized
v29 = AT.randomize([4,5,6])             # video, 29th slot, randomized
v29h = AT.randomize([{4:0},0,4])        # tv / audiobook / music
# slot
slot_29 = [
    [   # basic activities
        AT.sport("ВЕЧЕРНЯЯ ТРЕНИРОВКА", 3, available=[{4:0},{4:0},{4:0}]),
        AT.prs(3, available=[1,1,v29h()]),
        AT.project("Academy", 3, available=[v29(),v29(),v29h()]),
        AT.math(2, available=[2,v29()]),
        AT.act("Ремонт", available=[v29h()],long=True),
        AT.hobby("Фокусы", available=[3]),
        AT.game(AT.GAME_NOVEL, 2),
    ],[ # video activities
        AT.tv("Новенькая"),
        AT.video_prs(2),
        AT.video_edu(),
        AT.video("Фокусы"),
        AT.vid_theme(6, available=[{0:4},{0:4},{0:4},{0:4},a29(),a29()]),
        AT.youtube("СССР", available=[a29()]),
        AT.vid_letsplay(available=[a29()]),
    ],[ # audio activities
        AT.abook_novel(4),
        AT.music_theme(2),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 6-st slot of module (30th at all) - current - standard slot
# randomizer
a30 = AT.randomize([1,1,2,3])       # audio, 30th slot, randomized
v30 = AT.randomize([4,5,6])         # video, 30th slot, randomized
v30h = AT.randomize([0,4])          # tv / audiobook / music
# slot
slot_30 = [
    [   # basic activities
        AT.prs(5, available=[{4:0},{4:0},1,1,v30h()], last=True),
        AT.project("Academy", 3, available=[v30(),v30(),v30h()]),
        AT.math(2, available=[2,v30()], last=True),
        AT.act("Ремонт", available=[3]),
        AT.hobby("Фокусы", available=[{4:0}], last=True),
        AT.thought("Об Идеальном Партнёре"),
        AT.game(AT.GAME_NOVEL, 2, last=True),
    ],[ # video activities
        AT.tv("Новенькая"),
        AT.video_prs(2, last=True),
        AT.video_edu(last=True),
        AT.video("Ремонт"),
        AT.vid_theme(5, available=[{0:4},{0:4},{0:4},a30(),a30()], last=True),
        AT.youtube("Спорт", available=[a30()]),
        AT.vid_letsplay(available=[a30()], last=True),
    ],[ # audio activities
        AT.abook_novel(3, last=True),
        AT.music_theme(2, last=True),
        AT.music_fresh(last=True),
        AT.music_hits(last=True),
    ], 30] # length


# exported variable
LATEDAY = [slot_25, slot_26, slot_27, slot_28, slot_29, slot_30]


__all__ = ["LATEDAY"]

if __name__ == '__main__':
    print(LATEDAY)
