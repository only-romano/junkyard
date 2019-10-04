/*
    Arrays and methods with arrays app
*/

var someInts: Array<Int> = [1, 2, 3]
print(someInts)

// Default value
var fourDoubles = Array<Double>(repeating: 0.0, count: 4)
print(fourDoubles)

var shoppingList: [String] = ["Bread", "Milk"]
var additionBuies: [String] = ["Sugar", "Love"]
shoppingList += additionBuies
print(shoppingList)

var test: [Int] = [11, 22]


// Count property, isEmpty

if shoppingList.isEmpty {
    print("The shopping list is empty")
} else {
    print("The shopping list contains \(shoppingList.count) items")
}

var myArr = Array<Int>()

if myArr.isEmpty {
    print("Empty array")
} else {
    print(myArr.count)
}


// Modifying an array
shoppingList.append("Flour")
shoppingList += ["Juice", "Chocolate"]
var firstItem = shoppingList[0]

print(shoppingList, firstItem)

var myList = ["A", "B"]
myList += ["C", "D", "E"]
print(myList.count)

shoppingList[0] = "Two apples"
shoppingList[1...3] = ["Bananas", "Oranges"]
print(shoppingList)

shoppingList.insert("Syrup", at: 0)
print(shoppingList)

let syrup = shoppingList.remove(at: 0)
print(shoppingList, syrup)

let apples = shoppingList.removeLast()
print(shoppingList, apples)

var temp = ["oldItem"]
let r = temp.removeLast()
temp.insert("New Item", at: 0)
print(temp.count)


// Iterating over an array
var str = "Shopping list:"
for item in shoppingList {
    str += " \(item);"
}

str += "\nI repeat:"
for(index, value) in shoppingList.enumerated() {
    str += " item \(index + 1): \(value);"
}
print(str)

var myIntArr: Array<Int> = [1, 2, 3, 4, 5]
var sum = 0
for item in myIntArr {
    sum += item
}
print(sum)
