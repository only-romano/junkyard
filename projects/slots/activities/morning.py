"""
Morning activities (until morning training min-finish time [07:00 - 10:00])

 Now it consist of :
 - 1 micro-slot with modular activities
 - constant Breakfast slot
 - 2 standard slots
 - constant Morning Training 1.5 h slot
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of the module (7th at all) - current - mini-activity slot
# randomizer section
a7 = randomize([1,2,2,3])         # audio, 7th slot randomized
v7 = randomize([2,2,3,3,4])       # video, 7th slot randomized
# slot
slot_07 = [
    [   # basic activities
        AT.act(P.ACT_BREAKFAST, 5, available=[{3:0},0,1,v7(),v7()]),
        AT.hobby(P.HOBBY_BREAKFAST, 2, available=[{3:0},v7()], last=True),
        AT.act(P.ACT_NEWS, available=[v7()]),
        AT.act(P.ACT_SURF, available=[v7()]),
        AT.author(P.AUTHOR_WORLD, short=True),
        AT.game(P.GAME_NOVEL, 3, short=True),
        AT.game(P.GAME_ADVENTURE, 2, short=True),
    ],[ # video activities
        AT.video_prs(),
        AT.video_doc(),
        AT.youtube(P.YOUTUBE_BREAKFAST, 2, available=[a7(),a7()]),
        AT.vid_theme(4, available=[{0:3},{0:3},1,a7()]),
        AT.vid_letsplay(available=[a7()]),
    ],[ # audio activities
        AT.abook_short(2),
        AT.music_fresh(2),
        AT.music_hits(2),
        AT.music_radio(1),
    ], 20] # length


# 2-nd slot of module (8th at all) - current - breakfast slot
slot_08 = [P.BREAKFAST, P.CARTOON_BREAKFAST, None, 10]


# 3-rd slot of module (9th at all) - current - standard slot
# randomizer
a9 = randomize([3,4,5,6])        # audio, 9th slot randomized
v9 = randomize([5,5,6])          # video, 9th slot randomized
v9b = randomize([{4:0},3])       # audiobook/ documental video
v9e = randomize([2,4])           # educational video / theme video
# slot
slot_09 = [
    [   # basic activities
        AT.prs(P.PRS_REPEAT, 5, available=[{4:2},1,1,v9b(),v9()], last=True),
        AT.prs(P.PRS_IDEAS, available=[v9()]),
        AT.math(available=[v9e()]),
        AT.edu(P.SUBJECT_1, available=[v9e()]),
        AT.thought(P.THOUGHT_MORNING_1),
        *AT.game(P.GAME_MORNING, 6, available=[{4:1},0,v9b(),v9()], short=True),
    ],[ # video activities
        AT.anime(P.ANIME_ACTION),
        AT.video_prs(2),
        AT.video_edu(last=True),
        AT.video_doc(),
        AT.vid_theme(4, available=[{0:4},{1:4},{2:4},a9()]),
        AT.youtube(P.YOUTUBE_MORNING_1, 2, available=[a9(),a9()]),
        AT.vid_letsplay(available=[a9()]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.abook_short(),
        AT.podcast_prs(),
        AT.music_theme(),
        AT.music_fresh(),
        AT.music_hits(),
        AT.music_radio(),
    ], 30] # length


# 4-th slot of module (10th at all) - current - standard slot
# randomizer
a10 = randomize([3,4,5,6])   # audio, 10th slot, randomized
v10s = randomize([4,5])      # simple video, 10th slot, randomized
v10h = randomize([2,3,5,6])  # high-attention video, 10th slot, randomized
# slot
slot_10 = [
    [   # basic activities
        AT.sport(P.SPORT_MORNING, 3, available=[{4:0},{4:0},{4:0}]),
        AT.prs(P.PRS_LANG, 5, available=[{4:2},1,1,v10h(),v10h()], last=True),
        AT.prs(P.PRS_IDEAS, available=[v10h()], last=True),
        AT.math(available=[v10s()], last=True),
        AT.edu(P.SUBJECT_1, available=[v10s()], last=True),
        AT.thought(P.THOUGHT_MORNING_2),
        AT.game(P.GAME_MORNING, 3, available=[{4:1},0,v10h()], short=True),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2, last=True),
        AT.video_doc(1, last=True),
        AT.video(P.CLIPS),
        AT.vid_theme(6, available=[{0:4},{0:4},{0:4},{1:4},{2:4},a10()]),
        AT.youtube(P.YOUTUBE_MORNING_2, 2, available=[a10(),a10()]),
        AT.vid_letsplay(available=[a10()], last=True),
    ],[ # audio activities   [0,0,0,1]
        AT.abook_novel(3),
        AT.abook_short(last=True),
        AT.podcast_prs(last=True),
        AT.music_theme(last=True),
        AT.music_fresh(last=True),
        AT.music_hits(last=True),
        AT.music_radio(last=True),
    ], 30] # length


# 5-th slot of module (11th at all) - current - morning training slot
slot_11 = [P.SPORT_MORNING, P.VIDEO_THEME, P.ABOOK_NOVEL, 90]


# exported variable
MORNING = [slot_07, slot_08, slot_09, slot_10, slot_11]


__all__ = ["MORNING"]

if __name__ == '__main__':
    print(MORNING)
