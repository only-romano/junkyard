"""
Late night activities (until required sleep [not included, 00:30 - 03:30])

 Now it consist of:
 - 6 standard slots
 - NIGHT SLEEP slot
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (45th at all) - current - Standard slot
# randomizer
v45e = randomize([1,4,5])       # tv / educational video / documental video
# slot
slot_45 = [
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
        AT.video_prs(),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[{0:6},{1:6}]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 2-nd slot of module (46th at all) - current - Standard slot
slot_46 = P.SLOT_PLACEHOLDER


# 3-rd slot of module (47th at all) - current - Standard slot
slot_47 = P.SLOT_PLACEHOLDER


# 4-th slot of module (48th at all) - current - Standard slot
slot_48 = P.SLOT_PLACEHOLDER


# 5-th slot of module (49th at all) - current - Standard slot
slot_49 = P.SLOT_PLACEHOLDER


# 6-th slot of module (50th at all) - current - Standard slot
slot_50 = P.SLOT_PLACEHOLDER


# 7-th slot of module (51th at all) - current - NIGHT SLEEP slot
slot_51 = [P.SLEEP, None, None, 165]


# exported variable
LATE_NIGHT = [slot_45, slot_46, slot_47, slot_48, slot_49, slot_50, slot_51]


__all__ = ["LATE_NIGHT"]

if __name__ == '__main__':
    print(LATE_NIGHT)
