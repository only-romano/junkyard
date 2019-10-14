// Race app

class Car {
    var model : String = "No model"
    var weight : Float = 0.0
    var speed : Float = 0.0
    var wheels : Int = 4
    
    init(model: String, weight: Float, speed: Float, wheels: Int) {
        self.model = model
        self.weight = weight
        self.speed = speed
        self.wheels = wheels
    }
    
    func info () -> String {
        return  "\(self.model) with weight \(self.weight) kg. and  max speed of \(self.speed) km/h. It has \( Int.random(in: 1 ..< 3) < 2 ? "beautiful" : "wonderful") \(self.wheels)' wheels!"
    }
    
    func set (model: String) {
        self.model = model
    }
    
    func set (wheels: Int, weight: Float) {
        self.wheels = wheels
        self.weight = weight
    }
    
    func set (speed: Float) {
        self.speed = speed
    }
}


var mazda = Car(model: "Mazda", weight: 1550.0, speed: 229.0, wheels: 15)
var toyota = Car(model: "Toyota Mark II", weight: 1480.0, speed: 195.0, wheels: 17)
mazda.set(model: "Mazda Millenia")


print("""
Welcome to the 1/4 mile drag Race!
And today we have two competitors, here they are:
1) \( mazda.info() )
2) \( toyota.info() )

Let's get It starteeed!!!
""")


func Race <T: Car> (_ car1: T, _ car2: T) -> (T, Float) {

    func getRandom() -> Float { return Float.random(in: 0.7 ..< 1) }

    var distance: Float = 250.0

    print("Race starts!")
    print("Race!!!")
    print("Finish line!!!")

    var car1Time = distance / ( ( car1.speed * getRandom() ) / ( car1.weight * getRandom() * 0.008 ) )
    var car2Time = distance / ( ( car2.speed * getRandom() ) / ( car2.weight * getRandom() * 0.008 ) )

    return (car1Time < car2Time ? car1 : car2, car1Time < car2Time ? car1Time : car2Time)
}


var winner = Race(mazda, toyota)

print("And the Winner is \(winner.0.model) with time \(winner.1) seconds")
