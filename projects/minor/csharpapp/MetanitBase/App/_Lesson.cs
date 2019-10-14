using System;
using System.Collections.Generic;

namespace MetanitBase.App
{
    public static class Lesson
    {
        public static void Run(IReadOnlyList<string> stat, Question[] quiz, string[,] code, Func<bool> interactive 
                               , Func<bool>[] runs, string name, string intro, string menu=null)
        {
            Program.Count = Methods.Increase(stat[0]);
            Program.Quiz = stat[1];
            Program.Code = stat[2];

            Methods.Print(intro);

            Menu.Cycle( actions: new [,] { {"q", "в"}, {"c", "к"}, {"l", "у"}, {"e", "з"} }
                , functions: new []
                {
                    Methods.Bind(Quiz, quiz),
                    Methods.BindTwo(Code, code, runs),
                    interactive,
                    null
                }
                , info: menu ?? (Program.Language
                    ? "\n\tИнтерактивный урок: \"у\"(рус)\n\tВикторина: \"в\"\n\tКод: \"к\"\n\n\tЗакончить: \"з\"\n\n\t"
                    : "\n\tInteractive lesson: \"l\"\n\tQuiz: \"q\"\n\tCode: \"c\"\n\n\tExit: \"e\"\n\n\t")
                , stat: Methods.Bind(Statistics.Pretty, name)
            );
        }


        private static bool Quiz(Question[] quiz)
        {
            var shuffle = Shuffle(quiz);
            var final = 0;
            for (var i = 0; i < 10; i++) final += AskQuestion(shuffle[i]) ? 1 : 0;

            return Statistics.Align(final);
        }


        private static bool Code(string[,] code, Func<bool>[] runs)
        {
            if (Program.Code == "0")
            {
                Console.WriteLine(Program.Language
                    ? $"{Program.Name}, у вас нет доступа к кодам урока :("
                    : $"{Program.Name}, you have not access to Codes of lesson :(");
                return true;
            }
            var menu = "";
            var number = 1;
            var index = 0;
            var length = runs.Length * 2 + 1;
            var actions = new string[length,1];
            var functions = new Func<bool>[length--];
            var rows = code.GetUpperBound(0) + 1;

            for (var i = 0; i < rows; i++)
            {
                menu += $"\n\t{number}. \"{code[i, 0]}\"";
                actions[index, 0] = $"{number}";
                functions[index++] = Methods.Bind(Methods.Print, code[i, 1]);
                actions[index, 0] = $"{number++}+";
                functions[index++] = runs[i];
            }

            actions[length, 0] = "q";
            functions[length] = null;

            menu += "\n\n" + (Program.Language 

                ? "Чтобы увидеть код - наберите его номер, к примеру - чтобы увидеть код первого примера - введите \"" +
                  "1\" и нажмите ввод.\nЧтобы запустить код из примера наберите его номер с плюсом, то есть - чтобы з" +
                  "апустить код первого примера - введите \"1+\" и нажмите ввод. Для выхода введите \"q\" и нажмите в" +
                  "вод.\n\n\t"

                : "To see Code - input it's number. So, to see Code of second example - you must input \"2\" and pre" +
                  "ss enter. To run Code from example - input it's number with plus. So, to run Code of second examp" +
                  "le - you must input \"2+\" and press enter. To exit input \"q\" and press enter.\n\n\t");

            return Menu.Cycle( functions: functions
                , actions: actions
                , info: menu
            );
        }


        private static Question[] Shuffle(Question[] questions)
        {
            for (var t = 0; t < questions.Length; t++ )
            {
                var tmp = questions[t];
                var r = new Random().Next(t, questions.Length);
                questions[t] = questions[r];
                questions[r] = tmp;
            }

            return questions;
        }


        private static bool AskQuestion(Question quest) => Methods.CheckString(quest.Q, quiz: quest.A, exactly: quest.E);


        public struct Question
        {
            public readonly string Q;
            public readonly string A;
            public readonly bool E;
            public Question(string q, string a, bool e=true)
            {
                Q = q;
                A = a;
                E = e;
            }
        }
    }
}
