class Book {

    var name: String
    init(name: String){

        self.name = name
    }
}

class Library{

    var books: [Book] = [Book]()

    init() {

        books.append(Book(name: "Война и мир"))
        books.append(Book(name: "Отцы и дети"))
        books.append(Book(name: "Чайка"))
    }

    // Подписка позволяет по индексам получать доступ к указанным свойствам
    subscript(index: Int) -> Book {
        
        get{
            return books[index]
        }

        set(newValue) {
            books[index] = newValue
        }
    }
}

var myLibrary: Library = Library()
var firstBook: Book = myLibrary[0]  // получение по индексу
print(firstBook.name)

myLibrary[2] = Book(name: "Мартин Иден")  // изменение по индексу
print(myLibrary[2].name)
