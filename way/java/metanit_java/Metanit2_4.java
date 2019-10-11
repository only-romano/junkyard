import java.util.Arrays;

public class Metanit2_4 {
    public static void main(String[] args){


// Массивы.


    // Объявление и задание массива.

        int nums[] = new int[4];
        char[] stroka;
        stroka = new char[6];

    // Создание массива производится с помощью следующей конструкции:
    // new тип_данных[количество_элементов], где new - ключевое слово,
    // выделяющее память для указанного в скобках количества элементов.
    // Например, int nums[] = new int[4]; - в этом выражении создается
    // массив из четырех элементов int и каждый элемент по умолчанию
    // равен нулю.

    // После создания массива мы можем обратиться к любому его элементу
    // и изменить его:

        nums[0] = 1;    // Отсчет элементов массива начинается с 0.
        nums[1] = 2;
        nums[2] = 4;
        nums[3] = 100;

        System.out.println(nums);

    // и так как у нас массив определен только для 4 элементов, то мы
    // не можем обратиться, например, к шестому элементу: nums[5] = 5;.
    // Если мы так попытаемся сделать, то мы получим ошибку.

    // Eсть и альтернативные пути инициализации массивов:

        int[] nums2 = new int[] { 1, 2, 3, 5 };

        int[] nums3 = { 1, 2, 3, 5 };   // Способы равнозначны.

        System.out.println(nums3);


// Многомерные массивы

    // Ранее мы рассматривали одномерные массивы, которые можно
    // представить как цепочку или строку однотипных значений.  Но
    // кроме одномерных массивов также бывают и многомерными.
    // Наиболее известный многомерный массив - таблица,
    // представляющая двухмерный массив:

        int[][] nums1 = { { 0, 1, 2 }, {3, 4 , 5 } };

        System.out.println(nums1);

    // Поскольку массив nums1 двухмерный, он представляет собой
    // простую таблицу.  Его также можно было создать следующим
    // образом:

        int[][] nums4 = new int[3][3];

    // Количество квадратных скобок указывает на размерность массива.
    // А числа в скобках - на количество строк и столбцов.  и также,
    // используя индексы, мы можем использовать элементы массива в
    // программе:

        nums4[1][0] = 44;
        System.out.println(nums4[1][0]);

    // Объявление трехмерного массива:

        int[][][] nums7 = new int[2][3][4];


// Массив массивов

    // Многомерные массивы могут быть также представлены как
    // "зубчатые массивы".  В вышеприведенном примере двухмерный
    // массив имел 3 строчки и три столбца, поэтому у нас получалась
    // ровная таблица. Но мы можем каждому элементу в двухмерном
    // массиве присвоить отдельный массив с различным количеством
    // элементов:

        int[][] nums5 = new int[3][];
        nums5[0] = new int[2];
        nums5[1] = new int[3];
        nums5[2] = new int[5];

        System.out.println(nums5);


// Работа с массивами и класс Arrays

    // Важнейшее свойство, которым обладают массивы, является свойство
    // length, возвращающее длину массива, то есть количество его
    // элементов:
        int length = nums5.length;

    // Для работы с массивами в библиотеке классов Java в пакете
    // java.util определен специальный класс Arrays.  С его помощью мы
    // можем производить ряд операций над массивами.

    // Массивы, также как и переменные, мы можем присваивать:
        int[] numbers = new int[] { 1, 2, 3, 5 };
        int[] figures = numbers;

        figures[2] = 30;
        System.out.println(numbers[2]);
    // Здесь два массива, второму присваивается первый массив.  Однако
    // на самом деле при присвоении переменная figures будет хранить
    // ссылку на область в памяти, где находится массив.  В итоге и
    // figures и numbers будут указывать на один и тот же массив, и
    // если мы изменим элемент в массиве figures figures[2]=30, то
    // изменится и массив numbers, так как это фактически один и тот
    // же массив.  Чтобы такой проблемы избежать, надо использовать
    // копирование массивов.

    // Для копирования используется метод Arrays.copyOf:
    // import java.util.Arrays;
        int[] numbers2 = new int[] { 1, 2, 3, 5 };
        int[] figures2 = Arrays.copyOf(numbers2, numbers2.length);
    // Метод Arrays.copyOf(numbers, numbers.length) принимает два
    // параметра: первый параметр - массив, который надо скопировать,
    // а второй параметр - сколько элементов надо скопировать.

        figures2[2] = 30;
        System.out.println(numbers2[2]);    // Равно 3.

    // Сортировка
    // С помощью метода Arrays.sort можно отсортировать массив:
        int[] numbers3 = new int[] { 1, 7, 3, 5, 2, 6, 4 };

        Arrays.sort(numbers3);

        for(int i = 0; i < numbers3.length; i++)
            System.out.println(numbers3[i]);

    }
}