using System;

namespace MetanitBase.App
{
    public class Converter
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }
        public readonly string Final = ConvertBytes() + FinalWords();

        private static string ConvertBytes()
        {
            var x = GetByte("x");
            var y = GetByte("y");
            var z = GetDouble("z");
            var d = (decimal) z;
            string result;
            try
            {
                var a = checked((byte) (x + y));
                result = $"And we do this for x+y+z {a + d}";
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                result = $"So there it is, {x + y + d}";
            }

            return result;
        }

        private static string FinalWords()
        {
            Console.WriteLine("What is your name by the way?");
            return $"\n\tConverter app and all the staff was made for you, {Console.ReadLine()}, by me, Ridj";
        }

        private static byte GetByte(string name)
        {
            Console.WriteLine($"Please input value for byte {name} (0 to 255): ");
            byte result;
            try
            {
                var temp = Convert.ToInt16(Console.ReadLine());
                try
                {
                    result = Convert.ToByte(temp);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                    result = (byte) temp;
                    Console.WriteLine($"For byte {name} was selected value of {result}");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                result = GetByte(name);
            }

            return result;
        }

        private static double GetDouble(string name)
        {
            Console.WriteLine($"Please input value for double {name}: ");
            double result;
            try
            {
                result = Convert.ToDouble(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                result = GetDouble(name);
            }

            return result;
        }
    }
}