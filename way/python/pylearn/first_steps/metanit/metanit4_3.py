#! Работа с материалами Metanit, глава 4, часть 3. Файлы CVS.

# Каждая строка в файле "csv" представляет отдельную запись или строку,
# которая состоит из отдельных столбцов, разделенных запятыми.
# .csv = Comma Separated Values.  В python используется модуль csv
# для работы с этим форматом:

import csv

filename = "../d020/users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

# При открытии файла на запись в качестве параметра указывается значение
# ' newline="" ' - пустая строка позволяет корректно считывать строки из
# файла вне зависимости от операционной системы.  Для записи нам надо
# получить объект ' writer ', который возвращается функцией
# ' csv.writer(file) '.  В эту функцию передаётся открытый файл.  Запись
# производится с помощью метода ' .writerows(записываемое) '
# [.writerow() если одна запись].

with open(filename, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

# Для чтения файла нужно создать объект ' reader ':

with open(filename, 'r', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])


# Работа со словарями.

# Модуль csv имеет специальные дополнительные возможности для работы со
# словарями.  В частности, функция ' csv.DictWriter() ' возвращает
# объект ' writer ', который позволяет записывать в файл.  А функция
# ' csv.DictReader() ' возвращает объект ' reader ' для чтения из файла.
# Например:

filename = "../d020/users2.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": 'Alice', "age": 23},
    {"name": "Bob", "age": 34}
]

with open(filename, 'w', newline="") as file:
    colums = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=colums)
    writer.writeheader()        # Запись заголовков столбцов.
    writer.writerows(users)
    user = {"name": "Sam", "age": 41}
    writer.writerow(user)

with open(filename, 'r', newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], "-", row["age"])

# Запись строк производится теми же метожами, но теперь каждая строка
# представляет собой отдельный словарь, кроме того, производится запись
# заголовков столбцов при помощи медода ' .writeheader() ', а в метода
# ' csv.DictWriter() ' в качестве второго параметра передаётся набор
# столбцов.  При чтении строк, используя названия столбцов, можно
# обратиться к отдельным значениям внутри строки.
