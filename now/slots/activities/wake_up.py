"""
 Wake up activities (until 7:00).

 Now it consist of :
 - 5 slots with constant basic/video/audio activities
 - 1 micro-slot with modular activities
"""
from random import sample
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
# shuffles section
v6 = sample([2,3,3,3,3,4], 6)       # 6-th slot video shuffle
a6 = sample([1,1,1,2,2,3,3,4], 8)   # 6-th slot audio shuffle
#print(v6, a6)
# slot
slot_06 = [
    [   # basic activities
        ["Разминка Программиста", 5, True, [0,2,3,v6[0],v6[1]]],
        ["Зарядка для ума (задачи)", 4, True, [v6[2],v6[3],v6[4],v6[5]]],
        ["Фантазии под музыку", 2, True, [a6[0],a6[1]], True],
        AT.act("Фантазии под клипы", last=True, available=[1]),
        AT.default("Бритьё"),
        AT.default("Стирка"),
        AT.game("Заработало!"),
    ],[ # video activities
        AT.v_prs(),
        AT.video("YouTube (клипы)"),
        AT.video("YouTube (awesome people)", 2, available=[a6[2],a6[3]]),
        AT.v_theme(5, available=[0,0,a6[4],a6[5],a6[6]]),
        AT.v_play(available=[a6[7]]),
    ],[ # audio activities
        AT.ab_story(2),
        AT.m_theme(3, last=True),
        AT.m_hits(2),
        AT.m_fresh(2),
        AT.radio(),
    ], 10]


# exported variable
WAKE_UP = [slot_01, slot_02, slot_03, slot_04, slot_05, slot_06]


__all__ = ['WAKE_UP']

if __name__ == '__main__':
    print(WAKE_UP)
