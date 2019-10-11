using System;

namespace Classes_and_objects
{
    class App
    {
        static void Main(string[] args)
        {
            Person sergey = new Person();
            sergey.GetInfo();

            sergey.name = "Sergey";
            sergey.age = 28;

            Person kato = new Person("Kato Basiro", 2);
            kato.GetInfo();
            sergey.GetInfo();

            Console.WriteLine(Calculate(10, 15));

            State state1 = new State();
            State state2 = new State();
            state2.x = 1;
            state2.y = 2;
            state1 = state2;
            state2.x = 5;
            Console.WriteLine("{0}, {1}", state1.x, state2.x);

            state1.country = new Country();
            Country country1 = new Country();
            country1.x = 1;
            country1.y = 4;
            state1.country = country1;
            state1.country.x = 7;
            state2 = state1;
            Console.WriteLine("{0}, {1}", country1.x, state1.country.x);
            Console.WriteLine("{0}", state2.country.x);

            Person ridj = new Person { name = "Ridj", age = 17 };
            ChangePerson(ridj);

            ChangePerson(ref sergey);

            Console.WriteLine("{0}, {1}", ridj.name, ridj.age);
            Console.WriteLine("{0}, {1}", sergey.name, sergey.age);
        }

        static int Calculate(int x, int y)
        {
            int z = x + y;
            return z;
        }

        static void ChangePerson(Person person)
        {
            person.name = "Ekaterina";
            person = new Person { name = "Sexy", age = 10000 };
            Console.WriteLine(person.name);
        }

        static void ChangePerson(ref Person person)
        {
            person.name = "Loise";
            person = new Person { name = "Baka", age = 10000 };
            Console.WriteLine(person.name);
        }
    }

    struct State
    {
        public int x;
        public int y;
        public Country country;
    }

    class Country
    {
        public int x;
        public int y;
    }

    class Person
    {
        public string name;
        public int age;

        public void GetInfo()
        {
            Console.WriteLine("Name: {0}\tAge: {1}", name, age);
        }

        public Person() : this("Unknown")
        {
        }
        public Person(string name) : this(name, 18)
        {
        }
        public Person(string name, int age)
        {
            this.name = name;
            this.age = age;
        }
    }
}