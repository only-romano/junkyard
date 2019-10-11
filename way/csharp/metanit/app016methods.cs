using System;

namespace Meth
{
    class App
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Introduce yourself: ");
            string name = Console.ReadLine();
            SayHello(name);
            SayGoodbye(name);
            Console.WriteLine("Sums: {0}, {1}",OptionalParam(y:2,x:3), OptionalParam(3,4,5,6));

            int a = 5;
            Console.WriteLine("Starting value of special variable: {0}", a);
            IncrementVal(a);
            Console.WriteLine("Value after attribute by value: {0}", a);
            IncrementRef(ref a);
            Console.WriteLine("Value after referal attr: {0}", a);

            int z, area, perimetr;
            int x = 10;
            Sum(x, 15, out z);
            GetData(x, 15, out area, out perimetr);
            Console.WriteLine(z);
            Console.WriteLine("Square is : " + area);
            Console.WriteLine("Perimetr is : " + perimetr);
        }

        static void SayHello(string name) 
        {
            Console.WriteLine("Hello, {0}!", name);
        }
        static void SayGoodbye(string name)
        {
            Console.WriteLine("GoodBye, {0}", name);
        }
        static int OptionalParam(int x, int y, int z=0, int s=0)
        {
            return x + y + z + s;
        }
        static void IncrementVal(int x)
        {
            x++;
            Console.WriteLine("Increment Value: {0}", x);
        }
        static void IncrementRef(ref int x)
        {
            x++;
            Console.WriteLine("Increment Value: {0}", x);
        }
        static void Sum(int x, int y, out int a)
        {
            a = x + y;
        }
        static void GetData(int x, int y, out int area, out int perim)
        {
            area = x *  y;
            perim = (x+y) * 2;
        }
    }
}