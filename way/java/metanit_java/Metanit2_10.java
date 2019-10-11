import java.util.Scanner;
public class Metanit2_10{
    public static void main(String[] args){

    // Введение в обработку исключений.

        try{
            int[] numbers = new int[3];
            numbers[4] = 45;
            System.out.println(numbers[4]);
            numbers[6] = Integer.parseInt("gfd");
        }
        catch(ArrayIndexOutOfBoundsException ex){

            ex.printStackTrace();
        }
        catch(NumberFormatException ex){

            System.out.println("Error Str to Int"); 
        }
        finally{
            System.out.println("finally block");
        }
        System.out.println("Programm completed");

        try{
            Scanner in = new Scanner(System.in);
            int x = in.nextInt();
            if(x>=30){
                throw new Exception("'x' must be less then 30.");
                // C помощью этого оператора мы сами можем создать
                // исключение и вызвать его в процессе выполнения.
            }
        }
        catch(Exception ex){

            System.out.println(ex.getMessage());
        }
        System.out.println("Programm completed");

    }
}