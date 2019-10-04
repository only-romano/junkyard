using System;

namespace Litera
{
    class App
    {
        static void Main()
        {
            string name = "Kato";
            runSimple(name);
        }

        static void runSimple(string name)
        {
            Console.WriteLine("Do you want to start simple literals example? [Yes] to continue");
            bool isCool = Console.ReadLine() == "Yes";

            if (isCool)
            {
                Console.WriteLine("{0} is cool!", name);
                Console.WriteLine("Running simple literals...");
                byte bit1 = 1;
                byte bit2 = 245;
                sbyte bit3 = -101;
                sbyte bit4 = -20;
                Console.WriteLine("Sum of bites is " + (bit1+bit2));
                Console.WriteLine("Sum of sbites is " + (bit3+bit4));
                Console.WriteLine("Simple litterals running is FINISED");
            } else
            {
                Console.WriteLine("{0} is lame.", name);
            }
            Console.WriteLine("");
            runChar(name);
        }

        static void runChar(string name)
        {
            Console.WriteLine("Do you want to start Char literals example? [Y] to continue");
            string answer = Console.ReadLine();
            if (answer == "Y")
            {
                Console.WriteLine("{0} is cool!", name);
                char a = 'A';
                char b = '\x5A';
                char c = '\u0420';
                Console.WriteLine("Chars are: {0}, {1}, {2}", a, b, c);
                string hello = "Hello";
                string sharp = "C#";
                string world = "World";
                Console.WriteLine("Messege is:\n\t{0} {1} {2}!", hello, sharp, world);
            } else
            {
                Console.WriteLine("{0} is lame.", name);
            }
            Console.WriteLine("");
            runInt();
            runComplicated(name);
        }

        static void runInt()
        {
            short n1 = -30000;
            short n2 = 102;
            ushort n3 = 55999;
            Console.WriteLine("Sum of shorts {0}, {1} and uShort {2} is {3}", n1, n2, n3, n1+n2+n3);


            int a = 1123555555;
            int b = -0xfffffff;
            uint c = 4093344334U;
            Console.WriteLine("Sum of Ints {0},{1} and uInt {2} is: {3}", a, b, c, a+b+c);

            long l1 = -9020202202020202L;
            ulong l2 = 18000000000000000ul;
            Console.WriteLine("Sum of Long {0} and uLong {1} is fucked up", l1, l2);

            float fl = 3.220774141f;
            double db = 52311221.2222;
            decimal dm = 7.91281625162633785974535661m;
            Console.WriteLine("Sum of float {0}, double {1} and decimal {2} is fucked up", fl, db, dm);
        }

        static void runComplicated(string name)
        {
            object a = 22;
            object c = 3.14;
            object b = "Hello Code!";
            Console.WriteLine("Objects are: {0}, {1}, {2}", a, b, c);
            var hello = "Hell to World!";
            var num = 20;
            Console.WriteLine("Your last words: \"{0}\" multiplied by {1} times!", hello, num);
        }
    }
}