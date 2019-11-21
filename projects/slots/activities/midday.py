"""
Midday activites (until second dinner [included, 13:00 - 15:30])

 Now it consist of:
 - SLEEP slot
 - micro-activity slot
 - dinner slot
 - 3 standard slots
 - second dinner slot
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (18th at all) - current - SLEEP slot
slot_18 = [P.SLEEP, None, None, 15]


# 2-nd slot of module (19th at all) - current - micro-activity slot
# randomizer
a19 = randomize([1,2,2,2,3,3,3,3,3])     # audio, 19th slot, randomized
v19 = randomize([0,3,3,3,3,5])           # video, 19th slot, randomized
v19d = randomize([2,4])                  # clips / dance videos
# slot
slot_19 = [
    [   # basic activities
        AT.sport(P.SPORT_WARMUP, 5, available=[v19(),v19(),v19(),v19(),v19d()]),
        AT.sound_only(P.ACT_MIDDAY, 2, available=[0,a19()]),
        AT.act(P.SPORT_DANCE, 5, available=[1,2,4,4,v19d()]),
        AT.act(P.RELAX_MIDDAY),
        AT.game(P.GAME_RELAX, 2, available=[v19(),v19()], short=True),
    ],[ # video activities
        AT.cartoon(P.CARTOON_SHORT),
        AT.video(P.VIDEO_DANCE),
        AT.video(P.CLIPS, 2),
        AT.vid_theme(4, available=[a19(),a19(),a19(),a19()]),
        AT.youtube(P.SPORT_DANCE, 3, available=[a19(),a19(),a19()]),
        AT.vid_letsplay(available=[a19()]),
    ],[ # audio activities
        AT.abook_short(),
        AT.music_theme(),
        AT.music_hits(3, last=True),
        AT.music_radio(5, last=True),
    ], 15] # length


# 3-rd slot of module (20th at all) - current - DINNER slot
slot_20 = [P.DINNER, None, P.BROADCAST, 15]


# 4-th slot of module (21th at all) - current - standard slot
# randomizer
a21 = randomize([1,2,3])         # audio, 21th slot, randomized
v21 = randomize([1,5,6])         # anime / youtube / letsplay
v21d = randomize([3,3,4])        # educational videos / music
# slot
slot_21 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v21()]),
        AT.project(P.PROJECT_DAY, 2, available=[0, v21()]),
        AT.edu(P.SUBJECT_2, available=[v21d()]),
        AT.edu(P.SUBJECT_3, available=[v21d()]),
        AT.edu(P.SUBJECT_4, available=[v21d()]),
        AT.thought(P.THOUGHT_MIDDAY_1),
        AT.game(P.GAME_COMPLEX, 3, available=[{4:0},0,v21()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime(P.ANIME_ACTION),
        AT.video_prs(),
        AT.video_edu(2),
        AT.vid_theme(3, available=[{0:4},{0:4},a21()]),
        AT.youtube(P.YOUTUBE_MIDDAY_1, available=[a21()]),
        AT.vid_letsplay(available=[a21()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 5-th slot of module (22th at all) - current - standard slot
# randomizer
a22 = randomize([1,2,3])         # audio, 22th slot, randomized
v22 = randomize([1,5,6])         # anime / youtube / letsplay
v22d = randomize([3,3,4])        # educational videos / music
# slot
slot_22 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v22()]),
        AT.project(P.PROJECT_DAY, 2, available=[0, v22()]),
        AT.edu(P.SUBJECT_2, available=[v22d()]),
        AT.edu(P.SUBJECT_3, available=[v22d()], last=True),
        AT.edu(P.SUBJECT_4, available=[v22d()], last=True),
        AT.thought(P.THOUGHT_MIDDAY_2),
        AT.game(P.GAME_COMPLEX, 3, available=[{4:0},0,v22()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime(P.ANIME_ACTION),
        AT.video_prs(),
        AT.video_edu(2),
        AT.vid_theme(3, available=[{0:4},{0:4},a22()]),
        AT.youtube(P.YOUTUBE_MIDDAY_2, available=[a22()]),
        AT.vid_letsplay(available=[a22()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (23th at all) - current - standard slot
# randomizer
a23 = randomize([1,2,3])         # audio, 23th slot, randomized
v23 = randomize([1,5,6])         # anime / youtube / letsplay
v23d = randomize([3,3,4])        # educational videos / music
# slot
slot_23 = [
    [   # basic activities
        AT.prs(6, available=[{4:0},0,0,0,2,v23()]),
        AT.project(P.PROJECT_DAY, 2, available=[0, v23()]),
        AT.edu(P.SUBJECT_2, available=[v23d()], last=True),
        AT.edu(P.SUBJECT_5, available=[v23d()], last=True),
        AT.edu(P.SUBJECT_6, available=[v23d()], last=True),
        AT.thought(P.THOUGHT_MIDDAY_3),
        AT.game(P.GAME_COMPLEX, 3, available=[{4:0},0,v23()]),
    ],[ # video activities
        AT.movie(5),
        AT.anime(P.ANIME_ACTION),
        AT.video_prs(),
        AT.video_edu(2, last=True),
        AT.vid_theme(3, available=[{0:4},{0:4},a23()]),
        AT.youtube(P.YOUTUBE_MIDDAY_3, available=[a23()]),
        AT.vid_letsplay(available=[a23()]),
    ],[ # audio activities
        AT.abook_short(2, last=True),
        AT.music_theme(),
        AT.music_fresh(last=True),
        AT.music_hits(),
    ], 30] # length


# 7-th slot of module (24th at all) - current - second DINNER slot
slot_24 = [P.LUNCH, None, P.BROADCAST, 15]


# exported variable
MIDDAY = [slot_18, slot_19, slot_20, slot_21, slot_22, slot_23, slot_24]


__all__ = ["MIDDAY"]

if __name__ == '__main__':
    print(MIDDAY)
