import csv, os, pickle, random, shelve


def account_calculate(rate, money, month):
  print("Sum:", money, "\tProcent:", rate, '\tPeriod:', month, "\tAccount",
    calculate_income(rate, money, month))


def binary_reader():
  filename = "user.dat"
  name = "Kato"; age = 27;
  with open(filename, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

  with open(filename, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Name:", name, "\tAge:", age)


def calculate_income(rate, money, month):
  if money <= 0:
    return 0
  for i in range(1, month+1):
    money = round(money + money * rate / 100 / 12, 2)
  return money


def count_words():
  filename = 'newfile.txt'
  if not os.path.exists(filename):
    print("Where is no such file")
  else:
    words = get_words(filename)
    words_dict = get_words_dict(words)
    print("Words: %d, Unique words: %d" % (len(words), len(words_dict)))
    print("All words:")
    for word in words_dict:
      print(word.ljust(20), words_dict[word])


def csv_reader():
  filename = 'users.csv'
  users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
  ]
  with open(filename, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)
    user = {"name": "Sam", "age": 41}
    writer.writerow(user)

  with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row["name"], "-", row["age"])


def division(num1, num2):
  try:
    if num2 == '3':
      raise Exception("Dododo, tratata")
    print(int(num1)/int(num2))
  except ValueError as e:
    print("Value Error - not integer, info:", e)
  except ZeroDivisionError:
    print("Zero Division")
  except Exception as e:
    print("Unknown Error:", e)


def exchange(usd_rate, money):
  return round(money/usd_rate, 2)


def exchange_money(money):
  usd = 57; euro = 60; currency = usd;
  if currency == euro:
    cash = round(money/euro, 2)
  elif currency == usd:
    cash = round(money/usd, 2)
  else:
    cash = 0
  print(cash)


def factorial_for(num):
  factorial = 1
  for i in range(1, num+1):
    factorial *= i
  return  factorial


def factorial_rec(num):
  if num == 1:
    return 1
  return num * factorial_rec(num-1)


def factorial_while(num):
  i = 1
  factorial = 1
  while i <= num:
    factorial *= i
    i += 1
  return factorial


def get_circle_square(radius):
  global PI
  PI = 3.14
  print("Square of circle with radius", radius, "is", radius**2 * PI)


def get_words(filename):
  with open(filename, encoding="utf8") as file:
    text = file.read()
  return text.replace("\n", " ").replace(",", "").replace(".",
    "").replace("?", "").replace("!", "").replace(":",
    "").replace(";", "").replace("'", "").replace("\"",
    "").lower().split()


def get_words_dict(words):
  words_dict = dict()
  for word in words:
    if word in words_dict:
      words_dict[word] = words_dict[word] + 1
    else:
      words_dict[word] = 1
  return words_dict


def multiply_matrix():
  for i in range(1, 11):
    for j in range(1, 11):
      print(i*j, end="\t")
    print("\n")


def shelve_reader():
  filename = 'shelvefile'
  with shelve.open(filename) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
  with shelve.open(filename) as states:
    print(states["London"], states["Madrid"])


def shuffle_list():
  numbers = []
  for i in range(0, 10):
    numbers.append(random.randint(1, 100))
  random.shuffle(numbers)
  print(random.choice(numbers))


def sum_of_nums(*params):
  result = 0
  for n in params:
    result += n
  return result


def test_list_methods():
  list1 = [1, 4, 5, 'test', 'reverse']
  list2 = ['testing', 2, 'rev', 4, 1]
  try:
    list1.append('new element')
    list1.insert(4, 'temp_element')
    list1.remove('temp_element')
    list2.clear()
    list2 = list1[:]
    list2.append('new2')
    print('Test passed', list1, list2)
  except Exception as e:
    print('Something wrong:', e)
