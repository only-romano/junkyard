package inclasses;
import inclasses.Book;
import inclasses.Math;

public class Metanit3_9{

    public static void main(String[] args){

// Объекты внутренних классов могут быть созданы только в том классе, в котором
// внутренние классы опеределены. В других внешних классах объекты внутреннего
// класса создать нельзя.

        Book b1 = new Book("Война и мир", "Л. Н. Толстой", 1863, "ХудКнига");
        System.out.println(b1.publisher.name);

        Math.Factorial fact = Math.getFactorial(6);
        System.out.printf("Факториал числа %d равен %d \n", fact.getKey(), fact.getResult());
    }
}
