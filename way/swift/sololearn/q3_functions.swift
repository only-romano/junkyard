/*
    Functions adn Closures module quiz
*/

// First
func myFunc(_ num: Int) -> Void {
    print(num)
}
myFunc(42)


// Second
func myFunc2(p1: Int = 1, p2: Int = 2) {
    print(p1 * p2)
}
myFunc2(p1: 144)


// Third
enum Planet {
    case Mercury, Venus, Earth, Mars
}
let somePlanet = Planet.Earth

switch somePlanet {
    case .Earth:
        print("Mostly harmless")
    default:
        print("Not a safe place for humans")
}
