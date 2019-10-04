using System;

namespace Hello
{
    class App
    {
        static void Main()
        {
            Console.Write("Input your name: ");
            string name = Console.ReadLine();
            Console.Write("Hello, {0}", name);
            Console.ReadKey();
        }
    }
}
