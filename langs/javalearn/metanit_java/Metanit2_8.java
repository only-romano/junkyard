public class Metanit2_8{
    public static void main(String[] args){

        int num = 4;
        System.out.println(factorial(num));
        System.out.println(fibonachi(num));
    } 

// Рекурсивные функции.

    // Фактлоиал рекурсия.

    static int factorial(int x){
        if (x == 1){

            return 1;
        }
        else{

             return x * factorial(x - 1);
        }
    }

    // Факториал циклы.
    static int factorial_cicle(int x){
        int result=1;
        for (int i = 1; i <= x; i++)
        {
            result *= i;
        }
        return result;
    }

    // Числа Фибоначчи, рекурсия.
    static int fibonachi(int n){

        if (n == 0){
            return 0;
        }
        if (n == 1){
            return 1;
        }
        else{
            return fibonachi(n - 1) + fibonachi (n - 2);
        }
    }
}