from datetime import datetime
from print_patterns import *
from random import randint
try:
    from my_values import DESKTOP_PATH
except ImportError:
    try:
        from my_values_placeholder import DESKTOP_PATH
    except ImportError:
        DESKTOP_PATH = None


d = datetime.now()
FILENAME = "day_file_%d_%.2d_%.2d.md" % (d.year, d.month, d.day)
tabs = " "*4


def create_day_file(data, slots):
    to_write = _construct_file(data, slots)
    with open("day_files/" + FILENAME, 'w') as file:
        file.write(to_write)
    if DESKTOP_PATH:
        with open(DESKTOP_PATH + FILENAME, 'w') as file:
            file.write(to_write)


# internal use functions
def _construct_file(data, slots):
    special = data.pop()
    return separator(table_len+2+len(tabs)*2).join([
        "\n\t%d/%d/%d (дневной файл)" % (d.day, d.month, d.year),
        "\tЯ сегодня не курил: __\n\t" + smoke(special['smoke']),
        good(special['good_things']),
        new_things(special['new_things']),
        weight(special, slots),
        "\tДИЕТА\n\n\t\tЯ придерживался диеты: __\n\t\t" + diet_done(special['diet_done']) +
        "\n\n" + special['diet'],
        "\tРАСПИСАНИЕ НА СЕГОДНЯ:\n" + 
        "\t " + "_"*table_len + "".join([_table(x) for x in data]),
        "\t\t\t(день %i)\n" % (special['days_at_all']+1)
        ]).replace("\t", tabs)


def _broadcast():
    return "Евгеника" if randint(1,4) == 1 else "Маяк"


def _table(one):
    return "\n\t".join(["",
        "|".join([""," "*time_len," "*basic_len, " "*video_len, " "*audio_len, ""]),
        "|".join(["",
            "  %s  " % one['time'],
            "  %.40s  " % (one['basic'] + " "*40),
            "  %.25s  " % ((one['video'] if one['video'] else "") + " "*25),
            "  %.25s  " % ((one['audio'].replace("radiobroadcast", _cast) if one['audio'] else "") + " "*25),
            ""
            ]),
        "|".join(["","_"*time_len,"_"*basic_len, "_"*video_len, "_"*audio_len, ""]),
        ]) 


# todays broadcast choice
_cast = _broadcast()
