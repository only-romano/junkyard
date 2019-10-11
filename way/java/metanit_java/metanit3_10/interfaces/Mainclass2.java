public class Mainclass2{

    public static void main(String[] args){

        Journal2 printable = new Journal2("Хакер");
        printable.print();
    }

    static void read(Printable p){

        p.print();
    }
}