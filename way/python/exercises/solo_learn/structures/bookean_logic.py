print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)

if (1 == 1) and (2 + 2 > 3):
    print("True")
else:
    print("False")


print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)

age = 1
money = 500
if age > 18 or money > 100:
    print("Welcome")


print(not 1 == 1)
print(not 1 > 7)

if not True:
    print("1")
elif not(1 + 1 === 3):
    print("2")
else:
    print("3")


# Operator Precedence

print(False == False or True)
print(False == (False or True))
print((False == False) or True)

if 1 + 1 * 3 == 6:
    print("Yes")
else:
    print("No")


"""
    OPERATOR PRECEDENCE LIST

    **                          exponentiation
    ~, +, -                     complement, unary plus and minus (+@, -@)
    *, /, %, //                 multiply, divide, modulo, floor division
    +, -                        addition, subtraction
    >>, <<                      bitwise shift (right, left)
    &                           bitwise AND
    ^                           bitwise XOR
    |                           bitwise OR
    in, not in, is not,         membership and identity operators    ...
... <, <=, >, >=, !=, ==        comparison operators, equality operators
    not                         boolean NOT
    and                         boolean AND
    or                          boolean OR
    =,%=,/=,//=,+=,-=,*=,**=    assignment operators

"""

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
    print("Yes")
elif x > y:
    print("No")
