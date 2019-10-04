// Методы типа, статические методы
class Greeting {
    static let english = "hello"
    static let french = "salut"
    static let german = "halo"
}

print(Greeting.french)


class Account {

    var capital: Double
    var rate: Double

    // Свойство типа, общее для всего класса
    static var usdRate: Double = 67

    init(capital: Double, rate: Double){
        self.capital = capital
        self.rate = rate
    }

    func convert() -> Double {
        return capital / Account.usdRate
    }
}

var myAcc: Account = Account(capital: 1000, rate: 0.1)
var capitalInUsd = myAcc.convert()
print(capitalInUsd)
Account.usdRate = 65
capitalInUsd = myAcc.convert()
print(capitalInUsd)


class Exchange{
    static var rate = 58.9
    static func operate(sum: Double) -> Double {  // метод типа, общий для класса
        return sum / rate
    }
}

print(Exchange.operate(sum: 20000))
Exchange.rate = 58.5
print(Exchange.operate(sum: 15000))
print(Exchange.operate(sum: 56000))
