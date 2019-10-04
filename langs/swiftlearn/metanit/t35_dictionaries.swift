// Определение словаря
var dictDec1 = ["Key1": "Value1", "Key2": "Value2"]
var dictDec2: [String: String] = ["Key1": "Value1", "Key2": "Value2"]
var dcitDec3: Dictionary<String, String> = ["Key1": "Value1", "Key2": "Value2"]

var emptyDict1: Dictionary<String, String> = [:]
var emptyDict2: [String: String] = [:]
var emptyDict3 = [String: String]()

var phones = ["Apple": "iPhoneX", "Microsoft": "Lumia 950", "Samsung": "Galaxy S9"]
print(phones)


// Колличество элементов - isEmpty, count
func getLengthOrEmpty(_ dict: [String: String]) -> Void {
    if dict.isEmpty {
        print("Словарь \(dict) пуст")
    } else {
        print("В словаре \(dict) есть \(dict.count) элементов")
    }
}

getLengthOrEmpty(phones)
getLengthOrEmpty(emptyDict1)


// Изменение содержимого словаря - updateValue, removeValue
print(phones["Apple"])
phones["Apple"] = "iPhone 6S"

phones.updateValue("Galaxy 9 Tab", forKey: "Samsung")
print(phones)

phones["Microsoft"] = nil  // удаление элемента из словаря

if let removedValue = phones.removeValue(forKey: "Samsung") {
    print("Удалён элемент \(removedValue)")
} else {
    print("В словаре \(phones) нет такого элемента")
}


// Перебор словаря
phones = ["Apple": "iPhone 6S", "Microsoft": "Lumia 950", "Google": "Nexus X5"]
for (manufacturer, model) in phones {
    print("\(manufacturer) - \(model)")
}

var str: String = "Manufacturers:"
for manufacturer in phones.keys {
    str += " \(manufacturer);"
}

str += "\nModels:"
for model in phones.values {
    str += " \(model);"
}


// Создание словаря из массивов - zip
var countries: Array<String> = ["Iran", "Iraq", "Syria", "Lebanon"]
var capitals: Array<String> = ["Tehran", "Bagdad", "Damascus", "Beirut"]
var seq = zip(countries, capitals)

var dict = Dictionary(uniqueKeysWithValues: seq)
for (key, value) in dict {
    print("\(key) - \(value)")
}


// Повторяющиеся значения
countries.append("Iran"); capitals.append("Tehran")
seq = zip(countries, capitals)

dict = Dictionary(seq, uniquingKeysWith: {return $1})
for (key, value) in dict {
    print("\(key) - \(value)")
}
