// Если нам надо применить в классе несколько интерфейсов, то они все перечисляются
// через запятую после слова implements:

interface Printable4 {

    void print();
}

interface Readeble4 {

    static void read(){

        System.out.println("Чтение");
    }
}

class Book implements Printable4, Readeble4{

    Readeble4.read();

    Printable4.print();
}