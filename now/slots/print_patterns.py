try:
    from my_values import my_values_preset as MVP
except ImportError:
    from diet_patterns import get_MVP
    # put your values here
    height =  180               # your height in sm (inches * 2.54)
    age = 25                    # your age
    gender = "M"                # i'm sorry but to correct formula gender needed (available options: "M" for male, "F" for female, "T" for transgender)
    muscle = False              # a lot of muscles?
    desirable_weight = None     # leave None to auto-calculate else input float
    MVP = get_MVP(height, age, gender, muscle, desirable_weight)


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
    return "Не курю уже %i %s" % (i, _get_days(i)) if i > 0 else "Зря вчера покурили..."


def diet_done(i):
    return "Придерживаюсь диеты без срывов уже %i %s" % (i, _get_days(i)) if i > 0 else "Вчера был срыв..."


def good(things):
    return _ul(things, "Не было хороших поступков...", "Вчерашние хорошие поступки:", GOOD)


def new_things(things):
    return _ul(things, "Ничего нового вчера не было...", "Вчера узнали:", NEW)


def weight(values, slots):
    weight, time_weight = _get_old_value_and_time(values['weight'], slots.weight)
    muscle, time_muscle = _get_old_value_and_time(values['muscle'], slots.muscle)
    fat, time_fat = _get_old_value_and_time(values['fat'], slots.fat)
    water, time_water = _get_old_value_and_time(values['water'], slots.water)
    return WEIGHT + ("\n\n\tПрошлые показатели:%s%s%s%s" % (
        _wk("Вес  :", weight, MVP["weight"], time_weight, flag=0),
        _wk("Мышцы:", muscle, MVP["muscle"], time_muscle, flag=0),
        _wk("Жир  :", fat, MVP["fat"], time_fat, flag=1),
        _wk("Вода :", water, MVP["water"], time_water, flag=1),
        ))


# internal use functions
def _ul(things, ph1, ph2, template):
    things = [x for x in things if len(x.strip())]
    if not len(things):
        things = [ph1]
    return template + ("\n\n\t%s\n\t\t* " % ph2) + "\n\t\t* ".join([x for x in things])


def _li(num):
    return "\n\t\t" + "\n\t\t".join(["%i __________________" % i for i in range(1, num+1)])


def _wk(name, value=None, ideal=None, time=1, flag=0):
    result = "\n\t\t%s" % name
    if value is None:
        return "%s --- (нет данных)" % result
    add_space = " " if value < 100 else ""
    mesure = "% " if flag else "кГ"
    result = "%s %s%.1f %s" % (result, add_space, value, mesure)
    when = "вчера" if time == 1 else "%i %s назад" % (time, _get_days(time))
    if ideal is None:
        return "%s (%s)" % (result, when)
    diff = value/ideal * 100
    add_space = " " if diff < 100 else ""
    return "%s ... %s%.1f %% от идеала ... (%s)" % (result, add_space, diff, when)


def _wt(name, flag=0):
    return "\t%.9s: __._ %s" % (name+" "*2, "%" if flag else "кГ")


def _get_old_value_and_time(value, slots):
    result = value
    time = 1
    if not result:
        time = 0
        for item in reversed(slots):
            time += 1
            if item:
                result = item
                break
    return result, time


def _get_days(x):
    last_num = str(x)[-1]
    if last_num == "1":
        return "день"
    elif last_num in ["2", "3", "4"]:
        return "дня"
    return "дней"


# BASE TEMPLATES
GOOD = "\tСегодня вы сделали хорошего:%s" % (_li(3))
NEW = "\tСегодня вы узнали и выучили новое:%s" % (_li(3))
WEIGHT = "%s\n%s\n%s\n%s" % (_wt('Мой вес'), _wt('Мои мышцы'), _wt('Мой жир',1), _wt('Моя вода',1))
