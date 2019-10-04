using System;

namespace MetanitBase.App
{
    public class WordCounter
    {
        public static void Run(System.Collections.Generic.IReadOnlyList<string> stat)
        {
        }


        private static bool RunLesson()
        {
            return true;
        }
        public readonly string Final;
        public WordCounter()
        {
            Console.WriteLine("Write a string, please: ");
            var str = Console.ReadLine();
            Final = $"In string \"{str}\" there's {CountWords(str)} words\n\t" +
                    "Word Counter was made by Ridj";
        }

        private static int CountWords(string str)
        {
            return str.Split().Length;
        }
    }
}