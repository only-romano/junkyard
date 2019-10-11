package tenums;

import java.util.Scanner;

public class Enums {

    public static void main(String[] args) {

        Book b1 = new Book("Война и мир", "Л. Н. Толстой", 1863, Type.BELLETRE);

        Scanner in = new Scanner(System.in);
        System.out.println("Введите числовой тип книги:");
        int id = in.nextInt();

        Type type = Type.values()[id];
        System.out.println("Выбран тип: " + type);
        if(b1.bookType == type) {

            System.out.println("Книга '"+ b1.name +"' соответствует выбранному типу");
        }
    }
}