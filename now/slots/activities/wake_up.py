"""
 Wake up activities (until 7:00).

 Now it consist of :
 - 5 slots with constant basic/video/audio activities
 - 1 micro-slot with modular activities
"""
# import fix
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot - current - wake-up timespace slot
slot_01 = ["Wake Up", None, None, 5]

# 2-nd slot - current - wake-up-exercises slot
slot_02 = ["Зарядка", None, "Песня Дня", 5]

# 3-rd slot - current - morning shower slot
slot_03 = ["Душ", None, None, 10]

# 4-th slot - current - picker schedule file creation slot
slot_04 = ["To-Do-List на сегодня", None, None, 5]

# 5-th slot - current - materials/resources updates slot
slot_05 = ["Materials/Resources Updates", None, "Подкаст - English", 10]

# 6-th slot - current - micro-activity slot
slot_06 = [
    [   # basic activities
        ["Разминка Программиста", 5, True, [0,2,3,3,4]],
        ["Зарядка для ума (задачи)", 4, True, [2,3,3,3]],
        ["Фантазии под музыку", 2, True, [1,3], True],
        ["Фантазии под клипы", 1, True, [1]],
        AT.default("Бритьё"),
        AT.default("Стирка"),
        AT.game("Заработало!"),
    ],[ # video activities
        AT.v_prs(1),
        ["YouTube (клипы)", 1, True, None],
        ["YouTube (awesome people)", 2, True, [2,4]],
        AT.v_theme(5, [0,0,1,2,3]),
        AT.v_play([1]),
    ],[ # audio activities
        AT.ab_story(2),
        AT.m_theme(3, True),
        AT.m_hits(2),
        AT.m_fresh(2),
        AT.radio(1),
    ], 10]


# exported variable
WAKE_UP = [slot_01, slot_02, slot_03, slot_04, slot_05, slot_06]


__all__ = ['WAKE_UP']

if __name__ == '__main__':
    print(WAKE_UP)
