public class Metanit2_6{
    public static void main(String[] args){

    // Цикл for.
    // for ([инициализация счетчика]; [условие]; [изменение счетчика])
    // { действия }

        for (int i = 1; i < 9; i ++){       // for(; ;)    for (; i<9;)
            System.out.printf("Квадрат числа %d равен %d \n", i, i * i);
        }

    // ОО, ТУТ УДОБНЕЕ СЧЁТЧиК СДЕЛАН ЧЕМ В ПиТОНЕ.

    // Специальная версия цикла for предназначена для перебора элементов
    // в наборах элементов, например, в массивах и коллекциях:
    // for (тип_данных название_переменной : контейнер){ действия }

        int[] array = new int[] { 1, 2, 3, 4, 5 };
        for (int a : array){
            System.out.println(a);
        }

    // Аналог (версия более гибкая, в ней можно изменять элементы):
        for (int b = 0; b < array.length; b++){
            array[b] = array[b] * 2;
            System.out.println(array[b]);
        }

    // Понял смысл в print : println = print line, printf = print format и тд.

    // Перебор многомерных массивов в цикле.

        int[][] nums = new int[][]
        {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        for (int c = 0; c < nums.length; c++){
            for(int d = 0; d < nums[c].length; d++){

                System.out.printf("%d ", nums[c][d]);
            }
            System.out.println();
        }


    // Цикл do.

    // Цикл do сначала выполняет код цикла, а потом проверяет условие в
    // инструкции while.  и пока это условие истинно, цикл повторяется:

        int e = 7;
        do{
            System.out.println(e);
            e--;
        }
        while (e > 0);

    // Важно отметить, что цикл do гарантирует хотя бы однократное
    // выполнение действий, даже если условие в инструкции while не будет
    // истинно.  Так, мы можем написать:

        int f = -1;
        do{
            System.out.println(f);
            f--;
        }
        while (f > 0);


    // Цикл while.

    // Цикл while сразу проверяет истинность некоторого условия, и если
    // условие истинно, то код цикла выполняется:
        int g = 6;
        while (g > 0){

            System.out.println(g);
            g --;
        }


    // Операторы continue и break.

        int[] nums2 = new int[] { 1, 2, 3, 4, 12, 9 };
        for (int h = 0; h < nums2.length; h++){
            if(nums2[h] > 10)
                break;
            System.out.println(nums2[h]);
        }

    // Так как в цикле идет проверка, больше ли элемент массива 10, то мы
    // не увидим на консоли последние два элемента, так как когда nums[i]
    // окажется больше 10 (то есть равно 12), сработает оператор break, и
    // цикл завершится.

    // Правда, мы также не увидим и последнего элемента, который меньше 10.
    // Теперь сделаем так, чтобы если число больше 10, цикл не завершался,
    // а просто переходил к следующему элементу.  Для этого используем
    // оператор continue:

        for (int j = 0; j < nums2.length; j++){

            if (nums2[j] > 10)
                continue;
            System.out.println(nums2[j]);
        }

    // В этом случае, когда выполнение цикла дойдет до числа 12, которое
    // не удовлетворяет условию проверки, то программа просто пропустит
    // это число и перейдет к следующему элементу массива.

    }
}