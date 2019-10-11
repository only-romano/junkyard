using System;

namespace Equal
{
    class App
    {
        static void Main()
        {
            int a, b;
            a = b = 34 * 2 / 4;
            Console.WriteLine("\t{0}+=2...{1}-=2...{2}*=2...{3}/=2...{4}%=2...{5}",
                a, a+=2, a-=2, a*=2, a/=2, a%2);
            Console.WriteLine("\t{0}&=16...{1}|=2...{2}^=2...{3}<<=2...{4}>>=1...{5}",
                b, b&=16, b|=2, b^=2, b <<= 2, b >>= 1);
        }
    }
}