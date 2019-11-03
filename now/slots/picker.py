from activity_slots import *
from slots_tools import *

period = load_slots()
if period["day"] == 15:
    RESET_SLOTS(period)
    period["day"] = 0
else:
    period["day"] += 1

radio = "Радиопередача - " + ("Евгеника" if period["day"] % 3 == 0 else "Маяк")

SLOTS = [
    { "time": "06:15", "activity": ["Wake Up", None, None] },
    { "time": "06:20", "activity": ["Зарядка", None, "Песня Дня"] },
    { "time": "06:25", "activity": ["Душ", None, None] },
    { "time": "06:35", "activity": ["To-Do-List на сегодня", None, None] },
    { "time": "06:40", "activity": ["Materials/Resources Updates", None, "Подкаст - English"] },
    { "time": "06:50", "activity": get_activity(slot_01) },
    { "time": "07:00", "activity": get_activity(slot_02) },
    { "time": "07:20", "activity": ["Завтрак", "Букашки", None] },
    { "time": "07:30", "activity": get_activity(slot_03) },
    { "time": "08:00", "activity": get_activity(slot_04) },
    { "time": "08:30", "activity": ["УТРЕННЯЯ ТРЕНИРОВКА", "YouTube (тематика)", "АУДИОКНИГА - Роман"] },
    { "time": "10:00", "activity": get_activity(slot_05) },
    { "time": "10:30", "activity": get_activity(slot_06) },
    { "time": "11:00", "activity": get_activity(slot_07) },
    { "time": "11:30", "activity": get_activity(slot_08) },
    { "time": "12:00", "activity": get_activity(slot_09) },
    { "time": "12:30", "activity": get_activity(slot_10) },
    { "time": "13:00", "activity": ["СОН", None, None] },
    { "time": "13:15", "activity": get_activity(slot_11) },
    { "time": "13:30", "activity": ["Обед", None, radio] },
    { "time": "13:45", "activity": get_activity(slot_12) },
    { "time": "14:15", "activity": get_activity(slot_13) },
    { "time": "14:45", "activity": get_activity(slot_14) },
    { "time": "15:15", "activity": ["Полдник", None, radio] },
    { "time": "15:30", "activity": get_activity(slot_15) },
    { "time": "16:00", "activity": get_activity(slot_16) },
    { "time": "16:30", "activity": get_activity(slot_17) },
    { "time": "17:00", "activity": ["ВЕЧЕРНЯЯ ТРЕНИРОВКА", "YouTube (тематика)", "АУДИОКНИГА - Роман"] },
    { "time": "18:00", "activity": get_activity(slot_18) },
    { "time": "18:30", "activity": get_activity(slot_19) },
    { "time": "19:00", "activity": ["СОН", None, None] },
    { "time": "19:15", "activity": ["Ужин", None, radio] },
    { "time": "19:30", "activity": get_activity(slot_20) },
    { "time": "19:45", "activity": get_activity(slot_21) },
    { "time": "20:15", "activity": get_activity(slot_22) },
    { "time": "20:45", "activity": get_activity(slot_23) },
    { "time": "21:15", "activity": get_activity(slot_24) },
    { "time": "21:45", "activity": ["СОН", None, None] },
    { "time": "22:00", "activity": ["Ночной Ужин", None, radio] },
    { "time": "22:15", "activity": ["Душ", None, None] },
    { "time": "22:30", "activity": get_activity(slot_25) },
    { "time": "23:00", "activity": get_activity(slot_26) },
    { "time": "23:30", "activity": get_activity(slot_27) },
    { "time": "00:00", "activity": get_activity(slot_28) },
    { "time": "00:30", "activity": get_activity(slot_29) },
    { "time": "01:00", "activity": get_activity(slot_30) },
    { "time": "01:30", "activity": get_activity(slot_31) },
    { "time": "02:00", "activity": get_activity(slot_32) },
    { "time": "02:30", "activity": get_activity(slot_33) },
    { "time": "03:00", "activity": get_activity(slot_34) },
    { "time": "03:30", "activity": ["СОН", None, None] },
]

create_today_file(SLOTS)
write_slots(period)
