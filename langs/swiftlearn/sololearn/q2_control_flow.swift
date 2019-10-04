/*
    Control flow & Collections quiz
*/

// First
var str: String = "Exercise 1:"
for x in 1...7 {
    str += " \(x) loop;"
}
print(str)


// Second
var result = 0
for i in 0...4 {
    if i == 3 {
        result += 10
    } else {
        result += i
    }
}
print(result)


// Third
var myArr = [0, 1, 2, 3, 4, 5, 6, 7]
var count = 0
for item in myArr {
    if item % 2 == 0 {
        count += 1
    }
}
print(count)


// Fourth
var tmp = [5, 8, 9, 3]
print(tmp[2])


// Fifth
var temp = [1: 1, 2: 2, 3: 3]
for index in temp.keys {
    temp[index] = 0
}
print(temp)
