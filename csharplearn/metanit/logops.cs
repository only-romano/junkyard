using System;

namespace LogicOperations
{
    class Program
    {
        public static void Main()
        {
            int x = 2;
            int y = 5;
            Console.WriteLine("{0}, {1}", x&y, x|y);
            x = 4;
            Console.WriteLine("{0}, {1}", x&y, x|y);
            x = 12;
            Console.WriteLine(~x+1);
            x = 45;
            int key = 102;
            int encrypt = x ^ key;
            Console.WriteLine("Encrypted number: " +encrypt);
            int decrypt = encrypt ^ key;
            Console.WriteLine("Decrypted number: " +decrypt);
        }
    }
}