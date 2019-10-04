print('print("print")')
print(input("Input something please: ") or "Nothing...")

try:
    print(int(input("Input a number: ")))
except BaseException:
    print("Your input was not a number...")
