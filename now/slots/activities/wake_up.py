"""
 Wake up activities (until 7:00).

 Now it consist of :
 - 5 slots with constant basic/video/audio activities
 - 1 micro-slot with modular activities
"""
from placeholders import THEME, default

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
        ["Разминка Программиста", 2, 5, True, [0,2,3,4], False],
        ["Зарядка для ума (задачи)", 3, 4, True, [2,3], False],
        ["Бритьё", 5, 1, True, None, True],
        ["Стирка", 5, 1, True, None, True],
            slot("Бритьё"),
            slot("Стирка"),
            slot("Фантазии под музыку", audio=[1,2,3,4], count=2),
            slot("Фантазии под клипы", video=[1]),
            slot("Заработало!"),
    ],[ # video activities
            slot("YouTube (PRS)", length=2),
            slot("YouTube (клипы)"),
            slot("YouTube (%s)" % THEME, audio=[0,1,2,3,4], count=4, length=2),
            slot("YouTube (awesome people)", audio=[1,2,3,4], count=3),
            slot("YouTube (летсплей)", audio=[1,2,3,4], length=2),
    ],[ # audio activities
            slot("АУДИОКНИГА - Рассказ", count=2, length=2),
            slot("Музыка (%s)" % THEME, count=3),
            slot("Музыка (хиты)", count=2, length=2),
            slot("Музыка (новый альбом)", count=2, length=2),
            slot("Радио", length=2)
    ], 10]

# "name": a[0], "attn": a[1], "count": a[2], "last": a[3],
# "available": a[4], "audio_only": a[5]

WAKE_UP = [slot_01, slot_02, slot_03, slot_04, slot_05, slot_06]

__all__ = ["WAKE_UP"]
