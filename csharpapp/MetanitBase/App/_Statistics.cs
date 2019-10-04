using System;
using System.Linq;

namespace MetanitBase.App
{
    public static class Statistics
    {

        public static bool Align(int final)
        {
            var score = Program.Quiz;

            if (Program.Code == "0") Program.Code = final >= 9 ? "1" : "0";
            Program.Quiz = final > Convert.ToByte(score) ? final.ToString() : score;

            return true;
        }


        public static string[] Get()
        {
            string statistic;
            try
            {
                statistic = Files.Read();
            }
            catch(Exception)
            {
                statistic = "Init" + string.Concat(Enumerable.Range(0, Methods.ApN).Select(i => " 0-0-0"));
                Files.Write(statistic);
            }

            return statistic.Split();
        }


        public static string Pretty(string name)
        {
            var count = Program.Count;
            var code = Program.Code == "0";
            var quiz = Program.Quiz;
            var user = Program.Name;

            return Program.Language

                ? $"\n\t{user}, ваша обновлённая статистика по уроку \"{name}\"\n\tПосещений урока: {count} раз\n\tЛу" +
                  $"чший результат викторины {quiz}/10 и вы " + (code ? "не " : "") + "видели Код к этому уроку.\n"

                : $"\n\t{user}, your's updated stats for \"{name}\" course\n\tCourse was visited {count} times;\n\tQu" +
                  $"iz best result is {quiz}/10 and you have " + (code ? " not" : "") + " seen Code for this lesson.\n";
        }


        public static bool Show()
        {
            var lang = Program.Language;

            var apps = lang
                ? new []
                    {
                        "", "Hello World", "Литераллы", "Ввод\\Вывод", "Арифметика", "Бинарность",
                        "Подсчёт слов", "Присваивания", "Конвертер", "Сравнения", "Перебор, циклы",
                        "Пасхальный урок", "Нет такого урока"
                    }
                : new []
                    {
                        "", "Hello World", "Var Litterals", "Input\\Output", "Arithmetics", "Binary ops",
                        "Words Counter", "Assignments", "Type converter", "Compare numbers", "Cycle types",
                        "Easter Eggs", "Errors in choose"
                    };

            var fields = lang
                ? new[] { "Урок \"", "\"\tПросмотры: ", "\tЛучший результат в викторине, (из 10): ", "\tПоказан код: " }
                : new[] { "App \"", "\"\tVisits: ", "\tQuiz best (out of 10): ", "\tCode seen: " };

            var stats = Files.Read().Split();

            Console.WriteLine(
                $"\n{Program.Name}, " + (
                    lang 
                        ? "ваша статистика по всем урокам:"
                        : "is statistics for all lessons:"
                    ) + "\n"
                );

            for (byte a = 1; a < apps.Length; a++)
            {
                var stat = stats[a].Split('-');
                Console.WriteLine(
                    fields[0]+apps[a] + fields[1]+stat[0] + fields[2]+stat[1] +
                    fields[3]+( stat[2] == "0" ? lang ? "нет" : "no" : lang ? "да" : "yes" ) + "\n");
            }

            return true;
        }
    }
}
