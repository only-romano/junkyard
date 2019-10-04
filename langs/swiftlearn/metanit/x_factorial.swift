// Рекурсивная функция вычисления факториала
func factorial(_ n: Int) -> Int {

    if n == 0 {
        return 1
    }

    return n * factorial(n-1)
}

print(factorial(12))
