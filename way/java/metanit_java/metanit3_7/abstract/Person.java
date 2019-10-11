public abstract class Person{

    private String name;
    private String surname;

    public String getName() { return name; }
    public String getSurname() { return surname; }

    public Person(String name, String surname){

        this.name=name;
        this.surname=surname;
    }

    public abstract void displayInfo();
}

// Зачем нужны абстрактные классы? Допустим, мы делаем программу для обсулживания
// банковских операций и определяем в ней три класса: Person, который описывает
// человека, Employee, который описывает банковского служащего, и класс Client,
// который представляет клиента банка.  Очевидно, что классы Employee и Client
// будут производными от класса Person, так как оба класса имеют некоторые общие
// поля и методы.N так как все объекты будут представлять либо сотрудника, либо
// клиента банка, то напрямую мы от класса Person создавать объекты не будем.
// Поэтому имеет смысл сделать его абстрактным.

class Employee extends Person{

    private String bank;

    public Employee(String name, String surname, String company) {

        super(name, surname);
        this.bank=company;
    }

    public void displayInfo(){

        System.out.println("Nмя: " + super.getName() + " Фамилия: "
                + super.getSurname() + " Работает в банке: " + bank);
    }
}

class Client extends Person
{
    private String bank;

    public Client(String name, String surname, String company) {

        super(name, surname);
        this.bank=company;
    }

    public void displayInfo(){

        System.out.println("Nмя: " + super.getName() + " Фамилия "
                + super.getSurname() + " Клиент банка: " + bank);
    }
}