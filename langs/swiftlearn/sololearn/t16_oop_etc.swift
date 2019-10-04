/*
    !!! NOT RUNNING !!!

    Object Oriented Programming - methods, subscripts, inheritance, initialization, deinitialization

    !!! NOT RUNNING !!!
*/

class Counter {
    var count = 0

    func increment() {
        count += 1
    }

    func incrementBy(_ amount: Int) {
        count += amount
    }

    func reset() {
        count = 0
    }
}

let counter = Counter()
print(counter.count)

counter.increment()
print(counter.count)

counter.incrementBy(5)
print(counter.count)

counter.reset()
print(counter.count)


class Student {
    var age = 0

    func printAge() {
        print(age)
    }
}

var st = Student()
st.printAge()


// Self

struct Point {
    var x = 0.0, y = 0.0

    func isToTheRight(x: Double) -> Bool {
        return self.x > x
    }

    mutating func moveByX(dX: Double, dY: Double) {
        x += dX
        y += dY
    }
}

var p = Point()
print(p.isToTheRight(x: 1.1), p)

p.moveByX(dX: 2.2, dY: 2.4)
print(p)


struct Person{
    var age = 0
    mutating func AddOne() {
        age += 1
    }
}

var pers = Person()
pers.AddOne()
print(pers.age)


class SomeClass {
    static func someTypeMethod() {
        print("I amd a type method")
    }
}

SomeClass.someTypeMethod()


// Subscripts

struct TimesTable {
    let multiplier: Int

    subscript(index: Int) -> Int {
        return multiplier * index
    }
}

let threeTimesTable = TimesTable(multiplier: 3)
print(threeTimesTable[5])


struct Matrix {
    let rows: Int, columns: Int
    var grid: [Double]

    init(rows: Int, columns: Int) {
        self.rows = rows
        self.columns = columns
        grid = Array(repeating: 0.0, count: rows * columns)
    }

    subscript(row: Int, column: Int) -> Double {
        get {
            return grid[(row * columns) + column]
        }
        set {
            grid[(row * columns) + column] = newValue
        }
    }
}

var matrix = Matrix(rows: 3, columns: 2)
matrix[0, 1] = 1.5
matrix[1, 0] = 3.2
print(matrix.grid)


struct Test {
    var num = 0

    subscript(tmp: Int) -> Int {
        return tmp * num
    }
}

var t = Test(num: 8)
print(t[2])


// inheritance

class Vehincle {
    var currentSpeed: Double = 0.0
    var desc: String {
        return "traveling at \(currentSpeed) mph"
    }

    func makeNoise() {
        // do nothing
    }
}


class Bicycle : Vehincle {
    var hasBasket = false
}

let bicycle = Bicycle()
bicycle.hasBasket = true
bicycle.currentSpeed = 25.0

print("Bicycle: \(bicycle.desc)")


class Tandem : Bicycle {
    var currNumOfPassengers = 0
}

let tandem = Tandem()
tandem.hasBasket = true
tandem.currNumOfPassengers = 2
tandem.currentSpeed = 20.0

print("Tandem: \(tandem.desc)")


// Overriding

class Train : Vehincle {
    override func makeNoise() {
        print("Choo Choo")
    }
}


class Car : Vehincle {
    var gear = 1

    override var desc: String {
        return super.desc + " in gear \(gear)"
    }
}

let train = Train()
train.makeNoise()

let car = Car()
print("Car: \(car.desc)")


class Human {
    var name: ""

    func hello() {
        print("Hi from Person!")
    }
}


class Woman : Human {
    var year = 0
    override func hello() {
        print("Hi from Woman!")
    }
}

let woman = Woman()
woman.hello()


// initialization

struct Fahrenheit {
    var temp: Double
    init() {
        temp = 32.0
    }
}

var f = Fahrenheit()


struct Celsius {
    var tempInCelsius: Double

    init(fromFahrenheit fahrenheit: Double) {
        tempInCelsius = (fahrenheit - 32.0) / 1.8
    }

    init(fromKelvin: kelvin: Double) {
        tempInCelsius = kelvin - 273.15
    }
}

let boilingPoint = Celsius(fromFahrenheit: 212.0)
let freezingPoint = Celsius(fromKelvin: 273.15)

print(boilingPoint.tempInCelsius, freezingPoint.tempInCelsius)


struct Size {
    var width = 0.0, height = 0.0
}

let twoByTwo = Size(width: 2.0, height: 2.0)
print(twoByTwo)


class Size2 {
    var width: Double, height: Double

    init(w: Double, h: Double) {
        width = w
        height = h
    }

    deinit {
        print("Deinit is called")
    }
}

let threeByThree = Size(w: 3.0, h: 3.0)
print("Width: \(threeByThree.width)\nHeight: \(threeByThree.height)")

threeByThree = nil


class NewPerson {
    var age: Int
    init(a: Int) {
        age = a
    }
}

let p1 = NewPerson(a: 18)
let p2 = NewPerson(a: 22)

print(p1.age, p2.age)


// Required initialization

class SomeClass2 {
    var a: Int
    required init() {
        self.a = 1
    }
}


class SomeSubclass : SomeClass2 {
    required init() {
        self.a = 2
    }
}

let some = SomeSubclass()
print(some.a)
