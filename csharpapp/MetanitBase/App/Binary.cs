using System;

namespace MetanitBase.App
{
    public class Binary
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }

        public readonly string Final;

        public Binary()
        {
            var x = SetVariable("x");
            var y = SetVariable("y"); 
            Final = $"Numbers are {x},{y}.\n\tResults:" +
                    $"\n\tx % y = {x&y}\n\tx ^ y = {x ^ y}\n\tx | y = {x|y}\n\r~x = {~x}" +
                    $"x << 4 = {x<<4}\n\ty >> 4 = {y >> 4}\n\tThank You" +
                    "\n\nBinary app made by Ridj for You!";
        }

        private static short SetVariable(string label)
        {
            Console.WriteLine($"Input {label} number, please: ");
            short num;
            try
            {
                num = Convert.ToInt16(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                num = SetVariable(label);
            }

            return num;
        }
    }
}