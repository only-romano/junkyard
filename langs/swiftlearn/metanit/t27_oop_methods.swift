// Свойства и методы класса
class Exchange{

    // методы и свойства класса относятся ко всему классу, а не к экземпляру
    class var usd : Double { return 59.0 }
    class func convert(_ sum: Double) -> Double{
        return sum / usd
    }
}

class BankExchange : Exchange{

    // свойства класса должны быть вычисляемыми
    override class var usd : Double { return 59.1 }  // доступно для переопределения классам-наследникам
    override static func convert(_ sum: Double) -> Double{  // недоступно для переопределения классам-наследникам
        var res = sum / usd
        return res - res * 0.1
    }
}

print("Банк, конверация 20 000 рублей \(Exchange.convert(20000))")
print("Банкомат, конверация 20 000 рублей \(BankExchange.convert(20000))")
