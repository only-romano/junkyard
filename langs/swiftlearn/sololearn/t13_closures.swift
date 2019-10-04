/*
    Closures app
*/

func backwards(s1: String, s2: String) -> Bool {
    return s1 > s2
}

let names = ["Katik", "Coco", "Adrian", "Dealan", "Monroe"]
var reversed = names.sorted(by: backwards)
print(reversed)


var reversed2 = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})

print(reversed2)


var asc = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 < s2
})

print(asc)


var reversed3 = names.sorted(by: {s1, s2 in return s1 > s2})
print(reversed3)


func order(arr: [Int]) -> [Int] {
    return arr.sorted(by: {n1, n2 in n1 > n2})
}

print(order(arr: names))


var reversed4 = names.sorted(by: {$0 > $1})
var reversed5 = names.sorted(by: >)
print(reversed4, reversed5)
