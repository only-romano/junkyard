/*
    Functions app
*/

func sayHello(personName: String) -> String {
    let greeting = "Hello, " + personName + "!"
    return greeting
}

print(sayHello(personName: "Katik"))


func sq(num: Int) -> Int {
    return num * num
}

print(sq(num: 2))


// Multiple input parameters

func rangeLength(start: Int, end: Int) -> Int {
    return end - start
}

print(rangeLength(start: 2, end: 7))


func sayHelloWorld() -> String {
    return "Hello World!"
}

print(sayHelloWorld())


func mySum(n1: Int, n2: Int) -> Int {
    var sum = n1 + n2
    return sum
}

print(mySum(n1: 10, n2: 12))


// Functions without return values

func sayHi(name: String) -> Void {
    print("Hi, \(name)")
}

sayHi(name: "Katik")


// Multiple return values

func minMax(array: [Int]) -> (min: Int, max: Int) {
    var currMin = array[0]
    var currMax = array[0]

    for value in array[1..<array.count] {
        if value < currMin {
            currMin = value
        } else if value > currMax {
            currMax = value
        }
    }

    return (currMin, currMax)
}

let bounds = minMax(array: [4, -4, 1, 88, 7, 42])
print("Min is \(bounds.min) and max is \(bounds.max)")


func test(n1: Int, n2: Int) -> (a: Int, b: Int) {
    return ((n1 - n2), (n1 + n2))
}

let tmp = test(n1: 8, n2: 3)
print(tmp.b)


func sayHello2(to p1: String, and p2: String) -> String {
    return "Hello \(p1) and \(p2)"
}

print(sayHello2(to: "Tom", and: "Jerry"))


func myFunc(a n1: Int, b n2: Int) -> Int {
    return n1 * n2
}

print(myFunc(a: 11, b: 27))


// Default parameters and variadic parameters

func someFunc(p1: Int = 12) -> Int {
    return p1 * p1
}

print(someFunc(p1: 2), someFunc())


func arithmeticMean(numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }

    return total / Double(numbers.count)
}

print(arithmeticMean(numbers: 2, 4, 3, 6, 11))


// In-out parameters

func swapInts(a: inout Int, b: inout Int) {
    let tempA = a
    a = b
    b = tempA
}

var someInt = 3
var anotherInt = 107
print("Before swap: a = \(someInt); b = \(anotherInt)")

swapInts(a: &someInt, b: &anotherInt)
print("After swap: a = \(someInt); b = \(anotherInt)")


func calc(num: inout Int) {
    num = num * 5
}

var a = 8
print(calc(num: &a))


// Functions types

func addInts(_ a: Int, _ b: Int) -> Int {
    return a + b
}


func multiplyInts(_ a: Int, _ b: Int) -> Int {
    return a * b
}


func printByeWorld() -> Void {
    print("Goodbye World")
}

print(addInts(3, 5), multiplyInts(3, 5))
printByeWorld()

var mathFunction: (Int, Int) -> Int = addInts
print("Result: \(mathFunction(2, 3))")


func myFunc2(s1: String) -> Int {
    return s1.characters.count
}

var t: (String) -> Int = myFunc2
print(t("Hello"))


// Function types as parameter and return types

func printResult(mathFunc: (Int, Int) -> Int, a: Int, b: Int) {
    print("Result: \(mathFunc(a, b))")
}

printResult(mathFunc: addInts, a: 3, b: 5)


func plus(input: Int) -> Int { return input + 1 }
func minus(input: Int) -> Int { return input - 1 }


func chooseFunc(flag: Bool) -> (Int) -> Int {
    if flag {
        return plus
    } else {
        return minus
    }
}

print(chooseFunc(flag: true)(100))


// Nested functions

func chooseFunc2(flag: Bool) -> (Int) -> Int {
    func double(input: Int) -> Int { return input * 2 }
    func tripple(input: Int) -> Int { return input * 3 }

    if flag {
        return double
    } else {
        return tripple
    }
}

print(chooseFunc2(flag: false)(15))


// Recursion

func factorial(n: Int) -> Int {
    return n == 0 ? 1 : n * factorial(n: n - 1)
}

print(factorial(n: 6))


func fib(n: Int) -> Int {
    return n < 2 ? n : (fib(n: n-1) + fib(n: n - 2))
}

print(fib(n: 8))
