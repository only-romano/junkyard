"""
Night activities (until possible sleep start [not included, 22:00 - 00:30])

 Now it consist of:
 - Night Lunch slot
 - Shower slot
 - 4 standard slots
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (39th at all) - current - NIGHT LUNCH slot
slot_39 = [P.NIGHT_LUNCH, None, P.BROADCAST, 15]


# 2-nd slot of module (40th at all) - current - Shower slot
slot_40 = [P.SHOWER, None, None, 15]


# 3-rd slot of module (41th at all) - current - Standard slot
# randomizer
v41e = randomize([1,4,5])       # tv / educational video / documental video
# slot
slot_41 = [
    [   # basic activities
        AT.prs(5, available=[{6:0},{6:1},3,3,3]),
        AT.project(P.PROJECT_NIGHT, 3, available=[0,2,7]),
        AT.math(available=[v41e()]),
        AT.edu(P.SUBJECT_11, available=[v41e()]),
        AT.edu(P.SUBJECT_14, available=[v41e()]),
        AT.thought(P.THOUGHT_NIGHT_1),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_USSR, long=True),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(3),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[{0:6},{1:6}]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 4-th slot of module (42th at all) - current - Standard slot
# randomizer
v42e = randomize([1,4,5])       # tv / educational video / documental video
# slot
slot_42 = [
    [   # basic activities
        AT.prs(5, available=[{6:0},{6:1},3,3,3]),
        AT.project(P.PROJECT_NIGHT, 3, available=[0,2,7]),
        AT.math(available=[v42e()]),
        AT.edu(P.SUBJECT_11, available=[v42e()]),
        AT.edu(P.SUBJECT_14, available=[v42e()]),
        AT.thought(P.THOUGHT_NIGHT_2),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_USSR, long=True),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_COMEDY),
        AT.video_prs(3),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[{0:6},{1:6}]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 5-th slot of module (43th at all) - current - Standard slot
# randomizer
v43e = randomize([1,4,5])       # tv / educational video / documental video
# slot
slot_43 = [
    [   # basic activities
        AT.prs(5, available=[{6:0},{6:1},3,3,3]),
        AT.project(P.PROJECT_NIGHT, 3, available=[0,2,7]),
        AT.math(available=[v43e()]),
        AT.edu(P.SUBJECT_12, available=[v43e()]),
        AT.edu(P.SUBJECT_13, available=[v43e()]),
        AT.thought(P.THOUGHT_NIGHT_3),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_USSR),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(3),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[{0:6},{1:6}]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (44th at all) - current - Standard slot
# randomizer
v44e = randomize([1,4,5])       # tv / educational video / documental video
# slot
slot_44 = [
    [   # basic activities
        AT.prs(5, available=[{6:0},{6:1},3,3,3]),
        AT.project(P.PROJECT_FREE, 3, available=[0,2,7]),
        AT.math(available=[v43e()]),
        AT.edu(P.SUBJECT_12, available=[v43e()]),
        AT.edu(P.SUBJECT_13, available=[v43e()]),
        AT.thought(P.THOUGHT_NIGHT_4),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(3),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[{0:6},{1:6}]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# exported variable
NIGHT = [slot_39, slot_40, slot_41, slot_42, slot_43, slot_44]


__all__ = ["NIGHT"]

if __name__ == '__main__':
    print(NIGHT)
