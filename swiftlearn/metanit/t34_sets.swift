// Определение
var numbers: Set<Int> = [5, 6, 7, 8]
var setDec1: Set = [5, 6, 7, 8]
var setDec2 = Set<Int>(arrayLiteral: 5, 6, 7, 8)
var emptySet = Set<Int>()
var emptySet2: Set<Int> = []


// Методы работы с множествами - insert, remove, contains, sorted
numbers.insert(10)
print("Множество с новым элементом \"10\" - \(numbers)")

numbers.removeFirst()
numbers.remove(8)
print("Множество после операций по удалению 1, 3 (по индексу) элементов,",
    "\n а так же элемента со значением 8 - \(numbers)")

numbers.removeAll()
print("Множество после удаления всех элементов - \(numbers)")

numbers = [12, 4, 34]
print("Множество \(numbers) содержит элемент \"34\" - \(numbers.contains(34))")
print("Множество \(numbers) содержит элемент \"7\" - \(numbers.contains(7))")

numbers = [4, 7, 2, 6]
print("Отсортированное множество \(numbers): \(numbers.sorted())")


// Операции над множествами - intersection, union, substract, symmetricDifference
var setA: Set<Int> = [1, 2, 3, 4, 5]
var setB: Set<Int> = [4, 5, 6, 7, 8]

print("Множества \(setA) и \(setB).")
print("пересечение - \(setA.intersection(setB))")
print("объединение - \(setA.union(setB))")

setA = [1, 2, 3, 4, 5]
setB = [4, 5, 6, 7, 8]
setA.subtract(setB)  // не возвращает значения -_-
print("разность - \(setA)")

setA = [1, 2, 3, 4, 5]
setB = [4, 5, 6, 7, 8]
print("симметрическая разность - \(setA.symmetricDifference(setB))")
