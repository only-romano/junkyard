using System;

namespace MetanitBase.App
{
    public class Cycles
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }

        private static string SetCycle()
        {
            var num = GetByte();
            return DoCycle(num) + WhileCycle(num) + ForCycles(num) + FinalWords();
        }


        private static string DoCycle(byte a)
        {
            var result = "Instance One. Odds or Even?";
            do
            {
                result += $"\n\tNumber {a} is " + ((a>0 ? a--%2 : a++%2) == 0 ? "even": "odd");
            } while (a != 0);

            return result;
        }

        private static string WhileCycle(byte a)
        {
            var result = "\n\nInstanse Two. Divisions by number.";
            if (a == 0)
            {
                result += "\n\tYour's number is zero, there is no divisions";
                return result;
            }
            while (a != 0)
            {
                result += $"\n\t1 / {a} = {( a>0 ? 1/a-- : 1/a++ )}";
            }

            return result;
        }

        private static string ForCycles(byte a)
        {
            var result = "\n\nInstanse Three. Squares of numbers.";
            if (a == 0)
            {
                result += "\n\tYour's number is zero, there is only one square and it is Zero";
                return result;
            }

            switch (a > 0)
            {
                case true:
                    for (; a != 0;)
                    {
                        result += $"\n\tSquare of {a} is {a*a--}";
                    }
                    break;
                default:
                    for (; a != 0;)
                    {
                        result += $"\n\tSquare of {a} is {a*a++}";
                    }
                    break;
            }

            return result;
            /*
            for (;a>0;a-=2)
            {
                Console.WriteLine("Even square of {0} is {1}", a, a*a);
            }
            for (;num>0;)
            {
                if (num == 1) break;
                Console.WriteLine("Odd square of {0} is {1}", --num, num*num--);
            }
             */
        }

        private static string FinalWords()
        {
            Console.WriteLine("What is your name?");
            return $"Cycles app was made by Ridj for {Console.ReadLine()}";
        }

        private static byte GetByte()
        {
            Console.WriteLine($"Please input value for byte x (0 to 255): ");
            byte result;
            try
            {
                result = Convert.ToByte(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                result = GetByte();
            }

            return result;
        }
    }
}