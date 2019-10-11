using System;

namespace DataTypes
{
    class Program
    {
        public static void Main()
        {
            string name = "Tom";
            int age = 33;
            bool isEmployed = false;
            double weight = 78.65;

            Console.WriteLine("Man is {0} and he is {1} age old and is {2}employed and weight is {3}", name, age, isEmployed?"":"un", weight);

            var c = 20;
            var hello = "Hello to you";
            Console.WriteLine("Type of var c is {0} and type of var hello is {1}", c.GetType().ToString(), hello.GetType().ToString());
        }
    }
}