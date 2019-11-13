"""
Early daytime activities (until midday siesta [not included, 10:00 - 13:00])

 Now it consist of:
 - 6 standard slots
"""
# import fix
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of module (12th at all) - current - standard slot
# randomizer
a12 = AT.randomize([1,2,2])         # audio, 12th slot, randomized
v12 = AT.randomize([1,4,6])         # video, 12th slot, randomized
v12x = AT.randomize([5,0])          # porn/prs video
# slot
slot_12 = [
    [   # basic activities
        AT.sport("УТРЕННЯЯ ТРЕНИРОВКА", 4, [3,3,3,3]),
        AT.prs(2, available=[0,v12x()]),
        AT.project("PyMath", 3, available=[v12(),v12(),v12x()]),
        AT.hobby("Hardware", available=[2]),
        AT.hobby("Поделки", available=[v12()]),
        AT.author("Новелла"),
        AT.game("Grim Fandango", 3),
    ],[ # video activities
        AT.video_prs(2),
        AT.video_doc(1),
        AT.video("Hardware"),
        AT.vid_theme(4, available=[0,0,0,0]),
        AT.youtube("Девушки", available=[a12()]),
        AT.video("X-Rated", available=[a12()]),
        AT.vid_letsplay(available=[a12()]),
    ],[ # audio activities
        AT.abook_novel(4),
        AT.music_fresh(),
        AT.music_hits(2),
    ], 30] # length


# 2-nd slot of module (13th at all) - current - standard slot
# randomizer
a13 = AT.randomize([1,2,2])         # audio, 13th slot, randomized
v13 = AT.randomize([2,4,5,6])       # video, 13th slot, randomized
v13t = AT.randomize([0,1])          # tv/prs video
# slot
slot_13 = [
    [   # basic activities
        AT.sport("УТРЕННЯЯ ТРЕНИРОВКА", 3, [{4:0},{4:0},{4:0}], last=True),
        AT.prs(3, available=[1,v13(),v13t()]),
        AT.project("PyMath", 3, available=[v13(),v13(),v13t()]),
        AT.hobby("Hardware", available=[v13()], last=True),
        AT.hobby("Поделки", available=[3], last=True),
        AT.author("Новелла"),
        AT.game("Grim Fandango", 3),
    ],[ # video activities
        AT.tv('Новенькая'),
        AT.video_prs(2),
        AT.video_doc(1, last=True),
        AT.video("Поделки"),
        AT.vid_theme(4, available=[{0:4},{0:4},{0:4},a13()]),
        AT.youtube("Гармония и Форма", available=[a13()]),
        AT.vid_letsplay(available=[a13()]),
    ],[ # audio activities
        AT.abook_novel(3),
        AT.music_fresh(),
        AT.music_hits(2),
    ], 30] # length


# 3-rd slot of module (14th at all) - current - standard slot
# randomizer
a14 = AT.randomize([2,3,3,3])       # audio, 14th slot, randomized
v14 = AT.randomize([4,4,5,6])       # video, 14th slot, randomized
v14p = AT.randomize([1,{4:1}])      # prs video/podcast prs
# slot
slot_14 = [
    [   # basic activities
        AT.prs(4, available=[{4:0},1,v14(),v14p()]),
        AT.project("PyMath", 3, available=[v14(),v14(),v14p()], last=True),
        AT.hobby("Игра на Гитаре", available=[2]),
        AT.hobby("Вокал", available=[3]),
        AT.hobby("Шитьё", available=[0]),
        AT.author("Новелла"),
        *AT.game("Grim Fandango", 4, available=[v14()], last=True),
    ],[ # video activities
        AT.tv('Новенькая'),
        AT.video_prs(2),
        AT.video("Гитара"),
        AT.video("Вокал"),
        AT.vid_theme(4, available=[{0:4},{1:4},a14(),a14()]),
        AT.youtube("Розыгрыши", available=[a14()]),
        AT.vid_letsplay(available=[a14()]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.podcast_prs(),
        AT.music_fresh(last=True),
        AT.music_hits(3),
    ], 30] # length


# 4-th slot of module (15th at all) - current - standard slot
# randomizer
v15m = AT.randomize([2,4])          # clips / music with romantic
# slot
slot_15 = [
    [   # basic activities
        AT.prs(7, available=[0,0,0,0,1,3,5]),
        AT.hobby("Игра на Гитаре", available=[v15m()], last=True),
        AT.hobby("Вокал", available=[v15m()], last=True),
        AT.hobby("Шитьё", available=[0], last=True),
        AT.author("Новелла", last=True),
        AT.author("Поэзия"),
        AT.game("The Walking Deads", 3),
    ],[ # video activities
        AT.anime('Трогательный Комплекс', 5),
        AT.video_prs(),
        AT.video("Клипы"),
        AT.vid_theme(available=[0]),
        AT.youtube("Романтика", available=[2]),
        AT.vid_letsplay(available=[1]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.podcast_prs(),
        AT.music_hits(),
    ], 30] # length


# 5-th slot of module (16th at all) - current - standard slot
slot_16 = [
    [   # basic activities
        AT.prs(7, available=[0,0,0,0,1,3,5]),
        AT.hobby("Разбор техники", available=[2]),
        AT.hobby("Вокал", available=[4], last=True),
        AT.hobby("Рисование", available=[0]),
        AT.author("Поэзия"),
        AT.author("Здоровая Жизнь"),
        AT.game("The Walking Deads", 3),
    ],[ # video activities
        AT.cartoon('Тимон и Пумба', 5),
        AT.video_prs(),
        AT.video("Разбор Техники"),
        AT.vid_theme(available=[0]),
        AT.youtube("Животные", available=[2]),
        AT.vid_letsplay(available=[1]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.podcast_prs(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (17th at all) - current - standard slot
# randomizer
v17 = AT.randomize([0,4])      # anime / music
# slot
slot_17 = [
    [   # basic activities
        AT.prs(7, available=[{3:0},{3:1},1,3,4,5,v17()], last=True),
        AT.prs("Выбор проекта на день", available=[3], last=True),
        AT.hobby("Разбор техники", available=[v17()], last=True),
        AT.hobby("Рисование", available=[2], last=True),
        AT.author("Поэзия", last=True),
        AT.author("Здоровая Жизнь", last=True),
        AT.game("The Walking Deads", 3, last=True),
    ],[ # video activities
        AT.anime('Код ГИАС R2'),
        AT.video_prs(last=True),
        AT.video("Рисование"),
        AT.vid_theme(4, available=[{0:3},{1:3},2,2], last=True),
        AT.youtube("Релаксация и Дзен", 2, available=[2,2]),
        AT.vid_letsplay(available=[2], last=True),
    ],[ # audio activities
        AT.abook_novel(last=True),
        AT.podcast_prs(last=True),
        AT.music_hits(5, last=True),
    ], 30] # length


# exported variable
EARLY_DAY = [slot_12, slot_13, slot_14, slot_15, slot_16, slot_17]


__all__ = ["EARLY_DAY"]

if __name__ == '__main__':
    print(EARLY_DAY)
