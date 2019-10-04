/*
    Sets app
*/

var emptySet = Set<Character>()
var names: Set<String> = ["Katik", "Kuzya", "Solo"]
var mySet: Set = ["A", "B", "C"]
print(emptySet, names, mySet)

names.insert("Paul")


// Contains method
if names.contains("Katik") {
    print("Katik is here!")
} else {
    print("Katik is not with us")
}

if mySet.contains("42") {
    mySet.removeAll()
} else {
    print(mySet.count)
}


// Iterating over a set
var str = "Names:"
for name in names {
    str += " \(name);"
}

str += "\nSorted names:"
for name in names.sorted() {
    str += " \(name);"
}
print(str)


// Sets operations
let oddDigits: Set = [1, 3, 5, 7, 9]
let evenDigits: Set = [0, 2, 4, 6, 8]

print(oddDigits.union(evenDigits).sorted())

let a: Set = ["A", "B", "C"]
var b: Set = ["B", "D", "E", "A"]
print(b.subtracting(a).count)

var c: Set = ["A", "B", "C", "D"]
print("\(a) is equal to \(c) - \(a == c)")
print("\(a) is subset of \(c) - \(a.isSubset(of: c))")
print("\(c) is superset of \(a) - \(c.isSuperset(of: a))")
print("\(a) is strict subset \(c) - \(a.isStrictSubset(of: c))")
print("\(c) is strict superset of \(a) - \(c.isStrictSuperset(of: a))")
print("\(a) has common values with \(c) - \(a.isDisjoint(with: c))")

let num1: Set = [1, 2, 3]
let num2: Set = [3, 5, 2]
if !a.isSubset(of: b) {
    let c: Set = a.intersection(b)
}
