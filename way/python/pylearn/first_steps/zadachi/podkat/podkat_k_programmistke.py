#! Подкат к программистке.


# Вариант с инпутом.

def podkat():
    a = str(input("Привет, солнце, посветишь для меня сегодня ?): "))
    right_answers = ("да конечно посвечу афк пошли мяф го игого"
        "гоу хочу хотела красава мечтаю давай ага супер пойдём")
    if a.lower() in right_answers.lower():
        return print('Сегодня кому-то повезло :)')
    else:
        while a.lower() not in right_answers.lower():
            a = str(input("Некорректный ответ. Повторите попытку: "))
        return print("Столько времени потеряли зря :) Могли бы уже зажигать!")

if __name__ == "__main__":
    podkat()
