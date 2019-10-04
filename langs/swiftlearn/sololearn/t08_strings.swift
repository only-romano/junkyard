/*
    Strings data type and working with strings app

    String is an ordered collection of characters
*/

let someString = "Some string literal value"
var sample: String = "I love Swift!"
print(sample)

var emptyString: String = ""
var anotherEmptyString = String()

if emptyString.isEmpty {
    print("String is empty")
}

if someString.isEmpty {
    print("0")
} else {
    print(someString)
}


// Concatenation
let string1 = "Hello"
let string2 = "World"
print(string1 + string2)

var msg = "Hi"
msg += " Katik"
print(msg)

var s1 = "I love"
var s2 = " Swift"
var message = s1 + s2
print(message)


// Interpolation
let mult = 4
message = "\(mult) times 1.5 is \(Double(mult)*1.5)"
print(message)
print("String \"\(someString)\" has \(someString.count) characters")

var word = "SoloLearn"
print(word.characters.count)


// Comparing strings, hasPrefix, hasSuffix
s1 = "We are alike"
s2 = "We are alike"
if s1 == s2 {
    print("These two strings are equal")
}

var start = "We are"
print("String \"\(s1)\" starts with \(start) - \(s1.hasPrefix(start))")
print("String \"\(s1)\" ends with \(start) - \(s1.hasSuffix(start))")

s1 = "test"
s2 = "test"
if s1 == s2 {
    print("Equal!")
}
