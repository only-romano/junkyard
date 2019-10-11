package objects;

class Book{

    Book b1 = new Book("War and Peace", "Tolstoy", 1863);
    System.out.println(b1.toString());

    public String toString(){

        return "Book '" + name + "' (author " + author + ")";
    }
}