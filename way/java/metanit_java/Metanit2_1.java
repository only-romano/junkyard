public class Metanit2_1{
    public static void main(String[] args){

    /// boolean: хранит значение true или false.
    /// byte: хранит целое число от -128 до 127 и занимает 1 байт.
    /// short: хранит целое число от -32768 до 32767 и занимает 2 байта.
    /// int: хранит целое число от -2147483648 до 2147483647 и занимает 4 байта.
    /// long: хранит целое число от –9 223 372 036 854 775 808 до 9 223 372 036
    ///       854 775 807 и занимает 8 байт.
    /// float: хранит число с плавающей точкой от -3.4*1038 до 3.4*1038 и
    ///        занимает 4 байта.
    /// double: хранит число с плавающей точкой от ±4.9*10-324 до ±1.8*10308 и
    ///         занимает 8 байт.
    /// char: хранит одиночный символ в кодировке Unicode и занимает 2 байта, 
    ///       поэтому диапазон хранимых значений от 0 до 65536

    /// Переменные объявляются следующим образом: тип_данных имя_переменной.
    /// Например, int x;. В этом выражении мы объявляем переменную x типа int.

    /// - имя может содержать любые алфавитно-цифровые символы, а также знак
    /// подчеркивания, при этом первый символ в имени не должен быть цифрой.
    /// - в имени не должно быть знаков пунктуации и пробелов.
    /// - имя не может быть ключевым словом языка Java.
    /// - Java - регистрозависимый язык.

    /// Объявив переменную, мы можем тут же присвоить ее значение или
    /// инициализировать ее. инициализация переменных представляет присвоение
    /// переменной начального значения, например: int x=10;. Если мы не
    /// проинициализируем переменную до ее использования, то мы можем получить
    /// ошибку.
        boolean active = true;
        int x;
        int y=10;
        byte num = 50;
        char c='s';
        double d = 1.5;
        int a=4;
        int z=a+5;
        x = 15;
        y = 15;
        System.out.println("Variables: \n" + active + "\n" + x + "\n" + y + "\n" +
                           num + "\n" + c + "\n" + d + "\n" + a + "\n" + z);

    /// - Для задания шестнадцатеричного значения после символов 0x
    /// указывается число в шестнадцатеричном формате.
    /// - B восьмеричное значение указывается после символа 0.
    /// - A двоичное значение - после символов 0b.
        int num111 = 0x6F; // 16-тиричная система, число 111
        int num8 = 010; // 8-ричная система, число 8
        int num13 = 0b1101; // 2-ичная система, число 13
        System.out.println("\nNew Variables: \n" + num111 + "\n" + num8 + "\n" + num13);

/// использование суффиксов.

    /// При присвоении переменной типа float значения с плавающей точкой Java
    /// автоматически рассматривает это значение как объкт типа double. и чтобы
    /// указать, что данное значение должно рассматриваться как float, нам надо
    /// использовать суффикс f:
        float fl = 30.6f;
        double db = 30.6;
        System.out.println("\nVery New Variables: \n" + fl + "\n" + db);

    /// и хотя в данном случае обе переменных имеют практически одно значения,
    /// но эти значения будут по-разному рассматриваться и будут занимать разное
    /// место в памяти.

/// Символы и строки.

    /// В качестве значения переменная символьного типа получает одиночный символ,
    /// заключенный в ординарные кавычки: char ch='e';. Кроме того, переменной
    /// символьного типа также можно присвоить целочисленное значение от 0 до 65536.
    /// В этом случае переменная опять же будет хранить символ, а целочисленное
    /// значение будет указывать на номер символа в таблице символов Unicode.
    /// Например:
        char ch=102; // символ 'f'
        System.out.println(ch);

    /// Еще одной формой задания символьных переменных является шестнадцатеричная
    /// форма: переменная получает значение в шестнадцатеричной форме, которое
    /// следует после символов "u". Например, char ch='\u0066'; опять же будет
    /// хранить символ 'f'.

    /// Символьные переменные не стоит путать со строковыми, 'a' не идентично "a".
    /// Строковые переменные представляют объект String, который в отличие от char
    /// или int не является примитивным типов в Java:
        String hello = "Hellow...";
        System.out.println(hello);

/// Константы.

    /// Переменные можно объявить один раз в программе и затем несколько раз
    /// присваивать им различные значения:
        int num1=5;
        System.out.println(num1);
        int num2=57;
        System.out.println(num2);
        int num3=89;
        System.out.println(num3);
        num3=100;
        num=5;
        System.out.println(num1);

    /// Но в Java также имеются константы. В отличие от переменных константам
    /// можно присвоить значение только один раз. Константа объявляется также,
    /// как и переменная, только вначале идет ключевое слово final:
        final int num4=5;
        System.out.println(num4);

    /// num=57; так мы уже не можем написать, так как num - константа.
    /// Константы позволяют задать такие переменные, которые не должны больше
    /// изменяться. Например, если у нас есть переменная для хранения числа pi,
    /// то мы можем объявить ее константой, так как ее значение постоянно.

    }
}
