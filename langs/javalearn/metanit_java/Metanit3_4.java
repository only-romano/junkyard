public class Metanit3_4{
// Статические члены и модификатор static.
    public static void main(String[] args){
    // Для объявления статических переменных и методов перед их объявлением
    // указывается ключевое слово static.  Статические члены класса могут
    // использоваться без создания объектов класса.

        // B каждом вызове конструктора переменная counter будет увеличиваться на
        // единицу, так как она относится не к конкретному объекту, а ко всему
        // классу Book в целом или всем объектам Book сразу:

        // N поскольку методы factorial и fibonachi, а также поле PI являются
        // статическими, то мы можем к ним обратиться напрямую без создания
        // объекта класса: factorial(5).

        // При использовании статических методов надо учитывать ограничения: в
        // статических методах мы можем вызывать только другие статические методы
        // и использовать только статические переменные.

        Book b1 = new Book("Война и мир", "Л. Н. Толстой", 1863);
        b1.displayId();

        Book b2 = new Book("Отцы и дети", "N. Тургенев", 1862);
        b2.displayId(); // выведет Id: 2

        int num1 = Algorithm.factorial(5);
        int num2 = Algorithm.fibonachi(5);

        System.out.println(Algorithm.PI);
    }


class Algorithm{
 
    public final static double PI = 3.14;
  
    public static int factorial(int x){
         
        if (x == 1)
        {
            return 1;
        }
        else
        {
            return x * factorial(x - 1);
        }
    }
    public static int fibonachi(int x)
    {
        if (x == 0)
        {
            return 1;
        }
        if (x == 1)
        {
            return 1;
        }
        else
        {
            return fibonachi(x - 1) + fibonachi(x - 2);
        }
    }
}

class Book{
     
    private int id;
    private static int counter=1;
        // Класс Book содержит статическую переменную counter, которая
        // увеличивается в конструкторе и ее значение присваивается переменной id.

        // Hередко для инициализации статических полей применяется статический блок.
        // Этот блок вызывается один раз в программе при создании первого объекта
        // данного класса:
    //  static {

    //      counter=1;
    //      System.out.println("Вызов статичекского блока")
    //  }
     
    public void displayId(){
     
        System.out.printf("Id: %d \n", id);
    }
     
    private String author;
    private int year;
    private String name;
     
    Book(String name, String author, int year){
         
        this.name = name;
        this.author = author;
        this.year = year;
        id=counter++;
    } 
}
}