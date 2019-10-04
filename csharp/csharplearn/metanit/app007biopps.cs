using System;

namespace Binary
{
    class App
    {
        static void Main()
        {
            Console.WriteLine(
                "Numbers: {0}, {1}; \n\tResults: {2}(x%y), {3}(x^y), {4}(x|y), {5}(~y), {6}(x<<4), {7}(y>>4). \nThank You.",
                225, 11143, 225&11143, 225^11143, 225|11143, ~11143, 225<<4, 11143>>4);
        }
    }
}