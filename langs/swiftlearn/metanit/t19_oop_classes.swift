// ООП
class User {

    var experience: Int = 0
    var name: String = "Ridj"

    func move() {
        print("\(name) is coding \(experience > 1 ? experience + " years" : "sometimes") ...")
    }

    func getUserInfo(){
        print("Name: \(self.name); Experience: \(self.experience) years")
    }
}

var katik: User = User()
katik.age = 2
katik.name = "Katik"
katik.move()
katik.getUserInfo()
