using System;

namespace Cycle
{
    class App
    {
        static void Main()
        {
            Console.WriteLine("Input Number: ");
            try
            {
                cycles(Convert.ToInt16(Console.ReadLine()));
                Console.WriteLine();
                Console.Write("Finished");
            }
            catch (Exception ex)
            {
                Console.Write(ex.Message);
            }
        }
        static void cycles(int num)
        {
            forCycle(num);
            doCycle(num);
        }

        static void forCycle(int num)
        {
            int a = num;
            for (;a>0;a-=2)
            {
                Console.WriteLine("Even square of {0} is {1}", a, a*a);
            }
            Console.WriteLine();
            for (;num>0;)
            {
                if (num == 1) break;
                Console.WriteLine("Odd square of {0} is {1}", --num, num*num--);
            }
        }
        static void doCycle(int num)
        {
            Console.WriteLine();
            int a = num;
            do
            {
                Console.WriteLine("Number {0} is {1}", num,  num--%2 == 0 ? "even": "odd");
            }
            while (num > 0);
            Console.WriteLine();

            while (a > 0)
            {
                Console.WriteLine("Square of number {0} is {1} then 25", a, a*a-- > 25 ? "greter" : ++a*a-- == 25 ? "equal" : "smaller");
            }
        }
    }
}