// Структуры
struct User {
    var name: String
    var skill: Int

    // Если нет ицициализаторов, то нельзя передавать значение отдельных свойств, только все сразу
    init(name: String = "Katik"){
        self.init(name: name, skill: 88)
    }
    init(name: String, skill: Int){
        self.name = name
        self.skill = skill
    }

    func getInfo() -> String {
        return "Name: \(name); Skill: \(skill)"
    }

    // Для изменения свойств структуры используются методы mutating
    mutating func setName(name: String){
        self.name = name
    }
}

var katik: User = User()
print(katik.getInfo())

var bob = User()
bob.name = "Bob"; bob.skill = 23
print(bob.getInfo())
bob.setName(name: "Robert")
print(bob.getInfo())

var tom = User(name: "Tom")
print(tom.getInfo())
