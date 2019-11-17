try:
    from my_values import *
except ImportError:
    # put your ideal weight here
    IDEAL_WEIGHT = 66.6

# line pattern
LINE = "\n\n"

# lenghs of various values
SEP_LENGTH = 80
time_len = 9
basic_len = 44
video_len = 29
audio_len = 29
table_len = time_len + basic_len + video_len + audio_len + 3


def separator(length=False):
    return LINE + "-"*(length or SEP_LENGTH) + LINE


def smoke(i):
    def get_days(x):
        last_num = str(x)[-1]
        if last_num == "1":
            return "день"
        elif last_num in ["2", "3", "4"]:
            return "дня"
        return "дней"
    return "\tЯ не курю уже %i %s" % (i, get_days(i)) if i > 0 else "Зря покурили..."


def good(things):
    return _ul(things, "Не было хороших поступков...", "Вчерашние хорошие поступки:", GOOD)


def new_things(things):
    return _ul(things, "Ничего нового вчера не было...", "Вчера узнали:", NEW)

def weight(values):
    return WEIGHT + ("\n\n\tВчерашние показатели:%s%s%s%s" % (
        _wk("Вес  :", values['weight']),
        _wk("Мышцы:", values['muscle']),
        _wk("Жир  :", values['fat']),
        _wk("Вода :", values['water']),
        _wk("ИМТ  :", values['weight']),
        ))


# internal use functions
def _ul(things, ph1, ph2, template):
    if not len(things):
        things = [ph1]
    return template + ("\n\n\t%s\n\t\t* " % ph2) + "\n\t\t* ".join([x for x in things])


def _li(num):
    return "\n\t\t" + "\n\t\t".join(["%i __________________" % i for i in range(1, num+1)])


def _wk(name, value=None, ideal=None, flag=0):
    if value is None:
        return "%s --- (нет данных)" % name
    f = "%" if flag else "кГ"
    if ideal is None:
        return "\t%s: %.1f %s" % (name, value, f)
    return "\t%s: %.1f %s ... (%.1f %% от идеала)" % (name, value, f, value/ideal*100)


def _wt(name, flag=0):
    return "\t%.9s: __._ %s" % (name+" "*2, "%" if flag else "кГ")


GOOD = "\tСегодня вы сделали хорошего:%s" % (_li(3))
NEW = "\tСегодня вы узнали и выучили новое:%s" % (_li(3))

WEIGHT = "%s\n\n\t%s\n\t%s\n\t%s" % (_wt('Мой вес'), _wt('Мои мышцы'), _wt('Мой жир',1), _wt('Моя вода',1))
