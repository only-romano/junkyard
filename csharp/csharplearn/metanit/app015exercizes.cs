using System;

namespace Exercise
{
    class App
    {
        static void Main()
        {
            printKitty();
            Console.WriteLine("a*b*c - (a+b+c) =  {0}", findFourth(34, 36.7, 7.3));
            Console.WriteLine("(a + 4b)(a - 3b) + a² = {0}", exercise1(setNumber(1), setNumber(2)));

            exercise2(setNumber(1), setNumber(2), setNumber(3));
            exercise3(setNumber(1), setNumber(2), setNumber(3));

            Console.WriteLine("Done! Boolean is {0}", exercise4(true, false, false, true));

            Console.Write("Max number, demo version.\n");
            exercise5_0(setNumber(1), setNumber(2), setNumber(3), setNumber(4));

            Console.Write("The max number is (final version): {0}",
                exercise5_1(setNumber(1), setNumber(2), setNumber(3), setNumber(4)));

            Console.Write("The {0} year is earlier.",
             exercise6_0(setNumber(1), setNumber(2), setNumber(3), setNumber(1), setNumber(2), setNumber(3)));
        }


        // METHOD to simplify building of integer variable
        static int setNumber(int num)
        {
            Console.Write("\tInput {0} number: ", num);
            return Convert.ToInt16(Console.ReadLine());
        }


        // EXERCISE 0 - Drawing Kitty
        static void printKitty()
        {
            Console.WriteLine("\n\t\\    /\\\n\t )  ( *)\n\t (  /  )\n\t  \\(__)|\n");
        }


        // CANCELED EXERCISE - Arifmetic operations with double
        static double findFourth(int a, double b, double c)
        {
            return a*b*c - (a+b+c);
        }


        // EXERCISE 1 - Arifmetic expression with integers
        static int exercise1(int a, int b)
        {
            return (a + 4*b)*(a - 3*b) + a*a;
        }


        // EXERCISE 2 - Arifmetic operations with double
        static void exercise2(int a, int b, int c)
        {
            Console.WriteLine("Mid Arifmetic: {0}\tExpression: {1}", Convert.ToDouble(a+b+c)/3, 2*(a+c) - 3*b);
        }


        // EXERCISE 2.5 - puzzle
        static void exercise3(int a, int b, int c)
        {
            c += b + a;
            b = c - b - 2*a;
            Console.WriteLine("After reorganisation: a = {0}, b = {1}, c = {2}", c - a - b, b, c);
        }


        // EXERCISE 3 - Logical expressoin
        static bool exercise4(bool a, bool b, bool c, bool d)
        {
            return (a == c) && (a != b) || (c == d);
        }


        // EXERCISE 4.0 (beta version) - find max number
        public static void exercise5_0(int a, int b, int c, int d)
        {
            setFunc(a, b, delegate (int outerNum){
                setFunc(outerNum, c, delegate(int innerNum) {
                    setFunc(innerNum, d, Console.WriteLine); }); });
        }
        static void setFunc(int first, int second, Action<int> function)
        {
            if (first > second) function(first);
            else function(second);
        }


        // EXERCISE 5.1 (final version) - find max number
        public static int exercise5_1(int a, int b, int c, int d)
        {
            return findBigger(d, findBigger(c, findBigger(b, a)));
        }
        static int findBigger(int num1, int num2)
        {
            return num1 > num2 ? num1 : num2;
        }


        public static string exercise6_0(int y1, int m1, int d1, int y2, int m2, int d2)
        {
            return (y1 > y2) | (y1 == y2 && (m1 > m2 || (m1 == m2 && d1 > d2))) ? "second" : "first";
        }

    }
}