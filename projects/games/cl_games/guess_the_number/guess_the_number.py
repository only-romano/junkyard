# Игра угадай число
from random import randint
SAVEFILE_PATH = "data/save.txt"

def load_savefile():
    saves = {}
    with open(SAVEFILE_PATH) as savefile:
        for line in savefile:
            if len(line):
                save = line.split(',')
                name = save[0]
                score = int(save[1])
                saves[name] = score
    return saves


def update_savefile(saves, name, score):
    saves[name] = score
    return saves


def write_savefile(saves):
    with open(SAVEFILE_PATH, "w") as savefile:
        for key in saves:
            savefile.write(key + "," + str(saves[key]) + ",\n")


SAVES = load_savefile()

print("Привет, это игра напёрсточки, представьтесь пожалуйста!")
name = input("меня зовут ... ")
score = 100
print("Очень приятно,", name)

flag_name = False
for key in SAVES:
    if key == name:
        score = SAVES[name]
        flag_name = True

if flag_name:
    print("Рад видеть вас снова! Скучал по вас. Напоминаю, на вашем счету %s кредитов" % score)
    print("Если вы хотите сбросить прогресс и вернуться к стартовым 100 кредитам, введите \"reset\" (без кавычек)")
    reset = input("сброс: ")
    if reset.lower() == "reset":
        score = 100
        print("Сделано! Теперь у вас снова 100 кредитов! Самое мирное казино в мире.")
else:
    print("Добро пожаловать в наше казино напёрсточков. Мы дарим вам начальные 100 кредитов!")

print("\n\tПРАВИЛА ИГРЫ:\n")
print("Каждый раунд вы делаете ставку, под каким из трёх напёрстков будет шарик, если вы угадали - ставка удваивается, если же не угадали - то, увы, вы проиграли ставку.")
print("Начнём?\n\n")

words = [
    "Буль буль буль буль буль! Готово!",
    "Шалом, товарищи, шарик занял своё место!",
    "Бум, это стук моего сердца о шарик!",
    "Чтож, шарик занял своё место!",
    "Кукарача-чача-мачо",
    "Приехали!"
]

init_score = score

while True:
    if score == 0:
        break
    print(name, ", ваш счёт - %s кредитов" % score)
    odd = 0
    try:
        odd = int(input("Делайте вашу ставку! - "))
    except Exception:
        odd = 1
    if odd >= score:
        print("Вы идёте ва-банк!")
        odd = score
    score = score - odd
    print("\nСпасибо, ставки сделаны! Шарик запущен под %s напёрсток!" % randint(1, 3))
    print("Кручу верчу, чтобы вы победили, %s, хочу!" % name)
    ball = randint(1, 3)
    print(words[randint(0, 5)])
    answer = input("Итак! Ваш ответ, " + name + ", (1, 2 или 3) - ")
    try:
        answer = int(answer)
    except Exception:
        answer = 0
        print("Ну же, посерьёзнее, я же спрашивал 1, 2 или 3, а не номер вашей кредитки...")
    if answer == ball:
        score = score + odd * 2
        print("Ура, ура, ура! Вы выйграли! Вы удвоили вашу ставку! Теперь ваш счёт составляет - %s кредитов!" % score)
    else:
        print("Увы... Вы не угадали.. Но не отчаивайтесь, повезёт в следующий раз!")

    print("Будем ли играть дальше? (введите любую букву или число для продолджения) Чтобы закончить игру оставьте поле для ввода пустым и нажмите Enter")
    finish = input("играем - ")
    if not len(finish):
        break

print("Благодарим вас за игру, %s!" % name)

if init_score > score:
    print("Вы сегодня в небольшом минусе, вы проиграли %s кредитов" % (init_score - score))
elif init_score < score:
    print("Поздравляю! Вы сегодня выйграли %s кредитов!" % (score - init_score))
else:
    print("Вы остались при своих.")

print("Ваш счёт - %s кредитов!" % score)
print("\nЧтобы продолжить игру с вашим счётом не забывайте своё имя! Регистр выжен!")
print("Досвидания, %s!" % name)

SAVES = update_savefile(SAVES, name, score)
write_savefile(SAVES)
