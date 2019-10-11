// Рекурсия
func compare (_ r1: Double, _ r2: Double) {

    func square(_ r: Double) -> Double { return r * r * 3.14 }

    let s1 = square(r1)
    let s2 = square(r2)

    print("Difference of squares is \(s1 - s2)")
}

compare(16.0, 15.0)
