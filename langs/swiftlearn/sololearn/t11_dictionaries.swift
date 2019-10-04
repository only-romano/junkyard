/*
    Dictionaries app
*/

var sample = [Int: String]()
var airports: [String: String] = ["TOR": "Toronto", "NY": "New York"]
var s: [Int: String] = [1: "A", 2: "B", 3: "C"]
print(sample, airports, s)


// Modifying a dictionary
airports["LHR"] = "London"
airports["LHR"] = "London Heathrow"

let oldValue = airports.updateValue("New York International", forKey: "NY")
let airportName = airports["TOR"]
print(oldValue, airportName, airports)
airports["TOR"] = nil

if let removedValue = airports.removeValue(forKey: "NY") {
    print("The removed airport's name is \(removedValue)")
} else {
    print("The airports dictionary does not contain a value for NY.")
}
print(airports)

s[3] = nil
print(s.count)

airports["NY"] = "New York International"

// Iterating over a dictionary
for (airportCode, airportName) in airports {
    print("\(airportCode): \(airportName)")
}

for airportCode in airports.keys {
    print("Airport code: \(airportCode)")
}

for airportName in airports.values {
    print("Airport name: \(airportName)")
}
