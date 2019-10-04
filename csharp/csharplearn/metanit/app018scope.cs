using System;

namespace Scope
{
    class App
    {
        static int a = 9;
        static void Main(string[] args)
        {
            int b = a - 1;
            {
                int c = b - 1;
                Console.WriteLine(c);
            }
            Console.WriteLine(b);
            Console.WriteLine(Factorial(10));
            Console.WriteLine(Fibonachi(10));
        }

        void Display()
        {
            int d = a + 1;
            Console.WriteLine(d);
        }

        static int Factorial(int x)
        {
            if (x == 0)
            {
                return 1;
            }
            else
            {
                return x * Factorial(x -1);
            }
        }

        static int Fibonachi(int n)
        {
            if (n == 0)
            {
                return 0;
            }
            if (n == 1)
            {
                return 1;
            }
            else
            {
                return Fibonachi(n-1) + Fibonachi(n-2);
            }
        }
    }
}