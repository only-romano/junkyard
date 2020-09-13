"""
    TEMPORAL FIX FOR NEW START - INTRODUCTION SET
            sport  /  prs  / health
      from    1m   /   1m   /   1m
      to     45m   /  45m   /  45m
"""
try:
    import activity_placeholders as P
except ImportError:
    import activities.activity_placeholders as P


def do(name, time):
    return [name, None, None, time]


INTRODUCTION = [
    do(P.SLEEP, 165), do(P.FREE, 150),
    do("Программирование", 15), do("ТРЕНИРОВКА", 15), do(P.SHOWER, 15),
    do(P.FREE, 885), do(P.SLEEP, 30)
]

__all__ = ['INTRODUCTION']
