// Наследование
class User{

    var name: String
    var surname: String

    /* Ключевое слово final указывает на запрет переопределения свойств,
    методов, сабскриптов в производном классе.

    Также можно запретить наследование в целом:
    final class User{ ... }
    */
    final var age: Int

    /* Ключевое слово required указывает на обязательный для переопределения в
    подклассах инициализатор */ 
    required init(name: String, surname: String){

        self.name = name
        self.surname = surname
        self.age = 18
    }

    var fullInfo: String {
        return "\(self.name) \(self.surname)"
    }

    func getFullInfo() -> String {

        return self.fullInfo
    }
}

class Employee : User{  // класс Employee наследуется от User

    var company: String

    required init(name: String, surname: String){

        self.company = "Unknown"
        super.init(name: "Mr." + name, surname: surname)
    }

    init(name: String, surname: String, company: String){

        self.company = company
        super.init(name: name, surname: surname)
    }

    // Переопределение свойства родительского класса
    override var fullInfo: String{
        // ключевое слово super - обращение к родительскому классу
        return super.fullInfo + " and he works in"
    }

    // Переопределение метода родительского класса
    override func getFullInfo() -> String{
        return "\(super.getFullInfo()) - \(self.company)"
    }
}

var emp: Employee = Employee(name: "Steeve", surname: "Jobs", company: "Apple")
print(emp.getFullInfo())
emp = Employee(name:  "Tim", surname: "Cook")
print(emp.getFullInfo(), emp.age)
