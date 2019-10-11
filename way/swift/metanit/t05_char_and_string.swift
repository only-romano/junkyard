// Типы данных Character ии String
var char: Character = "O"
var hello: String = "Jello!"
var emptyString: String = String()
let text = """
OOO "Рога и копыта \(String(777))"
Ген. директор: Катик
"""
print(char, "\n" + hello + emptyString, "\n" + text)

var x = 5
var y = 11
hello = "Это шёпот усталых губ \(x + y)"
print(hello)
