// Определение последовательности
let range = 1...5
let uRange = -5 ..< -1  // не включая последнее значение
let inv = range.reversed()


// Перебор последовательности
var str = "Положительная последовательность:"
for val in range {
    str += " \(val);"
}

str += "\nОтрицательная последовательность:"
for val in uRange {
    str += " \(val);"
}

str += "\nОбратная последовательность:"
for val in inv {
    str += " \(val);"
}

print(str)


// Проверки последовательности - contains, starts, overlaps
print("Последовательность \(inv) содержит 3 - \(inv.contains(3))")
print("Последовательность \(range) содержит 7 - \(inv.contains(7))")

print("Последовательность \(range) начинается с 5...8 - \(range.starts(with: 5...8))")
print("Последовательность \(uRange) начинается с -5... -3 - \(uRange.starts(with: -5...(-3)))")

print("Последовательность \(range) хотя бы частично совпадает с последовательностью 3...9 - \(range.overlaps(3...9))")
print("Последовательность \(range) хотя бы частично совпадает с последовательностью 9...19 - \(range.overlaps(9...19))")
