package jerihon;

public class Manager extends Employee{

    public Manager(String name, String comp){

        super(name, comp);
    }

    public void displayInfo(){

        System.out.println("Nмя: " + super.getName() + " Менеджер банка " + super.getCompany());
    }
}