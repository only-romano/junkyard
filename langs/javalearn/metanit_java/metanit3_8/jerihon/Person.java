package jerihon;

public abstract class Person{

    private String name;

    public String getName() { return name; }

    public Person(String name){

        this.name=name;
    }

    public abstract void displayInfo();
}

class Employee extends Person{

    private String company;

    public Employee(String name, String company){

        super(name);
        this.company=company;
    }

    public String getCompany(){

        return this.company;
    }

    public void displayInfo(){

        System.out.println("Nмя: " + super.getName() + "Работает в : " + company);
    }
}

class Client extends Person{

    private int sum;
    private int percentage;
    private String bank;

    public Client(String name, String bankm, int sum, int percentage){

        super(name);
        this.bank=bank;
        this.sum=sum;
        this.percentage=percentage;
    }

    public void displayInfo(){

        System.out.println("Nмя: " + super.getName() + "Nмеет счёт в банке: " + bank);
    }

    public String getBank(){

        return this.bank;
    }

    public int getSum(){

        return this.sum;
    }

    public int getPercentage(){

        return this.percentage;
    }
}

// В этой иерархии классов можно проследить следующую цепь наследования:
// Object (все классы неявно наследуются от типа Object) ->
// Person -> Employee|Client.