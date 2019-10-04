using System;
using System.Collections.Generic;

namespace MetanitBase.App
{
    public static class HelloWorld
    {
        private static bool _lang;

        public static void Run(IReadOnlyList<string> stat)
        {
            _lang = Program.Language;
            Lesson.Run(name: "HelloWorld"
                , stat: stat
                , quiz: Quiz
                , code: Code
                , runs: Runs
                , interactive: Interactive

                , intro: "\n" + (_lang

                    ? "\t\tДобро пожаловать в урок \"Hello Wolrd\"!\n\nВ этом уроке мы разберём самые базовые возмож" +
                      "ности языка С#. Мы познакомимся с выводом в консоль и напишем вместе первую програму! А ещё уз" +
                      "наем несколько занимательных фактов из историиC#.\n"

                    : "\t\tWelcome to the \"Hello World\" lesson!\n\nIn this lesson we check out some basic C# syntax" +
                      " and learn about how to write some stuff to console. Plus we gonna write our first C# program!" +
                      " So let's get ready to Fuuuuun, oh yeah.\n")
                );
        }


        private static bool Interactive()
        {
            Methods.Print(_lang
                ? "Интерактивный урок в разработке"
                : "Interactive lesson in progress");
            return true;
        }


        private static readonly Lesson.Question[] Quiz = 
        {

            new Lesson.Question(
                _lang
                    ? "Какое ключевое слово для обозначения пространства имён?\n[1 слово, 9 букв]\n"
                    : "What's the keyword to set name space?\n[1 word, 9 letters]\n"
                , "namespace"),

            new Lesson.Question(
                _lang
                    ? "Назовите ключевое слово для обозначения имени класса.\n[1 слово, 5 букв]\n"
                    : "What's the keyword to set class name?\n[1 word, 5 letters]\n"
                , "class"),

            new Lesson.Question(
                _lang 
                    ? "Какое ключевое слово мы используем, для подключения пространства имён другой библиотеки?\n[1 слово, 5 букв]\n"
                    : "What's the keyword we should use to add name space of some library?\n[1 word, 5 letters]\n"
                , "using"),

            new Lesson.Question(
                _lang
                    ? "В каком пространстве имён (библиотеке) находится так любимый нами класс Console с методом Writ" +
                      "eLine? Внимание, не забудьте, что регистр имеет значение!\n[1 слово, 6 букв]\n"
                    : "What's name space using our favorite class Console which provide us awesome methods Write & Wr" +
                      "iteLine? Don't forget that register is matters!\n[1 word, 6 letters]\n"
                , "System"),

            new Lesson.Question(
                _lang
                    ? "Какой метод должен быть в каждой программе на C#?\n[1 слово, 4 буквы]\n"
                    : "Which method is required to every program in C#?\n[1 word, 4 letters]\n"
                , "Main"),

            new Lesson.Question(
                _lang
                    ? "Какими скобками мы обозначаем тело программы, класса, метода и т.д? Выберите номер правильного" +
                      "варианта.\n1. [ ]\t2. { }\t3. ( )\t4. < >\n"
                    : "In which breckets we include body of program, class, method etc. in C#? Input number of correc" +
                      "t variant.\n1. [ ]\t2. { }\t3. ( )\t4. < >\n"
                , "2"),

            new Lesson.Question(
                _lang
                    ? "Вопрос с подвохом. Зачем мы сделали для вас курс C#?\n[1 слово, 3 буквы]\n"
                    : "Trick-question. Why do we made for you this course of C#?\n[1 word, 3 letters]\n"
                , "fun", false),

            new Lesson.Question(
                _lang
                    ? "Какой класс библиотеки System используется для работы с консолью?\n[1 слово, 7 букв]\n"
                    : "Which class of System library using for work with console?\n[1 word, 7 letters]\n"
                , "Console"),

            new Lesson.Question(
                _lang
                    ? "Какой метод класса Console используется для печати в консоли без перевода строки?\n[1 слово, 5 букв]\n"
                    : "Which method of Console class using for print in console without line break?\n[1 word, 5 letters]\n"
                , "Write"),

            new Lesson.Question(
                _lang
                    ? "Каким символом мы разделяем класс и метод при вызове метода из другого класса? Выберите номер " +
                      "правильного варианта.\n1. \",\"\t2. \"!\"\t3. \".\"\t4. \"?\"\n"
                    : "Which symbol using to divide class and method names then method running from another class? In" +
                      "put number of correct variant.\n1 \",\"\t2 \"!\"\t3 \".\"\t4 \"?\"\n"
                , "3"),

            new Lesson.Question(
                _lang
                    ? "Какой метод класса Console используется для печати в консоли с переводом строки?\n[1 слово, 9 букв]\n"
                    : "Which method of Console class using for print in console with line break?\n[1 word, 9 letters]\n"
                , "WriteLine"),

            new Lesson.Question(
                _lang
                    ? "Выберите номер корректного использования метода Console.WriteLine, если text = это строковая п" +
                      "ременная:\n1. Console.WriteLine(text);\t2. Console.WriteLine := text; \n\t3. Console.WtiteLine" +
                      " text;\t4. Console.WriteLine[text];\n\t5. Console.WriteLine.text;\t6. text(Console.WriteLine);"

                    : "Choose number of correct using Console.WriteLine number if \"text\" is string variable:\n1. Co" +
                      "nsole.WriteLine(text);\t2. Console.WriteLine := text; \n\t3. Console.WtiteLine text;\t4. Conso" +
                      "le.WriteLine[text];\n\t5. Console.WriteLine.text;\t6. text(Console.WriteLine);"
                , "1"),

            new Lesson.Question(
                _lang
                    ? "Каким ключевым словом определяется переменная типа текстового содержимого?\n[1 слово, 6 букв]\n"
                    : "Which keyword used to define variables type with text content?\n[1 word, 6 letters]\n"
                , "string"),

            new Lesson.Question(
                _lang
                    ? "Выберите номер корректного определения и присваивания строковой переменной \"text\":\n1. text " +
                      "= \"some text\";\t2. string text where text = \"some text\"; \n\t3. string text := \"some text" +
                      "\";\t4. new string(text) = \"some text\";\n\t5. string text = \"some text\";\t6. using text; t" +
                      "ext = \"some text\""

                    : "Choose number of correct defining and assigning of \"text\" variable with text content:\n1. te" +
                      "xt = \"some text\";\t2. string text where text = \"some text\"; \n\t3. string text := \"some t" +
                      "ext\";\t4. new string(text) = \"some text\";\n\t5. string text = \"some text\";\t6. using text" +
                      "; text = \"some text\""
                , "5"),

            new Lesson.Question(
                _lang
                    ? "Какие кавычки используются для текстового содержимого (не символьного, а строкового): Выберит " +
                      "е номер правильного варианта.\n1. \'text\'\t2. <text>\t3. `text`\t4. \"text\"\n"
                    : "Which quotes using to assign text content (not char, but string)? Input number of correct vari" +
                      "ant.\n1. \'text\'\t2. <text>\t3. `text`\t4. \"text\"\n"
                , "4"),
        };


