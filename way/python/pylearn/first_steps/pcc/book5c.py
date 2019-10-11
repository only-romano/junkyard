#! Занятие по книге Python Crash Course, chapter 5, "if statesments"
#! Занятие третье.

# Using "if" Statements with Lists.

available_toppings = ('mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese',
                      'french fries']

print("What do you want for topping today?\n")

if requested_toppings:      # Понял что пустой лист возвращает "False".
    for requested_topping in requested_toppings:
        print(requested_topping.title() + "!")
        if requested_topping in available_toppings:
            if requested_topping is 'green peppers':
                print("Sorry, we're out of green peppers right now.\n")
            else:
                print("Adding", requested_topping + ".\n")
        else:
            print("Sorry, we don't have " + requested_topping + " at all.\n")
else:
    print("Are you sure you want a plain pizza?")

print("Finished making your pizza!\n")

# P.S.: assumption = предположение.


# Try it yourself 5-8, 5-9, 5-10.  Hello Admin:

login_users = {'Bobby': 132, 'Dick': 1, 'Michael': 2787, 'Helen': 14,
               'JR': 2222}

new_users = {'Alice': 2788, 'dick': 2789, 'Caroline': 2790, 'Sexy': 2791,
             'helen': 2792}

for new_user in new_users:
    check = 1
    for user in login_users:
        if new_user.lower() == user.lower():
            check -= 1
    if check < 1:
        print("Username", new_user, "is already exist.")
    else:
        newbie = {new_user: new_users.get(new_user)}
        login_users.update(newbie)
        print(new_user, "welcome aboard!")

if login_users:
    for user in login_users:
        if login_users.get(user) == 1:
            print("Whaazzzzzuup, " + user + "! Admin, you're finally here!")
        else:
            print("Hello,", user + ", how do you do?")
else:
    print("Noone here :(  We need to find some users!")


# Try it yourself 5-11.  Ordinal numbers:

numbers = list(range(1, 10))
final_string = ""

for number in numbers:
    if number is 1:
        final_string += str(number) + "st"
    elif number is 2:
        final_string += " " + str(number) + "nd"
    elif number is 3:
        final_string += " " + str(number) + "rd"
    else:
        final_string += " " + str(number) + "th"
print(final_string)
