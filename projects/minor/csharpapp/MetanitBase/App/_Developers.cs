namespace MetanitBase.App
{
    public static class Developers
    {
        public static bool Show()
        {
            Methods.Print(Program.Language

                ? "\n\nПрограмма была создана в августе 2018 года по материалам сайта Metanit.com - курс по C# и .NET" +
                  ". Авторы курса - Metanit.com, Ridj. Создатели программы - Kato Basiro, Ridj. Секретный код - 77. И" +
                  "дею для создания программы подал хороший человек Кузьма Филимонов. Всё было создано специально для" +
                  $" тебя, дорогой {Program.Name}. Все права защищены. СибКод, 2018.\n"

                : "\n\nApplication was made in august 2018, used open web content from Metanit.com - C# & .NET course" +
                  "s. Authors of this course - Metanit.com, Ridj. Application authors are Kato Basiro, Ridj. Secret C" +
                  "ode is 77. Idea for application was inspired with help of very good man Kuzma Filimonov. This all " +
                  $"was made special for you, dear {Program.Name}. All rights reserved. SibCode, 2018.\n");

            return true;
        }
    }
}
