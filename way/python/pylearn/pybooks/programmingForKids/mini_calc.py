try:
    a = int(input("a = "))
except Exception:
    a = 4

try:
    b = int(input("b = "))
except Exception:
    b = 2

op = input('add/sub/mul/div: ')

if op == 'add' or op == 'a':
    c = a + b
elif op == 'sub' or op == 's':
    c = a - b
elif op == 'mul' or op == 'm':
    c = a * b
elif op == 'div' or op == 'd':
    c = a / b
else:
    c = 'There is no such command. Lol.'

print("Answer is", c)
