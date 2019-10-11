public class Zadacha001{
    public static void main(String[] args){

        System.out.println(IsPrimal(4));
        System.out.println(IsPrimal(11));
        System.out.println(IsPrimal(121));
        System.out.println(IsPrimal(113));

    }
    static boolean IsPrimal(int n){

        for(int i=2;i < n; i++){
            if (n % i == 0){
                return false;
            }
        }
        return true;
    }
}