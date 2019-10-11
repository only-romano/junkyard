using System;

namespace MetanitBase.App
{
    public class Litterals
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }
        public readonly string Final = RunSimple("Ridj");


        private static string RunSimple(string name)
        {
            Console.WriteLine("Do you want to start simple literals example? [Yes] to continue");
            var isCool = Console.ReadLine() == "Yes";

            if (isCool)
            {
                Console.WriteLine($"{name} is cool!");
                Console.WriteLine("Running simple literals...");
                const byte bit1 = 1;
                const byte bit2 = 245;
                const sbyte bit3 = -101;
                const sbyte bit4 = -20;
                Console.WriteLine($"Sum of bites is {bit1+bit2}");
                Console.WriteLine($"Sum of sbites is {bit3+bit4}");
                Console.WriteLine("Simple litterals running is FINISED");
            } else
            {
                Console.WriteLine($"{name} is lame.");
            }
            Console.WriteLine("");
            RunChar(name);
            return $"Litterals app made by {name}";
        }

        
        private static void RunChar(string name)
        {
            Console.WriteLine("Do you want to start Char literals example? [Y] to continue");
            var answer = Console.ReadLine();
            if (answer == "Y")
            {
                Console.WriteLine($"{name} is cool!");
                const char a = 'A';
                const char b = '\x5A';
                const char c = '\u0420';
                Console.WriteLine($"Chars are: {a}, {b}, {c}");
                const string hello = "Hello";
                const string sharp = "C#";
                const string world = "World";
                Console.WriteLine($"Messege is:\n\t{hello} {sharp} {world}!");
            } else
            {
                Console.WriteLine($"{name} is lame.");
            }
            Console.WriteLine("");
            RunInt();
            RunComplicated();
        }

        private static void RunInt()
        {
            const short n1 = -30000;
            const short n2 = 102;
            const ushort n3 = 55999;
            Console.WriteLine($"Sum of shorts {n1}, {n2} and uShort {n3} is {n1+n2+n3}");

            const int a = 1123555555;
            const int b = -0xfffffff;
            const int c = 0b101110;
            const uint d = 3093344334U;
            Console.WriteLine($"Sum of Ints {a},{b} and uInt {c} is: {a+b+c+d}");

            const long l1 = -9020202202020202L;
            const ulong l2 = 18000000000000000ul;
            Console.WriteLine($"Sum of Long {l1} and uLong {l2} is fucked up");

            const float fl = 3.220774141f;
            const double db = 52311221.2222;
            const decimal dm = 7.91281625162633785974535661m;
            Console.WriteLine($"Sum of float {fl}, double {db} and decimal {dm} is fucked up");
        }

        
        private static void RunComplicated()
        {
            object a = 22;
            object c = 3.14;
            object b = "Hello Code!";
            Console.WriteLine($"Objects are: {a}, {b}, {c}");
            const string hello = "Hell to World!";
            const int num = 20;
            Console.WriteLine($"Your last words: \"{hello}\" multiplied by {num} times!");
        }
    }
}