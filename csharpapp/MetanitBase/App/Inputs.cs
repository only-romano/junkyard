using System;

namespace MetanitBase.App
{
    public class Inputs
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }
        public readonly string Final = RunInputMethod();


        private static string RunInputMethod()
        {
            Console.Write("Welcome to anketizing! Please introduce yourself to us: ");
            var name = Console.ReadLine();
            Console.WriteLine($"\tHello, {name}! Let's get it started!");
            return Anceting(name);
        }


        private static string Anceting(string name)
        {
            var final = $"Allright then, {name}.";
            Console.Write($"Input your age, {name}: ");
            try
            {
                var age = Convert.ToByte(70 - Convert.ToByte(Console.ReadLine()));
                final += $" You have {age} ages left remaining.";
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.Write($"Input your height in metres, {name}: ");
            try
            {
                var height = Convert.ToSByte((1.98 - Convert.ToDouble(Console.ReadLine())) * 100);
                final += $" You shorter then me by {height} sm.";
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.WriteLine($"{final}\nSee you later, {name}");
            return $"\tInput app made by Ridj special for {name}";
        }
    }
}