/*
    Loops app
*/

// While loops
var a = 2
var b = 3
while a < b {
    a += 1
}
print(a)


var x = 10
while x > 0 {
    x -= 1
}
print(x)

repeat {
    x -= 1
} while x > 0
print(x)

var i = 1, n = 3
repeat {
    i += 1
} while i < n
print(i)


// For loops
for index in 1...5 {
    i += index
}
print(i)

for index in 1...3 {
    i -= index * 3
}
print(i)


// Control transfer statements
var str = ""
for num in 1...10 {
    if num % 2 == 0 {
        continue
    }
    str += "\(num) "
}
print(str)

a = 10
b = 7
while a > 0 {
    if (a < b) {
        break
    }
    a -= 1
}
print(a)

a = 5
var letter = "X"
switch a {
    case 1:
        letter = "A"
    case 2:
        letter = "B"
    default:
        break
}
print(letter)

x = 0
while x < 10 {
    if x == 5 {
        break
    }
    x+=1
}
print(x)


// Fallthrough
let myInt = 5
var desc = "The number \(myInt) is"
switch myInt {
    case 2, 3, 5, 7, 11, 13, 17, 19:
        desc += " a prime number, and also"
        fallthrough
    default:
        desc += " an integer"
}
print(desc)
