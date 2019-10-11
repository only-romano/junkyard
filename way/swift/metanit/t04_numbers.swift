// Числовые типы данных
let a = 2    // Int
let b = 2.0  // Double

let n: Int8 = 10     // inplicit convertion
let x: Float = 3.14  // same as above

// var age: UInt8 = 1000  // type sizing error

// Constants:
var minInt16 = Int16.min
var maxInt16 = Int16.max
var minUInt16 = UInt16.min
var maxUInt16 = UInt16.max

// Binaries, decimal, hex, octal
let decimalInt = 10
let binaryInt = 0b1000001
let octalInt = 0o16
let hexInt = 0xAF15

var decimalFloat = 1.25e-2
var hexFloat = 0xFp-2


print(maxInt16 + minInt16, minUInt16 + maxUInt16)
print(Double(x) - b, Int8(a) * n)
print(decimalInt, binaryInt, octalInt, hexInt, decimalFloat, hexFloat)

// Division of integers and floats
print(n / Int8(x), Float(n) / x, n % Int8(x))

var d = 6
var s = 10
var c = Double(s) / Double(d)
print(s + d, s - d, s * d, s / d, s % d, c) // comment
print(s & d, s | d, s ^ d, ~s, s << d, s >> d)
