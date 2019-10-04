// Привер полиморфизма
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

    // динамическая диспетчеризация
    override func display() {
        print("Name: \(name); Age: \(age); Employee of company: \(company)")
    }
}

class Manager : Employee {

    override func display() {
        print("Name: \(name); Age: \(age); Manager of company: \(company)")
    }
}

let tom: Person = Person(name: "Tom", age: 23)
let bob: Person = Employee(name: "Bob", age: 28, company: "Apple")
let alice: Person = Manager(name: "Alice", age: 31, company: "Microsoft")

tom.display()
bob.display()
alice.display()
