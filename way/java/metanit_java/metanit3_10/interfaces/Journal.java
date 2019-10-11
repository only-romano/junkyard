// Одним из преимуществ использоваия интерфейсов является то, что они позволяют
// добавить в приложение гибкости. Например, в дополнение к классу Book определим
// еще один класс, который будет реализовывать интерфейс Printable:

public class Journal implements Printable {

    private String name;

    String getName(){
        return name;
    }

    Journal(String name){

        this.name = name;
    }
    public void print() {
        System.out.printf("Журнал '%s'\n", name);
    }
}