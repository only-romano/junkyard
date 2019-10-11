using System;

namespace ConsoleInput
{
    class Program
    {
        public static void Main()
        {
            Hello();
            Tom();
            Person();
        }

        private static void Hello()
        {
            string hello = "Hello World";
            Console.WriteLine(hello);
            Console.WriteLine("Welcome to the C# World!");
            Console.WriteLine("Goodbye hello-world...");
            Console.WriteLine(24.5);
            Console.ReadKey();
        }

        private static void Tom()
        {
            string name = "Tom";
            int age = 33;
            decimal height = 1.7;
            Console.WriteLine("{0} is {1} years old and has a height of {2} metres", name, age, height);
            Console.ReadKey();
        }

        private static void Person()
        {
            Console.WriteLine("Input your name: ");
            string name = Console.ReadLine();
            name = name == "" ? "Unknown" : name;

            Console.WriteLine("Input your age: ");
            int age = 18;
            try {
                age = Convert.ToInt32(Console.ReadLine());
            } catch (e) {
                Console.WriteLine(e);
            }

            Console.WriteLine("Input your height in metres: ");
            double height = 1.8;
            try {
                height = Convert.ToDouble(Console.ReadLine());
            } catch (e) {
                Console.WriteLine(e);
            }

            Console.WriteLine("Input your annual salary in US Dollars: ");
            decimal salary = Concert.ToDecimal(10000.00);
            try {
                salary = Convert.ToDecimal(Console.ReadLine());
            } catch (e) {
                Console.WriteLine(e);
            }

            Console.WriteLine("{0} is {1} years old and has height of {2} metres, has annual salary of {3} $.", name, age, height, salary);
            Console.ReadKey();
        }
    }
}