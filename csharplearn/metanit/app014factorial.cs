using System;

namespace Factorial
{
    class App
    {
        static void Main()
        {
            try 
            {
                Console.WriteLine( factorial(Convert.ToInt16(Console.ReadLine())) );
            }
            catch (Exception ex) 
            {
                Console.WriteLine(ex.Message);
            }
        }

        static int factorial(int num)
        {
            int sum = 1;
            do
            {
                sum *= num--;
            }
            while (num > 1);
            return sum;
        }
    }
}