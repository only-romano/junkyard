from datetime import datetime
from print_patterns import *
from random import randint

d = datetime.now()
FILENAME = "day_file_%d_%.2d_%.2d.md" % (d.year, d.month, d.day)
tabs = " "*4
time_len = 9
basic_len = 44
video_len = 29
audio_len = 29
table_len = time_len + basic_len + video_len + audio_len + 3

def create_day_file(data):
    with open(FILENAME, 'w') as file:
        file.write(_construct_file(data))


# internal use functions
def _construct_file(data):
    special = data.pop()
    return separator(table_len+2+len(tabs)*2).join([
        "\n\t%d/%d/%d (дневной файл)" % (d.day, d.month, d.year),
        "\tКурение: " + smoke(special['smoke']),
        GOOD,
        NEW,
        "\t" + special['diet'],
        "\tРАСПИСАНИЕ НА СЕГОДНЯ:\n" + 
        "\t " + "_"*table_len + "".join([_table(x) for x in data]),
        ""
        ]).replace("radiobroadcast", _broadcast()).replace("\t", tabs)


def _broadcast():
    return "Евгеника" if randint(1,4) == 1 else "Маяк"


def _table(one):
    return "\n\t".join(["",
        "|".join([""," "*time_len," "*basic_len, " "*video_len, " "*audio_len, ""]),
        "|".join(["",
            "  %s  " % one['time'],
            "  %.40s  " % (one['basic'] + " "*40),
            "  %.25s  " % ((one['video'] if one['video'] else "") + " "*25),
            "  %.25s  " % ((one['audio'] if one['audio'] else "") + " "*25),
            ""
            ]),
        "|".join(["","_"*time_len,"_"*basic_len, "_"*video_len, "_"*audio_len, ""]),
        ]) 
