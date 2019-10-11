using System;

namespace Inputs
{
    class App
    {
        static void Main()
        {
            Console.Write("Welcome to anketizing! Please introduce yourself to us: ");
            runInpitMethod(Console.ReadLine());
        }

        static void runInpitMethod(string name)
        {
            Console.WriteLine("\tHello, {0}!\nWelcome to the C# World!", name);
            Console.WriteLine(anceting(name));
            Console.WriteLine("See You later, {0}!", name);
            Console.ReadKey();
        }

        static string anceting(string name)
        {
            Console.Write("Input your age, {0}: ", name);
            int age = Convert.ToInt32(Console.ReadLine());
            Console.Write("Input your height in metres, {0}: ", name);
            double height = Convert.ToDouble(Console.ReadLine());
            return "Thank you, " + name + "! Yur age is " + age + " and your height is " + height + " metres!";
        }
    }
}