// Свойства класса
class User {

    lazy var skill: Int = 88  // ленивое хранимое свойстов, устанавливается при первом обращении, может быть только var
    let name: String
    init(name: String = "Katik"){
        self.name = name
    }
}

var katik: User = User()
var bob: User = User(name: "Bob")
print(katik.name, bob.name)


class Account{
    var capital: Double {
        // Наблюдатели свойства
        willSet (newCapital){  // до изменения
            print("Old capital: \(self.capital); New capital: \(newCapital)")
        }

        didSet (oldCapital){  // после изменения
            print("Sum of capital raised up by \(self.capital - oldCapital)")
        }
    }
    var rate: Double = 0.01

    // Вычисляемое свойство
    var profit: Double{
    
        get {
            return capital + capital * rate
        }
        set {
            self.capital = newValue / (1 + rate)
        }
    }

    init(capital: Double, rate: Double) {
        self.capital = capital
        self.rate = rate
    }
}

var myAcc: Account = Account(capital: 1000, rate: 0.1)
print(myAcc.profit)
myAcc.profit = 1210
print(myAcc.capital)
