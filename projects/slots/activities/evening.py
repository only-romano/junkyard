"""
Evening activities (until night siesta [included, 19:00 - 22:00])

 Now it consist of:
 - SLEEP slot
 - Evening meal slot
 - micro-activity slot
 - 4 standard slots
 - SLEEP slot
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (31th at all) - current - SLEEP slot
slot_31 = [P.SLEEP, None, None, 15]


# 2-nd slot of module (32th at all) - current - Evening meal slot
slot_32 = [P.LATE_DINNER, None, P.BROADCAST, 15]


# 3-rd slot of module (33th at all) - current - micro-activity slot
# randomizer
a33 = randomize([1,1,1,2,3,3,3])     # audio, 33th slot, randomized
v33 = randomize([2,3,4,5,6])         # video, 33th slot, randomized
v33e = randomize([1,2])              # educational video / music
v33b = randomize([{2:0},2])          # audiobook / music
# slot
slot_33 = [
    [   # basic activities
        AT.edu(P.SUBJECT_9, 6, available=[0,1,1,v33(),v33b(),v33e()], short=True),
        AT.edu(P.SUBJECT_8, 5, available=[v33(),v33(),v33(),v33(),v33e()], short=True),
        AT.author(P.AUTHOR_WORLD, short=True),
        AT.game(P.GAME_RELAX, available=[v33b()], short=True),
        AT.game(P.GAME_ADVENTURE, 2),
    ],[ # video activities
        AT.cartoon(P.CARTOON_SHORT),
        AT.video_edu(3, short=True),
        AT.vid_theme(4, available=[{0:2},a33(),a33(),a33()]),
        AT.youtube(P.YOUTUBE_EVENINIG_1, available=[a33()]),
        AT.youtube(P.YOUTUBE_EVENINIG_2, available=[a33()]),
        AT.youtube(P.YOUTUBE_EVENINIG_3, available=[a33()]),
        AT.vid_letsplay(available=[a33()]),
    ],[ # audio activities
        AT.abook_short(),
        AT.music_theme(3),
        AT.music_hits(),
        AT.music_radio(3),
    ], 15] # length


# 4-th slot of module (34th at all) - current - standard slot
# randomizer
a34 = randomize([1,1,1,1,2,3,4])     # audio, 34th slot, randomized
v34 = randomize([0,3,3,4,5])         # video, 34th slot, randomized
v34e = randomize([2,2,3,3])          # educational video / music
# slot
slot_34 = [
    [   # basic activities
        AT.prs(5, available=[{3:0},1,1,v34(),v34()], short=True),
        AT.project(P.PROJECT_EVENING, 3, available=[v34(),v34(),v34()], last=True),
        AT.math(2, available=[3,v34e()]),
        AT.edu(P.SUBJECT_1, available=[v34e()]),
        AT.edu(P.SUBJECT_7, available=[v34e()]),
        AT.edu(P.SUBJECT_10, available=[v34e()]),
        AT.game(P.GAME_ADVENTURE, 2),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2, short=True),
        AT.video_edu(2, short=True),
        AT.vid_theme(6, available=[{0:3},a34(),a34(),a34(),a34(),a34()], last=True),
        AT.youtube(P.YOUTUBE_EVENINIG_4, available=[a34()]),
        AT.vid_letsplay(available=[a34()], last=True),
    ],[ # audio activities
        AT.abook_short(last=True),
        AT.music_theme(4, last=True),
        AT.music_fresh(last=True),
        AT.music_hits(last=True),
        AT.music_radio(last=True),
    ], 30] # length


# 5-th slot of module (35th at all) - current - standard slot
slot_35 = [
    [   # basic activities
        AT.math(2, available=[0,1]),
        AT.edu(P.SUBJECT_1, available=[0]),
        AT.edu(P.SUBJECT_7, available=[0]),
        AT.edu(P.SUBJECT_10, available=[0]),
        AT.game(P.GAME_RELAX, available=[1]),
        AT.game(P.GAME_ADVENTURE, available=[0]),
        AT.game(P.GAME_PARENTS, 8, short=True),
    ],[ # video activities
        AT.movie(5),
        AT.tv(P.TV_BRAIN, 2, long=True),
    ],[ # audio activities is empty
    ], 30] # length


# 6-th slot of module (36th at all) - current - standard slot
slot_36 = [
    [   # basic activities
        AT.prs(6, available=[2,3,3,3,3,4]),
        AT.math(4, available=[0,1,3,4]),
        AT.edu(P.SUBJECT_1, available=[0]),
        AT.edu(P.SUBJECT_7, available=[0]),
        AT.edu(P.SUBJECT_10, available=[0]),
        AT.game(P.GAME_RELAX, available=[1]),
        AT.game(P.GAME_ADVENTURE, available=[0]),
    ],[ # video activities
        AT.movie(5),
        AT.tv(P.TV_BRAIN, 2),
        AT.tv(P.TV_BRAIN, long=True),
        AT.tv(P.TV_EASY, 5, long=True),
        AT.tv(P.TV_FUNNY, 2),
    ],[ # audio activities is empty
    ], 30] # length


# 7-th slot of module (37th at all) - current - standard slot
slot_37 = [
    [   # basic activities
        AT.prs(6, available=[1,2,2,2,2,3], last=True),
        AT.math(4, available=[0,2,3,3], last=True),
        AT.edu(P.SUBJECT_1, available=[0], last=True),
        AT.edu(P.SUBJECT_7, available=[0], last=True),
        AT.edu(P.SUBJECT_10, available=[0], last=True),
        AT.game(P.GAME_RELAX, available=[3], last=True),
        AT.game(P.GAME_ADVENTURE, available=[0], last=True),
    ],[ # video activities
        AT.movie(5, last=True),
        AT.tv(P.TV_BRAIN),
        AT.tv(P.TV_EASY, 5),
        AT.tv(P.TV_FUNNY, 4),
    ],[ # audio activities is empty
    ], 30] # length


# 8-th slot of module (38th at all) - current - SLEEP slot
slot_38 = [P.SLEEP, None, None, 15]


# exported variable
EVENING = [slot_31, slot_32, slot_33, slot_34, slot_35, slot_36, slot_37, slot_38]


__all__ = ["EVENING"]

if __name__ == '__main__':
    print(EVENING)
