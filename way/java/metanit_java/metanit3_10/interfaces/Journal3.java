// Вложенные интерфейсы

// Как и классы, интерфейсы могут быть вложенными, то есть могут быть определены
// в классах или других интерфейсах. Например:

class Printer{
    interface Printable {

        void print();
    }
}

// При применении вложенного интерфейса нам надо указывать его полное имя вместе
// с именем класса:

public class Journal3 implements Printer.Printable {

    String name;

    Journal3(String name){

        this.name = name;
    }
    public void print(){

        System.out.printf("Журнал '%s'\n", name);
    }
}