# функция возвращает строку с чётными либо нечётными словами (флаг - 2 аргумент)

def jump_one(string, flag=False):
    words = string.split(' ')
    start = 0
    new_str = ""
    if flag:
        start += 1
    for i in range(start, len(words), 2):
        new_str += words[i] + " "
    return new_str.strip()


if __name__ == '__main__':
    print(jump_one("этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"))
