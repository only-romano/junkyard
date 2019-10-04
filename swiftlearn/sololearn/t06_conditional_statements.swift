/*
    Conditional statement app
*/

var temp = 25
if temp <= 30 {
    print("It's cold outwhere")
}

var cardValue = 10
if cardValue == 11 {
    print("Jack")
} else if cardValue == 12 {
    print("Queen")
} else {
    print("Some another card")
}

if temp > cardValue {
    print(temp)
} else {
    print(cardValue)
}


// Switch statement
var distance = 3500
switch distance {
    case 0:
        print("He is so close!")
    case 1,2,3,4,5:
        print("He is near")
    default:
        print("He is too far :(")
}

switch distance {
    case 0...10:
        print("It's so close! You just right here beside me, my love!")
    case 10...100:
        print("Still it's pretty close enough to not miss you much ...")
    case 100...1000:
        print("Why do we have to be so far from each other?")
    default:
        print("I miss you so much :( ")
}



// Additional conditions
let myPoint = (1, -1)
switch myPoint {
    case let(x, y) where x == y:
        print("\(x), \(y) is on the line x == y")
    case let(x, y) where x == -y:
        print("\(x), \(y) is on the line x == -y")
    case let(x, y):
        print("\(x), \(y) is just some arbitrary point")
}

let currentPoint = (1, 2)
switch currentPoint {
    case let (x, y) where x > y:
        print("A")
    case let (x, y) where x == y:
        print("B")
    case let (x, y):
        print("C")
    
}
