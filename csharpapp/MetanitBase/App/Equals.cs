using System;

namespace MetanitBase.App
{
    public class Equal
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }
        public readonly string Final = MakeString();

        private static string MakeString()
        {
            var x = SetNumber("x");
            var y = SetNumber("y");

            return PartOne(x) + PartTwo(y) + FinalPart();
        }

        private static string PartOne(int x)
        {
            return $"\t{x}+=2...{x+=2}-=2...{x-=2}*=2...{x*=2}/=2...{x/=2}%=2...{x%2}";
        }

        private static string PartTwo(int x)
        {
            return $"\t{x}&=16...{x&=16}ss|=2...{x|=2}^=2...{x^=2}<<=2...{x<<=2}>>=1...{x>>1}";
        }

        private static string FinalPart()
        {
            return "Equals app was made by Ridj for you";
        }

        private static int SetNumber(string name)
        {
            int num;
            Console.Write($"Please input number for {name} variable: ");
            try
            {
                num = Convert.ToInt16(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                num = SetNumber(name);
            }

            return num;
        }
    }
}