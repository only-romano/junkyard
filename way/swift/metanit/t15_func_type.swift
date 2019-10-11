// Типы функций
func sum(_ a: Int, _ b: Int) -> Int{
    return a + b
}

func subtract(_ a: Int, _ b: Int) -> Int{
    return a - b
}

func multiply(_ a: Int, _ b: Int) -> Int{
    return a * b
}

func printName(name: String) {
    print(name)
}


printName(name: "Katik")


var someFunc: (Int, Int) -> Int

someFunc = sum
print("Now \"someFunc\" is equal to \"sum\" and \"someFunc(5,4)\" = \(someFunc(5,4))")

someFunc = subtract
print("Now \"someFunc\" is equal to \"subtract\" and \"someFunc(5,4)\" = \(someFunc(5,4))")


func getResult(_ binaryFunc: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    let result = binaryFunc(a, b)
    print(result)
}

getResult(sum, 13, 10)
getResult(subtract, 12, 8)


func select (_ n: Int) -> (Int, Int) -> Int {

    switch n {
        case 2:
            return subtract
        case 3:
            return multiply
        default:
            return sum
    }
}

let x = 12, y = 8

for i in 1...3 {
    someFunc = select(i)
    print(someFunc(x, y))
}
