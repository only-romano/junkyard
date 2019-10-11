/*
    Basic operators app

    unary operators: -a, !b etc.
    binary operators: a + b, a - b etc.
    ternary operator: (a ? b : c)
*/

let b = 7
var a: Int
a = b + 28
print("Simple operations results: ", a, a + b, a - b, a * b, a / b)
print("String concatenation result: ", "Hello, " + "world!")

a = 4 + 2
var c = 15 - a
var result = a / (c - a)
print(result, "\nRemainder operator:", c % a)

a = 10; c = 3
var d = a % (a - c)
print(d)


// Compound operator example
a = 1
a += 2
print("Now \"a\" is equal to \(a)")

a = 0; c = a + 1
c + 3
print(c)


// Comparison Operators
print("1 == 1 is \(1 == 1)\n2 != 1 is \(2 != 1)\n2 > 1 is \(2 > 1)\n")
print("1 < 2 is \(1 < 2)\n1 >= 1 is \(1 >= 1)\n2 <= 1 is \(2 <= 1)")


// Ternary operator
var gender = 0
print("My gender is \(gender == 0 ? "male" : "female")")

let height = 40
let isCheck = true
let rowHeight = height + ( isCheck ? 50 : 20 )
print("Some height is \(rowHeight)")


// Range operator
var rangeClosed = 1...3  // closed range operator, value 1,2,3
var rangeHalfOpen = 1..<3  // half-open range operator, value 1,2
print("Closed range: \(rangeClosed)\nHalf-open range: \(rangeHalfOpen)")


// Logical operators
var name = true
var pass = false
name && pass ? print("Success") : print("Fail")
