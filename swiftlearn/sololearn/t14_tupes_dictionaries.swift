/*
    Tuples and enumerations app
*/

// Tuples
let error = (404, "Not Found")
let (statusCode, statusMessage) = error

print("The status code is \(statusCode)")
print("The message is \(statusMessage)")
print("\(error.0) - \(error.1)")


let http200Status = (statusCode: 200, message: "OK")
print("The status code is \(http200Status.statusCode)")
print("The message is \(http200Status.message)")


let coords = (48, 27)
let (latitude, longitude) = coords
print(latitude, longitude)


// Enumerations

enum Compass {
    case North
    case South
    case East
    case West
}


enum Planet {
    case Mercury, Venus, Earth, Mars, Jupiter
}


enum Status {
    case None, Online, Offline
}

var direction = (Compass.West, Planet.Mars, Status.Online)
print(direction)
