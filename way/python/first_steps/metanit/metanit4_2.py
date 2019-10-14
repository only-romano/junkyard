#! Работа с материалами Metanit, глава 4, часть 2. Текстовые файлы.

# Запись в текстовый файл.

with open("../d020/file.txt", "w") as file:
    file.write("Hello world")

with open("../d020/file.txt", 'a') as file:
    file.write("\nGood bye, world")

with open("../d020/file.txt", 'a') as file:
    print("\nHello, world!", file = file)


# Чтение файла.

# reedline(): считывает одну строку из файла.
# read(): считывает все содержимое файла в одну строку.
# readlines(): считывает все строки файла в список.

with open("../d020/file.txt", 'r') as file:
    for line in file:
        print(line, end="")

with open("../d020/file.txt", 'r') as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

with open("../d020/file.txt", 'r') as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

with open("../d020/file.txt", 'r') as file:
    content = file.read()
    print(content)

with open("../d020/file.txt", 'r') as file:
    content = file.readlines()
    str1 = content[0]
    str2 = content[1]
    print(str1, end="")
    print(str2)

filename = "../d020/file.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
    print(text)


filename = "../d020/file.txt"
messeges = list()

for i in range(4):
    message = input("Введите строку" + str(i+1) + ": ")
    messeges.append(message + "\n")

with open(filename, 'a') as file:
    for message in messeges:
        file.write(message)

print("Считанные сообщения")
with open(filename, 'r') as file:
    for message in file:
        print(message, end="")
