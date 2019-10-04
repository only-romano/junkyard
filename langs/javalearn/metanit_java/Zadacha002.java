import java.util.Arrays;

public class Zadacha002{
    public static void main(String[] args){

        for(int i = 0; i < GetPrimals(12).length; i++)
            System.out.println(GetPrimals(12)[i]);

    }
    static int [] GetPrimals(int n){
        int y = 0;

        for(int i=2;i < n; i++){
            if (n % i == 0){
                y += 1 ;
            }
        }

        int[] primals = new int[y];

        int a = 0;
        for(int i=2;i < n; i++){
                if (n % i == 0){
                    primals[a] = i;
                    a += 1 ;
                }
        }
        return primals;
    }
}