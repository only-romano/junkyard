"""
Morning activities (until morning training min-finish time [07:00 - 10:00])

 Now it consist of :
 - 1 micro-slot with modular activities
 - constant Breakfast slot
 - 2 standard slots
 - constant Morning Training 1.5 h slot
"""
# import fix
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of the module (7th at all) - current - mini-activity slot
# randomizer section
a7 = AT.randomize([1,2,2,3])         # audio, 7th slot randomized
v7 = AT.randomize([2,2,3,3,4])       # video, 7th slot randomized
# slot
slot_07 = [
    [   # basic activities
        AT.act("Уборка", 5, available=[{3:0},0,1,v7(),v7()]),
        AT.hobby("Оригами", 2, last=True, available=[{3:0},v7()]),
        AT.act("Новости", available=[v7()]),
        AT.act("uCrazy.ru", available=[v7()]),
        AT.author("Моя Вселенная", short=True),
        AT.game("Бесконечное Лето", 3, short=True),
        AT.game("Tempest", 2, short=True),
    ],[ # video activities
        AT.video_prs(),
        AT.video_doc(),
        AT.youtube("Происшествия", 2, available=[a7(),a7()]),
        AT.vid_theme(4, available=[{0:3},{0:3},1,a7()]),
        AT.vid_letsplay(available=[a7()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_fresh(2),
        AT.music_hits(2),
        AT.music_radio(1),
    ], 20] # length


# 2-nd slot of module (8th at all) - current - breakfast slot
slot_08 = ["Завтрак", "Букашки", None, 10]


# 3-rd slot of module (9th at all) - current - standard slot
# randomizer
a9 = randomize([2,3,4,5,6])         # audio, 9th slot randomized
v9 = randomize([3,4,4,4,5,5,6])     # video, 9th slot randomized
v9e = randomize([2,4])              # educational video, 9th slot randomized
# slot
slot_09 = [
    [   # basic activities
        AT.prs("Повторение", 5, last=True, available=[x,x,x,x,x]),
        AT.prs("Идеи для Проектов", available=[x]),
        AT.math(available=[v9e()]),
        AT.edu("Физика", available=[v9e()]),
        AT.thought("О личном здоровье"),
        AT.game("Car Mechanic Simulator (с фоном)", 4, short=True, available=[x,x,x,x]),
        AT.game("Car Mechanic Simulator", 2, short=True),
    ],[ # video activities
        AT.anime('Код "ГИАС" R2'),
        AT.video_prs(2),
        AT.video_edu(last=True),
        AT.video_doc(),
        AT.vid_theme(4, available=[x,x,x,x]),
        AT.youtube("Подборка", 2, available=[x,x]),
        AT.vid_letsplay(available=[x]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.podcast_prs(),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
        AT.music_radio(),
    ], 30] # length


# 4-th slot of module (10th at all) - current - standard slot
# randomizer
a10 = sample([2,3,4,5,6], 5)        # 10-th slot audio shuffle
v10s = sample([4,4,5,6], 4)         # 10-th slot simple video shuffle
v10h = sample([2,3,4,5], 4)         # 10-th slot high-attention video shuffle
# slot
slot_10 = [
    [   # basic activities
        AT.train_m(3, [4,4,4]),
        ["PRS (новый язык)", 5, True, [1,1,v10h[0],v10s[0],v10s[1]]],
        ["PRS (идеи для проектов)", 1, True, [v10h[1]]],
        ["Математика", 1, True, [v10s[2]]],
        ["Физика", 1, True, [v10s[3]]],
        AT.default("АВТОР - О борьбе с агорафобией"),
        ["Car Mechanic Simulator (с фоном)", 3, True, [0,v10h[2],v10h[3]]],
    ],[ # video activities
        AT.movie('Новенькая'),
        AT.v_prs(2, True),
        AT.v_doc(1, True),
        ["YouTube (клипы)", 1, True, None],
        AT.v_theme(6, [0,0,0,1,a10[0],a10[1]]),
        ["YouTube (красота)", 2, True, [a10[2],a10[3]]],
        AT.v_play([a10[4]], True),
    ],[ # audio activities   [0,0,0,1]
        AT.ab_roman(3),
        AT.ab_story(1, True),
        AT.a_prs(1, True),
        AT.m_theme(1, True),
        AT.m_hits(1, True),
        AT.m_fresh(1, True),
        AT.radio(1, True),
    ], 30] # length


# 5-th slot of module (11th at all) - current - morning training slot
slot_11 = ["УТРЕННЯЯ ТРЕНИРОВКА", "YouTube (%s)" % AT.THEME, "АУДИОКНИГА - Роман", 90]


# exported variable
MORNING = [slot_07, slot_08, slot_09, slot_10, slot_11]


__all__ = ["MORNING"]

if __name__ == '__main__':
    print(MORNING)
