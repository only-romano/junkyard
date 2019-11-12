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


# 1-st slot - current - mini-activity slot
slot_07 = [
    [   # basic activities
        ["Уборка", 5, True, [0,1,2,3,4]],
        ["Оригами", 2, True, [2,3]],
        ["Новости", 1, True, [2]],
        ["uCrazy.ru", 1, True, [2]],
        AT.default("АВТОР - Моя Вселенная"),
        AT.game("Бесконечное Лето", 3),
        AT.game("Tempest", 2),
    ],[ # video activities
        AT.v_prs(1),
        AT.v_doc(1),
        AT.v_theme(4, [0,0,1,2]),
        ["YouTube (происшествия)", 2, True, [2,3]],
        AT.v_play([1]),
    ],[ # audio activities   []
        AT.ab_story(2),
        AT.m_hits(2),
        AT.m_fresh(2),
        AT.radio(1),
    ], 20] # length

# 2-nd slot - current - breakfast slot
slot_08 = ["Завтрак", "Букашки", None, 10]

x=1
# 3-rd slot - current - standard slot
slot_09 = [
    [   # basic activities
        ["PRS (закрепление пройденного)", 5, True, [x,x,x,x,x]],
        ["PRS (идеи для проектов)", 1, False, [x]],
        ["Математика", 1, False, [x]],
        ["Физика", 1, False, [x]],
        AT.default("АВТОР - О личном здоровье"),
        ["Car Mechanic Simulator (с фоном)", 4, False, [x,x,x,x]],
        ["Car Mechanic Simulator", 2, False, None],
    ],[ # video activities
        AT.movie('Код "ГИАС" R2'),
        AT.v_prs(2),
        AT.v_edu(1, True),
        AT.v_doc(1),
        AT.v_theme(4, [x,x,x,x]),
        ["YouTube (подборки)", 2, True, [x,x]],
        AT.v_play([x]),
    ],[ # audio activities   []
        AT.ab_roman(1),
        AT.ab_story(1),
        AT.a_prs(1),
        AT.m_theme(1),
        AT.m_hits(1),
        AT.m_fresh(1),
        AT.radio(1),
    ], 30] # length

# 4-th slot - current - standard slot
slot_10 = [
    [   # basic activities
        AT.train_m(3, [4,4,4]),
        ["PRS (новый язык)", 5, True, [x,x,x,x,x]],
        ["PRS (идеи для проектов)", 1, True, [x]],
        ["Математика", 1, True, [x]],
        ["Физика", 1, True, [x]],
        AT.default("АВТОР - О борьбе с агорафобией"),
        ["Car Mechanic Simulator (с фоном)", 3, True, [x,x,x]],
    ],[ # video activities
        AT.movie('Новенькая'),
        AT.v_prs(2, True),
        AT.v_doc(1, True),
        ["YouTube (клипы)", 1, True, None],
        AT.v_theme(6, [0,0,0,x,x,x]),
        ["YouTube (красота)", 2, True, [x,x]],
        AT.v_play([x], True),
    ],[ # audio activities   []
        AT.ab_roman(3),
        AT.ab_story(1, True),
        AT.a_prs(1, True),
        AT.m_theme(1, True),
        AT.m_hits(1, True),
        AT.m_fresh(1, True),
        AT.radio(1, True),
    ], 30] # length

# 5-th slot - current - morning training slot
slot_11 = ["УТРЕННЯЯ ТРЕНИРОВКА", "YouTube (%s)" % AT.THEME, "АУДИОКНИГА - Роман", 90]


# exported variable
MORNING = [slot_07, slot_08, slot_09, slot_10, slot_11]


__all__ = ["MORNING"]

if __name__ == '__main__':
    print(MORNING)
