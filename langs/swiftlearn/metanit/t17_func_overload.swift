// Перегрузка функции
func sum(_ x: Int8, _ y: Int8) {
    print("Sum is (two integers): \(x+y)")
}

func sum(_ x: Int, _ y: Int) -> Double {
    var sum = Double(x+y)
    print("Int to doubles sum: \(sum)")
    return sum
}

func sum(_ x: Double, _ y: Double) {
    print("Sum is (two doubles): \(x+y)")
}

func sum(_ numbers: Int...) -> Int {
    var total: Int = 0
    for num in numbers {
        total += num
    }

    print("Sum is (more than two integers): \(total)")
    return total
}

sum(Int8(1), Int8(2))
sum(1.2, 2.3)
sum(1, 2, 3, 4, 5)
var num: Int = sum(2, 3)
var doubNum: Double = sum(5, 6)
