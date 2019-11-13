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
# randomizer section
a6 = AT.randomize([1,1,1,2,3,3,4])      # audio, 6th randomized
v6 = AT.randomize([2,2,3,3,3,4])        # video, 6th randomized
#print(a6, v6)
# slot
slot_06 = [
    [   # basic activities
        AT.act("Разминка Программиста", 5, available=[{3:0},{3:0},0,v6(),v6()]),
        AT.act("Зарядка для ума (задачи)", 4, available=[v6(),v6(),v6(),v6()]),
        AT.sound_only("Фантазии под музыку", 2, available=[a6(),a6()]),
        AT.act("Фантазии под клипы", available=[1]),
        AT.act("Бритьё"),
        AT.act("Стирка"),
        AT.game("Заработало!", short=True),
    ],[ # video activities
        AT.video_prs(),
        AT.video("Клипы"),
        AT.youtube("Awesome People", 2, available=[a6(),a6()]),
        AT.vid_theme(5, available=[{0:3},{0:3},2,a6(),a6()]),
        AT.vid_letsplay(available=[a6()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_theme(3, last=True),
        AT.music_fresh(2),
        AT.music_hits(2),
        AT.music_radio(),
    ], 10]


# exported variable
WAKE_UP = [slot_01, slot_02, slot_03, slot_04, slot_05, slot_06]


__all__ = ['WAKE_UP']

if __name__ == '__main__':
    print(WAKE_UP)
