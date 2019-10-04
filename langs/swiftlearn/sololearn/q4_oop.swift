/*
    Object Oriented Programming quiz
*/

// First
class MyClass {
    func foo(a: Int, b: Int) {
        print((a - b) / b)
    }
}
let me = MyClass()
me.foo(20, 4)


// Second
class A {
    func myprint() {
        print("a")
    }
    func myprint(str: String) {
        print("b")
    }
    func myprint(x: Int) {
        print("c")
    }
}
var inst = A()
inst.myprint(x: 12)


// Third
class Test {
    final var num: Int = 0
    var name: String = ""
}
var test = Test()
print(test.num)


// Fourth
class Player {
    var lives: Int = 100
    var strength: Int
    init(lives: Int, st: Int) {
        self.lives = lives
        self.strength = st
    }

    func Attack(p: Player) {
        p.lives -= self.strength
    }
}
let p1 = Player(lives: 100, st: 15)
let p2 = Player(lives: 80, st: 30)
p2.Attack(p: p1)
print(p1.lives)


// Fifth
class Animal {
    var feet: Int = 2
    func makeSound() {
        print("Animal sound")
    }
}

class Dog : Animal {
    override func makeSound() {
        print("Barking")
    }

    override init() {
        super.init()
        feet = 4
    }
}
