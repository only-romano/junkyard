// Булевый тип данных, логические операции
var isEnabled: Bool = true

var a = 10
var b = 10
var d = 8
print(a == b, a == d, a != b, a != d, a > d, a > b, d < a, a < b, a >= b, d >= a)

var result = !isEnabled
var isAlive = true
print(isEnabled && isAlive, isEnabled && isAlive && result, isAlive || result, result || result)

b = 12
print(a > 8 && b < 10, a > 8 || b < 10)
