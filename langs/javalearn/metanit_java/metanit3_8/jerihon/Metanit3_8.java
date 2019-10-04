package jerihon;

public class Metanit3_8{

    public static void main(String[] args){

        Object emp = new Employee("Bill", "Microsoft");

        Person c1 = new Client("Tom", "UnitBank", 200, 20);

        //В данном случае работает неявное преобразование, так как
        // наши переменные представляют классы Object и Person, поэтому
        // допустимо неявное восходящее преобразование - преобразование
        // к типам, которые находятся вверху иерархии классов.

        // Однако при применении этих переменных нам придется
        // использовать явное преобразование.  Поскольку переменная emp
        // хранит ссылку на объект типа Employee, то мы можем
        // преобразовать к этому типу.

        // у класса Object нет метода displayInfo, поэтому
        // приводим к классу Employee

        ((Employee)emp).displayInfo();

        // у класса Person есть метод displayInfo
        c1.displayInfo();

        // у класса Person нет метода getBank(), поэтому
        // приводим к классу Client
        String bank = ((Client)c1).getBank();

        Employee man = new Manager("John", "City Bank");
        man.displayInfo(); // преобразование не нужно, так как в
                           // классе Employee есть метод displayInfo.

        Employee emp2 = new Employee("Gregor", "City Bank");

        // Выражение emp instanceof Manager проверяет, является ли
        // переменная emp объектом типа Manager.
        if(emp2 instanceof Manager){

            ((Manager)emp).displayInfo();
        }
        else{

            System.out.println("Преобразование недопустимо");
        }
    }
}