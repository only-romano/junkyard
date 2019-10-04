// Объявление массива
var numbersArray: Array<Int> = [3, 4, 5, 6, 7]  // полная форма
var numbersArray2: [Int]  // краткая форма
numbersArray2 = [1, 2, 3, 4, 5]
print(numbersArray, numbersArray2)


// Пустой массив
var emptyArray = [Int]()
var emptyArray2: [Int] = []
print(emptyArray, emptyArray2)


// Доступ к элементам массива
numbersArray = [11, 12, 13, 14, 15]
print(numbersArray[0], numbersArray)
// print(numbersArray[5])  - index error

numbersArray[0] = 21
print(numbersArray[0], numbersArray)

numbersArray[1...3] = [105, 106, 103]  // изменение нескольких элементов подряд
print(numbersArray)


// Размер массива count, свойство isEmpty
func isEmptyArray <T>(_ arr: [T]) -> Void {
    if (arr.isEmpty) {
        print( "Массив \(arr) пустой")
    } else {
        print( "Массив \(arr) содержит \(arr.count) элементов")
    }
}

isEmptyArray(numbersArray)
isEmptyArray(emptyArray)


// Перебор массива, функции forEach и enumerated
var str = "Перебор массивов, a:"
for i in numbersArray {
    str += " \(i)"
}

str += "; б: "
for i in 0..<numbersArray.count {
    str += " \(numbersArray[i])"
}

str += "; в: "
numbersArray.forEach({str += " \($0)"})
print(str)

var names: [String] = ["Tom", "Alice", "Kate"]
str = "Имена:"
names.enumerated().forEach({ str += " \($0) - \($1);"})

str += " второй проход:"
for (index, value) in names.enumerated() {
    str += " \(index) - \(value);"
}
print(str)


// Создание массива из последовательности, (repeating:, count:)
numbersArray = [Int] (3..<7)
numbersArray2 = Array (1...5)
print(numbersArray, numbersArray2)

numbersArray = Array (repeating: 5, count: 3)
print(numbersArray)

// Массив из последовательности объектов ссылочного типа хранят ссылку
// на один и тот же элемент
class Person {

    var name: String
    init(name: String) {
        self.name = name
    }
}

let katik = Person(name: "Ridj")
var people = Array (repeating: katik, count: 3)
people[0].name = "Katik"
str = "Repeating class:"

for person in people {
    str += " \(person.name)"
}
print(str)


// Сравнение массивов
var n1: [Int] = [1, 2, 3, 4, 5]
let n2 = [1, 2, 3, 4, 5]
print("Массивы \(n1) и \(n2) \(n1 == n2 ? "" : "не ")равны")


// Копирование массива
numbersArray = [1, 2, 3, 4, 5]
var sliceArray = numbersArray[1...3]
var nums: [Int] = numbersArray
nums[0] = 78; nums[2] = 12
print(numbersArray, sliceArray, nums)


// Добавление в массив, append и insert
numbersArray = [8, 11, 13]
numbersArray.append(20)
print(numbersArray)

numbersArray.insert(10, at: 2)
print(numbersArray)


// Удаление из массива, remove и drop
numbersArray = [1, 2, 3, 4, 5]; str = "\(numbersArray); "
numbersArray.remove(at: 2); str += "\(numbersArray); "
numbersArray.removeFirst(); str += "\(numbersArray); "
numbersArray.removeLast(); str += "\(numbersArray)"
print(str)

var n = [1, 2, 3, 4, 5];
print("\(n); \(n.dropFirst()); \(n.dropLast()); \(n)")
n.removeAll()
print(n)


// Сортировка массива, sort, sorted
numbersArray = [10, 4, 12, 1, 3]
numbersArray.sort()  // сортирует сам массив
print(numbersArray)

numbersArray = [10, 4, 12, 1, 3]
numbersArray2 = numbersArray.sorted()  // возвращает новый отсортированный массив
print(numbersArray2)

numbersArray2.sort(by: {$0 > $1})
print(numbersArray2, numbersArray2.sorted(by: <))


// Объединение массивов
numbersArray = [5, 6, 7]
numbersArray2 = [1, 2, 3]
numbersArray = numbersArray + numbersArray2
print(numbersArray)


// Фильтрация массивов, filter, frefix и drop
numbersArray = [1, 2, 3, 4, 5, 6]
var filteredNums = numbersArray.filter({$0 % 2 == 0})
print(filteredNums)

var prefixNums = numbersArray.prefix(while: {$0 < 4})
print(prefixNums)

var dropedNums = numbersArray.drop(while: {$0 < 4})
print(dropedNums)


// Преобразование массива, map
numbersArray = [1, 2, 3, 4, 5, 6, 7, 8]
var mappedNums = numbersArray.map({$0 * $0})
print(mappedNums)


// Многомерные массивы
var table: [[Int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var row = table[1]
var cell1 = row[0]
var cell2 = table[0][1]
print(table)
print(row, cell1, cell2)

table[1] = [16, 25, 36]
table[0][1] = -12
print(table)

str = "Table: "
for row in table{
    str += " \(row);"
}
print(str)

str = "Table cells: "
for row in table{
    str += "\n"
    for cell in row{
        str += "\t\(cell)"
    }
}
print(str)
