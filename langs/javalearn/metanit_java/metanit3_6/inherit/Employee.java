package inherit;

// Tак как этот класс реализует тот же функционал, что и класс Person, так
// как сотрудник - это также и человек, то было бы рационально сделать класс
// Employee производным (или наследником) от класса Person, который, в свою
// очередь, называется базовым классом или родителем.

// Для класса Employee базовым является Person, и поэтому класс Employee
// наследует все те же поля и методы, которые есть в классе Person.

class Employee extends Person{

    private String company;

    public Employee(String name, String surname, String company){

        // Так как поля name и surname в базовом классе Person объявлены с
        // модификатором private, то мы не можем к ним напрямую обратиться
        // из класса Employee.  Однако в данном случае нам это не нужно.  Чтобы
        // их установить, мы обращаемся к конструктору базового класса с помощью
        // ключевого слова super, в скобках после которого идет перечисление
        // передаваемых аргументов.

        super(name, surname);
        this.company = company;
    }

    public void displayInfo(){

        super.displayInfo();
        System.out.println("Компания: " + company);
    }
}