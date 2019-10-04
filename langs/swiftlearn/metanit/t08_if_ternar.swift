let num1 = 22
let num2 = 15

if num1 < num2 {
    print("\(num1) less then \(num2)")
} else if num1 > num2 {
    print("\(num1) greater then \(num2)")
} else {
    print("\(num1) equal to \(num2)")
}

// Работает теранарный оператор
var num3 = num1 > num2 ? num1 - num2 : num1 + num2
print(num3)
