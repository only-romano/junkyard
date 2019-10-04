#! Занятие по книге Python Crash Course, chapter 7, "User Input and
# While Loops".
# Занятие второе.

# The While Loop.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Tell me programm.

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\n(enter 'quit' to end the program): "

message = input(prompt)
while message != 'quit':
    print(message)
    message = input(prompt)
print("End of programm.")


# Использование flag.

active = True
message = input(prompt)
while active:
    if message == 'quit':
        active = False
        print("End of programm.")
    else:
        print(message)
        message = input(prompt)


# Использование break.

message = input(prompt)
while True:     # Infinite loop unless it reaches a break statement.
    if message == 'quit':
        break
    else:
        print(message)
        message = input(prompt)


# Использование continue в цикле.  Код выполняется только если не
# исполняется continue, иначе же следующий шаг цикла.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# Avoiding Infinite Loops.

x = 1
while x <= 5:
    print(x)
    x += 1      # Без этой строки цикл будет вечным.  Ctrl + C stops it.


# Try it yourself 7-4.  Pizza toppings.

topping = input("What toppings you would like to see on your pizza?\n"
                "Say 'stop' to finish your pizza.\n")

while True:
    if topping.lower() == 'stop':
        print("Your pizza's finished")
        break
    print("Adding", topping)
    topping = input("What else? Or you want to stop?\n")


# Try it yourself 7-5, 7-6, 7-7.  Movie tickets.

message = "Hello! Prices depends of your age. How old are you?\n"
price = input(message)

active = True
while active:
    if price.lower() == 'over':
        print("Goodbye.")
        active = False      # Убрать эту строку и T-i-y 7-7.
    elif int(price) < 3:
        print("For persons under age of 3 ticket is free!")
    elif 2 < int(price) < 13:
        print("For your ages price is $10")
    elif int(price) > 12:
        input("For your ages price is $15 Is it over or anyone else,"
              "how old is it?")
    price = input("")
