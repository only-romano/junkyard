/*
    Object Oriented Programming, Classes and Structures app
*/

struct Resolution {
    var width = 0
    var height = 0
}


class VideoMode {
    var resolution: Resolution
    var interlaced = false
    var frameRate = 0.0

    init(res: Resolution = Resolution()) {
        self.resolution = res
    }
}


class Student {
    var name: String = ""
    var age: Int = 0
}


let vga = Resolution(width: 640, height: 480)
let someVideoMode = VideoMode(res: vga)
let someStudent = Student()
print(vga, someVideoMode.resolution)


struct Size {
    var width = 10
    var height = 42
}

let mySize = Size()
print(mySize.width)


// Differences of classes vs. structures

let hd = Resolution(width: 1920, height: 1080)
var cinema = hd
cinema.width = 2048

print("While cinema width is changed and now is \(cinema.width)")
print("Hd is still \(hd.width) pixels wide")

let tenEighty = VideoMode()
tenEighty.resolution = hd
tenEighty.interlaced = true

let alsoTenEighty = tenEighty
alsoTenEighty.interlaced = false
print("Both: \(tenEighty.interlaced) and \(alsoTenEighty.interlaced)")


class Test {
    var num = 17
}

let a = Test()
let b = a
b.num = 42
print(a.num)

if tenEighty === alsoTenEighty {
    print("Same")
}

if a === b {
    print("Yes")
}


// Properties
var size1 = Size(width: 10, height: 35)
size1.width = 6
print(size1)


struct Point{
    var x: Double = 0.0
    var y: Double = 0.0
}


// Lazy stored properties

struct DataImporter {
    var pull = "Pull"
}


class DataManager {
    lazy var importer = DataImporter()
    var data = [String]()
}

var manager = DataManager()


struct Shape {
    var origin = Point()
    var center: Point {
        get {
            return Point(x: origin.x / 2, y: origin.y / 2)
        }
        set {
            origin.x = newValue.x / 2
            origin.y = newValue.y / 2
        }
    }
}

var circle = Shape()
print(manager, circle)


struct Cuboid{
    var w = 0.0, h = 0.0, d = 0.0
    var volume: Double {
        get {
            return w * h * d
        }
    }
}

var c = Cuboid(w: 2, h: 5, d: 3)
print(c.volume)


// Property observers

class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newSteps) {
            print("About to set totalSteps to \(newSteps)")
        }
        didSet{
            if totalSteps > oldValue {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}

let stepCounter = StepCounter()
stepCounter.totalSteps = 50
stepCounter.totalSteps = 150
stepCounter.totalSteps = 420


class myCounter {
    var steps: Int = 0 {
        willSet {
            print(newValue)
        }
        didSet {
            print(oldValue)
        }
    }
}

let counter = myCounter()
counter.steps = 50


// Type properties

class SomeClass {
    static var storedProp = "Some value."
    static var computedProp: Int {
        return 42
    }
}

print(SomeClass.storedProp)
