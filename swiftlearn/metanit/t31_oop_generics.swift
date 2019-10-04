// Использование обобщений (generics)
func swap<T>(_ a: inout T, _ b: inout T) {

    let temp: T = a
    a = b
    b = temp
}

var x: Int = 25
var y: Int = 14
swap(&x, &y)
print(x, y)

var s1: Double = 10.2
var s2: Double = -3.6
swap(&s1, &s2)
print(s1, s2)


// Обобщённые типы
class User<T>{

    var id: T  // свойство обобщённого типа
    var name: String

    init(id: T, name: String){

        self.id = id
        self.name = name
    }

    func displayId(){
        print(id)
    }
}


// Наследование и обобщения
class Employee<T> : User<T>{}
class UserInt : User<Int>{}

var tom: User = User(id: 12, name: "Tom")
var bob: User = User(id: "234nds", name: "Bob")

let alice = Employee<String>(id: "5746fgg", name: "Alice")
alice.displayId()
let robert = UserInt(id: 34, name: "Robert")
robert.displayId()


// Ограничение типа обобщения (constraint)
class Transport{

    func drive(){
        print("Transport is running")
    }
}

class Auto: Transport{

    override func drive(){
        print("Car is running")
    }
}

func driveTransport<T: Transport>(_ transport: T){  // ограничение обобщения классом Transport

    transport.drive()
}

var myAuto: Auto = Auto()
driveTransport(myAuto)
