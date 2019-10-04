package firstapp;

public class FirstApp{

    class Calculator {

        void Add(int x, int y){

            int z = x+y;
            System.out.printf("Сумма %d и %d равна %d \n", x, y, z);
            }
        }

    public static void main(String[] args) {

        Calculator calc = new Calculator();
        Calculator.Add(2,3);
    }

}



    

        
        
