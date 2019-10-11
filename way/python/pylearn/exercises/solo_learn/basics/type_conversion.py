print("2" + "3")
print(int("2") + int("3"))
print(int("3" + "4"))

try:
    print(float(input("Input a number: ")) + float(input("Input a number: ")))
except ValueError:
    print("Your input is not a number")

try:
    print(float("210" * int(input("Enter a number: "))))
except ValueError:
    print("Your input is not a number")
