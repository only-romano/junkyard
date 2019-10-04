using System;
using System.Collections.Generic;

namespace MetanitBase.App
{
    public static class Error
    {
        private static bool _lang;

        public static void Run(IReadOnlyList<string> stat)
        {
            _lang = Program.Language;
            Lesson.Run( name: _lang ? "Ошибки" : "Errors"
                , stat: stat
                , quiz: Quiz
                , code: Code
                , runs: Runs
                , interactive: Interactive
                , intro: "\n" + (_lang

                    ? $"Вы попали сюда, {Program.Name}, потому что выбрали номер урока, которого не сущестует. Тем не" +
                      " менее здесь тоже есть чем заняться. И, пускай, здесь нет интерактивного урока - зато, как все" +
                      "гда, в наличии Викторина и " + (Program.Code == "0" ? "Код, который вы сможете увидеть, ответи" +
                      "в правильно на 9 из 10 вопросов Викторины." : "у вас уже есть доступ к Коду, вы можете посмотр" +
                      "еть, как реализованы уроки в приложении.")

                    : $"You are here, {Program.Name}, because you choose number for lesson that doesn't exist. Nevert" +
                      "heless there's a usefull sources right here. There is no interactive lesson on this page, but " +
                      "as usual there are Quiz for you and " + (Program.Code == "0" ? "Code, that you can see if you " +
                      "provide nine of ten right answers to the Quiz." : "you already hava an access to Code that sho" +
                      "ws realisation of Lessons in Application."))
                 );
        }


        private static bool Interactive()
        {
            Methods.Print(_lang
                ? "Интерактивный урок не доступен для этого курса"
                : "Interactive lesson is not available for this course");
            return true;
        }


        private static readonly Lesson.Question[] Quiz = 
        {
            new Lesson.Question("Question 1", "1"),
            new Lesson.Question("Question 2", "2"),
            new Lesson.Question("Question 3", "3"),
            new Lesson.Question("Question 4", "4"),
            new Lesson.Question("Question 5", "5"),
            new Lesson.Question("Question 6", "6"),
            new Lesson.Question("Question 7", "7"),
            new Lesson.Question("Question 8", "8"),
            new Lesson.Question("Question 9", "9"),
            new Lesson.Question("Question 10", "10"),
            new Lesson.Question("Question 11", "11"),
            new Lesson.Question("Question 12", "12"),
            new Lesson.Question("Question 13", "13"),
            new Lesson.Question("Question 14", "14")
        };


        private static readonly string[,] Code = 
        {
            {"Code name 1", "Code source 1"},
            {"Code name 2", "Code source 2"}
        };


        private static readonly Func<bool>[] Runs =
        {
            Function1,
            Function2
        };



        // Functions to run Code examples
        private static bool Function1()
        {
            Console.WriteLine("Method 1");
            return true;
        }


        private static bool Function2()
        {
            Console.WriteLine("Method 2");
            return true;
        }
    }
}
