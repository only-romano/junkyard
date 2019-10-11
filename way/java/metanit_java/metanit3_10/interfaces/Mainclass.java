public class Mainclass{

    public static void main(String[] args){

        Book b1 = new Book("Война и Мир", "Л. Н. Толстой", 1863);
        b1.print();

        // В тоже время мы не можем напрямую создавать объекты интерфейсов, поэтому
        // следующий код не будет работать:
        // Printable pr = new Printable();
        // pr.print();

        // Класс Book и класс Journal связаны тем, что они реализуют интерфейс Printable.
        // Поэтому мы динамически в программе можем создавать объекты Printable как
        // экземпляры обоих классов:

        Printable printable = new Book("Ghandi", "Kingsley", 1980);
        printable.print();
        printable = new Journal("Хакер");
        printable.print();

        // N также как и в случае с классами, интерфейсы могут использоваться в качестве
        // типа параметров метода или в качестве возвращаемого типа:

        Printable printable2 = createPrintable("Компьютерра", false);
        printable2.print();

        read(new Book("Отцы и дети", "Тургенев", 1862));
        read(new Journal("Fucker"));
    }

    static void read(Printable p){

        p.print();
    }

    static Printable createPrintable(String name, boolean option){

        if(option)
            return new Book(name, "unknown", 2015);
        else
            return new Journal(name);
    }
}