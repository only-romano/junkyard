for item in 1...5 {
    print("Cycle 1: \(item)")
    if item == 2 {
        break
    }
}

// Дополнительное условие where
for i in 0...10 where i % 2 == 0 {
    if i < 3 || i > 6 {
        continue
    }
    print("Cycle 2: \(i)")
}

var i = 10
while i > 0 {
    i -= 1
    if (i > 2 || i == 0) {
        continue
    }
    print("Cycle 3: \(i)")
}


// аналог do {} while из других языков
repeat {
    print("Cycle 4: \(i)")
    i -= 1
} while i > 0
