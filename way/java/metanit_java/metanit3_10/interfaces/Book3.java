// Если нам надо применить в классе несколько интерфейсов, то они все перечисляются
// через запятую после слова implements:

interface Printable4 {

    void print();

// Кроме методов в интерфейсах могут быть определены статические константы:

    int MAX_NUMBER = 400;

// Хотя такие константы также не имеют модификаторов, но по умолчанию они имеют
// модификатор доступа public static final, и поэтому их значение доступно из
// любого места программы.
}

interface Readeble4 {

    static void read(){

        System.out.println("Чтение");
    }
}

// Nнтерфейсы, как и классы, могут наследоваться:

interface BookPrintable extends Printable4{

    void paint();

// При применении этого интерфейса класс Book должен будет реализовать как методы
// интерфейса BookPrintable, так и методы базового интерфейса Printable.
}

public class Book3 implements BookPrintable, Readeble4{

        public void print() {
            System.out.printf("Журнал");
        }

        String name;

        public void read(String name) {
            this.name = name;
        }

        int num;
        public void paint(){
            System.out.println("s");
        };
}