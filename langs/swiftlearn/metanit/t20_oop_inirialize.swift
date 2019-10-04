// Инициализаторы
class User {
    // Каздый класс имеет инициализатор по умолчанию
    let skill: Int
    let name: String

    // Переопределение инициализатора
    /*
    Делегируемый инициализатор:
    convenience init() {
        self.init(name: "x", skill: y) - вызывает другой инициализатор
    }

    failable ititializer позволяет возвращать nil, если в процессе инициализации
    произошла ошибка:
    init?(skill: Int){
        self.skill = skill
        if (skill < 0) {
            return nil
        }
    }
    */
    init?(name: String = "Katik", skill: Int = 88){
        self.skill = skill
        self.name = name

        if (skill < 0) {
            return nil
        }
    }

    func getUserInfo() {

        print("Name: \(name); Skill: \(skill)")
    }
}

// Объект созданный failable инициализатором будет Optional<User>
var bob: User = User(name: "Bob", skill: 34)!  // распаковка Optional
bob.getUserInfo()

if let lora = User(name: "Lora Palmer", skill: -4) {
    print(lora.name)
} else {
    print("He-he-he. Twin peaks.")
}
