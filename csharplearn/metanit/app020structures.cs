using System;

namespace Structures
{
    class App
    {
        static void Main(string[] args)
        {
            Book book;
            book.name = "War & Peace";
            book.author = "Lev Tolstoy";
            book.year = 1869;

            book.Info();

            Book[] books = new Book[3];
            books[0].name = "Crime & Punishment";
            books[0].author = "F.M.Dostoyevsky";
            books[0].year = 1866;

            books[1].name = "Fathers & Sons";
            books[1].author = "I.S.Turgenev";
            books[1].year = 1862;

            books[2].name = "Ridjaiada";
            books[2].author = "Ridj";
            books[2].year = 2019;

            foreach (Book b in books)
            {
                b.Info();
            }

            Book book2 = new Book("Sexy games", "Kato Basiro", 2020);
            book2.Info();
        }

        struct Book
        {
            public string name;
            public string author;
            public int year;

            public Book(string n, string a, int y)
            {
                name = n;
                author = a;
                year = y;
            }

            public void Info()
            {
                Console.WriteLine("Book '{0}' (author: {1}) was published in {2} year",
                    name, author, year);
            }
        }
    }
}