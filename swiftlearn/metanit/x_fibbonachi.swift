// Рекурсивная функция фибоначчи
func fibbonachi(_ n: Int) -> Int {

    if n == 0 {
        return 0
    }
    else if n == 1 {
        return 1
    }

    return fibbonachi(n - 1) + fibbonachi (n - 2)
}

print(fibbonachi(17))
