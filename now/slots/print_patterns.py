LINE = "\n\n"
SEP_LENGTH = 80

def separator(length=False):
    return LINE + "-"*(length or SEP_LENGTH) + LINE

J_BASIC = 60  # width of basic activities column
J_VIDEO = 40  # width of video activities column

def smoke(i):
    def get_days(x):
        last_num = str(x)[-1]
        if last_num == "1":
            return "день"
        elif last_num in ["2", "3", "4"]:
            return "дня"
        return "дней"
    return "\tЯ не курю уже %i %s" % (i, get_days(i)) if i > 0 else "Зря я покурил"

def _li(num):
    return "\n\t\t" + "\n\t\t".join(["%i __________________" % i for i in range(1, num+1)])

def _wt(name):
    return "\t%s: __._ кГ (__._ %)"

GOOD = "\tСегодня я сделал хорошего:%s" % (_li(3))
NEW = "\tСегодня я узнал и выучил новое:%s" % (_li(3))

WEIGHT = "%s\n\n\t%s\n\t%s\n\t%s" % (_wt('Мой вес'), _wt('Мои мышцы'), _wt('Мой жир'), _wt('Моя вода'))
