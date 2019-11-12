"""
Early daytime activities (until midday siesta [not included, 10:00 - 13:00])

 Now it consist of:
 - 6 standard slots
"""
from random import sample
# import fix
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-th slot of module (12th at all) - current - standard slot
# shuffles
a12 = sample([2,3,4,5,6], 5)        # 10-th slot audio shuffle
v12s = sample([4,4,5,6], 4)         # 10-th slot simple video shuffle
v12h = sample([2,3,4,5], 4)         # 10-th slot high-attention video shuffle
x=1
# slot
slot_12 = [
    [   # basic activities
        AT.train_m(4, [3,3,4,4]),
        AT.prs_l(2, [x,x]),
        AT.prs_p("PyMath", 3, [x,x,x]),
        AT.act("Компьютерное железо", [x]),
        AT.act("Поделки", [x]),
        AT.default("АВТОР - Новелла"),
        AT.game("Grim Fandango", 3)
        ["PRS (новый язык)", 5, True, [1,1,v10h[0],v10s[0],v10s[1]]],
        ["PRS (идеи для проектов)", 1, True, [v10h[1]]],
        ["Математика", 1, True, [v10s[2]]],
        ["Физика", 1, True, [v10s[3]]],
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


# 2-th slot of module (13th at all) - current - standard slot
slot_13 = AT.PLACEHOLDER


# 3-th slot of module (14th at all) - current - standard slot
slot_14 = AT.PLACEHOLDER


# 4-th slot of module (15th at all) - current - standard slot
slot_15 = AT.PLACEHOLDER


# 5-th slot of module (16th at all) - current - standard slot
slot_16 = AT.PLACEHOLDER


# 6-th slot of module (17th at all) - current - standard slot
slot_17 = AT.PLACEHOLDER


# exported variable
EARLY_DAY = [slot_12, slot_13, slot_14, slot_15, slot_16, slot_17]


__all__ = ["EARLY_DAY"]

if __name__ == '__main__':
    print(EARLY_DAY)
