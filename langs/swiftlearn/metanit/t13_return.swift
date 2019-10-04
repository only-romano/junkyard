func printHello(_ count: String = "") -> Void { print("Hello world \(count) times!") }

func sum (_ x: Int, _ y: Int) -> Int {
    return x + y
}

let a = sum(5,6)
printHello(String(a))

func getInfo(_ salary: Double) -> (tax: Double, rent: Double) {
    let tax = salary * 0.13
    let rent = salary * 0.05
    return (tax, rent)
}

let losses = getInfo(Double(a*1000))
print("Подоходный налог: \(losses.tax)\nРента: \(losses.rent)")

func measureTax(_ salary: Double) -> Double? {
    if (salary > 1000) {
        return salary * 0.13
    }
    return nil
}

if let tax = measureTax(11000) {
    print(tax)
}

if let tax = measureTax(110) {
    print(tax)
}
