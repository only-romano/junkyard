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
v45 = randomize([0,1,2])        # video, 45th slot, randomized
# slot
slot_45 = [
    [   # basic activities
        AT.sleep(2),
        AT.prs(5, available=[3,6,6,7,v45()]),
        AT.project(P.PROJECT_FREE, 3, available=[5,v45(),v45()]),
        AT.math(available=[4]),
        AT.author(P.AUTHOR_BOOK),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(),
        AT.video_edu(short=True),
        AT.video_doc(),
        AT.vid_theme(2, available=[0,1]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 2-nd slot of module (46th at all) - current - Standard slot
# randomizer
v46 = randomize([0,1,2])        # tv series randomized
# slot
slot_46 = [
    [   # basic activities
        AT.sleep(3),
        AT.prs(4, available=[3,5,5,6]),
        AT.project(P.PROJECT_FREE, 3, available=[4,v46(),v46()]),
        AT.math(available=[v46()]),
        AT.author(P.AUTHOR_BOOK),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(),
        AT.video_doc(),
        AT.vid_theme(2, available=[0,1]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 3-rd slot of module (47th at all) - current - Standard slot
# randomizer
v47 = randomize([0,1,2])        # tv series randomized
# slot
slot_47 = [
    [   # basic activities
        AT.sleep(3),
        AT.prs(4, available=[3,5,5,6]),
        AT.project(P.PROJECT_FREE, 3, available=[4,v47(),v47()]),
        AT.math(available=[v47()]),
        AT.author(P.AUTHOR_BOOK),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(),
        AT.video_doc(),
        AT.vid_theme(2, available=[0,1]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 4-th slot of module (48th at all) - current - Standard slot
# randomizer
v48 = randomize([0,1,2])        # tv series randomized
# slot
slot_48 = [
    [   # basic activities
        AT.sleep(3),
        AT.prs(4, available=[3,5,5,6]),
        AT.project(P.PROJECT_FREE, 3, available=[4,v48(),v48()]),
        AT.math(available=[v48()]),
        AT.author(P.AUTHOR_BOOK),
        AT.game(P.GAME_MAIN, 3),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(),
        AT.video_doc(),
        AT.vid_theme(2, available=[0,1]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 5-th slot of module (49th at all) - current - Standard slot
# randomizer
v49 = randomize([0,1,2])        # tv series randomized
# slot
slot_49 = [
    [   # basic activities
        AT.sleep(3),
        AT.prs(4, available=[3,5,5,6]),
        AT.project(P.PROJECT_FREE, 3, available=[4,v49(),v49()]),
        AT.math(available=[v49()], last=True),
        AT.author(P.AUTHOR_BOOK, last=True),
        AT.game(P.GAME_MAIN, 3, last=True),
    ],[ # video activities
        AT.tv(P.TV_COMEDY),
        AT.tv(P.TV_SOAP),
        AT.tv(P.TV_IT),
        AT.video_prs(),
        AT.video_doc(),
        AT.vid_theme(2, available=[0,1]),
        AT.vid_letsplay(available=[2]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (50th at all) - current - Standard slot
slot_50 = [
    [   # basic activities
        AT.sleep(4),
        AT.prs(4, available=[{3:0},0,3,4], last=True),
        AT.project(P.PROJECT_FREE, 3, available=[1,2,3], last=True),
        AT.thought(P.THOUGHT_SLEEP),
        AT.game(P.GAME_RELAX, 3, short=True),
    ],[ # video activities
        AT.video_prs(last=True),
        AT.video_doc(last=True),
        AT.youtube(P.YOUTUBE_NIGHT, available=[1]),
        AT.vid_theme(3, available=[{0:3},1,1], last=True),
        AT.vid_letsplay(available=[2], last=True),
    ],[ # audio activities
        AT.abook_novel(last=True),
        AT.abook_short(3, last=True),
        AT.music_hits(last=True),
    ], 30] # length


# 7-th slot of module (51th at all) - current - NIGHT SLEEP slot
slot_51 = [P.SLEEP, None, None, 165]


# exported variable
LATE_NIGHT = [slot_45, slot_46, slot_47, slot_48, slot_49, slot_50, slot_51]


__all__ = ["LATE_NIGHT"]

if __name__ == '__main__':
    print(LATE_NIGHT)
