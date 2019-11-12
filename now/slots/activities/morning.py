"""
Morning activities (until morning training min-finish time [07:00 - 10:00])

 Now it consist of :
 - 1 micro-slot with modular activities
 - constant Breakfast slot
 - 2 standard slots
 - constant Morning Training 1.5 h slot
"""
from random import sample
# import fix
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of module (7th at all) - current - mini-activity slot
# shuffles section
v7 = sample([2,2,2,3,3,4], 6)       # 7-th slot video shuffle
a7 = sample([1,1,2,2,3], 5)         # 7-th slot audio shuffle
# slot
slot_07 = [
    [   # basic activities
        ["Уборка", 5, True, [0,1,2,v7[0],v7[1]]],
        ["Оригами", 2, True, [v7[2],v7[3]]],
        ["Новости", 1, True, [v7[4]]],
        ["uCrazy.ru", 1, True, [v7[5]]],
        AT.default("АВТОР - Моя Вселенная"),
        AT.game("Бесконечное Лето", 3),
        AT.game("Tempest", 2),
    ],[ # video activities
        AT.v_prs(1),
        AT.v_doc(1),
        AT.v_theme(4, [0,0,a7[0],a7[1]]),
        ["YouTube (происшествия)", 2, True, [a7[2],a7[3]]],
        AT.v_play([a7[4]]),
    ],[ # audio activities   []
        AT.ab_story(2),
        AT.m_hits(2),
        AT.m_fresh(2),
        AT.radio(1),
    ], 20] # length


# 2-nd slot of module (8th at all) - current - breakfast slot
slot_08 = ["Завтрак", "Букашки", None, 10]


# 3-rd slot of module (9th at all) - current - standard slot
# shuffles
a9 = sample([2,3,4,5,6], 5)         # 9-th slot audio shuffle
v9 = sample([3,4,4,4,5,5,6], 7)     # 9-th slot video shuffle
v9e = sample([2,4], 2)              # 9-th slot educational shuffle
# slot
slot_09 = [
    [   # basic activities
        ["PRS (закрепление пройденного)", 5, True, [1,1,v9[0],v9[1],v9[2]]],
        ["PRS (идеи для проектов)", 1, False, [v9[3]]],
        ["Математика", 1, False, [v9e[0]]],
        ["Физика", 1, False, [v9e[1]]],
        AT.default("АВТОР - О личном здоровье"),
        ["Car Mechanic Simulator (с фоном)", 4, False, [0,v9[4],v9[5],v9[6]]],
        ["Car Mechanic Simulator", 2, False, None],
    ],[ # video activities
        AT.movie('Код "ГИАС" R2'),
        AT.v_prs(2),
        AT.v_edu(1, True),
        AT.v_doc(1),
        AT.v_theme(4, [0,1,a9[0],a9[1]]),
        ["YouTube (подборки)", 2, True, [a9[2],a9[3]]],
        AT.v_play([a9[4]]),
    ],[ # audio activities
        AT.ab_roman(1),
        AT.ab_story(1),
        AT.a_prs(1),
        AT.m_theme(1),
        AT.m_hits(1),
        AT.m_fresh(1),
        AT.radio(1),
    ], 30] # length


# 4-th slot of module (10th at all) - current - standard slot
# shuffles
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
