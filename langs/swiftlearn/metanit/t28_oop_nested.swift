class User{
    var name: String
    var skill: Int
    var profile: UserProfile  // внешний тип может хранить объект вложенного

    // Вложенная структура
    struct UserProfile{
        var login: String
        var password: String

        func authenticate(_ login: String, _ password: String) -> Bool{
            return self.login == login && self.password == password
        }
    }

    init(name: String, skill: Int, login: String, password: String) {
        self.name = name
        self.skill = skill
        self.profile = UserProfile(login: login, password: password)
    }
}

var katik = User(name: "Katik", skill: 88, login: "qwerty", password: "12345")
print("Проверка пользователя: \(katik.profile.authenticate("ssdf", "345"))")
print("Проверка пользователя: \(katik.profile.authenticate("qwerty", "12345"))")


// Вложенный тип может использоваться вне своего типа, с котором определены
var profile = User.UserProfile(login: "ssdf", password: "345")
print("Соответствие логина и пароля: \(profile.authenticate("ssdf", "345"))")
