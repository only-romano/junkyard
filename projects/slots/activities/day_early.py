"""
Early daytime activities (until midday siesta [not included, 10:00 - 13:00])

 Now it consist of:
 - 6 standard slots
"""
try:
    import activity_templates as AT
    import activity_placeholders as P
    from activity_randomizer import randomize
except ImportError:
    import activities.activity_templates as AT
    import activities.activity_placeholders as P
    from activities.activity_randomizer import randomize


# 1-st slot of module (12th at all) - current - standard slot
# randomizer
a12 = randomize([1,2,2])         # audio, 12th slot, randomized
v12 = randomize([1,4,6])         # video, 12th slot, randomized
v12x = randomize([5,0])          # porn/prs video
# slot
slot_12 = [
    [   # basic activities
        AT.sport(P.SPORT_MORNING, 4, [3,3,3,3]),
        AT.prs(2, available=[0,v12x()]),
        AT.project(P.PROJECT_MORNING, 3, available=[v12(),v12(),v12x()]),
        AT.hobby(P.HOBBY_HARD_1, available=[2]),
        AT.hobby(P.HOBBY_ART_1, available=[v12()]),
        AT.author(P.AUTHOR_NOVEL),
        AT.game(P.GAME_STORY, 3),
    ],[ # video activities
        AT.video_prs(2),
        AT.video_doc(1),
        AT.video(P.HOBBY_HARD_1),
        AT.vid_theme(4, available=[0,0,0,0]),
        AT.youtube(P.YOUTUBE_HOT, available=[a12()]),
        AT.video(P.XXX, available=[a12()]),
        AT.vid_letsplay(available=[a12()]),
    ],[ # audio activities
        AT.abook_novel(4),
        AT.music_fresh(),
        AT.music_hits(2),
    ], 30] # length


# 2-nd slot of module (13th at all) - current - standard slot
# randomizer
a13 = randomize([1,2,2])         # audio, 13th slot, randomized
v13 = randomize([2,4,5,6])       # video, 13th slot, randomized
v13t = randomize([0,1])          # tv/prs video
# slot
slot_13 = [
    [   # basic activities
        AT.sport(P.SPORT_MORNING, 3, [{4:0},{4:0},{4:0}], last=True),
        AT.prs(3, available=[1,v13(),v13t()]),
        AT.project(P.PROJECT_MORNING, 3, available=[v13(),v13(),v13t()]),
        AT.hobby(P.HOBBY_HARD_1, available=[v13()], last=True),
        AT.hobby(P.HOBBY_ART_1, available=[3], last=True),
        AT.author(P.AUTHOR_NOVEL),
        AT.game(P.GAME_STORY, 3),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2),
        AT.video_doc(1, last=True),
        AT.video(P.HOBBY_ART_1),
        AT.vid_theme(4, available=[{0:4},{0:4},{0:4},a13()]),
        AT.youtube(P.YOUTUBE_EARLY_1, available=[a13()]),
        AT.vid_letsplay(available=[a13()]),
    ],[ # audio activities
        AT.abook_novel(3),
        AT.music_fresh(),
        AT.music_hits(2),
    ], 30] # length


# 3-rd slot of module (14th at all) - current - standard slot
# randomizer
a14 = randomize([2,3,3,3])       # audio, 14th slot, randomized
v14 = randomize([4,4,5,6])       # video, 14th slot, randomized
v14p = randomize([1,{4:1}])      # prs video/podcast prs
# slot
slot_14 = [
    [   # basic activities
        AT.prs(4, available=[{4:0},1,v14(),v14p()]),
        AT.project(P.PROJECT_MORNING, 3, available=[v14(),v14(),v14p()], last=True),
        AT.hobby(P.HOBBY_MUSIC_1, available=[2]),
        AT.hobby(P.HOBBY_MUSIC_2, available=[3]),
        AT.hobby(P.HOBBY_RELAX, available=[0]),
        AT.author(P.AUTHOR_NOVEL),
        *AT.game(P.GAME_STORY, 4, available=[v14()], last=True),
    ],[ # video activities
        AT.tv(P.TV_SOAP),
        AT.video_prs(2),
        AT.video(P.HOBBY_MUSIC_1),
        AT.video(P.HOBBY_MUSIC_2),
        AT.vid_theme(4, available=[{0:4},{1:4},a14(),a14()]),
        AT.youtube(P.YOUTUBE_EARLY_2, available=[a14()]),
        AT.vid_letsplay(available=[a14()]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.podcast_prs(),
        AT.music_fresh(last=True),
        AT.music_hits(3),
    ], 30] # length


# 4-th slot of module (15th at all) - current - standard slot
# randomizer
v15m = randomize([2,4])          # clips / music with romantic
# slot
slot_15 = [
    [   # basic activities
        AT.prs(7, available=[0,0,0,0,1,3,5]),
        AT.hobby(P.HOBBY_MUSIC_1, available=[v15m()], last=True),
        AT.hobby(P.HOBBY_MUSIC_2, available=[v15m()], last=True),
        AT.hobby(P.HOBBY_RELAX, available=[0], last=True),
        AT.author(P.AUTHOR_NOVEL, last=True),
        AT.author(P.AUTHOR_POEM),
        AT.game(P.GAME_STORY2, 3),
    ],[ # video activities
        AT.anime(P.ANIME_ROMANTIC, 5),
        AT.video_prs(),
        AT.video(P.CLIPS),
        AT.vid_theme(available=[0]),
        AT.youtube(P.YOUTUBE_EARLY_3, available=[2]),
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
        AT.hobby(P.HOBBY_HARD_2, available=[2]),
        AT.hobby(P.HOBBY_MUSIC_2, available=[4], last=True),
        AT.hobby(P.HOBBY_ART_2, available=[0]),
        AT.author(P.AUTHOR_POEM),
        AT.author(P.AUTHOR_HEALTH),
        AT.game(P.GAME_STORY2, 3),
    ],[ # video activities
        AT.cartoon(P.CARTOON_MAIN, 5),
        AT.video_prs(),
        AT.video(P.HOBBY_HARD_2),
        AT.vid_theme(available=[0]),
        AT.youtube(P.YOUTUBE_EARLY_4, available=[2]),
        AT.vid_letsplay(available=[1]),
    ],[ # audio activities
        AT.abook_novel(),
        AT.podcast_prs(),
        AT.music_hits(),
    ], 30] # length


# 6-th slot of module (17th at all) - current - standard slot
# randomizer
v17 = randomize([0,4])      # anime / music
# slot
slot_17 = [
    [   # basic activities
        AT.prs(7, available=[{3:0},{3:1},1,3,4,5,v17()], last=True),
        AT.prs(P.PRS_ROADMAP, available=[3], last=True),
        AT.hobby(P.HOBBY_HARD_2, available=[v17()], last=True),
        AT.hobby(P.HOBBY_ART_2, available=[2], last=True),
        AT.author(P.AUTHOR_POEM, last=True),
        AT.author(P.AUTHOR_HEALTH, last=True),
        AT.game(P.GAME_STORY2, 3, last=True),
    ],[ # video activities
        AT.anime(P.ANIME_ACTION),
        AT.video_prs(last=True),
        AT.video(P.HOBBY_ART_2),
        AT.vid_theme(4, available=[{0:3},{1:3},2,2], last=True),
        AT.youtube(P.YOUTUBE_EARLY_5, 2, available=[2,2]),
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
