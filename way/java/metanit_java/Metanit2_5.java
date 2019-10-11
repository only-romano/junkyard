
import java.util.Scanner;

public class Metanit2_5{
    public static void main(String[] args){

    // Конструкция if - else if - else:

        int num1 = 8;
        int num2 = 4;
        if(num1>num2 && num1>7){
            System.out.println("Первое число больше второго и больше 7");
        }
        else if(num1>num2){
            System.out.println("Первое число больше второго");
        }
        else if(num1<num2){
            System.out.println("Второе число больше первого");
        }
        else{
            System.out.println("Числа равны");
        }


    // Конструкция switch - case:

        int num = 8;
        switch(num){

        // После ключевого слова switch в скобках идет сравниваемое
        // выражение.  Значение этого выражения последовательно
        // сравнивается со значениями, помещенными после оператора
        // сase.  Если совпадение будет найдено, то будет выполняться
        // определенный блок сase.

            case 1:
                System.out.println("число равно 1");
                break;
        // В конце блока сase ставится оператор break, чтобы избежать
        // выполнения других блоков.  Например, если бы убрали бы оператор
        // break в следующем случае:
            case 8:
                System.out.println("число равно 8");
                num++;
                break;
        // то так как у нас переменная num равно 8, то выполнился бы блок
        // case 8, но так как в этом блоке переменная num увеличивается
        // на единицу, оператор break отсутствует, то начал бы выполняться
        // блок case 9.
            case 9:
                System.out.println("число равно 9");
                break;
        // Если мы хотим также обработать ситуацию, когда совпадения не
        // будет найдено, то можно добавить блок default.  Хотя блок
        // default необязателен.
            default:
                System.out.println("число не равно 1, 8, 9");

        }

        // Начиная с JDK 7 в выражении switch..case кроме примитивных
        // типов можно также использовать строки:

        Scanner in = new Scanner(System.in);
        System.out.println("Введите Y или N: ");
        String input = in.nextLine();

        switch(input){

            case "Y":
                System.out.println("Вы нажали букву Y");
                break;
            case "N":
                System.out.println("Вы нажали букву N");
                break;
            default:
                System.out.println("Вы нажали неизвестную букву");

        }


        // Тернарная операция

        // Тернарную операция имеет следующий синтаксис:
        // [первый операнд - условие] ? [второй операнд] : [третий операнд].
        // Таким образом, в этой операции участвуют сразу три операнда.  В
        // зависимости от условия тернарная операция возвращает второй или
        // третий операнд: если условие равно true, то возвращается второй
        // операнд; если условие равно false, то третий.  Например:

        int x = 3;
        int y = 2;
        int z = x < y ? (x + y) : (x - y);
        System.out.println(z);

        // Здесь результатом тернарной операции является переменная z.
        // Сначала проверяется условие x<y. Если оно соблюдается,
        // то z будет равно второму операнду - (x + y), иначе z будет
        // равно третьему операнду.

    }
}