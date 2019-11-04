import pickle

THEME = "тематика"


# Slots constructor
def slot(name, video=[], audio=[], count=1, length=1):
    return {
        "name": name,
        "available_video": video,
        "available_audio": audio,
        "max_length": length,
        "COUNT": count,
    }

def create_slots_object(list_of_slots):
    slots = {}
    for i in range(len(list_of_slots)):
        slots[i] = {
            "activities": list_of_slots[i][0],
            "video": list_of_slots[i][1],
            "audio": list_of_slots[i][2],
            "length": list_of_slots[i][3],
        }
    return slots


# Initiator
def init_slots(file):
  slots = create_slots_object([
        [[
            slot("Разминка Программиста", video=[0,2,3,4], count=5),
            slot("Зарядка для ума (задачи)", video=[2,3], count=4),
            slot("Бритьё"),
            slot("Стирка"),
            slot("Фантазии под музыку", audio=[1,2,3,4], count=2),
            slot("Фантазии под клипы", video=[1]),
            slot("Заработало!"),
        ],[
            slot("YouTube (PRS)", length=2),
            slot("YouTube (клипы)"),
            slot("YouTube (%s)" % THEME, audio=[0,1,2,3,4], count=4, length=2),
            slot("YouTube (awesome people)", audio=[1,2,3,4], count=3),
            slot("YouTube (летсплей)", audio=[1,2,3,4], length=2),
        ],[
            slot("АУДИОКНИГА - Рассказ", count=2, length=2),
            slot("Музыка (%s)" % THEME, count=3),
            slot("Музыка (хиты)", count=2, length=2),
            slot("Музыка (новый альбом)", count=2, length=2),
            slot("Радио", length=2)
        ], 10,],
        [[
            slot("Уборка", video=[0,1,2,3,4], count=5),
            slot("Оригами", video=[0,1,2,3,4], count=2),
            slot("Новости", video=[2,3,4]),
            slot("uCrazy.ru", video=[2,3,4]),
            slot("АВТОР - Моя Вселенная"),
            slot("Бесконечное Лето", count=3),
            slot("Tempest", count=2),
        ],[
            slot("YouTube (PRS)"),
            slot("YouTube (документалка)"),
            slot("YouTube (%s)" % THEME, audio=[0,1,2,3], count=4),
            slot("YouTube (происшествия)", audio=[0,1,2,3], count=2),
            slot("YouTube (летсплей)", audio=[1,2,3]),
        ],[
        ], 20],
    ])
    return slots

print(init_slots(True)[0])

