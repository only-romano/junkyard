// Опциональный тип
var num1: Int? = nil
var num2: Optional<Int> = 2
var num3: Optional<Int> = Optional(3)
var num = 3

// Распаковка опционального типа
print(num + num3!)

var a: Int? = 12
var b: Int = 10
var c: Int? = Int("123")
print(a!+b, c!, c!+b)


var d: Int! = Int("123")
print(d, d+b)

var str: String = "123"
c = Int("456")
if let aVal = Int(str), let bVal = c  {
    print(aVal, bVal)
} else {
    print("Error")
}

let x: Int? = 10
if x == 10 {
    print("\"x\" is equal to 10")
} else {
    print("\"x\" is not equal to 10")
}

if x != nil && x! > 5 {
    print("\"x\" is greater than 5")
}

var i = Int("97")
switch i {
    case 1?:
        print("\"i\" is equal to 1")
    case let n?:
        print("\"i\" is equal to \(n)")
    case nil:
        print("\"i\" is undefined")

}

// Оператор nil-объединения, если i будет равен nil, то y присвоится 10
i = Int("234")
let y = i ?? 10
print(y)
