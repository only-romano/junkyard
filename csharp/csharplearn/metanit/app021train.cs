using System;

namespace Try
{
    class App
    {
        static void Main(string[] args)
        {
            Write(true, false, false);
            int[] a = new int[4];
            try
            {
                a[5] = 4;
                Console.WriteLine("End of \"Try\" block");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("\"Finally\" block");
            }

            try
            {
                string message = Console.ReadLine();
                if (message.Length > 6)
                {
                    throw new Exception("Length of string more then 6 symbols");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }

            Console.Write("Input number: ");
            int x;
            string input = Console.ReadLine();
            if (Int32.TryParse(input, out x))
            {
                x *= x;
                Console.WriteLine("Square of number: " + x);
            }
            else
            {
                Console.WriteLine("Incorrect input!");
            }

            Console.WriteLine(~true);
            Console.WriteLine(!true);
        }

        static void Write(object a, object b, object c) 
        { 
           Console.WriteLine("{0} & {1} = {2}", a, b, c); 
        }
    }
}