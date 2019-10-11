// Чтобы класс применил интерфейс, надо использовать ключевое слово implements.

class Book implements Printable{

    String name;
    String author;
    int year;

    Book(String name, String author, int year){

        this.name = name;
        this.author = author;
        this.year = year;
    }

    public void print() {

        System.out.printf("Книга '%s' (автор %s) была издана в %d году \n", name, author, year);
    }
}

// При этом надо учитывать, что если класс применяет интерфейс, то он должен
// реализовать все методы интерфейса, как в случае выше реализован метод print.