        private static readonly string[,] Code = 
        {
            // 1
            {
                "Hello World",

                "using System;\n\nnamespace Lesson\n{\n\tpublic static class HelloWorld\n\t{\n\t\tpublic static void " +
                "Main()\n\t\t{\n\t\t\tConsole.WriteLine(\"Hello C# World!\");\n\t\t}\n\t}\n}\n"
            },

            // 2
            {
                _lang
                    ? "Ориентированный Hello World с датой"
                    : "User directed Hello World with Date"
                , 

                "using System;\n\nnamespace Lesson\n{\n\tpublic static class HelloWorldUserOriented\n\t{\n\t\tpublic " +
                "static void Main\n\t\t{\n\t\t\tstring name = \""  + Program.Name + "\";\n\t\t\tConsole.WriteLine($\"" +
                (_lang ? "Привет, {name}\\n\\tПривет Мир С#!" : "Hello, {name}\\n\\tHello C# World!") + "\\n\\t\");\n" +
                "\t\t\tConsole.WriteLine(DateTime.Now);\n\t\t\tConsole.WriteLine($\"" + (_lang ? "Урок Hello World бы" +
                "л сделан специально для" : "Hello World app was made special for") + " {name}.\");\n\t\t}\n\t}\n}\n"
            },

            // 3
            {
                "Python 3.7 Hello World",
                "print(\"Hello Python 3.7 World!\")\n"
            },

            // 4
            {
                "Python 2.7 Hello World",
                "print \"Hello Python 2.7 World!\"\n"
            },

            // 5
            {
                "JavaScript Hello World",
                "console.log(\"Hello JavaScript World!\");\n"
            },

            // 6
            {
                "Java Hello World",
                "public class HelloWorld {\n\n\tpublic static void main(String[] args) {\n\n\t\tSystem.out.println(\"" +
                "Hello Java Wolrd!\");\n\t}\n}\n"
            },

            // 7
            {
                "Pascal Hello World",
                "begin\n\twriteln(\"Hello Pascal World!\");\nend.\n"
            },

            // 8
            {
                "Kotlin Hello World",
                "package demo\n\nfun main(args : Array<String>) {\n\tprintln(\"Hello Kotlin World!\")\n}\n"
            },

            // 9
            {
                "GoLang Hello World",
                "package main\nimport \"fmt\"\nfunc main() {\n\tfmt.Println(\"Hello GoLang World!\")\n}\n"
            }
        };


        private static readonly Func<bool>[] Runs =
        {
            Methods.Bind(RunHelloWorld, "C#"),
            SayHelloWorldToUserWithDate,
            Methods.Bind(RunHelloWorld, "Python 3.7"),
            Methods.Bind(RunHelloWorld, "Python 2.7"),
            Methods.Bind(RunHelloWorld, "Python JavaScript"),
            Methods.Bind(RunHelloWorld, "Java"),
            Methods.Bind(RunHelloWorld, "Pascal"),
            Methods.Bind(RunHelloWorld, "Kotlin"),
            Methods.Bind(RunHelloWorld, "GoLang")
        };


        // Functions to run Code examples
        private static bool RunHelloWorld(string language)
        {
            Console.WriteLine($"Hello {language} World!");
            return true;
        }


        private static bool SayHelloWorldToUserWithDate()
        {
            var name = Program.Name;
            Console.WriteLine(Program.Language
                ? $"\nПривет, {name}\n\tПривет Мир C#!\n\t{DateTime.Now}\nУрок Hello World был сделан специально для {name}."
                : $"\nHello, {name}\n\tHello C# World!\n\t{DateTime.Now}\nHello World app was made special for {name}.");

            return true;
        }
    }
}
