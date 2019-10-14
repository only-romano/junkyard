using System;

namespace MetanitBase.App
{
    public class Arithmetics
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }

        private static string RunSimpleArithmetics()
        {
            Console.Write("Input operand: ");
            var num = Convert.ToInt16(Console.ReadLine());
            num += 12 - 6;
            var newNum = Convert.ToDouble(num * 5) / 2.0;
            return $"Result of simple Arifmetics is {newNum} & final is {++newNum%2}\n\tArithmetics app made 4U by Ridj";
        }
    }
}