public class Test {

    public static void main(String[] args){

        byte x = 5;
        int y = x;  /// Происходит преобразование типа byte в int.
        System.out.println("x");
    	System.out.println(func(10));
    }

	static int func(int x)	{
		return x*x;
	}
}
