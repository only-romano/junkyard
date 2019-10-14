using System;

namespace MetanitBase.App
{
    public class Condition
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }

        public readonly string Final= CompareNumbers(GetNumber("x"), GetNumber("y")) + FinalWords();

        private static string CompareNumbers(int x, int y)
        {
            if (x == y)
            {
                return $"Numbers {x} and {y} are Equal";
            }
            
            string result;
            var z = x - y;

            switch (z > 0)
            {
                case true:
                    result = $"{x} is greater then {y} by {z}";
                    break;
                default:
                    result = $"{x} is smaller then {y} by {-z}";
                    break;
            }
            result += $"x - y = {z} and it's is" + (z%2 == 0 ? "Even" : "Odd");
            
            return result;
        }


        private static string FinalWords()
        {
            Console.WriteLine("Introduce yourself, please: ");
            return $"Comapare app was made by Ridj for {Console.ReadLine()}";
        }

        
        private static int GetNumber(string name)
        {
            int result;
            Console.Write($"Please input number value to {name} variable: ");
            try
            {
                result = Convert.ToInt32(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                result = GetNumber(name);
            }

            return result;
        }
    }
}