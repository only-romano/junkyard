package inherit;

public class Person{

    // Чтобы запретить наследование:
// public final class Person{} // - ключевое слово 'final', c помощью этого слова
                             // можно запретить переопределение отдельных методов:
// public final void displayInfo(){}
    
    // В этом случае в классе Employee надо будет создать метод с другим именем
    // для вывода информации об объекте.

    private String name;
    private String surname;

    public String getName() { return name; }
    public String getSurname() { return surname; }

    public Person(String name, String surname){

        this.name = name;
        this.surname = surname;
    }

    public void displayInfo(){

        System.out.println("Nмя: " + name + " Фвмилия: " + surname);
    }
}