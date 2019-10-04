package metanit3_1;

public class Book{

    public String name;
    public String author;
    public int year;

    Book(){

        name = "неизвестно";
        author = "неизвестно";
        year = 0;
    }

    Book(String name, String author, int year){

        this.name = name;
        this.author = author;
        this.year = year;
    }

    public void info(){
        System.out.printf("Книга '%ы' (автор %s) была издана в %d году \n",
            name, author, year);
    }
}