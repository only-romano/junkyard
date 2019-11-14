"""
Late daytime activities (until evening siesta [not included, 15:30 - 19:00])

 Now it consist of:
 - 3 standard slots
 - constant Evening Training 1h slot
 - 2 standard slots
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (25th at all) - current - standard slot
# randomizer
a25 = randomize([2,3,3,3])         # audio, 25th slot, randomized
v25 = randomize([3,4,4,5])         # video, 25th slot, randomized
# slot
slot_25 = [
    [   # basic activities
        AT.prs(6, available=[{3:0},0,0,0,1,1]),
        AT.project(P.PROJECT_DAY, 2, available=[0, v25()], last=True),
        AT.math(available=[v25()]),
        AT.edu(P.SUBJECT_1, available=[v25()]),
        AT.hobby(P.HOBBY_MUSIC_3, available=[2]),
        AT.author(P.AUTHOR_STORY),
        AT.game(P.GAME_COMPLEX, 3, available=[{3:1},0,v25()], last=True),
    ],[ # video activities
        AT.movie(5),
        AT.video_prs(2),
        AT.video(P.HOBBY_MUSIC_3),
        AT.vid_theme(3, available=[{0:3},{1:3},a25()]),
        AT.youtube(P.YOUTUBE_DAY_1, 2, available=[a25(),a25()]),
        AT.vid_letsplay(available=[a25()]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.music_theme(),
        AT.music_hits(3),
    ], 30] # length


# 2-nd slot of module (26th at all) - current - standard slot
# randomizer
a26 = randomize([2,3,4])         # audio, 26th slot, randomized
v26 = randomize([0,4,5])         # video, 26th slot, randomized
v26e = randomize([2,4])          # educational video / music
# slot
slot_26 = [
    [   # basic activities
        AT.sport(P.SPORT_EVENING, available=[{3:0}]),
        AT.prs(6, available=[{3:0},0,0,0,1,1]),
        AT.math(available=[v26e()]),
        AT.edu(P.SUBJECT_1, available=[v26e()]),
        AT.hobby(P.HOBBY_MUSIC_3, available=[v26()], last=True),
        AT.author(P.AUTHOR_STORY),
        AT.game(P.GAME_BRAIN, 4, available=[{3:1},0,v26(),v26()], short=True),
    ],[ # video activities
        AT.movie(5),
        AT.video_prs(2, last=True),
        AT.video_edu(),
        AT.vid_theme(4, available=[{0:3},{0:3},{1:3},a26()]),
        AT.youtube(P.YOUTUBE_DAY_2, available=[a26()]),
        AT.vid_letsplay(available=[a26()]),
    ],[ # audio activities
        AT.abook_novel(2),
        AT.abook_short(),
        AT.music_theme(last=True),
        AT.music_hits(),
        AT.music_radio(),
    ], 30] # length


# 3-rd slot of module (27th at all) - current - standard slot
# randomizer
a27 = randomize([2,3])           # audio, 27th slot, randomized
v27 = randomize([0,5,6])         # video, 27th slot, randomized
v27e = randomize([0,1,4])        # movie / educational video / music
# slot
slot_27 = [
    [   # basic activities
        AT.sport(P.SPORT_EVENING, 6, available=[2,2,2,2,2,2]),
        AT.prs(available=[v27()], last=True),
        AT.math(available=[v27e()], last=True),
        AT.edu(P.SUBJECT_1, available=[v27e()], last=True),
        AT.edu(P.SUBJECT_7, available=[v27e()], last=True),
        AT.author(P.AUTHOR_STORY, last=True),
        AT.game(P.GAME_BRAIN, 4, available=[0,3,v27(),v27()], short=True),
    ],[ # video activities
        AT.movie(3, last=True),
        AT.video_edu(last=True),
        AT.vid_theme(6, available=[0,0,0,0,0,0]),
        AT.youtube(P.YOUTUBE_DAY_3, available=[1]),
        AT.youtube(P.YOUTUBE_DAY_4, available=[a27()]),
        AT.youtube(P.YOUTUBE_DAY_5, available=[0]),
        AT.vid_letsplay(available=[a27()], last=True),
    ],[ # audio activities
        AT.abook_novel(7),
        AT.abook_short(last=True),
        AT.music_hits(last=True),
        AT.music_radio(last=True),
    ], 30] # length


# 4-th slot of module (28th at all) - current - evening training slot
slot_28 = [P.SPORT_EVENING, P.VIDEO_THEME, P.ABOOK_NOVEL, 60]


# 5-st slot of module (29th at all) - current - standard slot
# randomizer
a29 = randomize([1,1,2,3])           # audio, 29th slot, randomized
v29 = randomize([4,5,6])             # video, 29th slot, randomized
v29h = randomize([{4:0},0,4])        # tv / audiobook / music
# slot
slot_29 = [
    [   # basic activities
        AT.sport(P.SPORT_EVENING, 3, available=[{4:0},{4:0},{4:0}]),
        AT.prs(3, available=[1,1,v29h()]),
        AT.project(P.PROJECT_EVENING, 3, available=[v29(),v29(),v29h()]),
        AT.math(2, available=[2,v29()]),
        AT.act(P.ACT_USEFUL, available=[v29h()],long=True),
        AT.hobby(P.HOBBY_FUN, available=[3]),
        AT.game(P.GAME_NOVEL, 2),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2),
        AT.video_edu(),
        AT.video(P.HOBBY_FUN),
        AT.vid_theme(6, available=[{0:4},{0:4},{0:4},{0:4},a29(),a29()]),
        AT.youtube(P.YOUTUBE_LATEDAY_1, available=[a29()]),
        AT.vid_letsplay(available=[a29()]),
    ],[ # audio activities
        AT.abook_novel(4),
        AT.music_theme(2),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 6-st slot of module (30th at all) - current - standard slot
# randomizer
a30 = randomize([1,1,2,3])       # audio, 30th slot, randomized
v30 = randomize([4,5,6])         # video, 30th slot, randomized
v30h = randomize([0,4])          # tv / audiobook / music
# slot
slot_30 = [
    [   # basic activities
        AT.prs(5, available=[{4:0},{4:0},1,1,v30h()], last=True),
        AT.project(P.PROJECT_EVENING, 3, available=[v30(),v30(),v30h()]),
        AT.math(2, available=[2,v30()], last=True),
        AT.act(P.ACT_USEFUL, available=[3]),
        AT.hobby(P.HOBBY_FUN, available=[{4:0}], last=True),
        AT.thought(P.THOUGHT_EVENING),
        AT.game(P.GAME_NOVEL, 2, last=True),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2, last=True),
        AT.video_edu(last=True),
        AT.video(P.ACT_USEFUL),
        AT.vid_theme(5, available=[{0:4},{0:4},{0:4},a30(),a30()], last=True),
        AT.youtube(P.YOUTUBE_LATEDAY_2, available=[a30()]),
        AT.vid_letsplay(available=[a30()], last=True),
    ],[ # audio activities
        AT.abook_novel(3, last=True),
        AT.music_theme(2, last=True),
        AT.music_fresh(last=True),
        AT.music_hits(last=True),
    ], 30] # length


# exported variable
LATEDAY = [slot_25, slot_26, slot_27, slot_28, slot_29, slot_30]


__all__ = ["LATEDAY"]

if __name__ == '__main__':
    print(LATEDAY)
