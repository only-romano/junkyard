using System;

namespace Converter
{
    class App
    {
        static void Main()
        {
            Console.Write("Input byte 0 to 255: ");
            byte a = (byte)(Convert.ToInt16(Console.ReadLine()));
            byte b = (byte)(a + 70);
            double c = 4.0;
            decimal d = (decimal)c;
            try
            {
                byte num3 = checked((byte)(a+b));
                Console.WriteLine(num3 + d);
            }
            catch (OverflowException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}