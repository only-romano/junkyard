// Перечисления
enum Season {  // фактически Season представляет новый тип данных

    case Winter, Spring, Summer, Autumn
}

var currentSeason = Season.Spring
currentSeason = .Summer

let lastSeason: Season
lastSeason = Season.Winter

switch (currentSeason) {
    case .Winter:
        print("Зима")
    case .Spring:
        print("Весна")
    case .Summer:
        print("Лето")
    case .Autumn:
        print("Осень")
}


/* С каждым значением в перечислении можно ассоциировать значения, которое может
представлять любой тип. При этом ассоциированные значения для разных значений
одного и того же перечисления могут представлять различные типы.*/
enum Person{

    case Human(String, Int)
    case Elf(String)
    case Gnome
}

var hero = Person.Elf("Feonor")
hero = Person.Human("Trogvar", 5)

switch (hero) {
    // можно получить ассоциированные значения в константы или переменные
    case .Human(let name, let lives):
        print("You are playing human. Name: \(name); Lives: \(lives)")
    case .Elf(let name):
        print("You are playing elf. Name: \(name)")
    case .Gnome:
        print("You are playing gnome.")
}


enum Flagman: String {
    case Samsung = "Galaxy S9"
    case Apple = "iPhone X"
    case Microsoft = "Lumia 950"
    case Google = "Pixel 2"
    case Xiaomi
}

var myPhone = Flagman.Apple
var xiaomi = Flagman.Xiaomi

// Получение чистого значения члена перечисления - rawValue
print("Член перечисления: \(myPhone): чистое значение rawValue: \(myPhone.rawValue)")
print("Член перечисления: \(xiaomi): rawValue по умолчанию: \(xiaomi.rawValue)")


enum DayOfWeek: Int {
    /* Если типом для чистых знчений является тип Int, то элементы получат
    значения по порядку, первый элемент задаёт начальное значение для элементов
    перечисления; если же первый элемент не указан, то
    начальным значением будет "0" */
    case Monday=1, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

    // Свойство перечисления, должны быть вычисляемыми
    var label : String {
        switch self {
            case .Monday: return "День тяжёлый"
            case .Tuesday: return "День сурка"
            case .Wednesday: return "Рутина"
            case .Thursday: return "Золотое сечение"
            case .Friday: return "Это финааал"
            case .Saturday: return "Бухаем"
            case .Sunday: return "Умираем"
        }
    }

    func getCurrentDay() -> String {
        return DayOfWeek.getDay(number: rawValue)
    }

    static func getDay(number: Int) -> String {
        switch number {
            case 1:
                return "Понедельник"
            case 2:
                return "Вторник"
            case 3:
                return "Среда"
            case 4:
                return "Четверг"
            case 5:
                return "Пятница"
            case 6:
                return "Суббота"
            case 7:
                return "Воскресенье"
            default:
                return "undefined"
        }
    }
}

var currentDay: DayOfWeek = DayOfWeek.Wednesday
var sunday = DayOfWeek(rawValue: 7)  // возварщает объект Optional
print("Член перечисления: \(currentDay); чистое значение: \(currentDay.rawValue)")
print("Извлечение Optional(член перечисления): \(sunday!)")
print("Метод перечисления: \(currentDay.getCurrentDay()); свойство: \(currentDay.label)")

if let day = DayOfWeek(rawValue: 8) {  // Безопасное извлечение
    print(day)
}


enum Lol: Int {

    case Light=1, Occasion, Less

    // Инициализатор перечисления
    init?(_ val: String) {

        switch val {
            case "Смеюся" : self = .Light
            case "Писаюся" : self = .Occasion
            case "Уснул" : self = .Less
            case _ : return nil
        }
    }
}

let laught = Lol("Смеюся")
print(laught!.rawValue)
