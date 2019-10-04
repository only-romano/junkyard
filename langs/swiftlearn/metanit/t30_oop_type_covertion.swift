class Person{

    var name: String
    var age: Int

    init(name: String, age: Int){
        self.name = name
        self.age = age
    }

    func display(){
        print("Name: \(name); Age: \(age)")
    }
}

class Employee : Person{

    var company: String

    init(name: String, age: Int, company: String) {
        self.company = company
        super.init(name: name, age: age)
    }

    override func display() {
        print("Name: \(name); Age: \(age); Employee of company: \(company)")
    }

    func work(){
        print("\(self.name) is working")
    }
}

func getInfo(p: Employee){
    p.display()
}

let tom: Employee = Employee(name: "Tom", age: 23, company: "Google")
let bob: Person = Employee(name: "Bob", age: 28, company: "Apple")


// Нисходящее преобразование as!
print((bob as! Employee).company)
(bob as! Employee).work()
getInfo(p: tom)
getInfo(p: (bob as! Employee))


// Безопасное преобразование
let serj: Person = Person(name: "Serj", age: 28)

if bob is Employee {
    let bobEmpl = bob as! Employee
    bobEmpl.work()
}


// Преобразование в тип Optional
let serjEmpl: Employee? = serj as? Employee
if serjEmpl != nil {
    serjEmpl!.work()
} else {
    serj.display()
    print("Not an employee...")
}

(bob as? Employee)?.work()
(serj as? Employee)?.work()
