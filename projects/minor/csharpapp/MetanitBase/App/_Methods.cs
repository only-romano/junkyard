using System;

namespace MetanitBase.App
{
    public static class Methods
    {
        public const byte ApN = 12;

        // Running methods


        // Getters

        public static byte GetBytes(string str="", string question="")
        {
            Console.Write(question);

            try
            {
                var bytes = str != "" ? str : Console.ReadLine();
                if (bytes == "" || bytes == "q") return 99; 
                return Convert.ToByte(bytes);
            }
            catch (Exception e)
            {
                if (str != "") return 255;
                Console.WriteLine(e.Message);

                return GetBytes();
            }
        }


        public static byte GetIndex(byte n) => (byte) (n == 77 ? ApN - 1 : n < 1 || n > ApN ? ApN : n);


        public static string GetString(string text="", string final="", string fail="", Func<string, bool> check=null)
        {
            Console.Write(text);

            string result;
            try
            {
                result = Console.ReadLine();
                if (check != null && !check(result)) throw new Exception();
            }
            catch (Exception)
            {
                result = fail;
            }

            if (final != "") Print(final + result);

            return result;
        }



        // Checkers

        public static bool CheckString(string statement="", Func<string, bool> check=null, string quiz="",bool exactly=false)
        {
            Console.WriteLine(statement);
            try
            {
                var answer = Console.ReadLine();
                answer = answer == null ? "" : exactly ? answer : answer.ToLower();

                if (quiz != "") return answer == quiz;

                return check?.Invoke(answer) ?? answer == "y" || answer == "д";
            }
            catch (Exception)
            {
                return false;
            }
        }



        // Helpers

        public static Func<TResult> Bind<T, TResult>(Func<T, TResult> func, T arg) =>  () => func(arg);
        public static Func<TResult> BindTwo<T1, T2, TResult>(Func<T1, T2, TResult> func, T1 arg, T2 arg2) =>  () => func(arg, arg2);
        public static string Increase(string count) => count == "255" ? count : Convert.ToString(GetBytes(count)+1);
        public static string UpdatedStat() => $"{Program.Count}-{Program.Quiz}-{Program.Code}";
        public static bool Print(string text)
        {
            Console.WriteLine(text + (Program.Language
                                  ? "\nНажмите ввод для продожения\n"
                                  : "\nPress enter to continue.\n"));
            Console.ReadLine();
            return true;
        }
    }
}
