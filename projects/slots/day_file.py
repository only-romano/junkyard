from datetime import datetime
from print_patterns import *
from random import randint
try:
    from my_values import DESKTOP_PATH, PATH_TO_FOLDER, CHARSET
except ImportError:
    try:
        from my_values_placeholder import DESKTOP_PATH, PATH_TO_FOLDER, CHARSET
    except ImportError:
        DESKTOP_PATH = None
        PATH_TO_FOLDER = "day_files/"
        CHARSET = 'utf-8'


d = datetime.now()
FILENAME = "day_file_%d_%.2d_%.2d.md" % (d.year, d.month, d.day)
tabs = " "*4
#ENCODE = lambda a: a.encode(CHARSET).decode("cp1252")


def create_day_file(data, slots):
    to_write = _construct_file(data, slots)
    with open(PATH_TO_FOLDER + FILENAME, 'w', encoding=CHARSET) as file:
        file.write(to_write)
    if DESKTOP_PATH:
        with open(DESKTOP_PATH + FILENAME, 'w', encoding=CHARSET) as file:
            file.write(to_write)


# internal use functions
def _construct_file(data, slots):
    special = data.pop()
    return separator(table_len+2+len(tabs)*2).join([
        "\n\t%d/%d/%d (дневной файл)" % (d.day, d.month, d.year),
        "\tЗАМЕТКИ" + notes(5) + "\n",
        good(special['good_things']),
        new_things(special['new_things']),
        "\tЯ сегодня не курил: __\n\t" + smoke(special['smoke']),
        weight(special, slots),

        "\tДИЕТА\n\n\t\tЯ придерживался диеты: __\n\t\t" +
        diet_done(special['diet_done']) +
        "\n\n" + special['diet'],

        "\tРАСПИСАНИЕ НА СЕГОДНЯ:\n" + 
        "\t " + "_"*table_len + "".join([_table(data[x]) \
            for x in range(len(data)) \
                if not _previous_the_same(data, x)]),

        "\t\t\t(день %i)\n" % (special['days_at_all']+1)
        ]).replace("\t", tabs)


def _broadcast():
    return "Евгеника" if randint(1,4) == 1 else "Маяк"


def _previous_the_same(d, i):
    if i == 0: return False
    p = i-1
    return (d[i]['basic'] == d[p]['basic'] and
            d[i]['video'] == d[p]['video'] and
            d[i]['audio'] == d[p]['audio'])


def _table(one):
    a, b, r, t, v = "audio", "basic", "radiobroadcast", "time", "video"
    al, bl, tl, vl = audio_len, basic_len, time_len, video_len
    return "\n\t".join(["",
        "|".join(["", " "*tl, " "*bl, " "*vl, " "*al, ""]),
        "|".join(["",
          "  %s  " % one[t],
          "  %.40s  " % (one[b] + " "*40),
          "  %.25s  " % ((one[v] if one[v] else "") + " "*25),
          "  %.25s  " % ((one[a].replace(r, _cast) if one[a] else "") + " "*25),
          ""]),
        "|".join(["","_"*tl,"_"*bl, "_"*vl, "_"*al, ""]),
        ])


# todays broadcast choice
_cast = _broadcast()
