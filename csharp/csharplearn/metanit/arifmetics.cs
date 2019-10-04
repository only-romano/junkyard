using System;

namespace Arifmetics
{
    class Program
    {
        public static void Main()
        {
            int x = 10;
            int y = 3;
            int z = x / y;
            double a = 10;
            double b = 3;
            double c = a / b;
            double d = 10.0 / 4.0;
            double e = a / 4.0;
            Console.WriteLine("{0}, {1}, {2}, {3}", z, c, d, e);

            int x1 = 3;
            int x2 = 5;
            int x3 = 40;
            int r1 = x3---x2*x1;
            Console.WriteLine("a={0}, b={1}, c={2}, result={3}", x1, x2, x3, r1);

            int y1 = 3;
            int y2 = 5;
            int y3 = 40;
            int r2 = (y3-(--y2))*y1;
            Console.WriteLine("a={0}, b={1}, c={2}, result={3}", y1, y2, y3, r2);
        }
    }
}