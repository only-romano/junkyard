namespace MetanitBase.App
{
    public static class AppChoice
    {
        public static byte Make()
        {
            return Methods.GetBytes(
                question: Program.Language

                    ? "\nУроки:\n\t1) Hello World;\t2) Литераллы;\t3) Ввод\\Вывод;\n\t4) Арифметика;\t5) Логика;\t6) " +
                      "Подсчёт слов;\n\t7) Присваивания;\t8) Конвертер;\t9) Сравнения;\n\t10) Циклы;\n\nПожалуйста, в" +
                      "ыберите урок (введите номер урока и нажмите ввод): "

                    : "\nApps:\n\t1) Hello World;\t2) Litterals;\t3) Inputs;\n\t4) Arithmetics;\t5) Binary;\t6) Word " +
                      "Counter;\n\t7) Equals;\t8) Converter;\t9) Compare;\n\t10) Cycles;\n\nPlease, select app (inpit" +
                      " lesson number and press the enter to run App): " );
        }
    }
}
