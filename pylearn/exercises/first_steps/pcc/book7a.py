#! Занятие по книге Python Crash Course, chapter 7, "User Input and
# While Loops".
# Занятие первое.

message = input("Tell me something and I'll repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# Multiline string:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# Работа с числительными:
age = input("How old are yo? ")
print(int(age) >= 18)

height = input("How tall are you, in inches? ")

if int(height) >= 36:       # 1 inch = 2.54 sm.
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator:

number = input("Enter a number, and I'll tell you if it's even or odd: ")

if int(number) % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# In Python 2.7 " input() " interprets user's input as Python code and
# attempts to rin the input.  For string input use " raw_input() ".


# Try it yourself 7-1.  Rental Car.

rental = input("What kind of rental car you would like?")
print("Let's me see if I can find you a " + rental + ".")


# Try it yourself 7-2.  Restaurant Seating.

tables, free_sits = 32, 7
sit = input("How many people in your dinner group? ")

if int(sit) <= free_sits:
    print("Your table is ready!")
    free_sits -= int(sit)
elif  free_sits < int(sit) < tables:
    print("Regretfully You'll have to wait for a table for a while.")
else:
    print("Our restraunt is not for that kind of purposes")


# Try it yourself 7-3.  Multiples of Ten.

number = input("Tell me a number: ")

if int(number) % 10 == 0:
    print("Number", number, "is multiple of 10! Oh eh.")
else:
    print("Number", number, "isn't multiple of 10 .. Heh..")
