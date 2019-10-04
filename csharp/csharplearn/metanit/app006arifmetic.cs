using System;

namespace Arifmetics
{
    class App
    {
        static void Main()
        {
            Console.WriteLine(runSimpleArifmetics());
        }
        static string runSimpleArifmetics()
        {
            Console.Write("Input operand: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int num1 = num + 12;
            int num2 = num1 - 6;
            int num3 = num2 * 5;
            int num4 = num3 / 2;
            double num5 = Convert.ToDouble(num4) / 2.0;
            return "Result of simple Arifmetics is "+num5+" and final is: " + ++num5%2;
        }
    }
}