# placeholders
PLACEHOLDER = ["Activity", "Video", "Audio", 10]
THEME = "тематика"

# default basic activity templates
def default(name, count=1, last=True, available=None):
    return [name, count, last, available]
game = movie = default

# training activities templates
def train_m(count, available, last=False):
    return ["УТРЕННЯЯ ТРЕНИРОВКА", count, last, available]

# youtube videos templates
def v_prs(count, last=False):         # programming video
    return ["Видео по программированию", count, last, None]

def v_edu(count, last=False):         # educational video
    return ["Образовательное видео", count, last, None]

def v_doc(count, last=False):         # documental video
    return ["Документальный фильм", count, last, None]

def v_theme(count, audio, last=False):  # themed video
    return ["YouTube (%s)" % THEME, count, last, audio]

def v_play(audio, last=False):          # letsplay video
    return ["YouTube (летсплей)", 1, last, audio]

# Audiobook templates
def ab_roman(count, last=False):  # Novel
    return ["АУДИОКНИГА - Роман", count, last]

def ab_story(count, last=False):  # Story
    return ["АУДИОКНИГА - Рассказ", count, last]

# Programming podcast template
def a_prs(count, last=False):
    return ["Подкаст по программированию", count, last]

# Music templates
def m_theme(count, last=False):  # Theme music
    return ["Музыка (%s)" % THEME, count, last]

def m_hits(count, last=False):   # Hits music
    return ["Музыка (хиты)", count, last]

def m_fresh(count, last=False):  # Fresh music
    return ["Музыка (новый альбом)", count, last]

# Radio template
def radio(count, last=False):
    return ["Радио", count, last]


__all__ = [
    'PLACEHOLDER', 'THEME',             # placeholders
    'default', 'game', 'movie',         # basic activities templates
    'v_prs', 'v_edu', 'v_doc',          # useful videos templates
    'v_theme', 'v_play',                # funny videos templates
    'ab_roman', 'ab_story', 'a_prs',    # audiobook templates & podcast
    'm_theme', 'm_hits', 'm_fresh',     # music templates
    'radio',
    ]
