// Великолепный switch\case с диапазонами и доп.условиями
var num: Int = 28

switch num {
    case 0:  // точное значение
        print("\(num) is equal 0")
    case 10:
        break
    case 28:
        print("\(num) is equal 28")
    default:
        print("\(num) is equal whatever")
}

switch num {
    case 1:
        print("\(num) is equal 1")
    case 2:
        print("\(num) is equal 2")
    case _:  // любой другой num
        print("\(num) is not equal to 1 or 2, but that's not guaranted...")
}

switch num {
    case ..<0:  // диапазон не включая крайнее значение 0
        print("\(num) less then 0")
    case 1,2,3:  // перечисление возможных значений
        print("\(num) is equal to 1 or 2 or 3")
    case 4..<10:  // диапазон от 4 (включая)  до 10 (не включая)
        print("\(num) is in range from 4 to 10 (not including 10 -_-)")
    case 10...20:  // диапазон от 10 до 20 (включая оба значения)
        print("\(num) is in range from 10 to 20 (including both)")
    case 21...:  // диапазон от 21 (включая)
        print("\(num) more or equal to 21")
    default:break
}

let personInfo = ("Katik", num)

switch personInfo {
    case ("Bob", 33):
        print("Sup, Бобик")
    case (_, 28):  // игнорирование ненужных значений в кортеже
        print("Ах ты 28-time dummy")
        fallthrough  // провалиться вниз по кейсам
    case("Katik", _):
        print("Да, я тебе, Катик")
    case("Katik", 22...30):  // также можно использовать диапазоны
        print("Ты всё ещё крут, поверь мне -_-")
    default:
        print("Fuck you, I don't know you")
}

switch num {
    case 1:break
    case 2:
        print("And so?")
    case let n:  // присваивание значения переменной
        print("Now variable \"n\" has value of \(num)!")
}

switch personInfo {
    case (let name, 25):
        print("Name: \(name); dummy: \(num)")
    case ("Bobby", let dummy):
        print("Name: Bob; dummy: \(dummy)")
    case let (name, dummy) where personInfo.1 < 20:  // увловие
        print("Name: \(name); dummy: \(dummy)")
    case let (name, dummy):
        print("Name: \(name); dummy: \(dummy)")
}

let i  = 8
switch i {
    case let k where k < 0:
        print("Now \"k\" has value of \(k) and it's negative number")
    case let k where k > 0:
        print("Now \"k\" has value of \(k) and it's positive number")
    case 0:
        print("\"i\" is zero, nothing, emptyness. period.")
    default:break
}

switch personInfo {
    case ("Katik", _) where personInfo.1 > 10 && personInfo.1 < 15:
        print("Name is \(personInfo.0); dumness from 10 to 15.")
    case ("Katik", _) where personInfo.1 >= 20:
        print("Name is \(personInfo.0); dumness more then 20. True story.")
    default:
        print("Identity failed. Selfdestruct process started.")
}
