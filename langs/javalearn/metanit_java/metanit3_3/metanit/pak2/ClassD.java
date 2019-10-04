package metanit.pak2;

import metanit.pak1.ClassA;

public class ClassD extends ClassA{

    public void result(){

        // System.out.println(num1);  // ошибка, так как private
        displayNum1();  // public

        // System.out.println(num2);  // ошибка, так как по умолчанию
        displayNum2();  // protected

        System.out.println(num3);  // protected
        // displayNum3();  // ошибка, так как по умолчанию

        // System.out.ptintln(num4);  // public
        // classA.displayNum4();  // ошибка, так как private
    }
}