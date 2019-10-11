using System.IO;
using System.Text;

namespace MetanitBase.App
{
    public static class Files
    {
        private const string History = "history.txt";


        public static string Read(string address=History)
        {
            using (var fs = File.OpenRead(address))
            {
                var arr = new byte[fs.Length];
                fs.Read(arr, 0, arr.Length);
                return Encoding.Default.GetString(arr);
            }
        }


        public static void Write(string text, string address=History)
        {
            using (var fs = new FileStream(address, FileMode.OpenOrCreate))
            {
                var arr = Encoding.Default.GetBytes(text);
                fs.Write(arr, 0, arr.Length);
            }
        }
    }
}
