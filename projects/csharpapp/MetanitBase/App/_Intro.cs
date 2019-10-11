namespace MetanitBase.App
{
    public static class Intro
    {
        public static void Run()
        {
            var lang = Program.Language = Methods.CheckString(
                "\nВведите \"y\"(eng) или \"д\"(рус) для переключения на русский язык (press enter to continue)"
                );

            Program.Name = Methods.GetString(
                check: name => name != null && name.Length > 2,
                fail: lang ? "Аноним" : "Anonymous",

                text: lang

                    ? "\nПривет и Добро пожаловать в милую прогамму обучения С# по материалам сайта Metanit.com.\n\tМеня " +
                      "зовут Ridj и я рад видеть вас здесь :)\n\tp.s.: и это совершенно серьёзно!\n\nИтак, единственная в" +
                      "ещь о которой я хочу вас спросить сейчас - и вы мне сделаете огромное одолжение, если вы представи" +
                      "тесь сейчас, иначе мне придётся назвать вас повсюду Анонимом..\n\nНапишите своё имя (оно должно со" +
                      "держать хотя бы 3 - три символа), \n\tМеня зовут: "

                    : "\nHello and Welcome to my sweet C# program from Metanit.com!\n\tMy name is Ridj and I'm pleased to" +
                      " see you here!\n\tp.s.: and I mean it\n\nSo, can I ask you one thing - You'll do for me a big favo" +
                      "r if you'll introduce yourself right now, overwise we'll have to name you an Anonymous.\n\nInput y" +
                      "our name right now (it must consist at least of 3 - three - characters), \n\tMy name is: ",

                final: lang
                    ? "\nЧтож, очень хорошо, с этого момента я буду звать вас "
                    : "\nSo, very well, from now on you are be named an "
                );
        }
    }
}
