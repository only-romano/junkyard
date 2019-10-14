using MetanitBase.App;

namespace MetanitBase
{
    internal static class Program
    {
        public static bool Language;
        public static string Name, Count, Code, Quiz;

        private static void Main()
        {
            Intro.Run();
            while (AppCycle.Start()) {}
        }
    }
}
