// Статические методы
// Начиная с JDK 8 в интерфейсах доступны статические методы - они аналогичны методам класса.

interface Printable3 {

    void print();

    static void read(){

        System.out.println("Чтение печатного издания");
    }
}