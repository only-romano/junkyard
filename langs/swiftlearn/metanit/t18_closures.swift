// Замыкания
let hello = {
    (name: String) in
    print("Hello to the Swift World, \(name)")
}
// let hello: () -> Void = { print("Hello World") }
hello("Katik")


let sum = {
    (x: Int, y: Int) -> Int in
    return x + y
}
print(sum(2,5))
print(sum(12,15))


func operation(_ a: Int, _ b: Int, _ action: (Int, Int) -> Int) -> Int {
    return action(a, b)
}

let x = 10
let y = 12

print("Result one: \(operation(x, y, {(a: Int, b: Int) -> Int in return a + b}))")
print("Result two: \(operation(x, y, {(a, b) in a - b}))")
print("Result three: \(operation(x, y, {$0 * $1}))")
print("Result four: \(operation(14, y, %))")


func action() -> (()->Int) {
    var val = 0
    return {
        val = val + 1
        return val
    }
}

let inc = action()
for i in 1...3 {
    print(inc())
}


var a = 14
var b = 2

let myClosure: () -> Int = {return a + b}
let constClosure: () -> Int = {[a, b] in return a + b}
print("This closure changing with var changes (1, before): \(myClosure())")
print("And this is not (2, before): \(constClosure())")
a = 5; b = 6
print("-_- (1, after): \(myClosure())")
print("Told you so :) (2, after): \(constClosure())")
    