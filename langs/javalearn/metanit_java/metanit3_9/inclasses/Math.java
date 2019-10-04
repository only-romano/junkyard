package inclasses;

// В отличие от обычных классов внутренние классы могут быть статическими.
// Такие классы еще называют вложенными. Статические внутренние классы
// позволяют скрыть некоторую комплексную информацию внутри внешнего класса:

class Math{

    public static class Factorial{

        private int result;
        private int key;

        public Factorial(int number, int x){

            result=number;
            key = x;
        }

        public int getResult(){
            return result;
        }

        public int getKey(){
            return key;
        }
    }

    public static Factorial getFactorial(int x){

        int result=1;
        for (int i = 1; i <= x; i++){

            result *= i;
        }
        return new Factorial(result, x);
    }

    Math.Factorial fact = Math.getFactorial(6);
}

// Здесь определен вложенный класс для хранения данных о вычислении факториала.
// Основные действия выполняет метод getFactorial, который возвращает объект
// вложенного класса.Здесь определен вложенный класс для хранения данных о вычислении факториала. Основные действия выполняет метод getFactorial, который возвращает объект вложенного класса.