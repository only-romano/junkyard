using System;
using System.Collections.Generic;

namespace MetanitBase.App
{
    public static class AppCycle
    {
        // Runs new app, returns continue condition for Program cycle. Main method of the class.
        public static bool Start()
        {
            var number = AppChoice.Make();
            var statistic = Statistics.Get();
            var index = Methods.GetIndex(number);

            RunApp(number, statistic[index].Split('-'));

            // Prints statistics & updates statistic file
            statistic[index] = Methods.UpdatedStat();
            Files.Write(string.Join(" ", statistic));

            // After app menu
            return Menu.Cycle( functions: new Func<bool>[] { Statistics.Show, Developers.Show, null }
                , actions: new [,] {{"s", "с"}, {"d", "р"}, {"q", ""}}
                , info: Program.Language

                    ? "\n\nСтатистика - введите \"c\"\nИнфо о разработчиках - \"р\"\nВыход - \"q\"\nдля продолжения н" +
                      "ажмите ввод.\n"

                    : "\n\nСomputed statistics - \"s\"\nDevelopers information - \"d\"\nExit - \"q\"press enter to co" +
                      "ntinue.\n"

                , final: Program.Language
                    ? "\nВведите \"д\", чтобы продолжить обучение (для подтверждения нажмите ввод)"
                    : "\nInput \"y\" to continue running app (press enter to continue)"
            );
        }


        private static void RunApp(byte choice, IReadOnlyList<string> stat)
        {
            switch (choice)
            {
                case 1:
                    HelloWorld.Run(stat);
                    break;
                case 2:
                    Litterals.Run(stat);
                    break;
                case 3:
                    Inputs.Run(stat);
                    break;
                case 4:
                    Arithmetics.Run(stat);
                    break;
                case 5:
                    Binary.Run(stat);
                    break;
                case 6:
                    WordCounter.Run(stat);
                    break;
                case 7:
                    Equal.Run(stat);
                    break;
                case 8:
                    Converter.Run(stat);
                    break;
                case 9:
                    Condition.Run(stat);
                    break;
                case 10:
                    Cycles.Run(stat);
                    break;
                case 77:
                    EasterEgg.Run(stat);
                    break;
                case 99:
                    break;

                default:
                    Error.Run(stat); 
                    break;
            }
        }
    }
}
