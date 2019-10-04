// Значимые и ссылочные типы
class Person {  // класс является ссылочным типом (reference types)

    var name: String
    var skill: Int
    init(name: String, skill: Int) {

        self.name = name
        self.skill = skill
    }
}

struct User {  // структуры и перечисления являются значимым типом (value types)

    var name: String
    var skill: Int
}


/* Значимым типам нельзя менять свойства объекта, так как при изменении его
отдельных свойств меняеется объект этой стуктуры, что для константных объектов
недопустимо */

let katik: Person = Person(name: "Katik", skill: 28)
let bob: User = User(name: "Bob", skill: 24)
katik.skill = 25  // можно, так как класс - ссылочный тип
// bob.skill = 25  - ошибка, так как структура - значимый тип


// Копирование значений
var tom: Person = Person(name: "Tom", skill: 24)
var rob = tom     // при копировании ссылочного типа - копируется только
rob.name = "Bob"  // ссылка на один и тот же объект в памяти
print("Tom becomes \(tom.name), rob and tom are equal: \(rob === tom)")

// Можно проверить, содержат ли переменные один объект в памяти с помощью "==="
var anotherTom = Person(name: "Tom", skill: 24)
print("But another tom not equal to that tom: \(tom === anotherTom)")

var alice: User = User(name: "Alice", skill: 24)
var bil = alice   // при копировании значимого типа, копируется не ссылка на
bil.name = "Bil"  // объект, а знаения объекта, поэтому при изменении переменной
print("Alice remains \(alice.name), alice and bil are not equal")
// вторая переменная не изменится
