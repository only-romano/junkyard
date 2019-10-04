// Наследование, переопределение методов и ключевое слово super

package inherit;

public class Metanit3_6{

    public static void main(String[] args){

        Employee empl = new Employee("Tom", "Simpson", "Oracle");
        empl.displayInfo();
        String firstName = empl.getName();
        System.out.println(firstName);
    }
}