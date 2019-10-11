package inclasses;

class Book{

    String name;
    String author;
    int year;
    public Publisher publisher;

    Book(String name, String author, int year, String publ){

        this.name = name;
        this.author = author;
        this.year = year;
        publisher = new Publisher(publ);
    }

// Внутренний класс ведет себя как обычный класс за тем исключением, что его объекты
// могут быть созданы только внутри внешнего класса.  Внутренний класс имеет доступ
// ко всем полям внешнего класса, в том числе закрытым с помощью модификатора private.
// А саму ссылку на внешний класс из внутреннего можно получить с помощью выражения
// Book.this, где вначале идет имя внешнего класса.

    class Publisher{

        public String name;
        public Book book;

        public Publisher(String name){
            book=Book.this;
            this.name=name;
        }
    }

// Еще одной особенностей внутренних классов является то, что их можно объявить
// внутри любого контекста, в том числе внутри метода и даже в цикле:

    public void setPublisher(String pub1){

        class Publisher1{
            void displayInfo(){

                System.out.println("Nздатель: " + pub1);
            }
        }

        Publisher1 publisher1 = new Publisher1();
        publisher1.displayInfo();
    }

    Book b1 = new Book("Война и мир", "Л. Н. Толстой", 1863, "ХудКнига");
}