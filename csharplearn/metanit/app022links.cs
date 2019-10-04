using System;

namespace Links
{
    class App
    {
        static void Main(string[] args)
        {
            int a = 5;
            int b = 7;
            int c = 10;

            a *= b;
            b -= c;
            c +=c;
            b *= b;
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            int d = 1;
            int e = 2;
            int f = 5;
            e -= f -= d;

            Console.WriteLine("{0}, {1}, {2}",d, e, f);
            bool isDead;
            isDead = a != b;
            Console.WriteLine(isDead);

            Console.WriteLine("1: {0}", true ^ true & false | false);
            Console.WriteLine("2: {0}", (true == true ^ false != true));
            Console.WriteLine("3: {0}", false & false != false);
            Console.WriteLine("4: {0}", true ^ true == true);
            Console.WriteLine("5: {0}", (true != false & true == false));
            Console.WriteLine("6: {0}", !(true & false));
            Console.WriteLine("7: {0}", !(true == true & false != true));
            Console.WriteLine("8: {0}", !(false == true | false == false));
            Console.WriteLine("9: {0}", !(false != true ^ false == true));
            Console.WriteLine("10: {0}", (true == true & !(false == true | true == false)));
            Console.WriteLine("11: {0}", (false == true & !(true == false ^ false == false)));
            Console.WriteLine("12: {0}", (false == false & !(false == false ^ false == true)));
            Console.WriteLine("12: {0}", "sex".Length);
        }
    }
}