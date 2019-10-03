#! Занятие по книге Python Crash Course, chapter 10, "Files and
# Exceptions".  Занятие пятое.


# Хранение информации.  JSON (Java Script Object Notation) модуль.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '../day/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)   # Метод для хранения информации.

with open(filename) as f_obj:
    numbers = json.load(f_obj)  # Метод для загрузки информации.

print(numbers)


# Рефакторинг + Try it yourself 10-11, 10-12, 10-13.


def get_stored_usernames(filename):
    """
    Load the usernames if it has been stored previously.
    """
    try:
        with open(filename) as f_obj:
            usernames = json.load(f_obj)
    except FileNotFoundError:
        with open(filename, 'w') as f_obj:
            usernames = {}
            json.dump(usernames, f_obj)
    return usernames


def store_new_username(filename, username, favorite_n):
    """Stores new username."""
    with open(filename, 'r') as f_obj:
        usernames = json.load(f_obj)
    usernames[username] = favorite_n
    with open(filename, 'w') as f_obj:
        json.dump(usernames, f_obj)


def usernames():
    """
    Greet the user by name.
    """
    filename = '../day/username.json'
    username = input("What is your name? ")
    if username in get_stored_usernames(filename):
        print("Welcome back, " + username + "!\n" + "Your number is " +
              get_stored_usernames(filename)[username] + '!')
    else:
        favorite_n = input("What is your favorite number? ")
        store_new_username(filename, username, favorite_n)
        print("We'll remember you when you come back, " + username + "!")
    return 'Success'


usernames()
