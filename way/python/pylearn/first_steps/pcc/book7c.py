#! Занятие по книге Python Crash Course, chapter 7, "User Input and
# While Loops".
# Занятие третье.

# Не модифицировать листы внутри цикла for, использовать while.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:    # Пока лист не пустт.
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in sorted(confirmed_users):
    print(confirmed_user.title())

# Удаление специфичных values.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Заполнение словаря внутри цикла.

responses = {}
poll = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Name your president for next 6 years! ")
    responses[name] = response
    repeat = input("Anyone else is going to take the pole?"
                   "yes/no")
    if repeat.lower() == 'yes':
        continue
    elif repeat.lower() == 'no':
        print("Thank you")
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " votes for " + response)
    if response in poll:
        poll[response] += 1
    else:
        poll[response] = 1
print("\n Голоса распределились:\n")
for response, votes in poll.items():
    print(response.title(), ' - ', str(votes))


# Try it yourself 7-8, 7-9.  Deli, No Pastrami.

sandwich_orders = ['hamburger', 'pastrami', 'cheeseburger', 'tunburger',
                   'pastrami', 'doublecheese', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'd like to " + sandwich)
    if sandwich == 'pastrami':
        print("Sorry, we out of " + sandwich + " today.")
    else:
        finished_sandwiches.append(sandwich)
        print("I made your " + sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)


# Try it yourself 7-10.  Dream Vacation.

dreams = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your dream? ")
    dreams[name] = response
    repeat = input("Does anyone else? Yes/no")
    if repeat == 'yes':
        continue
    elif repeat == 'no':
        print("Thanks")
        polling_active = False
    else:
        print("Stop joking around")
        break

print(dreams)
