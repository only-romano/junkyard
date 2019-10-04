// Неопределённое количество параметров
func sum(numbers: Int...) -> Int {
    var total: Int = 0
    for number in numbers {
        total += number
    }

    return total
}

print(sum(numbers: 1, 2, 3, 4, 5))


// Работа с параметрами фунекции, изменение выходных параметров
func increase(_ n : inout Int) {
    n += 10
}

var d = 20
print("Before increase: \(d)")
increase(&d)
print("After increase: \(d)")


func swap(a: inout Int, b: inout Int) {
    let temp = a
    a = b
    b = temp
}

var num1 = 10
var num2 = 13
print("Before swap; \"num1\" = \(num1), \"num2\" = \(num2)")

swap(&num1, &num2)
print("After swap; \"num1\" = \(num1), \"num2\" = \(num2)")
