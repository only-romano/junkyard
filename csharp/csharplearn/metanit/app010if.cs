using System;

namespace Ifs
{
    class App
    {
        static void Main()
        {
            Console.Write("Input first number: ");
            int num1 = Convert.ToInt16(Console.ReadLine());
            Console.Write("Input second number: ");
            int num2 = Convert.ToInt16(Console.ReadLine());

            if (num1 != num2)
            {
                int num3 = num1 - num2;
                switch (num3 > 0)
                {
                    case true:
                        Console.WriteLine("{0} is Greater then {1} by {2}!", num1, num2, num3);
                        break;
                    default:
                        Console.WriteLine("{0} is Smaller then {1} by {2}!", num1, num2, -num3);
                        break;
                }

                Console.Write("{0} is {1}", num3, num3%2 == 0 ? "Even" : "Odd");
            }
            else
            {
                 Console.WriteLine("Numbers are Equal !");
            }
        }
    }
}